# ACadSharp.Objects.Evaluations.BlockXYParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockXYParameter`

Represents a BLOCKXYPARAMETER object, used in AutoCAD to control a x y in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockXYParameter Dxf class name F:ACadSharp.DxfSubclassMarker.BlockXYParameter

Base type: `ACadSharp.Objects.Evaluations.Block2PtParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockXYParameter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockXYParameter()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### DescriptionX

```text
System.String DescriptionX { get; set; }
```

### DescriptionY

```text
System.String DescriptionY { get; set; }
```

### LabelOffsetX

```text
System.Double LabelOffsetX { get; set; }
```

### LabelOffsetY

```text
System.Double LabelOffsetY { get; set; }
```

### LabelX

```text
System.String LabelX { get; set; }
```

### LabelY

```text
System.String LabelY { get; set; }
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

### ValueSetX

```text
ACadSharp.Objects.Evaluations.ParameterValueSet ValueSetX { get; set; }
```

### ValueSetY

```text
ACadSharp.Objects.Evaluations.ParameterValueSet ValueSetY { get; set; }
```
