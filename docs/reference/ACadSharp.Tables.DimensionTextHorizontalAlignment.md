# ACadSharp.Tables.DimensionTextHorizontalAlignment

`enum` · `ACadSharp` · CLR name: `ACadSharp.Tables.DimensionTextHorizontalAlignment`

Controls the vertical placement of dimension text in relation to the dimension line.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.DimensionTextHorizontalAlignment')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Centered

```text
static ACadSharp.Tables.DimensionTextHorizontalAlignment Centered = 0
```

Centers the dimension text along the dimension line between the extension lines.

### Left

```text
static ACadSharp.Tables.DimensionTextHorizontalAlignment Left = 1
```

Left-justifies the text with the first extension line along the dimension line.

### OverFirstExtLine

```text
static ACadSharp.Tables.DimensionTextHorizontalAlignment OverFirstExtLine = 3
```

Positions the text over or along the first extension line.

### OverSecondExtLine

```text
static ACadSharp.Tables.DimensionTextHorizontalAlignment OverSecondExtLine = 4
```

Positions the text over or along the second extension line.

### Right

```text
static ACadSharp.Tables.DimensionTextHorizontalAlignment Right = 2
```

Right-justifies the text with the second extension line along the dimension line.
