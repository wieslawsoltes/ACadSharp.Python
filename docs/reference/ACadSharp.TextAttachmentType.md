# ACadSharp.TextAttachmentType

`enum` · `ACadSharp` · CLR name: `ACadSharp.TextAttachmentType`

Text attachment type, controls how the text label of a ACadSharp.Entities.MultiLeader is to placed relative to the landing point.

Values 0-8 are used for the left/right attachment points (attachment direction is horizontal),values 9-10 are used for the top/bottom attachment points (attachment direction is vertical).

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.TextAttachmentType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### BottomLine

```text
static ACadSharp.TextAttachmentType BottomLine = 5
```

Bottom text line.

### BottomOfBottomLine

```text
static ACadSharp.TextAttachmentType BottomOfBottomLine = 4
```

Bottom of bottom text line.

### BottomOfTopLineUnderlineBottomLine

```text
static ACadSharp.TextAttachmentType BottomOfTopLineUnderlineBottomLine = 6
```

Bottom of top text line. Underline bottom line.

### BottomOfTopLineUnderlineTopLine

```text
static ACadSharp.TextAttachmentType BottomOfTopLineUnderlineTopLine = 7
```

Bottom of top text line. Underline top line.

### BottomofTopLineUnderlineAll

```text
static ACadSharp.TextAttachmentType BottomofTopLineUnderlineAll = 8
```

Bottom of top text line. Underline all content.

### CenterOfText

```text
static ACadSharp.TextAttachmentType CenterOfText = 9
```

Center of text (y-coordinate only).

### CenterOfTextOverline

```text
static ACadSharp.TextAttachmentType CenterOfTextOverline = 10
```

Center of text (y-coordinate only), and overline top/underline bottom content.

### MiddleOfBottomLine

```text
static ACadSharp.TextAttachmentType MiddleOfBottomLine = 3
```

Middle of bottom text line.

### MiddleOfText

```text
static ACadSharp.TextAttachmentType MiddleOfText = 2
```

Middle of text.

### MiddleOfTopLine

```text
static ACadSharp.TextAttachmentType MiddleOfTopLine = 1
```

Middle of top text line.

### TopOfTopLine

```text
static ACadSharp.TextAttachmentType TopOfTopLine = 0
```

Top of top text line.
