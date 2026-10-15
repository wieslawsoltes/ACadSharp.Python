# ACadSharp.Objects.TableStyle

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.TableStyle`

Represents a ACadSharp.Objects.TableStyle object.

Object name F:ACadSharp.DxfFileToken.ObjectTableStyle Dxf class name F:ACadSharp.DxfSubclassMarker.TableStyle

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.TableStyle')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.TableStyle()
```

Initializes a new instance of the ACadSharp.Objects.TableStyle class.

### .ctor

```text
ACadSharp.Objects.TableStyle(System.String name)
```

Initializes a new instance of the ACadSharp.Objects.TableStyle class and sets the name of this style.

### DefaultName

```text
static System.String DefaultName = Standard
```

Represents the default name used when no specific name is provided.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### CellStyles

```text
System.Collections.Generic.List[ACadSharp.Objects.TableStyle.CellStyle] CellStyles { get; }
```

Gets the collection of cell styles applied to the table entity.

### DataCellStyle

```text
ACadSharp.Objects.TableStyle.CellStyle DataCellStyle { get; set; }
```

Gets the style settings applied to data cells within the table entity.

### Default

```text
static ACadSharp.Objects.TableStyle Default { get; }
```

Gets the default TableStyle.

### Description

```text
System.String Description { get; set; }
```

Table style description.

**Remarks:** 255 characters maximum.

### Flags

```text
System.Int16 Flags { get; set; }
```

Meaning unknown.

### FlowDirection

```text
ACadSharp.Objects.TableFlowDirectionType FlowDirection { get; set; }
```

Gets or sets the direction in which table rows and columns are arranged.

### HeaderCellStyle

```text
ACadSharp.Objects.TableStyle.CellStyle HeaderCellStyle { get; set; }
```

Gets the style settings applied to the header cells of the table.

### HorizontalCellMargin

```text
System.Double HorizontalCellMargin { get; set; }
```

Gets or sets the horizontal margin, in drawing units, applied to the content within each cell.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### SuppressHeaderRow

```text
System.Boolean SuppressHeaderRow { get; set; }
```

### SuppressTitle

```text
System.Boolean SuppressTitle { get; set; }
```

Gets or sets a value indicating whether the title should be suppressed.

### TableCellStyle

```text
ACadSharp.Objects.TableStyle.CellStyle TableCellStyle { get; set; }
```

### TitleCellStyle

```text
ACadSharp.Objects.TableStyle.CellStyle TitleCellStyle { get; set; }
```

### VerticalCellMargin

```text
System.Double VerticalCellMargin { get; set; }
```

Gets or sets the vertical margin, in drawing units, applied to the content within a cell.
