# ACadSharp.Entities.Polyline2D

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Polyline2D`

Represents a ACadSharp.Entities.Polyline2D entity.

Object name F:ACadSharp.DxfFileToken.EntityPolyline Dxf class name F:ACadSharp.DxfSubclassMarker.Polyline

Base type: `ACadSharp.Entities.Polyline[ACadSharp.Entities.Vertex2D]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IPolyline`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Polyline2D')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Polyline2D()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Entities.Polyline2D(System.Collections.Generic.IEnumerable[ACadSharp.Entities.Vertex2D] vertices, System.Boolean isClosed)
```

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
