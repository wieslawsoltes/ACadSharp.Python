# ACadSharp.Objects.LinkedTableData

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.LinkedTableData`

Represents a ACadSharp.Objects.LinkedTableData object.

Dxf class name F:ACadSharp.DxfSubclassMarker.LinkedTableData

Base type: `ACadSharp.Objects.LinkedData`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.LinkedTableData')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Columns

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.Column] Columns { get; }
```

### Rows

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.Row] Rows { get; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
