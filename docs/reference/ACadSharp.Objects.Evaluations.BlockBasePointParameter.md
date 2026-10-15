# ACadSharp.Objects.Evaluations.BlockBasePointParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockBasePointParameter`

Represents a BLOCKBASEPOINTPARAMETER object, used in AutoCAD to control a position of a point in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockBasePointParameter Dxf class name F:ACadSharp.DxfSubclassMarker.BlockBasePointParameter

Base type: `ACadSharp.Objects.Evaluations.Block1PtParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockBasePointParameter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockBasePointParameter()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### Point1011

```text
CSMath.XYZ Point1011 { get; set; }
```

### Point1012

```text
CSMath.XYZ Point1012 { get; set; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
