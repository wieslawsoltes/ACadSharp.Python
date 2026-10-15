# ACadSharp.Entities.AttributeFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.AttributeFlags`

Attribute flags.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.AttributeFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Constant

```text
static ACadSharp.Entities.AttributeFlags Constant = 2
```

This is a constant attribute.

### Hidden

```text
static ACadSharp.Entities.AttributeFlags Hidden = 1
```

Attribute is invisible (does not appear).

### None

```text
static ACadSharp.Entities.AttributeFlags None = 0
```

No flags.

### Preset

```text
static ACadSharp.Entities.AttributeFlags Preset = 8
```

Attribute is preset (no prompt during insertion).

### Verify

```text
static ACadSharp.Entities.AttributeFlags Verify = 4
```

Verification is required on input of this attribute.
