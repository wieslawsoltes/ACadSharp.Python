# ACadSharp.Entities.TableEntity

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.TableEntity`

Represents a ACadSharp.Entities.TableEntity entity.

Object name F:ACadSharp.DxfFileToken.EntityTable Dxf class name F:ACadSharp.DxfSubclassMarker.TableEntity

Base type: `ACadSharp.Entities.Insert`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.TableEntity')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.TableEntity()
```

Initializes a new instance of the ACadSharp.Entities.TableEntity class.

### .ctor

```text
ACadSharp.Entities.TableEntity(ACadSharp.Tables.BlockRecord block)
```

Initializes a new instance of the ACadSharp.Entities.TableEntity class bound to the given anonymous ACadSharp.Tables.BlockRecord that will host the table cache.

- `block`: Anonymous block record used as the table's owning block (DXF 343).

- Raises `System.ArgumentNullException`: 

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### GetCell

```text
ACadSharp.Entities.TableEntity.Cell GetCell(System.Int32 row, System.Int32 column)
```

Retrieves the cell at the specified row and column indices.

**Returns:** The cell located at the specified row and column.

- `row`: The zero-based index of the row containing the cell to retrieve.
- `column`: The zero-based index of the column containing the cell to retrieve.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### BreakData

```text
ACadSharp.Entities.TableEntity.TableBreakData BreakData { get; }
```

Gets the table break data that defines how the table should be divided across breaks, including spacing, flow direction,

### CellStyleOverride

```text
ACadSharp.Objects.TableStyle.CellStyle CellStyleOverride { get; }
```

Gets the cell style override applied at the table level. Use this to set table-level overrides such as flow direction (FlowDirectionBottomToTop).

### Columns

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.Column] Columns { get; }
```

Gets the collection of columns in the table entity.

### HasBreadData

```text
System.Boolean HasBreadData { get; set; }
```

Gets or sets a value indicating whether bread data is available.

### HorizontalDirection

```text
CSMath.XYZ HorizontalDirection { get; set; }
```

Horizontal direction vector

### MergedCellRanges

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.CellRange] MergedCellRanges { get; }
```

Gets the collection of merged cell ranges associated with this table.

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

### OverrideBorderColor

```text
System.Boolean OverrideBorderColor { get; set; }
```

Flag for an override of border color.

### OverrideBorderLineWeight

```text
System.Boolean OverrideBorderLineWeight { get; set; }
```

Flag for an override of border line weight.

### OverrideBorderVisibility

```text
System.Boolean OverrideBorderVisibility { get; set; }
```

Flag for an override of border visibility.

### OverrideFlag

```text
System.Boolean OverrideFlag { get; set; }
```

Flag for an override.

### Rows

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.Row] Rows { get; }
```

Table rows.

### Style

```text
ACadSharp.Objects.TableStyle Style { get; set; }
```

Gets or sets the table style associated with this object.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### ValueFlag

```text
System.Int32 ValueFlag { get; set; }
```

Flag for table value.

### Version

```text
System.Int16 Version { get; set; }
```

Table data version
