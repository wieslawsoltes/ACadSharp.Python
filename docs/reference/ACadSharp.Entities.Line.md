# ACadSharp.Entities.Line

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Line`

Represents a ACadSharp.Entities.Line entity.

Object name F:ACadSharp.DxfFileToken.EntityLine Dxf class name F:ACadSharp.DxfSubclassMarker.Line

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Line')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Line()
```

Default constructor.

### .ctor

```text
ACadSharp.Entities.Line(CSMath.IVector start, CSMath.IVector end)
```

Constructor with the start and end.

- `start`: 
- `end`: 

### .ctor

```text
ACadSharp.Entities.Line(CSMath.XYZ start, CSMath.XYZ end)
```

Constructor with the start and end.

- `start`: 
- `end`: 

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

### ToSegment3D

```text
CSMath.Geometry.Segment3D ToSegment3D()
```

### EndPoint

```text
CSMath.XYZ EndPoint { get; set; }
```

A 3D coordinate representing the end point of the object.

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

### StartPoint

```text
CSMath.XYZ StartPoint { get; set; }
```

A 3D coordinate representing the start point of the object.

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
