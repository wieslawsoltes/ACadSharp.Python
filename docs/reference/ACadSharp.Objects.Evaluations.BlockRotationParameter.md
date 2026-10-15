# ACadSharp.Objects.Evaluations.BlockRotationParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockRotationParameter`

Represents a BLOCKROTATIONPARAMETER object.

Object name F:ACadSharp.DxfFileToken.ObjectBlockRotationParameter Dxf class name F:ACadSharp.DxfSubclassMarker.BlockRotationParameter

Base type: `ACadSharp.Objects.Evaluations.Block2PtParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockRotationParameter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockRotationParameter()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### Description

```text
System.String Description { get; set; }
```

### Label

```text
System.String Label { get; set; }
```

### LabelOffset

```text
System.Double LabelOffset { get; set; }
```

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### Point

```text
CSMath.XYZ Point { get; set; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### ValueSet

```text
ACadSharp.Objects.Evaluations.ParameterValueSet ValueSet { get; set; }
```
