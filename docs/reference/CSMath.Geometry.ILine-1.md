# CSMath.Geometry.ILine

`interface` · `ACadSharp` · CLR name: ``CSMath.Geometry.ILine`1``

No upstream type summary is available.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Geometry.ILine`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### FindIntersection

```text
T FindIntersection(CSMath.Geometry.ILine[T] line)
```

Find the intersection between 2 lines.

**Returns:** NaN if there is no intersection.

- `line`: 

### Direction

```text
T Direction { get; }
```

Direction fo the line

### Origin

```text
T Origin { get; }
```

Origin point that the line intersects with
