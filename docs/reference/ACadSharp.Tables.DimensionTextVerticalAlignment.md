# ACadSharp.Tables.DimensionTextVerticalAlignment

`enum` · `ACadSharp` · CLR name: `ACadSharp.Tables.DimensionTextVerticalAlignment`

Controls the placement of dimension text.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.DimensionTextVerticalAlignment')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Above

```text
static ACadSharp.Tables.DimensionTextVerticalAlignment Above = 1
```

Places the dimension text above the dimension line except when the dimension line is not horizontal and text inside the extension lines is forced horizontal (ACadSharp.Tables.DimensionStyle.TextInsideHorizontal = true). The distance from the dimension line to the baseline of the lowest line of text is the current ACadSharp.Tables.DimensionStyle.DimensionLineGap value.

### Below

```text
static ACadSharp.Tables.DimensionTextVerticalAlignment Below = 4
```

Places the dimension text under the dimension line.

### Centered

```text
static ACadSharp.Tables.DimensionTextVerticalAlignment Centered = 0
```

Centers the dimension text between the two parts of the dimension line.

### JIS

```text
static ACadSharp.Tables.DimensionTextVerticalAlignment JIS = 3
```

Places the dimension text to conform to a Japanese Industrial Standards (JIS) representation.

### Outside

```text
static ACadSharp.Tables.DimensionTextVerticalAlignment Outside = 2
```

Places the dimension text on the side of the dimension line farthest away from the first defining point.
