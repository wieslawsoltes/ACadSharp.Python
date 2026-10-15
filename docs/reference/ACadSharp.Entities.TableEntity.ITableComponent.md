# ACadSharp.Entities.TableEntity.ITableComponent

`interface` · `ACadSharp` · CLR name: `ACadSharp.Entities.TableEntity+ITableComponent`

Represents a table row with a collection of cells, height, custom data, and style information.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.TableEntity+ITableComponent')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### CellStyle

```text
ACadSharp.Objects.TableStyle.CellStyle CellStyle { get; set; }
```

Gets or sets the style applied to the cells in the component.

### CellStyleOverride

```text
ACadSharp.Objects.TableStyle.CellStyle CellStyleOverride { get; set; }
```

Gets or sets the style to apply to the cell, overriding the default cell style.

**Remarks:** Set this property to customize the appearance of the cell independently of the default or inherited styles. If not set, the cell uses the default style.

### CustomData

```text
System.Int32 CustomData { get; set; }
```

Gets or sets the custom data value associated with the entity.

### CustomDataCollection

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.CustomDataEntry] CustomDataCollection { get; }
```

Gets the collection of custom data entries associated with this instance.
