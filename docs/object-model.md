# Object model

## Full managed type access

The managed backend exposes the public types of the shipped assembly directly through Python.NET. It does not maintain separate Python copies of CAD entities. Objects returned from readers and collections are the same managed types that constructors create.

```python
import acadsharp
acadsharp.load()

from ACadSharp import CadDocument
from ACadSharp.Entities import Line
from ACadSharp.Objects import Layout
from ACadSharp.Tables import Layer
from CSMath import XYZ
```

Convenience modules include `acadsharp.entities`, `acadsharp.tables`, `acadsharp.objects`, `acadsharp.io` and `acadsharp.geometry`. Use the original namespaces for every additional namespace, or resolve one explicitly:

```python
entities = acadsharp.namespace("ACadSharp.Entities")
Line = acadsharp.get_type("ACadSharp.Entities.Line")
Vertex = acadsharp.get_type("ACadSharp.Entities.LwPolyline+Vertex")
```

The [reference](reference/index.md) records exact CLR names, namespaces, inheritance, interfaces, generic arity, constructors and public members for every exported type. Nested CLR names use `+`; Python attribute access uses a dot, such as `LwPolyline.Vertex`.

## Documents, ownership and handles

`CadDocument` contains tables, a root dictionary, layouts, a header, summary information and model/paper space block records. `cad.Entities` aliases `cad.ModelSpace.Entities`.

```python
from acadsharp import CadDocument, XYZ
from acadsharp.entities import Line

cad = CadDocument()
line = Line(XYZ.Zero, XYZ(5, 0, 0))
cad.Entities.Add(line)
assert line.Document == cad
assert cad.GetCadObject(line.Handle) == line
```

Use the owning collection's `Add` and `Remove` methods so ACadSharp can maintain handles and ownership. When moving content between documents, clone it using its public `Clone()` operation and add the clone to the destination. Follow the upstream constraints on references between entities, layers, block records and other document objects.

## Tables and layers

Tables implement .NET enumeration and expose name indexers. Their mutating operations use upstream method names.

```python
from acadsharp.tables import Layer

layer = Layer("construction")
cad.Layers.Add(layer)
line.Layer = cad.Layers["construction"]
layer.IsOn = False
for item in cad.Layers:
    print(item.Name)
```

The same pattern applies to block records, text styles, dimension styles, line types, registered applications and other table entries. See each type's reference for constructors and collection-specific operations.

## Blocks and inserts

Define a `BlockRecord`, populate its entities and add it to `cad.BlockRecords`. An `Insert` references that record. Its placement, rotation and scales belong to the insert rather than the definition.

```python
from acadsharp.entities import Insert
from acadsharp.tables import BlockRecord

block = BlockRecord("marker")
block.Entities.Add(Line(XYZ.Zero, XYZ(10, 0, 0)))
cad.BlockRecords.Add(block)
insert = Insert(block)
insert.InsertPoint = XYZ(20, 30, 0)
cad.Entities.Add(insert)
```

See `examples/blocks.py` for a round trip that preserves the definition and insert. Attributes, dynamic blocks and nested block structures use the same underlying upstream API.

## Geometry is made of value types

Many CSMath types, including `XYZ`, are .NET structs. Reading a struct-valued property returns a boxed value. Assign the complete value back when changing it:

```python
point = line.StartPoint
point.X = 25
line.StartPoint = point
# Or directly:
line.StartPoint = XYZ(25, 0, 0)
```

A chained assignment such as `line.StartPoint.X = 25` can modify only the boxed copy. See [interoperability](interop.md) for generics, overloads, out parameters, arrays and events.

## Coverage and compatibility

Every exported public type is included in the generated inventory, including interfaces, delegates, nested classes and open generics. The tests compare that inventory against the loaded assembly and resolve each exported type through the Python package. Functional tests separately exercise document editing and CAD file I/O. This verifies API exposure; it is not a claim that every upstream CAD operation or every possible drawing has been exhaustively tested.

The binding keeps upstream names and semantics. File-format support is defined by the pinned ACadSharp revision. See the upstream README and the package's generated reference when checking a feature or an overload.
