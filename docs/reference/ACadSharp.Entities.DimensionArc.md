# ACadSharp.Entities.DimensionArc

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.DimensionArc`

Represents a ACadSharp.Entities.DimensionArc entity.

Object name F:ACadSharp.DxfFileToken.EntityArcDimension Dxf class name F:ACadSharp.DxfSubclassMarker.ArcDimension

Base type: `ACadSharp.Entities.Dimension`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.DimensionArc')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.DimensionArc()
```

Default constructor.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### UpdateBlock

```text
System.Void UpdateBlock()
```

Documentation inherited from: `base member`.

**Remarks:** For ACadSharp.Entities.DimensionArc the generation of the block is not yet implemented.

### Center

```text
CSMath.XYZ Center { get; set; }
```

Center of the dimensioned arc (in WCS).

### EndAngle

```text
System.Double EndAngle { get; set; }
```

End angle in radians.

### FirstPoint

```text
CSMath.XYZ FirstPoint { get; set; }
```

Start point of the first extension line (in WCS).

### HasLeader

```text
System.Boolean HasLeader { get; set; }
```

Flag indicating whether the dimension has a leader.

### IsPartial

```text
System.Boolean IsPartial { get; set; }
```

Flag indicating whether the dimension covers a partial section of the arc.

### LeaderPoint1

```text
CSMath.XYZ LeaderPoint1 { get; set; }
```

First leader point (in WCS).

### LeaderPoint2

```text
CSMath.XYZ LeaderPoint2 { get; set; }
```

Second leader point (in WCS).

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

### SecondPoint

```text
CSMath.XYZ SecondPoint { get; set; }
```

Start point of the second extension line (in WCS).

### StartAngle

```text
System.Double StartAngle { get; set; }
```

Start angle in radians.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
