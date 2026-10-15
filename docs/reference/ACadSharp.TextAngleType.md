# ACadSharp.TextAngleType

`enum` · `ACadSharp` · CLR name: `ACadSharp.TextAngleType`

No upstream type summary is available.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.TextAngleType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Horizontal

```text
static ACadSharp.TextAngleType Horizontal = 1
```

Text is horizontal

### Optimized

```text
static ACadSharp.TextAngleType Optimized = 2
```

Text angle is equal to last leader line segment angle, but potentially rotated by 180 degrees so the right side is up for readability.

### ParllelToLastLeaderLine

```text
static ACadSharp.TextAngleType ParllelToLastLeaderLine = 0
```

Text angle is equal to last leader line segment angle
