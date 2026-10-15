# ACadSharp.Tables.LineTypeShapeFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Tables.LineTypeShapeFlags`

Represents a line type complex element type.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.LineTypeShapeFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### None

```text
static ACadSharp.Tables.LineTypeShapeFlags None = 0
```

None.

### RotationIsAbsolute

```text
static ACadSharp.Tables.LineTypeShapeFlags RotationIsAbsolute = 1
```

Text is rotated 0 degrees, otherwise it follows the segment.

### Shape

```text
static ACadSharp.Tables.LineTypeShapeFlags Shape = 4
```

Complex shape code holds the index into the text area of the string to be drawn.

### Text

```text
static ACadSharp.Tables.LineTypeShapeFlags Text = 2
```

Complex shape code holds the index of the shape to be drawn.
