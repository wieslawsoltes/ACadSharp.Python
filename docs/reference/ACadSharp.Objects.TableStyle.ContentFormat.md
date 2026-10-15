# ACadSharp.Objects.TableStyle.ContentFormat

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.TableStyle+ContentFormat`

Represents the content format settings for a table cell in AutoCAD. This class encapsulates various properties that define how the content of a cell is formatted, including alignment, color, rotation, scale, text style, and value formatting.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.TableStyle+ContentFormat')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.TableStyle.ContentFormat()
```

### Alignment

```text
System.Int32 Alignment { get; set; }
```

Gets or sets the alignment code for the cell content.

**Remarks:** This is a bit-coded value that defines the horizontal and vertical alignment of the content within the cell.

### Color

```text
ACadSharp.Color Color { get; set; }
```

Gets or sets the content color.

### HasData

```text
System.Boolean HasData { get; set; }
```

Gets or sets a value indicating whether this content format contains data.

### PropertyFlags

```text
System.Int32 PropertyFlags { get; set; }
```

Gets or sets the property flags for the content format.

### PropertyOverrideFlags

```text
ACadSharp.Objects.TableStyle.CellStylePropertyFlags PropertyOverrideFlags { get; set; }
```

Gets or sets the property override flags for the cell style.

### Rotation

```text
System.Double Rotation { get; set; }
```

Gets or sets the rotation angle of the content.

### Scale

```text
System.Double Scale { get; set; }
```

Gets or sets the scale applied to the content.

### TextHeight

```text
System.Double TextHeight { get; set; }
```

Gets or sets the text height for the content.

### TextStyle

```text
ACadSharp.Tables.TextStyle TextStyle { get; set; }
```

Gets or sets the text style used by the content.

### ValueDataType

```text
System.Int32 ValueDataType { get; set; }
```

Gets or sets the value data type.

### ValueFormatString

```text
System.String ValueFormatString { get; set; }
```

Gets or sets the value format string.

### ValueUnitType

```text
System.Int32 ValueUnitType { get; set; }
```

Gets or sets the value unit type.
