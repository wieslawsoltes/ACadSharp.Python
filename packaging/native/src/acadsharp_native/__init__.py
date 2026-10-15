"""Binary provider for :mod:`acadsharp.native`; requires no .NET host."""

from pathlib import Path
import sys

__version__ = "0.1.0"


def library_path() -> Path:
    """Return the packaged shared library for this wheel's platform."""
    suffix = {"win32": ".dll", "darwin": ".dylib"}.get(sys.platform, ".so")
    path = Path(__file__).parent / ("acadsharp_native" + suffix)
    if not path.is_file():
        raise FileNotFoundError(f"The native wheel is incomplete: {path}")
    return path
