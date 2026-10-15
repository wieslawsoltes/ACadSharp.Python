# ACadSharp.Entities.TableEntity.TableBreakData

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.TableEntity+TableBreakData`

Represents the configuration data for handling table breaks, including spacing, flow direction, break options, and break segment details.

Use this class to specify how a table should be divided across breaks, such as pages or sections. The properties allow customization of break spacing, direction, and additional options that influence table layout behavior.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.TableEntity+TableBreakData')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.TableEntity.TableBreakData()
```

### BreakSpacing

```text
System.Double BreakSpacing { get; set; }
```

Gets or sets the spacing between table breaks.

### Flags

```text
ACadSharp.Entities.TableEntity.BreakOptionFlags Flags { get; set; }
```

Gets or sets the break option flags that control how table breaks are handled.

### FlowDirection

```text
ACadSharp.Entities.TableEntity.BreakFlowDirection FlowDirection { get; set; }
```

Gets or sets the direction in which the table flows across breaks.

### Heights

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.TableBreakData.BreakHeight] Heights { get; set; }
```

Gets or sets the collection of break heights and their positions.
