# ACadSharp.Entities.LeaderPathType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.LeaderPathType`

Controls the way the leader is drawn.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.LeaderPathType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Spline

```text
static ACadSharp.Entities.LeaderPathType Spline = 1
```

Draws the leader line as a spline.

### StraightLineSegments

```text
static ACadSharp.Entities.LeaderPathType StraightLineSegments = 0
```

Draws the leader line as a set of straight line segments.
