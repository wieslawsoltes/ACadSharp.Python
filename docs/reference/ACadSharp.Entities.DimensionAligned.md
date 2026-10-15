# ACadSharp.Entities.DimensionAligned

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.DimensionAligned`

Represents a ACadSharp.Entities.DimensionAligned entity.

Object name F:ACadSharp.DxfFileToken.EntityDimension Dxf class name F:ACadSharp.DxfSubclassMarker.AlignedDimension

Base type: `ACadSharp.Entities.Dimension`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.DimensionAligned')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.DimensionAligned()
```

Default constructor.

### .ctor

```text
ACadSharp.Entities.DimensionAligned(CSMath.XYZ firstPoint, CSMath.XYZ secondPoint)
```

Constructor with the first and second point.

- `firstPoint`: 
- `secondPoint`: 

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

### ExtLineRotation

```text
System.Double ExtLineRotation { get; set; }
```

Linear dimension types with an oblique angle have an optional group code 52. When added to the rotation angle of the linear dimension(group code 50), it gives the angle of the extension lines

### FirstPoint

```text
CSMath.XYZ FirstPoint { get; set; }
```

Insertion point for clones of a dimension—Baseline and Continue (in OCS).

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

Definition point offset relative to the ACadSharp.Entities.DimensionAligned.SecondPoint.

### SecondPoint

```text
CSMath.XYZ SecondPoint { get; set; }
```

Definition point for linear and angular dimensions(in WCS).

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
