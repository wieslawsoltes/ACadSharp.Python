# CSMath.Geometry.LineExtensions

`class` · `ACadSharp` · CLR name: `CSMath.Geometry.LineExtensions`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Geometry.LineExtensions')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### CreateFromPoints

```text
static T CreateFromPoints[T, R](R pt1, R pt2)
```

Creates a line from 2 points, the first point is the origin and the second point is used to calculate the direction.

**Returns:** A new instance of the specified line type.

- `pt1`: The first point, which will be the origin of the line.
- `pt2`: The second point, used to calculate the direction of the line.

### IsPointOnLine

```text
static System.Boolean IsPointOnLine[T](CSMath.Geometry.ILine[T] line, T point)
```

Determines whether the specified point is on the line, or not.

**Returns:** True if the point is on the line; otherwise, false.

- `line`: The line to check against.
- `point`: The point to check.

### TryFindIntersection

```text
static System.Boolean TryFindIntersection[T, S, R](T line1, S line2, out R intersection)
```

Tries to find the intersection between 2 lines.

**Returns:** True if the intersection is found.

- `line1`: The first line.
- `line2`: The second line.
- `intersection`: The intersection point, if found.
