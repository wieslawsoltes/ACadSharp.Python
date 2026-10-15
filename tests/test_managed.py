"""End-to-end verification against the real upstream model and serializers."""

import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

import pytest

import acadsharp as ac
from acadsharp import ACadVersion, CadDocument, Color, XY, XYZ
from acadsharp.entities import Circle, Entity, Hatch, Insert, Line, LwPolyline
from acadsharp.tables import AppId, BlockRecord, Layer


def drawing():
    document = CadDocument(ACadVersion.AC1032)
    layer = Layer("Python geometry")
    layer.Color = Color(25, 100, 240)
    document.Layers.Add(layer)
    line = Line()
    line.StartPoint = XYZ(1, 2, 3)
    line.EndPoint = XYZ(10, 20, 30)
    line.Layer = layer
    document.Entities.Add(line)
    circle = Circle()
    circle.Center = XYZ(5, 6, 0)
    circle.Radius = 2.5
    document.Entities.Add(circle)
    block = BlockRecord("PYTHON_BLOCK")
    block.Entities.Add(Line())
    document.BlockRecords.Add(block)
    insert = Insert(block)
    insert.InsertPoint = XYZ(50, 60, 0)
    document.Entities.Add(insert)
    document.SummaryInfo.Title = "Python round trip"
    return document


def assert_drawing(document, format):
    assert document.Entities.Count == 3
    # ACadSharp's DXF writer does not emit CadSummaryInfo (DWG does).
    if format == "dwg":
        assert document.SummaryInfo.Title == "Python round trip"
    line = next(item for item in document.Entities if isinstance(item, Line))
    assert line.StartPoint == XYZ(1, 2, 3)
    assert line.EndPoint == XYZ(10, 20, 30)
    assert line.Layer.Name == "Python geometry"
    assert document.Layers["Python geometry"].Color == Color(25, 100, 240)
    circle = next(item for item in document.Entities if isinstance(item, Circle))
    assert circle.Radius == pytest.approx(2.5)
    insert = next(item for item in document.Entities if isinstance(item, Insert))
    assert insert.Block.Name == "PYTHON_BLOCK"
    assert insert.Block.Entities.Count == 1
    assert insert.InsertPoint == XYZ(50, 60, 0)


@pytest.mark.parametrize(("format", "binary"), [("dxf", False), ("dxf", True), ("dwg", False)])
def test_file_round_trip(tmp_path, format, binary):
    path = tmp_path / f"drawing.{format.upper()}"
    ac.write(drawing(), path, binary=binary)
    assert path.stat().st_size > 0
    document = ac.read(path)
    assert_drawing(document, format)
    # A read model is editable, and changes survive a second write.
    document.Entities[0].Layer = document.Layers["0"]
    edited = tmp_path / f"edited.{format}"
    ac.write(document, edited, binary=binary)
    assert ac.read(edited).Entities[0].Layer.Name == "0"


@pytest.mark.parametrize(("format", "binary"), [("dxf", False), ("dxf", True), ("dwg", False)])
def test_bytes_round_trip(format, binary):
    data = ac.dumps(drawing(), format=format, binary=binary)
    assert isinstance(data, bytes)
    assert_drawing(ac.loads(memoryview(data), format=format), format)


def test_original_clr_namespaces_and_identity():
    import ACadSharp
    import ACadSharp.Entities
    import CSMath

    assert CadDocument is ACadSharp.CadDocument
    assert Line is ACadSharp.Entities.Line
    assert XYZ is CSMath.XYZ
    document = drawing()
    line = document.Entities[0]
    assert line.Document == document
    assert line.Owner == document.ModelSpace
    assert document.GetCadObject(line.Handle) == line
    assert isinstance(line, Entity)


def test_generics_out_parameters_arrays_and_clone():
    from System import Array, UInt64
    from System.Collections.Generic import List

    document = CadDocument()
    lines = List[Line]()
    lines.Add(Line())
    document.Entities.AddRange(lines)
    line = document.Entities[0]
    assert document.GetCadObject[Line](UInt64(line.Handle)) == line
    found, result = document.TryGetCadObject[Line](UInt64(line.Handle))
    assert found and result == line
    found, result = document.TryGetCadObject[Line](UInt64(0xFFFFFFFF))
    assert not found and result is None
    clone = line.Clone()
    assert isinstance(clone, Line)
    assert clone.Owner is None
    document.Entities.AddRange(Array[Entity]([clone, Circle()]))
    assert len(list(document.Entities)) == 3


def test_events_can_cancel_mutations():
    document = CadDocument()
    events = []

    def on_add(sender, args):
        events.append(args.Item)

    def cancel_remove(sender, args):
        args.Cancel = True

    document.Entities.OnAdd += on_add
    line = Line()
    document.Entities.Add(line)
    document.Entities.OnAdd -= on_add
    assert events == [line]
    document.Entities.OnBeforeRemove += cancel_remove
    assert not document.Entities.Remove(line)
    assert document.Entities.Count == 1
    document.Entities.OnBeforeRemove -= cancel_remove
    assert document.Entities.Remove(line)
    assert line.Owner is None


def test_nested_types_structs_and_generic_collections():
    polyline = LwPolyline()
    vertex_type = ac.get_type("ACadSharp.Entities.LwPolyline+Vertex")
    vertex = vertex_type(XY(1, 2))
    polyline.Vertices.Add(vertex)
    assert polyline.Vertices[0].Location == XY(1, 2)
    hatch = Hatch()
    hatch.SeedPoints.Add(XY(3, 4))
    assert hatch.SeedPoints[0] == XY(3, 4)
    assert ac.get_type("ACadSharp.CadObjectCollection`1")[Line] is not None
    # Value types are boxed copies; reassign the modified value to its owner.
    line = Line()
    point = line.StartPoint
    point.X = 10
    line.StartPoint = point
    assert line.StartPoint.X == 10


def test_xdata_and_extended_dictionary_round_trip():
    from ACadSharp.Objects import XRecord
    from ACadSharp.XData import ExtendedData, ExtendedDataString

    document = CadDocument()
    app = AppId("PYTHON_APP")
    document.AppIds.Add(app)
    line = Line()
    data = ExtendedData()
    data.Records.Add(ExtendedDataString("hello from Python"))
    line.ExtendedData.Add(app, data)
    line.CreateExtendedDictionary()
    line.XDictionary.Add("PYTHON_RECORD", XRecord())
    document.Entities.Add(line)
    for format in ("dxf", "dwg"):
        result = ac.loads(ac.dumps(document, format=format), format=format)
        restored = result.Entities[0]
        assert restored.ExtendedData.Get(result.AppIds["PYTHON_APP"]).Records[0].Value == "hello from Python"
        assert restored.XDictionary.GetEntry[XRecord]("PYTHON_RECORD") is not None


def test_loader_is_idempotent_across_threads():
    with ThreadPoolExecutor(max_workers=8) as executor:
        assemblies = list(executor.map(lambda _: ac.load(), range(16)))
    assert all(assembly == assemblies[0] for assembly in assemblies)
    assert ac.runtime_info()["runtime"] == "CoreCLR"


def test_base_import_does_not_initialize_pythonnet():
    subprocess.run(
        [sys.executable, "-c", "import sys; import acadsharp; assert 'clr' not in sys.modules; assert 'pythonnet' not in sys.modules"],
        check=True,
    )


def test_invalid_inputs_and_managed_exceptions(tmp_path):
    from System import ArgumentException
    from System.IO import FileNotFoundException

    with pytest.raises(ValueError, match="format"):
        ac.read(tmp_path / "drawing.unknown")
    with pytest.raises(TypeError, match="bytes"):
        ac.loads("not bytes", format="dxf")
    with pytest.raises(ValueError, match="DXF"):
        ac.dumps(CadDocument(), format="dwg", binary=True)
    with pytest.raises(LookupError):
        ac.get_type("ACadSharp.DoesNotExist")
    with pytest.raises(FileNotFoundException):
        ac.read(tmp_path / "missing.dxf")
    document = CadDocument()
    line = Line()
    document.Entities.Add(line)
    with pytest.raises(ArgumentException):
        document.Entities.Add(line)
