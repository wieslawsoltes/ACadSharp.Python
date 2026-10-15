# ACadSharp.Entities.LwPolyline

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.LwPolyline`

Represents a ACadSharp.Entities.LwPolyline entity

Object name F:ACadSharp.DxfFileToken.EntityLwPolyline Dxf class name F:ACadSharp.DxfSubclassMarker.LwPolyline

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IPolyline`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.LwPolyline')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.LwPolyline()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Entities.LwPolyline(System.Collections.Generic.IEnumerable[ACadSharp.Entities.LwPolyline.Vertex] vertices)
```

Initializes a new instance of the ACadSharp.Entities.LwPolyline class with the specified vertices.

**Remarks:** The provided vertices are added to the polyline in the order they appear in the collection.

- `vertices`: A collection of ACadSharp.Entities.LwPolyline.Vertex objects that define the vertices of the polyline.

### .ctor

```text
ACadSharp.Entities.LwPolyline(System.Collections.Generic.IEnumerable[CSMath.IVector] vertices)
```

Initializes a new instance of the ACadSharp.Entities.LwPolyline class with the specified vertices.

**Remarks:** This constructor allows you to create a lightweight polyline by specifying its vertices as a collection of CSMath.IVector points. The vertices are internally converted to ACadSharp.Entities.LwPolyline.Vertex objects.

- `vertices`: A collection of CSMath.IVector objects that define the vertices of the polyline.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### ConstantWidth

```text
System.Double ConstantWidth { get; set; }
```

Constant width

**Remarks:** Not used if variable width (codes 40 and/or 41) is set

### Elevation

```text
System.Double Elevation { get; set; }
```

The current elevation of the object.

### Flags

```text
ACadSharp.Entities.LwPolylineFlags Flags { get; set; }
```

Polyline flags.

### IsClosed

```text
System.Boolean IsClosed { get; set; }
```

Documentation inherited from: `base member`.

### Normal

```text
CSMath.XYZ Normal { get; set; }
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

### Thickness

```text
System.Double Thickness { get; set; }
```

Specifies the distance a 2D object is extruded above or below its elevation.

### Vertices

```text
System.Collections.Generic.List[ACadSharp.Entities.LwPolyline.Vertex] Vertices { get; }
```

Vertices that form this LwPolyline
