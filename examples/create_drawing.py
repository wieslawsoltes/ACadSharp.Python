"""Create a layered line/circle drawing and verify its DXF or DWG round trip."""

from pathlib import Path
import sys

from acadsharp import CadDocument, XYZ
from acadsharp.entities import Circle, Line
from acadsharp.io import DwgReader, DwgWriter, DxfReader, DxfWriter
from acadsharp.tables import Layer


def main(output: Path) -> None:
    if output.suffix.lower() not in {".dwg", ".dxf"}:
        raise ValueError("Output must have a .dxf or .dwg suffix")
    cad = CadDocument()
    layer = Layer("geometry")
    cad.Layers.Add(layer)
    line = Line(XYZ(0, 0, 0), XYZ(100, 50, 0))
    line.Layer = layer
    cad.Entities.Add(line)
    circle = Circle()
    circle.Center = XYZ(50, 25, 0)
    circle.Radius = 10
    circle.Layer = layer
    cad.Entities.Add(circle)
    reader, writer = (DwgReader, DwgWriter) if output.suffix.lower() == ".dwg" else (DxfReader, DxfWriter)
    writer.Write(str(output), cad)
    restored = reader.Read(str(output))
    assert restored.Entities.Count == 2
    assert restored.Layers["geometry"].Name == "geometry"
    assert all(entity.Layer.Name == "geometry" for entity in restored.Entities)
    print(f"Wrote and verified {output}: {restored.Entities.Count} entities")


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else "drawing.dxf"))
