"""NativeAOT integration tests, enabled when a compiled library is available."""
from __future__ import annotations

import ctypes
import gc
import importlib.util
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

import pytest

from acadsharp import api, native

pytestmark = pytest.mark.native

ROOT = Path(__file__).resolve().parents[1]


def library_path() -> Path:
    configured = os.environ.get("ACADSHARP_NATIVE_LIBRARY")
    if configured:
        path = Path(configured)
        if not path.is_file():
            pytest.fail(f"ACADSHARP_NATIVE_LIBRARY points to a missing library: {path}")
        return path
    provider = importlib.util.find_spec("acadsharp_native")
    if provider:
        return native._library_path(None)
    system = {"Darwin": "osx", "Linux": "linux", "Windows": "win"}[platform.system()]
    arch = "arm64" if platform.machine().lower() in ("arm64", "aarch64") else "x64"
    suffix = {"osx": ".dylib", "linux": ".so", "win": ".dll"}[system]
    path = ROOT / "artifacts/native" / f"{system}-{arch}" / f"acadsharp_native{suffix}"
    if not path.is_file():
        pytest.skip("Build the NativeAOT library with scripts/build_native.py")
    return path


@pytest.fixture
def runtime():
    with native.load(library_path()) as rt:
        yield rt


def test_native_does_not_load_pythonnet():
    # A fresh interpreter is essential: other tests exercise the managed backend.
    code = "from acadsharp import native; import sys; rt=native.load(sys.argv[1]); assert 'clr' not in sys.modules; assert 'pythonnet' not in sys.modules; rt.ACadSharp.CadDocument(); rt.close()"
    subprocess.run([sys.executable, "-c", code, str(library_path())], check=True)


def test_complete_public_type_metadata(runtime):
    assert runtime.info()["type_count"] == len(runtime.types)
    assert set(runtime.types) == {item["fullname"] for item in api()["types"]}
    for name in runtime.types:
        description = runtime.describe(name)
        assert description["name"] == name
        assert all("parameters" in method for method in description["methods"])
    assert "Line" in dir(runtime.ACadSharp.Entities)
    assert "StartPoint" in dir(runtime.ACadSharp.Entities.Line)


def test_every_default_constructible_entity(runtime):
    # Exercise the broad model: the classes include dimensions, surfaces, solids,
    # blocks, images, text, hatches and entities beyond the quickstart examples.
    created = 0
    for name in runtime.types:
        if not name.startswith("ACadSharp.Entities.") or "+" in name:
            continue
        description = runtime.describe(name)
        if description["abstract"] or description["generic"] or description["enum"]:
            continue
        if not any(not constructor["parameters"] for constructor in description["constructors"]):
            continue
        instance = runtime.type(name)()
        assert instance.type_name == name
        instance.close()
        created += 1
    assert created >= 50


@pytest.mark.parametrize("format,binary", [("dxf", False), ("dxf", True), ("dwg", False)])
def test_document_roundtrip(runtime, tmp_path, format, binary):
    doc = runtime.ACadSharp.CadDocument()
    layer = runtime.ACadSharp.Tables.Layer("Geometry")
    doc.Layers.Add(layer)
    line = runtime.ACadSharp.Entities.Line()
    line.StartPoint = runtime.CSMath.XYZ(1.25, 2.5, 3.75)
    line.EndPoint = runtime.CSMath.XYZ(10.0, 20.0, 30.0)
    line.Layer = layer
    doc.Entities.Add(line)
    circle = runtime.ACadSharp.Entities.Circle()
    circle.Center = runtime.CSMath.XYZ(5.0, 6.0, 0.0)
    circle.Radius = 2.5
    doc.Entities.Add(circle)
    polyline = runtime.ACadSharp.Entities.LwPolyline()
    polyline.Vertices.Add(runtime.ACadSharp.Entities.LwPolyline.Vertex(0.0, 0.0))
    polyline.Vertices.Add(runtime.ACadSharp.Entities.LwPolyline.Vertex(10.0, 5.0))
    polyline.IsClosed = True
    doc.Entities.Add(polyline)
    text = runtime.ACadSharp.Entities.TextEntity()
    text.Value = "Native Python – CAD"
    doc.Entities.Add(text)
    path = tmp_path / f"drawing.{format}"
    runtime.write(doc, path, binary=binary)
    assert path.stat().st_size > 100
    loaded = runtime.read(path)
    assert len(loaded.Entities) == 4
    entities = list(loaded.Entities)
    assert entities[0].StartPoint.X == 1.25
    assert entities[0].EndPoint.Z == 30.0
    assert entities[0].Layer.Name == "Geometry"
    assert entities[1].Radius == 2.5
    assert entities[2].Vertices[1].Location.Y == 5.0
    assert entities[2].IsClosed is True
    assert entities[3].Value == "Native Python – CAD"
    assert loaded.Entities[-1].Value == entities[3].Value


def test_methods_clone_collections_and_out_parameters(runtime):
    document = runtime.ACadSharp.CadDocument()
    layer = runtime.ACadSharp.Tables.Layer("Original")
    document.Layers.Add(layer)
    success, found = document.Layers.TryGetValue("Original", None)
    assert success and found.Name == "Original"
    assert document.Layers["Original"].Name == "Original"
    success, missing = document.Layers.TryGetValue("Missing", None)
    assert not success and missing is None
    line = runtime.ACadSharp.Entities.Line()
    line.EndPoint = runtime.CSMath.XYZ(3.0, 4.0, 0.0)
    clone = line.Clone()
    clone.EndPoint = runtime.CSMath.XYZ(6.0, 8.0, 0.0)
    assert line.EndPoint.X == 3.0
    assert clone.EndPoint.X == 6.0
    document.Entities.Add(line)
    document.Entities.Add(clone)
    document.Entities.Remove(line)
    assert len(document.Entities) == 1
    assert document.Entities[0].EndPoint.Y == 8.0
    assert "Add" in dir(document.Entities)


def test_static_members_enums_and_boxed_values(runtime):
    version = runtime.ACadSharp.ACadVersion.AC1032
    assert isinstance(version, native.NativeEnum)
    assert version.name == "AC1032"
    document = runtime.ACadSharp.CadDocument(version)
    assert document.Header.Version == version
    point = runtime.CSMath.XYZ(2.0, 3.0, 4.0)
    point.X = 7.0
    assert point.X == 7.0
    assert runtime.CSMath.XYZ.AxisX.X == 1.0
    cross = runtime.CSMath.XYZ.Cross(runtime.CSMath.XYZ.AxisX, runtime.CSMath.XYZ.AxisY)
    assert cross.Z == 1.0
    explicit = runtime.CSMath.XYZ.construct(5, signature=["System.Double"])
    assert explicit.X == explicit.Y == explicit.Z == 5.0
    nan = runtime.CSMath.XYZ(float("nan"))
    assert nan.X != nan.X


def test_error_mapping_and_release(runtime, tmp_path):
    with pytest.raises(native.NativeError, match="FileNotFoundException"):
        runtime.read(tmp_path / "missing.dxf")
    with pytest.raises(native.NativeError, match="Format must be"):
        runtime.read(tmp_path / "drawing.unknown")
    doc = runtime.ACadSharp.CadDocument()
    with pytest.raises(AttributeError):
        _ = doc.NoSuchMember
    with pytest.raises(native.NativeError, match="writable"):
        doc.Handle = 5
    # ACadSharp's CadObjectCollection indexer uses ElementAtOrDefault, whereas
    # List<T> raises for an invalid index. Preserve both upstream contracts.
    assert doc.Entities[0] is None
    with pytest.raises(IndexError):
        _ = runtime.ACadSharp.Entities.LwPolyline().Vertices[0]
    with pytest.raises(ValueError, match="only supported for DXF"):
        runtime.write(doc, tmp_path / "drawing.dwg", binary=True)
    doc.close()
    doc.close()
    with pytest.raises(RuntimeError, match="released"):
        _ = doc.Entities


def test_gc_and_context_release_all_handles(runtime):
    gc.collect()
    before = runtime.info()["handle_count"]
    doc = runtime.ACadSharp.CadDocument()
    for _ in range(20):
        entities = doc.Entities
    del entities, doc
    gc.collect()
    assert runtime.info()["handle_count"] == before
    child = native.load(library_path())
    retained = child.ACadSharp.CadDocument()
    child.close()
    assert runtime.info()["handle_count"] == before
    with pytest.raises(RuntimeError, match="released"):
        _ = retained.Entities


def test_cross_session_objects_rejected(runtime):
    with native.load(library_path()) as other:
        line = other.ACadSharp.Entities.Line()
        doc = runtime.ACadSharp.CadDocument()
        with pytest.raises(ValueError, match="different runtime"):
            doc.Entities.Add(line)


def test_malformed_request_stays_inside_c_boundary(runtime):
    pointer = runtime._library.acadsharp_call(b"{invalid json")
    try:
        response = json.loads(ctypes.string_at(pointer))
        assert response["ok"] is False
        assert "Json" in response["error"]
    finally:
        runtime._library.acadsharp_free(pointer)
    assert runtime.info()["abi"] == 1
