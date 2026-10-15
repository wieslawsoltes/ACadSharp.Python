# ACadSharp.Extensions.PolylineExtensions

`class` · `ACadSharp` · CLR name: `ACadSharp.Extensions.PolylineExtensions`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Extensions.PolylineExtensions')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Explode

```text
static System.Collections.Generic.IEnumerable[ACadSharp.Entities.Entity] Explode(ACadSharp.Entities.IPolyline polyline)
```

Explodes the polyline into a collection of entities formed by ACadSharp.Entities.Line and ACadSharp.Entities.Arc.

### GetPoints

```text
static System.Collections.Generic.IEnumerable[T] GetPoints[T](ACadSharp.Entities.IPolyline polyline)
```

Retrieves the points of the specified polyline as a sequence of the specified vector type.

**Returns:** An System.Collections.Generic.IEnumerable`1 containing the points of the polyline, converted to the specified vector type.

- `polyline`: The polyline from which to retrieve the points. Cannot be null.

### GetPoints

```text
static System.Collections.Generic.IEnumerable[T] GetPoints[T](ACadSharp.Entities.IPolyline polyline, System.Int32 precision)
```

Generates a collection of points representing the vertices of the specified polyline, including interpolated points for arcs based on the given precision.

**Remarks:** This method processes the vertices of the polyline and generates a sequence of points. For straight segments, the start and end points are included. For arc segments, additional points are interpolated based on the specified precision. If the polyline is closed, the method ensures continuity by connecting the last vertex to the first.

**Returns:** An System.Collections.Generic.IEnumerable`1 containing the points of the polyline, including interpolated points for arcs.

- `polyline`: The polyline from which to extract points. The polyline may contain straight segments and arcs.
- `precision`: The number of points to generate for each arc segment. Must be equal to or greater than 2.

- Raises `System.ArgumentOutOfRangeException`: Thrown if precision is less than 2.
