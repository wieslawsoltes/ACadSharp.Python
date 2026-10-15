# ACadSharp.Objects.TableStyle.CellStyle

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.TableStyle+CellStyle`

Represents the cell style of a table cell. Cell styles are defined at the table level and can be overridden at the cell level.

A ACadSharp.Objects.TableStyle.CellStyle defines visual and layout properties such as colors, margins, borders, and text alignment for cells in a ACadSharp.Objects.TableStyle. Default cell styles are provided for data, header, and title cells.

Base type: `ACadSharp.Objects.TableStyle.ContentFormat`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.TableStyle+CellStyle')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.TableStyle.CellStyle()
```

### DataCellStyleName

```text
static System.String DataCellStyleName = _DATA
```

The name constant for the default data cell style.

### HeaderCellStyleName

```text
static System.String HeaderCellStyleName = _HEADER
```

The name constant for the default header cell style.

### TableCellStyleName

```text
static System.String TableCellStyleName = Table
```

The name constant for the default table-level cell style.

### TitleCellStyleName

```text
static System.String TitleCellStyleName = _TITLE
```

The name constant for the default title cell style.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### BackgroundColor

```text
ACadSharp.Color BackgroundColor { get; set; }
```

Gets or sets the background (fill) color of the cell content. Override applied at the cell level.

### BottomBorder

```text
ACadSharp.Objects.TableStyle.CellBorder BottomBorder { get; set; }
```

Gets or sets the bottom border style of the cell.

### BottomMargin

```text
System.Double BottomMargin { get; set; }
```

Gets or sets the bottom margin of the cell.

### CellAlignment

```text
ACadSharp.Objects.TableStyle.CellAlignmentType CellAlignment { get; set; }
```

Gets or sets the alignment of the content within a cell.

### ContentColor

```text
ACadSharp.Color ContentColor { get; }
```

Gets or sets the color of cell content. Override applied at the cell level.

### ContentLayoutFlags

```text
ACadSharp.Objects.TableStyle.CellContentLayoutFlags ContentLayoutFlags { get; set; }
```

Gets or sets the layout flags that control how content is arranged within the cell.

### DefaultDataCellStyle

```text
static ACadSharp.Objects.TableStyle.CellStyle DefaultDataCellStyle { get; }
```

Gets the default cell style used for data cells.

### DefaultHeaderCellStyle

```text
static ACadSharp.Objects.TableStyle.CellStyle DefaultHeaderCellStyle { get; }
```

Gets the default cell style used for header cells.

### DefaultTableCellStyle

```text
static ACadSharp.Objects.TableStyle.CellStyle DefaultTableCellStyle { get; }
```

Gets the default cell style used as the table's overall ("Table") style.

### DefaultTitleCellStyle

```text
static ACadSharp.Objects.TableStyle.CellStyle DefaultTitleCellStyle { get; }
```

Gets the default cell style used for title cells.

### HorizontalInsideBorder

```text
ACadSharp.Objects.TableStyle.CellBorder HorizontalInsideBorder { get; set; }
```

Gets or sets the horizontal inside border style of the cell.

### HorizontalMargin

```text
System.Double HorizontalMargin { get; set; }
```

Gets or sets the horizontal margin of the cell. Default is 0.06.

### IsFillColorOn

```text
System.Boolean IsFillColorOn { get; set; }
```

Gets or sets a value indicating whether the fill color is enabled. Override applied at the cell level.

### LeftBorder

```text
ACadSharp.Objects.TableStyle.CellBorder LeftBorder { get; set; }
```

Gets or sets the left border style of the cell.

### MarginHorizontalSpacing

```text
System.Double MarginHorizontalSpacing { get; set; }
```

Gets or sets the horizontal spacing between cell margins.

### MarginOverrideFlags

```text
ACadSharp.Objects.TableStyle.MarginFlags MarginOverrideFlags { get; set; }
```

Gets or sets the flags that indicate which margin overrides are applied.

### MarginVerticalSpacing

```text
System.Double MarginVerticalSpacing { get; set; }
```

Gets or sets the vertical spacing between cell margins.

### Name

```text
System.String Name { get; set; }
```

Gets or sets the name of the cell style.

### RightBorder

```text
ACadSharp.Objects.TableStyle.CellBorder RightBorder { get; set; }
```

Gets or sets the right border style of the cell.

### RightMargin

```text
System.Double RightMargin { get; set; }
```

Gets or sets the right margin of the cell.

### StyleClass

```text
ACadSharp.Objects.TableStyle.CellStyleClass StyleClass { get; set; }
```

Gets or sets the class of the cell style, which categorizes the style type.

### TableCellStylePropertyFlags

```text
ACadSharp.Objects.TableStyle.CellStylePropertyFlags TableCellStylePropertyFlags { get; set; }
```

Gets or sets the property flags that define which table cell style properties are applied.

### TextColor

```text
ACadSharp.Color TextColor { get; set; }
```

Gets or sets the text color of the cell content.

### TopBorder

```text
ACadSharp.Objects.TableStyle.CellBorder TopBorder { get; set; }
```

Gets or sets the top border style of the cell.

### Type

```text
ACadSharp.Objects.TableStyle.CellStyleType Type { get; set; }
```

Gets or sets the type of the cell style.

### VerticalInsideBorder

```text
ACadSharp.Objects.TableStyle.CellBorder VerticalInsideBorder { get; set; }
```

Gets or sets the vertical inside border style of the cell.

### VerticalMargin

```text
System.Double VerticalMargin { get; set; }
```

Gets or sets the vertical margin of the cell. Default is 0.06.
