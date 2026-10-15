# ACadSharp.Extensions.UnitExtensions

`class` · `ACadSharp` · CLR name: `ACadSharp.Extensions.UnitExtensions`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Extensions.UnitExtensions')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ToUnits

```text
static ACadSharp.Types.Units.UnitsType ToUnits(ACadSharp.Objects.PlotPaperUnits units)
```

Converts a ACadSharp.Objects.PlotPaperUnits to a ACadSharp.Types.Units.UnitsType.

**Returns:** The corresponding units type.

- `units`: The plot paper units to convert.
