# CSMath.Geometry.Arc2D

`struct` · `ACadSharp` · CLR name: `CSMath.Geometry.Arc2D`

Represents a 2D circular arc defined by a center point, radius, and angular range.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Geometry.Arc2D')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.Geometry.Arc2D(CSMath.XY center, System.Double radius, System.Double startAngle, System.Double endAngle)
```

### FindIntersections

```text
System.Collections.Generic.IEnumerable[CSMath.XY] FindIntersections(CSMath.Geometry.Line2D line, System.Double precision = 1e-12)
```

Calculates the intersection points between this arc and a line segment.

**Returns:** An enumerable collection of intersection points. Returns an empty collection if no intersections exist.

- `line`: The line segment to test for intersection.
- `precision`: The precision value for the calculation.

### InAngularRange

```text
System.Boolean InAngularRange(CSMath.XY point)
```

Determines whether a point lies within the angular range of this arc.

**Returns:** true if the point's angle from the center falls within the arc's angular range; otherwise, false.

- `point`: The point to test.

### Center

```text
CSMath.XY Center { get; set; }
```

Gets or sets the center point of the arc.

### EndAngle

```text
System.Double EndAngle { get; set; }
```

Gets or sets the ending angle of the arc in radians.

### Radius

```text
System.Double Radius { get; set; }
```

Gets or sets the radius of the arc.

### StartAngle

```text
System.Double StartAngle { get; set; }
```

Gets or sets the starting angle of the arc in radians.
