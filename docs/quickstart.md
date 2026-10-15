# Quickstart

## Create and round-trip a drawing

```python
from acadsharp import CadDocument, XYZ
from acadsharp.entities import Circle, Line
from acadsharp.io import DxfReader, DxfWriter
from acadsharp.tables import Layer

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

DxfWriter.Write("drawing.dxf", cad)
copy = DxfReader.Read("drawing.dxf")
assert copy.Entities.Count == 2
assert copy.Layers["geometry"].Name == "geometry"
```

`CadDocument()` creates the default tables, model space and paper space. `cad.Entities` is the model space entity collection. Adding entities assigns document ownership and handles through ACadSharp.

## Inspect an existing file

```python
from acadsharp.io import DwgReader

cad = DwgReader.Read("input.dwg")
for entity in cad.Entities:
    print(entity.ObjectName, entity.Handle, entity.Layer.Name)

for layer in cad.Layers:
    print(layer.Name, layer.IsOn)
```

Use `DxfReader` for DXF input. Readers and writers retain upstream format support, validation and limitations. See [I/O](io.md) to collect parsing notifications and configure readers.

## Run the examples

The repository includes runnable scripts:

```sh
python examples/create_drawing.py drawing.dxf
python examples/inspect_drawing.py drawing.dxf
python examples/blocks.py blocks.dxf
python examples/interop.py
```

`create_drawing.py` also accepts a `.dwg` output path. Examples print their results and fail if their round-trip assertions do not hold.
