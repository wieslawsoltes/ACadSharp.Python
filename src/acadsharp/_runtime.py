"""Initialize Python.NET exactly once and load the packaged managed assembly."""

from __future__ import annotations

import importlib
import os
import sys
import threading
from pathlib import Path

_lock = threading.RLock()
_assembly = None
_assembly_dir: Path | None = None


def load(*, assembly_dir=None, runtime_config=None, dotnet_root=None):
    """Load ACadSharp and return its CLR assembly.

    ``assembly_dir`` (or ``ACADSHARP_ASSEMBLY_DIR``) may override the bundled
    assembly. ``runtime_config`` and ``dotnet_root`` are passed to Python.NET
    when starting CoreCLR. An already loaded CoreCLR runtime is reused.
    """
    global _assembly, _assembly_dir
    with _lock:
        override = assembly_dir or os.environ.get("ACADSHARP_ASSEMBLY_DIR")
        directory = Path(override or Path(__file__).parent / "_managed").resolve()
        if _assembly is not None:
            if override and directory != _assembly_dir:
                raise RuntimeError("ACadSharp is already loaded from another directory; start a new Python process")
            return _assembly
        dll = directory / "ACadSharp.dll"
        if not dll.is_file():
            raise FileNotFoundError(
                f"ACadSharp assembly not found at {dll}. Install a built acadsharp wheel "
                "or run `python scripts/build_managed.py` in a recursive source checkout."
            )
        try:
            import pythonnet
        except ImportError as exc:
            raise ImportError(
                "Managed bindings require Python.NET: pip install 'acadsharp[managed]'. "
                "Install .NET 10 as well, or use acadsharp.native with acadsharp[native]."
            ) from exc
        info = pythonnet.get_runtime_info()
        if info is None:
            config = Path(runtime_config) if runtime_config else directory / "ACadSharp.runtimeconfig.json"
            options = {}
            if runtime_config or config.is_file():
                options["runtime_config"] = str(config)
            if dotnet_root:
                options["dotnet_root"] = str(dotnet_root)
            try:
                pythonnet.load("coreclr", **options)
            except Exception as exc:
                raise RuntimeError(
                    "Could not start .NET. Install the .NET 10 runtime for your Python "
                    "architecture; set DOTNET_ROOT for a nonstandard installation. "
                    "Call acadsharp.load() before importing clr."
                ) from exc
        elif info.kind != "CoreCLR":
            raise RuntimeError(
                f"ACadSharp requires CoreCLR, but {info.kind} is already loaded. "
                "Start a new process and call acadsharp.load() before importing clr."
            )
        import clr

        # Python.NET uses sys.path when resolving managed assembly dependencies.
        if str(directory) not in sys.path:
            sys.path.append(str(directory))
        _assembly = clr.AddReference(str(dll))
        _assembly_dir = directory
        return _assembly


def namespace(name: str):
    """Import any ACadSharp, CSMath, or CSUtilities namespace after loading .NET."""
    if not isinstance(name, str) or name.split(".")[0] not in {"ACadSharp", "CSMath", "CSUtilities"}:
        raise ValueError("Expected an ACadSharp, CSMath, or CSUtilities namespace")
    load()
    return importlib.import_module(name)


def get_type(fullname: str):
    """Resolve a public CLR type, including nested and open generic types.

    Use CLR names such as ``ACadSharp.Entities.Line`` or
    ``ACadSharp.CadObjectCollection`1``. Close generics with Python.NET's
    subscript syntax, e.g. ``get_type('ACadSharp.CadObjectCollection`1')[Line]``.
    """
    if not isinstance(fullname, str):
        raise TypeError("fullname must be a string")
    assembly = load()
    clr_type = assembly.GetType(fullname, False)
    if clr_type is None or not clr_type.IsVisible:
        raise LookupError(f"No public ACadSharp type named {fullname!r}")
    names = []
    current = clr_type
    while current is not None:
        # Keep arity: Python.NET accepts CLR names containing backticks. A
        # non-generic type may share the same name (ExtendedDataRecord<T>).
        names.append(str(current.Name))
        current = current.DeclaringType
    value = namespace(str(clr_type.Namespace))
    for name in reversed(names):
        value = getattr(value, name)
    return value


def runtime_info():
    """Return diagnostic version/path information (loads the managed backend)."""
    assembly = load()
    import platform

    import pythonnet
    from System import Environment

    return {
        "backend": "pythonnet",
        "python": platform.python_version(),
        "architecture": platform.machine(),
        "dotnet": str(Environment.Version),
        "runtime": str(pythonnet.get_runtime_info().kind),
        "assembly": str(assembly.FullName),
        "assembly_path": str(assembly.Location),
    }
