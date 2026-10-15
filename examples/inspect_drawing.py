"""Print model space entities and layer names from a DXF or DWG file."""

from pathlib import Path
import sys

from acadsharp.io import DwgReader, DxfReader


def main(path: Path) -> None:
    suffix = path.suffix.lower()
    if suffix not in {".dxf", ".dwg"}:
        raise ValueError("Input must have a .dxf or .dwg suffix")
    cad = (DwgReader if suffix == ".dwg" else DxfReader).Read(str(path))
    print(f"{path}: {cad.Header.Version}, {cad.Entities.Count} model space entities")
    for entity in cad.Entities:
        print(entity.ObjectName, entity.Handle, entity.Layer.Name)
    print("Layers:", ", ".join(layer.Name for layer in cad.Layers))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python examples/inspect_drawing.py drawing.dxf")
    main(Path(sys.argv[1]))
