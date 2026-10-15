# ACadSharp.Objects.Evaluations.BlockFlipParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockFlipParameter`

Represents a BLOCKFLIPPARAMETER object, used in AutoCAD to control a flip in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockFlipParameter Dxf class name F:ACadSharp.DxfSubclassMarker.BlockFlipParameter

Base type: `ACadSharp.Objects.Evaluations.Block2PtParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockFlipParameter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockFlipParameter()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### BaseStateName

```text
System.String BaseStateName { get; set; }
```

Gets or sets the base state name.

### Description

```text
System.String Description { get; set; }
```

Gets or sets the description.

### FlippedStateName

```text
System.String FlippedStateName { get; set; }
```

Gets or sets the flipped state name.

### Label

```text
System.String Label { get; set; }
```

Gets or sets the label.

### LabelPosition

```text
CSMath.XYZ LabelPosition { get; set; }
```

Gets or sets the label position.

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

### UpdatedFlipConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection UpdatedFlipConnection { get; set; }
```

Gets or sets the connection.
