# ACadSharp.Entities.Hatch.BoundaryPath.Arc

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Hatch+BoundaryPath+Arc`

No upstream type summary is available.

Base type: `ACadSharp.Entities.Hatch.BoundaryPath.Edge`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IGeometricEntity`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Hatch+BoundaryPath+Arc')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Arc()
```

Initializes a new instance of the Arc class.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Arc(ACadSharp.Entities.Circle circle)
```

Initializes a new instance of the Arc class based on the specified circle or arc geometry.

**Remarks:** If the provided circle is an arc, the arc's center, radius, start angle, and end angle are used. If the provided circle is a full circle, the arc will represent a full circle with a start angle of 0 and an end angle of 2π. The arc is always constructed in a counterclockwise direction.

- `circle`: The circle or arc from which to construct the arc. Must not be null.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### FindIntersections

```text
System.Collections.Generic.IEnumerable[CSMath.XY] FindIntersections(CSMath.Geometry.Line2D line)
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

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

### ToEntity

```text
ACadSharp.Entities.Entity ToEntity()
```

Documentation inherited from: `base member`.

### Center

```text
CSMath.XY Center { get; set; }
```

Center point (in OCS).

### CounterClockWise

```text
System.Boolean CounterClockWise { get; set; }
```

Is counterclockwise flag.

### EndAngle

```text
System.Double EndAngle { get; set; }
```

End angle.

### Radius

```text
System.Double Radius { get; set; }
```

Radius.

**Remarks:** For the ellipse this is the length of minor axis (percentage of major axis length).

### StartAngle

```text
System.Double StartAngle { get; set; }
```

Start angle.

### Type

```text
ACadSharp.Entities.Hatch.BoundaryPath.EdgeType Type { get; }
```

Documentation inherited from: `base member`.
