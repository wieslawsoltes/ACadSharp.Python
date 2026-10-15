"""Create a block definition and an insert, then verify their DXF round trip."""

from pathlib import Path
import sys

from acadsharp import CadDocument, XYZ
from acadsharp.entities import Insert, Line
from acadsharp.io import DxfReader, DxfWriter
from acadsharp.tables import BlockRecord


def main(output: Path) -> None:
    cad = CadDocument()
    block = BlockRecord("marker")
    block.Entities.Add(Line(XYZ.Zero, XYZ(10, 0, 0)))
    block.Entities.Add(Line(XYZ(5, -5, 0), XYZ(5, 5, 0)))
    cad.BlockRecords.Add(block)
    insert = Insert(block)
    insert.InsertPoint = XYZ(20, 30, 0)
    cad.Entities.Add(insert)
    DxfWriter.Write(str(output), cad)
    restored = DxfReader.Read(str(output))
    assert restored.BlockRecords["marker"].Entities.Count == 2
    instance = next(iter(restored.Entities))
    assert isinstance(instance, Insert)
    assert instance.Block.Name == "marker"
    assert instance.InsertPoint == XYZ(20, 30, 0)
    print(f"Wrote and verified block and insert in {output}")


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else "blocks.dxf"))
