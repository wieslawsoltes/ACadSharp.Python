# CSMath.Geometry.Segment2D

`struct` · `ACadSharp` · CLR name: `CSMath.Geometry.Segment2D`

No upstream type summary is available.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

Interfaces: `CSMath.Geometry.ILine[CSMath.XY]`, `System.IEquatable[CSMath.Geometry.Segment2D]`.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Geometry.Segment2D')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.Geometry.Segment2D(CSMath.XY origin, CSMath.XY end)
```

### Equals

```text
System.Boolean Equals(CSMath.Geometry.Segment2D other)
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

Calculates the intersection point of the current line segment and the specified line.

**Returns:** The intersection point as an XY object, or XY.NaN if there is no intersection within the bounds of the current segment.

- `line`: The line to intersect with.

### GetHashCode

```text
System.Int32 GetHashCode()
```

Documentation inherited from: `base member`.

### Direction

```text
CSMath.XY Direction { get; }
```

Documentation inherited from: `base member`.

### End

```text
CSMath.XY End { get; set; }
```

Gets or sets the end point of the segment in the XY plane.

### Origin

```text
CSMath.XY Origin { get; set; }
```

Documentation inherited from: `base member`.
