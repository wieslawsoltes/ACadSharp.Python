# ACadSharp.Entities.Tolerance

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Tolerance`

Represents a ACadSharp.Entities.Tolerance entity.

Object name F:ACadSharp.DxfFileToken.EntityTolerance Dxf class name F:ACadSharp.DxfSubclassMarker.Tolerance

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Tolerance')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Tolerance()
```

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

### Direction

```text
CSMath.XYZ Direction { get; set; }
```

X-axis direction vector (in WCS)

### InsertionPoint

```text
CSMath.XYZ InsertionPoint { get; set; }
```

Insertion point (in WCS)

### Normal

```text
CSMath.XYZ Normal { get; set; }
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

### Style

```text
ACadSharp.Tables.DimensionStyle Style { get; set; }
```

Dimension style

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Text

```text
System.String Text { get; set; }
```

Visual representation of the tolerance
