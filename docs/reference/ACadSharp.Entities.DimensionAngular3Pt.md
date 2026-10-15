# ACadSharp.Entities.DimensionAngular3Pt

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.DimensionAngular3Pt`

Represents a ACadSharp.Entities.DimensionAngular3Pt entity.

Object name F:ACadSharp.DxfFileToken.EntityDimension Dxf class name F:ACadSharp.DxfSubclassMarker.Angular3PointDimension

Base type: `ACadSharp.Entities.Dimension`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.DimensionAngular3Pt')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.DimensionAngular3Pt()
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

### UpdateBlock

```text
System.Void UpdateBlock()
```

Documentation inherited from: `base member`.

**Remarks:** For ACadSharp.Entities.DimensionAngular3Pt the generation of the block is not yet implemented.

### AngleVertex

```text
CSMath.XYZ AngleVertex { get; set; }
```

Definition point for diameter, radius, and angular dimensions (in WCS).

**Remarks:** It has the same value as the center of the arc.

### FirstPoint

```text
CSMath.XYZ FirstPoint { get; set; }
```

Definition point for linear and angular dimensions (in WCS).

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

Definition point for linear and angular dimensions (in WCS)

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
