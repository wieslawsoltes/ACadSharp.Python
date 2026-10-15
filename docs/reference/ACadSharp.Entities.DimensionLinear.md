# ACadSharp.Entities.DimensionLinear

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.DimensionLinear`

Represents a ACadSharp.Entities.DimensionLinear entity.

Object name F:ACadSharp.DxfFileToken.EntityDimension Dxf class name F:ACadSharp.DxfSubclassMarker.LinearDimension

Base type: `ACadSharp.Entities.DimensionAligned`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.DimensionLinear')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.DimensionLinear()
```

Documentation inherited from: `base member`.

### UpdateBlock

```text
System.Void UpdateBlock()
```

Documentation inherited from: `base member`.

### Measurement

```text
System.Double Measurement { get; }
```

Documentation inherited from: `base member`.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.

### Offset

```text
System.Double Offset { get; set; }
```

Documentation inherited from: `base member`.

### Rotation

```text
System.Double Rotation { get; set; }
```

Angle of rotated, horizontal, or vertical dimensions.

**Value:** Value in radians.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
