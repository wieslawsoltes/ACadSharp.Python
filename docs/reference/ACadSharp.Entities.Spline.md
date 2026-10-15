# ACadSharp.Entities.Spline

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Spline`

Represents a ACadSharp.Entities.Spline entity.

Object name F:ACadSharp.DxfFileToken.EntitySpline Dxf class name F:ACadSharp.DxfSubclassMarker.Spline

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Spline')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Spline()
```

Documentation inherited from: `base member`.

### MaxDegree

```text
static System.Int16 MaxDegree = 10
```

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

### PointOnSpline

```text
CSMath.XYZ PointOnSpline(System.Double t)
```

Calculates the point on the spline at the specified parametric position.

**Returns:** The point on the spline at the specified parametric position, represented as an CSMath.XYZ object.

- `t`: The parametric position along the spline, where 0 represents the start of the spline and 1 represents the end. Must be a value between 0 and 1.

- Raises `System.ArgumentOutOfRangeException`: Thrown if t is less than 0 or greater than 1.

### PolygonalVertexes

```text
System.Collections.Generic.List[CSMath.XYZ] PolygonalVertexes(System.Int32 precision)
```

Generates a list of vertex points representing a polygonal approximation of the curve.

**Remarks:** The method calculates the vertex points by dividing the curve into segments based on the specified precision. If the curve is not closed or periodic, the last control point is explicitly added to the result.

**Returns:** A list of CSMath.XYZ objects representing the vertex points of the polygonal approximation.

- `precision`: The number of segments used to approximate the curve. Must be equal to or greater than 2.

- Raises `System.ArgumentOutOfRangeException`: Thrown if precision is less than 2.

### TryPointOnSpline

```text
System.Boolean TryPointOnSpline(System.Double t, out CSMath.XYZ point)
```

Attempts to calculate a point on the spline at the specified parameter value.

**Remarks:** This method catches any exceptions that occur during the calculation and returns false in such cases. Ensure that the parameter t is within the valid range for the spline to avoid errors.

**Returns:** true if the point was successfully calculated; otherwise, false.

- `t`: The parameter value along the spline, typically in the range [0, 1].
- `point`: When this method returns, contains the calculated point on the spline if the operation succeeds; otherwise, F:CSMath.XYZ.NaN. This parameter is passed uninitialized.

### TryPolygonalVertexes

```text
System.Boolean TryPolygonalVertexes(System.Int32 precision, out System.Collections.Generic.List[CSMath.XYZ] points)
```

Attempts to calculate the polygonal vertexes of the current object with the specified precision.

**Remarks:** This method catches and suppresses any exceptions that occur during the calculation, returning false in such cases. The points parameter will always be initialized, even if the operation fails.

**Returns:** true if the polygonal vertexes were successfully calculated; otherwise, false.

- `precision`: The level of precision to use when calculating the polygonal vertexes. Must be a positive integer.
- `points`: When this method returns, contains a list of CSMath.XYZ objects representing the calculated polygonal vertexes, if the operation succeeds; otherwise, contains an empty list.

### UpdateFromFitPoints

```text
System.Boolean UpdateFromFitPoints(System.UInt32 iterationLimit = 255)
```

Updates the spline's control points, knots, and weights based on the current fit points and tangents.

**Remarks:** This method performs the following operations: Validates the spline's degree, fit points, and knot parametrization. Generates knots and control points based on the fit points and tangents. Refines the tangents iteratively if necessary, up to the specified iteration limit. Assigns uniform weights to the control points. The method returns false if the spline's degree is not 3, if there are fewer than two fit points, if the knot parametrization is set to F:ACadSharp.Entities.KnotParametrization.Custom, or if tangent refinement fails.

**Returns:** true if the spline was successfully updated; otherwise, false.

- `iterationLimit`: The maximum number of iterations allowed for refining the tangents. Defaults to F:System.Byte.MaxValue.

### ControlPointTolerance

```text
System.Double ControlPointTolerance { get; set; }
```

Control-point tolerance.

### ControlPoints

```text
System.Collections.Generic.List[CSMath.XYZ] ControlPoints { get; }
```

Number of control points (in WCS).

### Degree

```text
System.Int32 Degree { get; set; }
```

Gets or sets the polynomial degree of the resulting spline.

**Remarks:** Valid values are 1 (linear), degree 2 (quadratic), degree 3 (cubic), and so on up to degree 10.

### EndTangent

```text
CSMath.XYZ EndTangent { get; set; }
```

End tangent—may be omitted in WCS.

### FitPoints

```text
System.Collections.Generic.List[CSMath.XYZ] FitPoints { get; }
```

Number of fit points (in WCS).

### FitTolerance

```text
System.Double FitTolerance { get; set; }
```

Fit tolerance.

### Flags

```text
ACadSharp.Entities.SplineFlags Flags { get; set; }
```

Spline flags.

### Flags1

```text
ACadSharp.Entities.SplineFlags1 Flags1 { get; set; }
```

Spline flags1.

**Remarks:** Only valid for dwg.

### HasValidKnotCount

```text
System.Boolean HasValidKnotCount { get; }
```

Gets a value indicating whether the knot vector has a valid count based on the control points, degree, and closure status of the curve.

**Remarks:** The expected knot count is calculated as the number of control points plus the degree of the curve, adjusted for whether the curve is closed.

### IsClosed

```text
System.Boolean IsClosed { get; set; }
```

Flag whether the spline is closed.

### IsPeriodic

```text
System.Boolean IsPeriodic { get; set; }
```

Gets or sets a value indicating whether the spline is periodic.

**Remarks:** A periodic spline forms a closed loop, where the start and end points are connected seamlessly. Setting this property updates the internal flags to reflect the periodicity of the spline.

### KnotParametrization

```text
ACadSharp.Entities.KnotParametrization KnotParametrization { get; set; }
```

Knot parameters.

### KnotTolerance

```text
System.Double KnotTolerance { get; set; }
```

Knot tolerance.

### Knots

```text
System.Collections.Generic.List[System.Double] Knots { get; }
```

Number of knots.

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.

**Remarks:** Omitted if the spline is non-planar.

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

### StartTangent

```text
CSMath.XYZ StartTangent { get; set; }
```

Start tangent—may be omitted in WCS.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Weights

```text
System.Collections.Generic.List[System.Double] Weights { get; }
```

Weight(if not 1); with multiple group pairs, they are present if all are not 1.
