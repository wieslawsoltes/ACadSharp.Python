# ACadSharp.Objects.Evaluations.BlockAlignmentParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockAlignmentParameter`

Represents a BLOCKALIGNMENTPARAMETER object, used in AutoCAD to control the alignment in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockAlignmentParameter Dxf class name F:ACadSharp.DxfSubclassMarker.BlockAlignmentParameter

Base type: `ACadSharp.Objects.Evaluations.Block2PtParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockAlignmentParameter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockAlignmentParameter()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### IsPerpendicular

```text
System.Boolean IsPerpendicular { get; }
```

Gets or sets the perpendicular flag.

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
