# ACadSharp.Entities.Hatch.BoundaryPath.Ellipse

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Hatch+BoundaryPath+Ellipse`

No upstream type summary is available.

Base type: `ACadSharp.Entities.Hatch.BoundaryPath.Edge`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IGeometricEntity`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Hatch+BoundaryPath+Ellipse')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Ellipse()
```

Initializes a new instance of the Ellipse class.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Ellipse(ACadSharp.Entities.Ellipse ellipse)
```

Initializes a new instance of the Ellipse class based on the specified ellipse entity.

**Remarks:** The constructed Ellipse will represent a full ellipse if the source entity indicates so; otherwise, it will use the start and end parameters from the source. The orientation and axes are derived from the source entity's properties.

- `ellipse`: The source ellipse entity containing the geometric parameters to initialize this instance. Cannot be null.

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

Converts the ellipse in a list of vertexes.

**Returns:** A list vertexes that represents the arc expressed in object coordinate system.

- `precision`: Number of vertexes generated.

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

Counterclockwise flag.

### EndAngle

```text
System.Double EndAngle { get; set; }
```

End angle.

### MajorAxis

```text
System.Double MajorAxis { get; }
```

Length of the major axis.

### MajorAxisEndPoint

```text
CSMath.XY MajorAxisEndPoint { get; set; }
```

Endpoint of major axis relative to center point (in OCS).

### MinorAxis

```text
System.Double MinorAxis { get; }
```

Length of the minor axis.

### RadiusRatio

```text
System.Double RadiusRatio { get; set; }
```

Length of minor axis (percentage of major axis length).

### Rotation

```text
System.Double Rotation { get; }
```

Rotation of the major axis from the world X axis.

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
