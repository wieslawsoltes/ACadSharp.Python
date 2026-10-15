# ACadSharp.Entities.PolyfaceMesh

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.PolyfaceMesh`

Represents a ACadSharp.Entities.PolyfaceMesh entity.

Object name F:ACadSharp.DxfFileToken.EntityPolyline Dxf class name F:ACadSharp.DxfSubclassMarker.PolyfaceMesh

Base type: `ACadSharp.Entities.Polyline[ACadSharp.Entities.VertexFaceMesh]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IPolyline`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.PolyfaceMesh')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.PolyfaceMesh()
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### Faces

```text
ACadSharp.CadObjectCollection[ACadSharp.Entities.VertexFaceRecord] Faces { get; }
```

Face records with the triangle indexes.

### Flags

```text
ACadSharp.Entities.PolylineFlags Flags { get; set; }
```

Documentation inherited from: `base member`.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

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
