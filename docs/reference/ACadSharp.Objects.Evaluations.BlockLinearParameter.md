# ACadSharp.Objects.Evaluations.BlockLinearParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockLinearParameter`

Represents a BLOCKLINEARPARAMETER object, used in AutoCAD to control a distance between two points in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockLinearParameter Dxf class name F:ACadSharp.DxfSubclassMarker.BlockLinearParameter

Base type: `ACadSharp.Objects.Evaluations.Block2PtParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockLinearParameter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockLinearParameter()
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

Gets or sets the description of the parameter.

### Label

```text
System.String Label { get; set; }
```

Label text.

### LabelOffset

```text
System.Double LabelOffset { get; set; }
```

Gets or sets the label offset.

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

### ValueSet

```text
ACadSharp.Objects.Evaluations.ParameterValueSet ValueSet { get; set; }
```
