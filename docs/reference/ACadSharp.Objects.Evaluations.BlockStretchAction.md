# ACadSharp.Objects.Evaluations.BlockStretchAction

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockStretchAction`

Represents a BLOCKSTRETCHACTION object, used in AutoCAD to control a stretch action in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockStretchAction Dxf class name F:ACadSharp.DxfSubclassMarker.BlockStretchAction

Base type: `ACadSharp.Objects.Evaluations.StretchActionBase`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockStretchAction')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockStretchAction()
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

Documentation inherited from: `base member`.

### Boundary

```text
System.Collections.Generic.List[CSMath.XY] Boundary { get; }
```

Documentation inherited from: `base member`.

### DistanceMultiplier

```text
System.Double DistanceMultiplier { get; set; }
```

Documentation inherited from: `base member`.

### EndXDeltaConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection EndXDeltaConnection { get; set; }
```

### EndYDeltaConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection EndYDeltaConnection { get; set; }
```

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

Documentation inherited from: `base member`.
