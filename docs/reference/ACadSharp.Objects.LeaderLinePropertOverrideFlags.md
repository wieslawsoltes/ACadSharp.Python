# ACadSharp.Objects.LeaderLinePropertOverrideFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Objects.LeaderLinePropertOverrideFlags`

These flags specify whether properties of a leader line primarily defined by the ACadSharp.Objects.MultiLeaderStyle object or overidden by properties of the ACadSharp.Entities.MultiLeader object are overridden for an individual leader line.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.LeaderLinePropertOverrideFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Arrowhead

```text
static ACadSharp.Objects.LeaderLinePropertOverrideFlags Arrowhead = 32
```

ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.Arrowhead property overrides settings from ACadSharp.Entities.MultiLeader and ACadSharp.Objects.MultiLeaderStyle.

### ArrowheadSize

```text
static ACadSharp.Objects.LeaderLinePropertOverrideFlags ArrowheadSize = 16
```

ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.ArrowheadSize property overrides settings from ACadSharp.Entities.MultiLeader and ACadSharp.Objects.MultiLeaderStyle.

### LineColor

```text
static ACadSharp.Objects.LeaderLinePropertOverrideFlags LineColor = 2
```

ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.LineColor property overrides settings from ACadSharp.Entities.MultiLeader and ACadSharp.Objects.MultiLeaderStyle.

### LineType

```text
static ACadSharp.Objects.LeaderLinePropertOverrideFlags LineType = 4
```

ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.LineType property overrides settings from ACadSharp.Entities.MultiLeader and ACadSharp.Objects.MultiLeaderStyle.

### LineWeight

```text
static ACadSharp.Objects.LeaderLinePropertOverrideFlags LineWeight = 8
```

ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.LineWeight property overrides settings from ACadSharp.Entities.MultiLeader and ACadSharp.Objects.MultiLeaderStyle.

### None

```text
static ACadSharp.Objects.LeaderLinePropertOverrideFlags None = 0
```

No property to be overridden

### PathType

```text
static ACadSharp.Objects.LeaderLinePropertOverrideFlags PathType = 1
```

ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.PathType property overrides settings from ACadSharp.Entities.MultiLeader and ACadSharp.Objects.MultiLeaderStyle.
