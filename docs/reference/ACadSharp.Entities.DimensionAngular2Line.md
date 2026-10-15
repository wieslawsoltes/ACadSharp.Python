# ACadSharp.Entities.DimensionAngular2Line

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.DimensionAngular2Line`

Represents a ACadSharp.Entities.DimensionAngular2Line entity.

Object name F:ACadSharp.DxfFileToken.EntityDimension Dxf class name F:ACadSharp.DxfSubclassMarker.Angular2LineDimension

Base type: `ACadSharp.Entities.Dimension`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.DimensionAngular2Line')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.DimensionAngular2Line()
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

**Remarks:** For ACadSharp.Entities.DimensionAngular2Line the generation of the block is not yet implemented.

### AngleVertex

```text
CSMath.XYZ AngleVertex { get; set; }
```

Definition point for diameter, radius, and angular dimensions (in WCS).

### Center

```text
CSMath.XYZ Center { get; }
```

Gets the center point of the measured arc.

### DimensionArc

```text
CSMath.XYZ DimensionArc { get; set; }
```

Point defining dimension arc for angular dimensions (in OCS).

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

### Offset

```text
System.Double Offset { get; set; }
```

Definition point offset relative to the ACadSharp.Entities.DimensionAngular2Line.Center.

### SecondPoint

```text
CSMath.XYZ SecondPoint { get; set; }
```

Definition point for linear and angular dimensions (in WCS).

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
