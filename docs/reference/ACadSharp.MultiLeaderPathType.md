# ACadSharp.MultiLeaderPathType

`enum` · `ACadSharp` · CLR name: `ACadSharp.MultiLeaderPathType`

Controls the way the leader is drawn.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.MultiLeaderPathType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Invisible

```text
static ACadSharp.MultiLeaderPathType Invisible = 0
```

Invisible leader

### Spline

```text
static ACadSharp.MultiLeaderPathType Spline = 2
```

Draws the leader line as a spline

### StraightLineSegments

```text
static ACadSharp.MultiLeaderPathType StraightLineSegments = 1
```

Draws the leader line as a set of straight line segments
