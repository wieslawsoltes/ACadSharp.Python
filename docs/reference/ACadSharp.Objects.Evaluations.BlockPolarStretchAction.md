# ACadSharp.Objects.Evaluations.BlockPolarStretchAction

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockPolarStretchAction`

Represents a BLOCKPOLARSTRETCHACTION object, used in AutoCAD to control a polar stretch action in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockPolarStretchAction Dxf class name F:ACadSharp.DxfSubclassMarker.BlockPolarStretchAction

Base type: `ACadSharp.Objects.Evaluations.StretchActionBase`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockPolarStretchAction')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockPolarStretchAction()
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

### BaseConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection BaseConnection { get; set; }
```

### BaseXDeltaConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection BaseXDeltaConnection { get; set; }
```

### BaseYDeltaConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection BaseYDeltaConnection { get; set; }
```

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

### EndConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection EndConnection { get; set; }
```

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### RotateBindings

```text
System.Collections.Generic.List[ACadSharp.Entities.Entity] RotateBindings { get; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### UpdatedBaseConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection UpdatedBaseConnection { get; set; }
```

### UpdatedEndConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection UpdatedEndConnection { get; set; }
```
