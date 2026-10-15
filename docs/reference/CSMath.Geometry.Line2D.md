# CSMath.Geometry.Line2D

`struct` · `ACadSharp` · CLR name: `CSMath.Geometry.Line2D`

Represents a 2D line defined by an origin point and a direction vector.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

Interfaces: `CSMath.Geometry.ILine[CSMath.XY]`, `System.IEquatable[CSMath.Geometry.Line2D]`.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Geometry.Line2D')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.Geometry.Line2D(CSMath.XY origin, CSMath.XY direction)
```

### Equals

```text
System.Boolean Equals(CSMath.Geometry.Line2D other)
```

Documentation inherited from: `base member`.

### Equals

```text
System.Boolean Equals(System.Object obj)
```

Documentation inherited from: `base member`.

### FindIntersection

```text
CSMath.XY FindIntersection(CSMath.Geometry.ILine[CSMath.XY] line)
```

Documentation inherited from: `base member`.

### FromPoints

```text
static CSMath.Geometry.Line2D FromPoints(CSMath.XY pt1, CSMath.XY pt2)
```

Creates a line from 2 points, the first point is the origin and the second point is used to calculate the direction.

**Returns:** A new instance of the CSMath.Geometry.Line2D class.

- `pt1`: The first point, which will be the origin of the line.
- `pt2`: The second point, used to calculate the direction of the line.

### FromSegment2D

```text
static CSMath.Geometry.Line2D FromSegment2D(CSMath.Geometry.Segment2D segment)
```

Creates a line from a 2D segment, using the segment's origin and direction.

**Returns:** A new instance of the CSMath.Geometry.Line2D class.

- `segment`: The 2D segment used to create the line.

### GetHashCode

```text
System.Int32 GetHashCode()
```

Documentation inherited from: `base member`.

### PointInLine

```text
CSMath.XY PointInLine(System.Double lambda)
```

Determines if a given point lies on the line.

**Returns:** The point on the line corresponding to the given parameter value.

- `lambda`: The parameter value along the line.

### Direction

```text
CSMath.XY Direction { get; set; }
```

Documentation inherited from: `base member`.

### Offset

```text
System.Double Offset { get; }
```

Gets the y-intercept of the line, calculated from the origin and slope.

### Origin

```text
CSMath.XY Origin { get; set; }
```

Documentation inherited from: `base member`.

### Slope

```text
System.Double Slope { get; }
```

Gets the slope of the line based on its direction vector.
