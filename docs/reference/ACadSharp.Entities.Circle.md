# ACadSharp.Entities.Circle

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Circle`

Represents a ACadSharp.Entities.Circle entity.

Object name F:ACadSharp.DxfFileToken.EntityCircle Dxf class name F:ACadSharp.DxfSubclassMarker.Circle

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`, `CSMath.Geometry.ICurve`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Circle')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Circle()
```

Default constructor.

### .ctor

```text
ACadSharp.Entities.Circle(CSMath.XYZ center, System.Double radius)
```

Initializes a new instance of the Circle class with the specified center point and radius.

- `center`: The center point of the circle.
- `radius`: The radius of the circle. Must be a non-negative value.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### PolarCoordinateRelativeToCenter

```text
CSMath.XYZ PolarCoordinateRelativeToCenter(System.Double angle)
```

Documentation inherited from: `base member`.

### PolygonalVertexes

```text
System.Collections.Generic.List[CSMath.XYZ] PolygonalVertexes(System.Int32 precision)
```

Documentation inherited from: `base member`.

### Center

```text
CSMath.XYZ Center { get; set; }
```

Specifies the center of an arc, circle, ellipse, view, or viewport.

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

### Radius

```text
System.Double Radius { get; set; }
```

Specifies the radius of an arc, circle, or position marker.

### RadiusRatio

```text
System.Double RadiusRatio { get; }
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
