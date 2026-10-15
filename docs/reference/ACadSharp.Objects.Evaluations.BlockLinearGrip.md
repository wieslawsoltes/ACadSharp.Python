# ACadSharp.Objects.Evaluations.BlockLinearGrip

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockLinearGrip`

Represents a BLOCKLINEARGRIP object.

Object name F:ACadSharp.DxfFileToken.ObjectBlockLinearGrip Dxf class name F:ACadSharp.DxfSubclassMarker.BlockLinearGrip

Base type: `ACadSharp.Objects.Evaluations.BlockGrip`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockLinearGrip')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockLinearGrip()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### DistanceX

```text
System.Double DistanceX { get; set; }
```

Gets or sets the distance in the X direction.

### DistanceY

```text
System.Double DistanceY { get; set; }
```

Gets or sets the distance in the Y direction.

### DistanceZ

```text
System.Double DistanceZ { get; set; }
```

Gets or sets the distance in the Z direction.

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
