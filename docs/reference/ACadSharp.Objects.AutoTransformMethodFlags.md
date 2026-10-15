# ACadSharp.Objects.AutoTransformMethodFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Objects.AutoTransformMethodFlags`

No upstream type summary is available.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.AutoTransformMethodFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### IncludeCurrentBlock

```text
static ACadSharp.Objects.AutoTransformMethodFlags IncludeCurrentBlock = 4
```

Include current block transform in mapper transform.

### NoAutoTransform

```text
static ACadSharp.Objects.AutoTransformMethodFlags NoAutoTransform = 1
```

No auto transform.

### None

```text
static ACadSharp.Objects.AutoTransformMethodFlags None = 0
```

None.

### ScaleMapper

```text
static ACadSharp.Objects.AutoTransformMethodFlags ScaleMapper = 2
```

Scale mapper to current entity extents; translate mapper to entity origin.
