# ACadSharp.Entities.MLineFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.MLineFlags`

Flags (bit-coded values).

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.MLineFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Closed

```text
static ACadSharp.Entities.MLineFlags Closed = 2
```

Closed

### HasVertices

```text
static ACadSharp.Entities.MLineFlags HasVertices = 1
```

Has at least one vertex (code 72 is greater than 0)

### NoEndCaps

```text
static ACadSharp.Entities.MLineFlags NoEndCaps = 8
```

Suppress end caps

### NoStartCaps

```text
static ACadSharp.Entities.MLineFlags NoStartCaps = 4
```

Suppress start caps

### None

```text
static ACadSharp.Entities.MLineFlags None = 0
```

No flags set.
