# ACadSharp.Entities.HookLineDirection

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.HookLineDirection`

Hook line direction for leaders.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.HookLineDirection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Opposite

```text
static ACadSharp.Entities.HookLineDirection Opposite = 0
```

Hook line (or end of tangent for a splined leader) is the opposite direction from the horizontal vector.

### Same

```text
static ACadSharp.Entities.HookLineDirection Same = 1
```

Hook line (or end of tangent for a splined leader) is the same direction as horizontal vector.
