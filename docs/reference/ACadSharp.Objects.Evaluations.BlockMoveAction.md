# ACadSharp.Objects.Evaluations.BlockMoveAction

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockMoveAction`

Represents a BLOCKMOVEACTION object, used in AutoCAD to control a movement action in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockMoveAction Dxf class name F:ACadSharp.DxfSubclassMarker.BlockMoveAction

Base type: `ACadSharp.Objects.Evaluations.BlockAction`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockMoveAction')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockMoveAction()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### AngleOffset

```text
System.Double AngleOffset { get; set; }
```

Gets or sets the angle offset for the move action.

### DistanceMultiplier

```text
System.Double DistanceMultiplier { get; set; }
```

Gets or sets the distance multiplier for the move action.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### UnknownFlag

```text
System.Byte UnknownFlag { get; set; }
```

Gets or sets an unknown flag value.

### XDeltaConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection XDeltaConnection { get; set; }
```

Gets or sets the evaluation connection for the X delta displacement.

### YDeltaConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection YDeltaConnection { get; set; }
```

Gets or sets the evaluation connection for the Y delta displacement.
