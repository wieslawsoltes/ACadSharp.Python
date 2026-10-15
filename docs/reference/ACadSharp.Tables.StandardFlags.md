# ACadSharp.Tables.StandardFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Tables.StandardFlags`

Standard flags for tables

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.StandardFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### None

```text
static ACadSharp.Tables.StandardFlags None = 0
```

None

### Referenced

```text
static ACadSharp.Tables.StandardFlags Referenced = 64
```

If set, the table entry was referenced by at least one entity in the drawing the last time the drawing was edited.

### XrefDependent

```text
static ACadSharp.Tables.StandardFlags XrefDependent = 16
```

If set, table entry is externally dependent on an xRef

### XrefResolved

```text
static ACadSharp.Tables.StandardFlags XrefResolved = 32
```

If both this bit and bit 16 are set, the externally dependent xRef has been successfully resolved
