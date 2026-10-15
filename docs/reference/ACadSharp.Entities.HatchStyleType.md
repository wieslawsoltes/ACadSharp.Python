# ACadSharp.Entities.HatchStyleType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.HatchStyleType`

Hatch pattern style.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.HatchStyleType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Ignore

```text
static ACadSharp.Entities.HatchStyleType Ignore = 2
```

Hatch through entire area.

### Normal

```text
static ACadSharp.Entities.HatchStyleType Normal = 0
```

Hatch "odd parity" area.

### Outer

```text
static ACadSharp.Entities.HatchStyleType Outer = 1
```

Hatch outermost area only.
