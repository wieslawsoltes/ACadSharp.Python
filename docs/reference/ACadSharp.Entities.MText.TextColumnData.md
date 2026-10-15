# ACadSharp.Entities.MText.TextColumnData

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.MText+TextColumnData`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.MText+TextColumnData')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.MText.TextColumnData()
```

### Clone

```text
ACadSharp.Entities.MText.TextColumnData Clone()
```

### AutoHeight

```text
System.Boolean AutoHeight { get; set; }
```

Gets or sets a value indicating whether height is automatic

### ColumnCount

```text
System.Int32 ColumnCount { get; set; }
```

Number of columns

### ColumnType

```text
ACadSharp.Entities.ColumnType ColumnType { get; set; }
```

Text column type

### FlowReversed

```text
System.Boolean FlowReversed { get; set; }
```

Gets or sets a value indicating whether flow is reversed

### Gutter

```text
System.Double Gutter { get; set; }
```

Column gutter.

### Heights

```text
System.Collections.Generic.List[System.Double] Heights { get; }
```

Column heights.

### Width

```text
System.Double Width { get; set; }
```

Width of the column.
