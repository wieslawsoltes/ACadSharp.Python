# ACadSharp.Entities.Arc

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Arc`

Represents a ACadSharp.Entities.Arc entity.

Object name F:ACadSharp.DxfFileToken.EntityArc Dxf class name F:ACadSharp.DxfSubclassMarker.Arc

Base type: `ACadSharp.Entities.Circle`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`, `CSMath.Geometry.ICurve`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Arc')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Arc()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Entities.Arc(CSMath.XYZ center, CSMath.XYZ start, CSMath.XYZ end)
```

Initializes a new instance of the Arc class that passes through the specified center, start, and end points, using the default axis of rotation.

**Remarks:** This constructor creates an arc in the plane defined by the provided points, using the Z axis as the default normal. To specify a different axis of rotation, use the constructor that accepts an axis parameter.

- `center`: The center point of the arc.
- `start`: The start point of the arc.
- `end`: The end point of the arc.

### .ctor

```text
ACadSharp.Entities.Arc(CSMath.XYZ center, CSMath.XYZ start, CSMath.XYZ end, CSMath.XYZ normal)
```

Initializes a new instance of the Arc class that passes through the specified start and end points, is centered at the given point, and lies in the plane defined by the specified normal vector.

**Remarks:** The arc is constructed in the plane defined by the normal vector, with its center at the specified point. The start and end points determine the angular span of the arc. The direction from start to end is determined by the order of the points and the orientation of the normal vector.

- `center`: The center point of the arc. Defines the origin of the arc's circle.
- `start`: The start point of the arc. Must lie on the circle defined by the center and radius.
- `end`: The end point of the arc. Must lie on the circle defined by the center and radius.
- `normal`: The normal vector defining the plane in which the arc lies. Must be a non-zero vector.

### .ctor

```text
ACadSharp.Entities.Arc(CSMath.XYZ center, System.Double radius, System.Double start, System.Double end)
```

Initializes a new instance of the ACadSharp.Entities.Arc class.

- `center`: 
- `radius`: 
- `start`: 
- `end`: 

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### CreateFromBulge

```text
static ACadSharp.Entities.Arc CreateFromBulge(CSMath.XY p1, CSMath.XY p2, System.Double bulge)
```

Creates an arc using 2 points and a bulge.

- `p1`: 
- `p2`: 
- `bulge`: 

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### GetCenter

```text
static CSMath.XY GetCenter(CSMath.XY start, CSMath.XY end, System.Double bulge)
```

Get the center coordinate from a start, end an a bulge value.

**Returns:** Center of the represented circle.

- `start`: Start point.
- `end`: Ending point.
- `bulge`: Bulge.

### GetCenter

```text
static CSMath.XY GetCenter(CSMath.XY start, CSMath.XY end, System.Double bulge, out System.Double radius)
```

Get the center coordinate from a start, end an a bulge value.

**Returns:** Center of the represented circle.

- `start`: Start point.
- `end`: Ending point.
- `bulge`: Bulge.
- `radius`: Radius of the circle.

### GetEndVertices

```text
System.Void GetEndVertices(out CSMath.XYZ start, out CSMath.XYZ end)
```

Process the 2 points limiting the arc segment

- `start`: Start point of the arc segment
- `end`: End point of the arc segment

### PolygonalVertexes

```text
System.Collections.Generic.List[CSMath.XYZ] PolygonalVertexes(System.Int32 precision)
```

Converts the arc in a list of vertexes.

**Returns:** A list vertexes that represents the arc expressed in object coordinate system.

- `precision`: Number of vertexes generated.

### ToArc2D

```text
CSMath.Geometry.Arc2D ToArc2D()
```

### EndAngle

```text
System.Double EndAngle { get; set; }
```

The end angle in radians.

**Remarks:** Use 6.28 radians to specify a closed circle or ellipse.

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

### StartAngle

```text
System.Double StartAngle { get; set; }
```

The start angle in radians.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Sweep

```text
System.Double Sweep { get; }
```

Sweep of the arc, in radians.
