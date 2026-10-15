# ACadSharp.Objects.MultiLeaderObjectContextData.BreakInfo

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.MultiLeaderObjectContextData+BreakInfo`

Information about a break in a ACadSharp.Objects.MultiLeaderObjectContextData object.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MultiLeaderObjectContextData+BreakInfo')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.MultiLeaderObjectContextData.BreakInfo()
```

### Clone

```text
ACadSharp.Objects.MultiLeaderObjectContextData.BreakInfo Clone()
```

Creates a new instance of the ACadSharp.Objects.MultiLeaderObjectContextData.BreakInfo class.

**Returns:** A new ACadSharp.Objects.MultiLeaderObjectContextData.BreakInfo instance with the same segment index and start/end points.

### SegmentIndex

```text
System.Int32 SegmentIndex { get; set; }
```

The index of the segment that is broken.

### StartEndPoints

```text
System.Collections.Generic.IList[ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair] StartEndPoints { get; }
```

The start and end points of the broken segment.
