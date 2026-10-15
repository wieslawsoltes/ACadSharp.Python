"""Full ACadSharp object model for Python, with lazy .NET initialization.

Install ``acadsharp[managed]`` and .NET 10 to use the managed API. Importing
this package alone does not load .NET; ``acadsharp.native`` is independent.
"""

from importlib import import_module

from ._runtime import get_type, load, namespace, runtime_info

__version__ = "0.1.0"
__all__ = [
    "ACadVersion", "CadDocument", "Color", "XY", "XYZ", "api", "dumps",
    "get_type", "load", "loads", "namespace", "read", "runtime_info", "write",
]


def api():
    """Return the packaged public API inventory without starting .NET."""
    import json
    from importlib.resources import files

    return json.loads(files(__package__).joinpath("api.json").read_text(encoding="utf-8"))


def __getattr__(name):
    if name in {"read", "write", "loads", "dumps"}:
        value = getattr(import_module("._io", __package__), name)
    elif name in {"entities", "tables", "objects", "io", "geometry", "header", "classes", "types", "native"}:
        value = import_module(f".{name}", __package__)
    elif not name.startswith("_"):
        # Preserve the actual CLR types: no wrappers, copies, or reduced model.
        for source in ("ACadSharp", "CSMath"):
            module = namespace(source)
            if hasattr(module, name):
                value = getattr(module, name)
                break
        else:
            raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    globals()[name] = value
    return value


def __dir__():
    return sorted(set(globals()) | set(__all__))
