# ACadSharp.Objects.MultiLeaderObjectContextData.LeaderRoot

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.MultiLeaderObjectContextData+LeaderRoot`

Represents a leader root

Appears in DXF as 302 DXF: “LEADER“

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `System.ICloneable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MultiLeaderObjectContextData+LeaderRoot')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.MultiLeaderObjectContextData.LeaderRoot()
```

### Clone

```text
System.Object Clone()
```

### BreakStartEndPointsPairs

```text
System.Collections.Generic.IList[ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair] BreakStartEndPointsPairs { get; }
```

Gets a list of ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair.

### ConnectionPoint

```text
CSMath.XYZ ConnectionPoint { get; set; }
```

Connection point

### ContentValid

```text
System.Boolean ContentValid { get; set; }
```

Is content valid (ODA writes true)

### Direction

```text
CSMath.XYZ Direction { get; set; }
```

Direction

### LandingDistance

```text
System.Double LandingDistance { get; set; }
```

Landing distance

### LeaderIndex

```text
System.Int32 LeaderIndex { get; set; }
```

Leader index

### Lines

```text
System.Collections.Generic.IList[ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine] Lines { get; }
```

Gets a list of ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine objects representing leader lines starting from the landing point of the multi leader.

### TextAttachmentDirection

```text
ACadSharp.TextAttachmentDirectionType TextAttachmentDirection { get; set; }
```

Attachment direction

### Unknown

```text
System.Boolean Unknown { get; set; }
```

Unknown (ODA writes true)
