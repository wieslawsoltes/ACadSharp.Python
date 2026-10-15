# ACadSharp.Entities.PolygonMesh

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.PolygonMesh`

Represents a ACadSharp.Entities.PolygonMesh entity.

Object name F:ACadSharp.DxfFileToken.EntityPolyline Dxf class name F:ACadSharp.DxfSubclassMarker.PolygonMesh

Base type: `ACadSharp.Entities.Polyline[ACadSharp.Entities.PolygonMeshVertex]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IPolyline`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.PolygonMesh')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.PolygonMesh()
```

### Flags

```text
ACadSharp.Entities.PolylineFlags Flags { get; set; }
```

Documentation inherited from: `base member`.

### MSmoothSurfaceDensity

```text
System.Int16 MSmoothSurfaceDensity { get; set; }
```

Gets or sets the number of smoothing surface density divisions for the M direction.

### MVertexCount

```text
System.Int16 MVertexCount { get; set; }
```

Gets or sets the number of vertices in the M direction.

### NSmoothSurfaceDensity

```text
System.Int16 NSmoothSurfaceDensity { get; set; }
```

Gets or sets the number of smoothing surface density divisions for the N direction.

### NVertexCount

```text
System.Int16 NVertexCount { get; set; }
```

Gets or sets the number of vertices in the N direction.

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
