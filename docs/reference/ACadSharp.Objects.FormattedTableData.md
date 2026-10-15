# ACadSharp.Objects.FormattedTableData

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.FormattedTableData`

Represents a ACadSharp.Objects.FormattedTableData object.

Dxf class name F:ACadSharp.DxfSubclassMarker.FormattedTableData

Base type: `ACadSharp.Objects.LinkedTableData`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.FormattedTableData')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### CellStyleOverride

```text
ACadSharp.Objects.TableStyle.CellStyle CellStyleOverride { get; set; }
```

### MergedCellRanges

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.CellRange] MergedCellRanges { get; set; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
