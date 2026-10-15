"""Array-backed adapters for upstream methods returning stack-only RGB spans.

The original ``Color`` type remains unchanged. Python.NET cannot marshal
``ReadOnlySpan<byte>`` return values, so a compiled bridge calls each original
method and copies its result into a byte array before crossing into Python.
"""

from functools import lru_cache
from pathlib import Path

from ._runtime import load

__all__ = ["rgb", "true_color_rgb", "index_rgb"]


# Fully qualified compiler XML member IDs, kept in sync by reflection tests.
ADAPTERS = {
    "M:ACadSharp.Color.GetRgb": "acadsharp.colors.rgb",
    "M:ACadSharp.Color.GetTrueColorRgb": "acadsharp.colors.true_color_rgb",
    "M:ACadSharp.Color.GetIndexRGB(System.Byte)": "acadsharp.colors.index_rgb",
}


@lru_cache(maxsize=1)
def _bridge():
    assembly = load()
    path = Path(str(assembly.Location)).parent / "ACadSharp.Python.dll"
    if not path.is_file():
        raise FileNotFoundError(
            f"Python compatibility assembly not found at {path}. Install a built "
            "acadsharp wheel or run `python scripts/build_managed.py`."
        )
    import clr

    clr.AddReference(str(path))
    from ACadSharp.Python import ColorInterop

    return ColorInterop


def rgb(color) -> bytes:
    """Return ``Color.GetRgb()`` as three immutable RGB bytes."""
    return bytes(_bridge().GetRgb(color))


def true_color_rgb(color) -> bytes:
    """Return ``Color.GetTrueColorRgb()`` as immutable RGB bytes.

    Returns three bytes for true colors and empty bytes for indexed colors,
    preserving the original operation. Use ``rgb`` for palette lookup.
    """
    return bytes(_bridge().GetTrueColorRgb(color))


def index_rgb(index: int) -> bytes:
    """Return ``Color.GetIndexRGB(index)`` as three immutable RGB bytes.

    ``index`` must fit the upstream byte parameter (0 through 255).
    """
    return bytes(_bridge().GetIndexRGB(index))
