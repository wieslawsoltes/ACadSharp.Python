# ACadSharp.Entities.Hatch.BoundaryPath.Spline

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Hatch+BoundaryPath+Spline`

No upstream type summary is available.

Base type: `ACadSharp.Entities.Hatch.BoundaryPath.Edge`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IGeometricEntity`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Hatch+BoundaryPath+Spline')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Spline()
```

Initializes a new instance of the Spline class.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Spline(ACadSharp.Entities.Spline spline)
```

Initializes a new instance of the Spline class using the specified spline entity.

- `spline`: The spline entity that provides the data for initializing this Spline instance. Cannot be null.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.Entities.Hatch.BoundaryPath.Edge Clone()
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

Converts the spline in a list of vertexes.

**Returns:** A list vertexes that represents the spline expressed in object coordinate system.

- `precision`: Number of vertexes generated.

### ToEntity

```text
ACadSharp.Entities.Entity ToEntity()
```

Documentation inherited from: `base member`.

### ControlPoints

```text
System.Collections.Generic.List[CSMath.XYZ] ControlPoints { get; }
```

**Remarks:** Position values are only X and Y, Z represents the weight.

### Degree

```text
System.Int32 Degree { get; set; }
```

Degree.

### EndTangent

```text
CSMath.XY EndTangent { get; set; }
```

End tangent.

### FitPoints

```text
System.Collections.Generic.List[CSMath.XY] FitPoints { get; }
```

**Remarks:** Number of fit data.

### IsPeriodic

```text
System.Boolean IsPeriodic { get; set; }
```

Gets or sets a value indicating whether the spline is periodic.

**Remarks:** A periodic spline forms a closed, continuous curve where the start and end points are joined seamlessly. Setting this property to true creates a smooth, looping spline; setting it to false creates an open spline.

### IsRational

```text
System.Boolean IsRational { get; set; }
```

Gets or sets a value indicating whether the spline is rational.

### Knots

```text
System.Collections.Generic.List[System.Double] Knots { get; }
```

Number of knots.

### StartTangent

```text
CSMath.XY StartTangent { get; set; }
```

Start tangent.

### Type

```text
ACadSharp.Entities.Hatch.BoundaryPath.EdgeType Type { get; }
```

Documentation inherited from: `base member`.

### Weights

```text
System.Collections.Generic.IEnumerable[System.Double] Weights { get; }
```

Gets a collection of weights derived from the Z-coordinates of the control points.
