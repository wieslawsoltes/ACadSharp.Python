# ACadSharp.Objects.Evaluations.BlockPolarParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockPolarParameter`

Represents a BLOCKPOLARPARAMETER object, used in AutoCAD to control a polar parameter in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockPolarParameter Dxf class name F:ACadSharp.DxfSubclassMarker.BlockPolarParameter

Base type: `ACadSharp.Objects.Evaluations.Block2PtParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockPolarParameter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockPolarParameter()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### AngleDescription

```text
System.String AngleDescription { get; set; }
```

Gets or sets the description of the angle.

### AngleName

```text
System.String AngleName { get; set; }
```

Gets or sets the name of the angle.

### AngleValueSet

```text
ACadSharp.Objects.Evaluations.ParameterValueSet AngleValueSet { get; set; }
```

Gets or sets the angle of the polar parameter.

### Description

```text
System.String Description { get; set; }
```

Gets or sets the description of the polar parameter.

### DistanceValueSet

```text
ACadSharp.Objects.Evaluations.ParameterValueSet DistanceValueSet { get; set; }
```

Gets or sets the distance of the polar parameter.

### Label

```text
System.String Label { get; set; }
```

Gets or sets the label text of the polar parameter.

### LabelOffset

```text
System.Double LabelOffset { get; set; }
```

Gets or sets the position of the label text of the polar parameter.

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
