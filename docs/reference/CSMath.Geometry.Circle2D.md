# CSMath.Geometry.Circle2D

`struct` · `ACadSharp` · CLR name: `CSMath.Geometry.Circle2D`

Represents a circle in 2D space defined by a center point and radius.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Geometry.Circle2D')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.Geometry.Circle2D(CSMath.XY center, System.Double radius)
```

Initializes a new instance of the CSMath.Geometry.Circle2D struct with a center point and radius.

- `center`: The center point of the circle.
- `radius`: The radius of the circle.

### .ctor

```text
CSMath.Geometry.Circle2D(System.Double centerX, System.Double centerY, System.Double radius)
```

Initializes a new instance of the CSMath.Geometry.Circle2D struct with center coordinates and radius.

- `centerX`: The X coordinate of the center point.
- `centerY`: The Y coordinate of the center point.
- `radius`: The radius of the circle.

### FindIntersections

```text
System.Collections.Generic.IEnumerable[CSMath.XY] FindIntersections(CSMath.Geometry.Line2D line)
```

Finds the intersection points between this circle and a line.

**Returns:** An enumerable collection of intersection points. Returns: - Empty enumerable if the line does not intersect the circle. - Single point if the line is tangent to the circle. - Two points if the line intersects the circle at two locations.

- `line`: The line to test for intersection with this circle.

### Center

```text
CSMath.XY Center { get; set; }
```

Gets or sets the center point of the circle.

### Radius

```text
System.Double Radius { get; set; }
```

Gets or sets the radius of the circle.
