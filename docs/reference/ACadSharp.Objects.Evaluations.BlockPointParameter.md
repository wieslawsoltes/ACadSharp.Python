# ACadSharp.Objects.Evaluations.BlockPointParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockPointParameter`

Represents a BLOCKPOINTPARAMETER object, used in AutoCAD to control a position of a point in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockPointParameter Dxf class name F:ACadSharp.DxfSubclassMarker.BlockPointParameter

Base type: `ACadSharp.Objects.Evaluations.Block1PtParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockPointParameter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockPointParameter()
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

Gets or sets the description.

### Label

```text
System.String Label { get; set; }
```

Gets or sets the label text.

### LabelPosition

```text
CSMath.XYZ LabelPosition { get; set; }
```

Gets or sets the position of label text.

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
