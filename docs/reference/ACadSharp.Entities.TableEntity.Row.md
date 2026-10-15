# ACadSharp.Entities.TableEntity.Row

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.TableEntity+Row`

Represents a table row with a collection of cells, height, custom data, and style information.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.TableEntity.ITableComponent`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.TableEntity+Row')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.TableEntity.Row()
```

### CellStyle

```text
ACadSharp.Objects.TableStyle.CellStyle CellStyle { get; set; }
```

Documentation inherited from: `base member`.

### CellStyleOverride

```text
ACadSharp.Objects.TableStyle.CellStyle CellStyleOverride { get; set; }
```

Documentation inherited from: `base member`.

### Cells

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.Cell] Cells { get; set; }
```

Gets or sets the collection of cells contained in the current object.

### CustomData

```text
System.Int32 CustomData { get; set; }
```

Documentation inherited from: `base member`.

### CustomDataCollection

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.CustomDataEntry] CustomDataCollection { get; }
```

Documentation inherited from: `base member`.

### Height

```text
System.Double Height { get; set; }
```

Row height.
