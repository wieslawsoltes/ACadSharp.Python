# ACadSharp.Tables.LayerFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Tables.LayerFlags`

Standard layer flags (bit-coded values).

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.LayerFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Frozen

```text
static ACadSharp.Tables.LayerFlags Frozen = 1
```

Layer is frozen; otherwise layer is thawed

### FrozenNewViewports

```text
static ACadSharp.Tables.LayerFlags FrozenNewViewports = 2
```

Layer is frozen by default in new viewports

### Locked

```text
static ACadSharp.Tables.LayerFlags Locked = 4
```

Layer is locked

### None

```text
static ACadSharp.Tables.LayerFlags None = 0
```

None

### Referenced

```text
static ACadSharp.Tables.LayerFlags Referenced = 64
```

If set, the table entry was referenced by at least one entity in the drawing the last time the drawing was edited.

### XrefDependent

```text
static ACadSharp.Tables.LayerFlags XrefDependent = 16
```

If set, table entry is externally dependent on an xRef

### XrefResolved

```text
static ACadSharp.Tables.LayerFlags XrefResolved = 32
```

If both this bit and bit 16 are set, the externally dependent xRef has been successfully resolved
