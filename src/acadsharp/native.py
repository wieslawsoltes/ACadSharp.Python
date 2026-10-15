"""Optional ctypes interface to ACadSharp's NativeAOT library.

This module does not import pythonnet or load an installed .NET runtime. The
native library embeds the runtime and preserves ACadSharp's reflection metadata.
Use the managed backend when you need Python callbacks or dynamic CLR generics.
"""
from __future__ import annotations

import ctypes
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import threading
from typing import Any, Iterator
import weakref


class NativeError(RuntimeError):
    """An exception raised inside the native ACadSharp library."""

    def __init__(self, managed_type: str, message: str) -> None:
        self.managed_type = managed_type
        super().__init__(f"{managed_type}: {message}")


class NativeEnum(int):
    """A CLR enum value with its declared type and symbolic name attached."""

    def __new__(cls, value: int, type_name: str, name: str) -> NativeEnum:
        instance = super().__new__(cls, value)
        instance.type_name = type_name
        instance.name = name
        return instance

    def __repr__(self) -> str:
        return f"{self.type_name}.{self.name}"


class NativeMethod:
    """A public CLR method; ``signature=`` selects an exact overload."""

    def __init__(self, owner: NativeObject | NativeType, name: str) -> None:
        self.owner = owner
        self.name = name

    def __call__(self, *args: Any, signature: list[str] | None = None) -> Any:
        return self.owner.call(self.name, *args, signature=signature)


class NativeNamespace:
    """Attribute lookup for namespaces and public CLR types."""

    def __init__(self, runtime: NativeRuntime, name: str) -> None:
        self._runtime = runtime
        self._name = name

    def __getattr__(self, name: str) -> NativeNamespace | NativeType:
        full_name = f"{self._name}.{name}" if self._name else name
        if full_name in self._runtime._types:
            return self._runtime.type(full_name)
        if any(t.startswith(full_name + ".") for t in self._runtime._types):
            return NativeNamespace(self._runtime, full_name)
        raise AttributeError(full_name)

    def __dir__(self) -> list[str]:
        prefix = self._name + "." if self._name else ""
        return sorted({t[len(prefix):].split(".")[0] for t in self._runtime._types if t.startswith(prefix)})


class NativeType:
    """A public CLR type, its constructors, static members and nested types."""

    def __init__(self, runtime: NativeRuntime, name: str) -> None:
        object.__setattr__(self, "_runtime", runtime)
        object.__setattr__(self, "type_name", name)

    def __call__(self, *args: Any, signature: list[str] | None = None) -> Any:
        return self.construct(*args, signature=signature)

    def construct(self, *args: Any, signature: list[str] | None = None) -> Any:
        request: dict[str, Any] = {"op": "create", "type": self.type_name, "args": self._runtime._encode(args)}
        if signature is not None:
            request["signature"] = signature
        return self._runtime._request(request)

    def describe(self) -> dict[str, Any]:
        return self._runtime.describe(self.type_name)

    def get(self, name: str) -> Any:
        return self._runtime._request({"op": "get", "type": self.type_name, "name": name}, owner=self)

    def set(self, name: str, value: Any) -> None:
        self._runtime._request({"op": "set", "type": self.type_name, "name": name, "value": self._runtime._encode(value)})

    def call(self, name: str, *args: Any, signature: list[str] | None = None) -> Any:
        request: dict[str, Any] = {"op": "invoke", "type": self.type_name, "name": name, "args": self._runtime._encode(args)}
        if signature is not None:
            request["signature"] = signature
        return self._runtime._request(request)

    def __getattr__(self, name: str) -> Any:
        try:
            return self.get(name)
        except NativeError as error:
            if error.managed_type == "System.MissingMemberException":
                raise AttributeError(name) from error
            raise

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_"):
            object.__setattr__(self, name, value)
        else:
            self.set(name, value)

    def __dir__(self) -> list[str]:
        info = self.describe()
        return sorted({member["name"] for key in ("properties", "fields", "methods") for member in info[key]} |
                      {name.rsplit("+", 1)[-1] for name in info["nested_types"]})

    def __repr__(self) -> str:
        return f"<native type {self.type_name}>"


class NativeObject:
    """An owned bridge handle to a CLR object or boxed value type.

    ``close()`` releases the bridge reference, not the underlying object's CLR
    ``Dispose`` method. Invoke ``Dispose()`` explicitly for disposable resources.
    Other handles to the same object remain valid after this handle is released.
    """

    def __init__(self, runtime: NativeRuntime, handle: int, type_name: str) -> None:
        object.__setattr__(self, "_runtime", runtime)
        object.__setattr__(self, "_handle", handle)
        object.__setattr__(self, "type_name", type_name)
        runtime._handles.add(handle)
        object.__setattr__(self, "_finalizer", weakref.finalize(self, runtime._release, handle))

    def _target(self, op: str, **kwargs: Any) -> dict[str, Any]:
        if not self._finalizer.alive or self._handle not in self._runtime._handles:
            raise RuntimeError("Native object handle has been released")
        return {"op": op, "handle": self._handle, **kwargs}

    def close(self) -> None:
        self._finalizer()

    def describe(self) -> dict[str, Any]:
        return self._runtime._request(self._target("describe"))

    def get(self, name: str) -> Any:
        return self._runtime._request(self._target("get", name=name), owner=self)

    def set(self, name: str, value: Any) -> None:
        self._runtime._request(self._target("set", name=name, value=self._runtime._encode(value)))

    def call(self, name: str, *args: Any, signature: list[str] | None = None) -> Any:
        request = self._target("invoke", name=name, args=self._runtime._encode(args))
        if signature is not None:
            request["signature"] = signature
        return self._runtime._request(request)

    def __getattr__(self, name: str) -> Any:
        try:
            return self.get(name)
        except NativeError as error:
            if error.managed_type == "System.MissingMemberException":
                raise AttributeError(name) from error
            raise

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_"):
            object.__setattr__(self, name, value)
        else:
            self.set(name, value)

    def __getitem__(self, index: Any) -> Any:
        if isinstance(index, int) and index < 0:
            index += len(self)
        try:
            return self._runtime._request(self._target("getitem", index=self._runtime._encode(index)))
        except NativeError as error:
            if error.managed_type in ("System.IndexOutOfRangeException", "System.ArgumentOutOfRangeException"):
                raise IndexError(index) from error
            if error.managed_type == "System.Collections.Generic.KeyNotFoundException":
                raise KeyError(index) from error
            raise

    def __setitem__(self, index: Any, value: Any) -> None:
        if isinstance(index, int) and index < 0:
            index += len(self)
        self._runtime._request(self._target("setitem", index=self._runtime._encode(index), value=self._runtime._encode(value)))

    def __len__(self) -> int:
        return self._runtime._request(self._target("length"))

    def __bool__(self) -> bool:
        return True

    def __iter__(self) -> Iterator[Any]:
        iterator = self._runtime._request(self._target("iterate"))
        try:
            while True:
                result = self._runtime._request(iterator._target("next"))
                if result["done"]:
                    return
                yield result["value"]
        finally:
            if not self._runtime._closed:
                self._runtime._request(iterator._target("dispose_iterator"))
            iterator.close()

    def __dir__(self) -> list[str]:
        info = self.describe()
        return sorted({member["name"] for key in ("properties", "fields", "methods") for member in info[key]})

    def __str__(self) -> str:
        return self._runtime._request(self._target("string"))

    def __repr__(self) -> str:
        return f"<native {self.type_name} handle={self._handle}>"

    def __enter__(self) -> NativeObject:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()


def _library_path(path: str | os.PathLike[str] | None) -> Path:
    if path is not None:
        selected = Path(path)
        if not selected.is_file():
            raise FileNotFoundError(selected)
        return selected.resolve()
    configured = os.environ.get("ACADSHARP_NATIVE_LIBRARY")
    if configured:
        return _library_path(configured)
    filename = "acadsharp_native" + {"Darwin": ".dylib", "Windows": ".dll", "Linux": ".so"}.get(platform.system(), ".so")
    spec = importlib.util.find_spec("acadsharp_native")
    if spec and spec.origin:
        root = Path(spec.origin).parent
        for candidate in (root / filename, root / "_native" / filename):
            if candidate.is_file():
                return candidate
    raise FileNotFoundError(
        "ACadSharp NativeAOT library was not found. Install the acadsharp-native wheel, "
        "pass load('/path/to/acadsharp_native'), or set ACADSHARP_NATIVE_LIBRARY. "
        "Source builds use python scripts/build_native.py."
    )


class NativeRuntime:
    """A ctypes bridge session; close it to release every outstanding object handle."""

    def __init__(self, library: str | os.PathLike[str] | None = None) -> None:
        self.library_path = _library_path(library)
        self._library = ctypes.CDLL(str(self.library_path))
        self._library.acadsharp_abi_version.argtypes = []
        self._library.acadsharp_abi_version.restype = ctypes.c_int
        self._library.acadsharp_call.argtypes = [ctypes.c_char_p]
        self._library.acadsharp_call.restype = ctypes.c_void_p
        self._library.acadsharp_free.argtypes = [ctypes.c_void_p]
        self._library.acadsharp_free.restype = None
        if self._library.acadsharp_abi_version() != 1:
            raise RuntimeError("Unsupported ACadSharp native ABI version")
        self._lock = threading.RLock()
        self._handles: set[int] = set()
        self._closed = False
        self._types = frozenset(self._request({"op": "types"}))
        self.ACadSharp = NativeNamespace(self, "ACadSharp")
        self.CSMath = NativeNamespace(self, "CSMath")
        self.CSUtilities = NativeNamespace(self, "CSUtilities")

    @property
    def types(self) -> tuple[str, ...]:
        return tuple(sorted(self._types))

    def info(self) -> dict[str, Any]:
        return self._request({"op": "info"})

    def type(self, name: str) -> NativeType:
        if name not in self._types:
            raise AttributeError(f"Unknown public CLR type {name}")
        return NativeType(self, name)

    def describe(self, name: str) -> dict[str, Any]:
        return self._request({"op": "describe", "type": name})

    def read(self, path: str | os.PathLike[str], *, format: str | None = None) -> NativeObject:
        path = Path(path)
        return self._request({"op": "read", "path": str(path.resolve()), "format": (format or path.suffix.lstrip(".")).lower()})

    def write(self, document: NativeObject, path: str | os.PathLike[str], *, format: str | None = None, binary: bool = False) -> None:
        self._encode(document)  # Validate ownership before handing a handle to the bridge.
        path = Path(path)
        selected_format = (format or path.suffix.lstrip(".")).lower()
        if binary and selected_format != "dxf":
            raise ValueError("binary=True is only supported for DXF output")
        self._request(document._target("write", path=str(path.resolve()), format=selected_format, binary=binary))

    def close(self) -> None:
        with self._lock:
            if self._closed:
                return
            for handle in tuple(self._handles):
                self._release(handle)
            self._closed = True

    def _release(self, handle: int) -> None:
        with self._lock:
            if handle in self._handles:
                if not self._closed:
                    self._request({"op": "release", "handle": handle})
                self._handles.discard(handle)

    def _encode(self, value: Any) -> Any:
        if isinstance(value, NativeObject):
            if value._runtime is not self:
                raise ValueError("Native objects belong to different runtime sessions")
            value._target("validate")
            return {"$ref": value._handle}
        if isinstance(value, NativeEnum):
            return {"$enum": value.type_name, "value": int(value)}
        if isinstance(value, float) and not math.isfinite(value):
            return {"$number": "NaN" if math.isnan(value) else "Infinity" if value > 0 else "-Infinity"}
        if isinstance(value, (tuple, list)):
            return [self._encode(item) for item in value]
        if value is None or isinstance(value, (bool, int, float, str)):
            return value
        raise TypeError(f"Cannot pass {type(value).__name__} to the native bridge")

    def _decode(self, value: Any, owner: NativeObject | NativeType | None = None) -> Any:
        if isinstance(value, list):
            return [self._decode(item) for item in value]
        if not isinstance(value, dict):
            return value
        if "$ref" in value:
            return NativeObject(self, value["$ref"], value["$type"])
        if "$enum" in value:
            return NativeEnum(value["value"], value["$enum"], value["name"])
        if "$type_ref" in value:
            return self.type(value["$type_ref"])
        if "$method" in value:
            if owner is None:
                raise RuntimeError("Method descriptor has no owner")
            return NativeMethod(owner, value["$method"])
        if "$number" in value:
            return float(value["$number"])
        if "$return" in value:
            return (self._decode(value["$return"]), *self._decode(value["$out"]))
        return {key: self._decode(item) for key, item in value.items()}

    def _request(self, request: dict[str, Any], owner: NativeObject | NativeType | None = None) -> Any:
        with self._lock:
            if self._closed:
                raise RuntimeError("Native runtime session is closed")
            encoded = json.dumps(request, allow_nan=False, ensure_ascii=False).encode("utf-8")
            pointer = self._library.acadsharp_call(encoded)
            if not pointer:
                raise MemoryError("Native bridge did not allocate a response")
            try:
                response = json.loads(ctypes.string_at(pointer))
            finally:
                self._library.acadsharp_free(pointer)
            if not response["ok"]:
                raise NativeError(response["error"], response["message"])
            return self._decode(response.get("result"), owner)

    def __enter__(self) -> NativeRuntime:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()


def load(library: str | os.PathLike[str] | None = None) -> NativeRuntime:
    """Load the optional NativeAOT backend without initializing pythonnet."""
    return NativeRuntime(library)


__all__ = ["NativeError", "NativeEnum", "NativeObject", "NativeType", "NativeRuntime", "load"]
