# ACadSharp.Entities.Point

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Point`

Represents a ACadSharp.Entities.Point entity.

Object name F:ACadSharp.DxfFileToken.EntityPoint Dxf class name F:ACadSharp.DxfSubclassMarker.Point

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Point')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Point()
```

Default constructor

### .ctor

```text
ACadSharp.Entities.Point(CSMath.XYZ location)
```

Create a point in a specific location

- `location`: 

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

### Location

```text
CSMath.XYZ Location { get; set; }
```

Point location(in WCS)

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

### Rotation

```text
System.Double Rotation { get; set; }
```

Specifies the rotation angle for the object.

**Value:** The rotation angle in radians.

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
