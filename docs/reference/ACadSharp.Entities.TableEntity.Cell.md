# ACadSharp.Entities.TableEntity.Cell

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.TableEntity+Cell`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.TableEntity+Cell')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.TableEntity.Cell()
```

### AutoFit

```text
System.Boolean AutoFit { get; set; }
```

Boolean flag indicating if the auto fit option is set for the cell.

### BlockScale

```text
System.Double BlockScale { get; set; }
```

Gets or sets the scale factor applied to the block reference.

**Remarks:** A value of 1.0 represents the original size of the block. Values greater than 1.0 increase the size, while values less than 1.0 decrease it. Negative values may mirror the block depending on the context.

### BorderHeight

```text
System.Int32 BorderHeight { get; set; }
```

Cell border height.

**Remarks:** Applicable only for merged cells.

### BorderWidth

```text
System.Int32 BorderWidth { get; set; }
```

Cell border width.

**Remarks:** Applicable only for merged cells.

### Content

```text
ACadSharp.Entities.TableEntity.CellContent Content { get; }
```

Gets the single cell content if available; otherwise, returns null.

**Remarks:** If the cell contains multiple content items or no content, this property returns null. Use this property when you expect the cell to have at most one content item.

### Contents

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.CellContent] Contents { get; }
```

Gets the collection of cell contents contained in this instance.

### CustomData

```text
System.Int32 CustomData { get; set; }
```

Gets or sets the custom data value associated with this cell.

### CustomDataCollection

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.CustomDataEntry] CustomDataCollection { get; set; }
```

Gets or sets the collection of custom data entries associated with this instance.

### EdgeFlags

```text
System.Int16 EdgeFlags { get; set; }
```

Cell flag value.

### Geometry

```text
ACadSharp.Entities.TableEntity.CellContentGeometry Geometry { get; set; }
```

Gets or sets the geometric layout information for the cell content.

### HasLinkedData

```text
System.Boolean HasLinkedData { get; set; }
```

Gets or sets a value indicating whether the entity has linked data associated with it.

### HasMultipleContent

```text
System.Boolean HasMultipleContent { get; }
```

Gets a value indicating whether the instance contains more than one content item.

### MergedValue

```text
System.Int16 MergedValue { get; set; }
```

Cell merged value.

### Rotation

```text
System.Double Rotation { get; set; }
```

Rotation value.

**Remarks:** Applicable for a block-type cell and a text-type cell.

### StateFlags

```text
ACadSharp.Entities.TableEntity.TableCellStateFlags StateFlags { get; set; }
```

Gets or sets the state flags that describe the current state of the table cell.

### Style

```text
ACadSharp.Objects.TableStyle.CellStyle Style { get; set; }
```

Gets or sets the style applied to the cell.

### StyleOverride

```text
ACadSharp.Objects.TableStyle.CellStyle StyleOverride { get; }
```

Gets or sets the style that overrides the default cell appearance.

**Remarks:** When set, this style takes precedence over any default or inherited cell styles. Use this property to apply custom formatting or visual changes to an individual cell without affecting other cells.

### ToolTip

```text
System.String ToolTip { get; set; }
```

Gets or sets the tooltip text associated with the cell, providing additional information or context when the user hovers over the cell.

### Type

```text
ACadSharp.Entities.TableEntity.CellType Type { get; set; }
```

Cell type.

### VirtualEdgeFlag

```text
System.Int16 VirtualEdgeFlag { get; set; }
```

Flag value for a virtual edge.
