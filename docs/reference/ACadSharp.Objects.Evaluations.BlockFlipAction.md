# ACadSharp.Objects.Evaluations.BlockFlipAction

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockFlipAction`

Represents a BLOCKFLIPACTION object, used in AutoCAD to control a flip action in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockFlipAction Dxf class name F:ACadSharp.DxfSubclassMarker.BlockFlipAction

Base type: `ACadSharp.Objects.Evaluations.BlockAction`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockFlipAction')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockFlipAction()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### FlipConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection FlipConnection { get; set; }
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

### UpdatedBaseConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection UpdatedBaseConnection { get; set; }
```

### UpdatedEndConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection UpdatedEndConnection { get; set; }
```

### UpdatedFlipConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection UpdatedFlipConnection { get; set; }
```
