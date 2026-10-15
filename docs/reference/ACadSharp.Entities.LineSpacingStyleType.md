# ACadSharp.Entities.LineSpacingStyleType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.LineSpacingStyleType`

Line spacing style for Multiline text and Dimensions.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.LineSpacingStyleType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### AtLeast

```text
static ACadSharp.Entities.LineSpacingStyleType AtLeast = 1
```

Taller characters will override.

### Exact

```text
static ACadSharp.Entities.LineSpacingStyleType Exact = 2
```

Taller characters will not override.

### None

```text
static ACadSharp.Entities.LineSpacingStyleType None = 0
```

None.
