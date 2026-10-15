# ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.MultiLeaderObjectContextData+LeaderLine`

Represents a leader line of a ACadSharp.Objects.MultiLeaderObjectContextData object.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MultiLeaderObjectContextData+LeaderLine')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine()
```

Creates a new instance of the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine class.

### Clone

```text
ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine Clone()
```

Creates a new instance of ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine with the specified index.

**Returns:** A new ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine instance with the same properties.

### Arrowhead

```text
ACadSharp.Tables.BlockRecord Arrowhead { get; set; }
```

Gets or sets a ACadSharp.Tables.BlockRecord containig elements to be dawn as arrow symbol.

### ArrowheadSize

```text
System.Double ArrowheadSize { get; set; }
```

Arrowhead size

### BreakInfoEntries

```text
System.Collections.Generic.List[ACadSharp.Objects.MultiLeaderObjectContextData.BreakInfo] BreakInfoEntries { get; }
```

Gets or sets the list of ACadSharp.Objects.MultiLeaderObjectContextData.BreakInfo entries for this ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.

### Index

```text
System.Int32 Index { get; set; }
```

Leader line index.

### LineColor

```text
ACadSharp.Color LineColor { get; set; }
```

Line color

### LineType

```text
ACadSharp.Tables.LineType LineType { get; set; }
```

Line type

### LineWeight

```text
ACadSharp.LineWeightType LineWeight { get; set; }
```

Line weight

### OverrideFlags

```text
ACadSharp.Objects.LeaderLinePropertOverrideFlags OverrideFlags { get; set; }
```

Override flags

### PathType

```text
ACadSharp.MultiLeaderPathType PathType { get; set; }
```

Leader type

### Points

```text
System.Collections.Generic.IList[CSMath.XYZ] Points { get; }
```

Get the list of points of this ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.
