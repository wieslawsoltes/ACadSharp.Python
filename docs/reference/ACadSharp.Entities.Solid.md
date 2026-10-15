# ACadSharp.Entities.Solid

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Solid`

Represents a ACadSharp.Entities.Solid entity.

Object name F:ACadSharp.DxfFileToken.EntitySolid Dxf class name F:ACadSharp.DxfSubclassMarker.Solid

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Solid')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Solid()
```

Initializes a new instance of the ACadSharp.Entities.Solid class.

### .ctor

```text
ACadSharp.Entities.Solid(CSMath.XYZ firstCorner, CSMath.XYZ secondCorner, CSMath.XYZ thirdCorner)
```

Initializes a new instance of the Solid class using the specified three corner points.

**Remarks:** The three corner points must be specified to define the base of the solid. The order and position of the points affect the orientation and shape of the resulting solid.

- `firstCorner`: The first corner point of the solid. Defines one vertex of the solid's base.
- `secondCorner`: The second corner point of the solid. Defines a second vertex of the solid's base.
- `thirdCorner`: The third corner point of the solid. Defines a third vertex of the solid's base.

### .ctor

```text
ACadSharp.Entities.Solid(CSMath.XYZ firstCorner, CSMath.XYZ secondCorner, CSMath.XYZ thirdCorner, CSMath.XYZ fourthCorner)
```

Initializes a new instance of the Solid class using the specified corner points.

**Remarks:** The four corner points define the base of the solid in 3D space. The order of the points determines the orientation of the solid.

- `firstCorner`: The first corner point of the solid. Defines one vertex of the quadrilateral base.
- `secondCorner`: The second corner point of the solid. Must be distinct from the other corners.
- `thirdCorner`: The third corner point of the solid. Must be distinct from the other corners.
- `fourthCorner`: The fourth corner point of the solid. Must be distinct from the other corners.

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

### FirstCorner

```text
CSMath.XYZ FirstCorner { get; set; }
```

First corner.

### FourthCorner

```text
CSMath.XYZ FourthCorner { get; set; }
```

Fourth corner.

**Remarks:** If only three corners are entered to define the SOLID, then the fourth corner coordinate is the same as the third.

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

### SecondCorner

```text
CSMath.XYZ SecondCorner { get; set; }
```

Second corner.

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

### ThirdCorner

```text
CSMath.XYZ ThirdCorner { get; set; }
```

Third corner.
