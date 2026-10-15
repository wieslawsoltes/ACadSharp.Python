# ACadSharp.Entities.VertexFaceRecord

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.VertexFaceRecord`

Represents a ACadSharp.Entities.VertexFaceRecord entity.

Object name F:ACadSharp.DxfFileToken.EntityVertex Dxf class name F:ACadSharp.DxfSubclassMarker.PolyfaceMeshVertex

Base type: `ACadSharp.Entities.Vertex`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IVertex`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.VertexFaceRecord')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.VertexFaceRecord()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Entities.VertexFaceRecord(CSMath.IVector location)
```

Documentation inherited from: `base member`.

### Flags

```text
ACadSharp.Entities.VertexFlags Flags { get; set; }
```

Documentation inherited from: `base member`.

### Index1

```text
System.Int16 Index1 { get; set; }
```

Index 1 of the face.

**Remarks:** The start value for indexes is 1, if 0 the index will not take an effect.

### Index2

```text
System.Int16 Index2 { get; set; }
```

Index 2 of the face.

**Remarks:** The start value for indexes is 1, if 0 the index will not take an effect.

### Index3

```text
System.Int16 Index3 { get; set; }
```

Index 3 of the face.

**Remarks:** The start value for indexes is 1, if 0 the index will not take an effect.

### Index4

```text
System.Int16 Index4 { get; set; }
```

Index 4 of the face.

**Remarks:** The start value for indexes is 1, if 0 the index will not take an effect.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
