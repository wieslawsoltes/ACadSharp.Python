# ACadSharp.Objects.Evaluations.BlockFlipGrip

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockFlipGrip`

Represents a BLOCKFLIPGRIP object.

Object name F:ACadSharp.DxfFileToken.ObjectBlockFlipGrip Dxf class name F:ACadSharp.DxfSubclassMarker.BlockFlipGrip

Base type: `ACadSharp.Objects.Evaluations.BlockGrip`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockFlipGrip')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockFlipGrip()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### DirectionX

```text
System.Double DirectionX { get; set; }
```

Gets or sets the X component of the direction vector.

### DirectionY

```text
System.Double DirectionY { get; set; }
```

Gets or sets the Y component of the direction vector.

### DirectionZ

```text
System.Double DirectionZ { get; set; }
```

Gets or sets the Z component of the direction vector.

### FlipExpressionId

```text
System.Int32 FlipExpressionId { get; set; }
```

Gets or sets the expression id.

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
