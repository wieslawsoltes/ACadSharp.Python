# ACadSharp.Entities.TextEntity

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.TextEntity`

Represents a ACadSharp.Entities.TextEntity

Object name F:ACadSharp.DxfFileToken.EntityText Dxf class name F:ACadSharp.DxfSubclassMarker.Text

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IText`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.TextEntity')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.TextEntity()
```

Initializes a new instance of the ACadSharp.Entities.TextEntity class.

### .ctor

```text
ACadSharp.Entities.TextEntity(System.String value)
```

Initializes a new instance of the ACadSharp.Entities.TextEntity class with the specified text value.

- `value`: The text value.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### AlignmentPoint

```text
CSMath.XYZ AlignmentPoint { get; set; }
```

Second alignment point (in OCS)

**Remarks:** This value is meaningful only if the value of a 72 or 73 group is nonzero (if the justification is anything other than baseline/left)

### Height

```text
System.Double Height { get; set; }
```

Documentation inherited from: `base member`.

### HorizontalAlignment

```text
ACadSharp.Entities.TextHorizontalAlignment HorizontalAlignment { get; set; }
```

Horizontal text justification type.

### InsertPoint

```text
CSMath.XYZ InsertPoint { get; set; }
```

First alignment point(in OCS)

### Mirror

```text
ACadSharp.Entities.TextMirrorFlag Mirror { get; set; }
```

Mirror flags.

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

### ObliqueAngle

```text
System.Double ObliqueAngle { get; set; }
```

Specifies the oblique angle of the object.

**Value:** The angle in radians within the range of -85 to +85 degrees. A positive angle denotes a lean to the right; a negative value will have 2*PI added to it to convert it to its positive equivalent.

### Rotation

```text
System.Double Rotation { get; set; }
```

Documentation inherited from: `base member`.

### Style

```text
ACadSharp.Tables.TextStyle Style { get; set; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Thickness

```text
System.Double Thickness { get; set; }
```

Specifies the distance a 2D object is extruded above or below its elevation.

### Value

```text
System.String Value { get; set; }
```

Documentation inherited from: `base member`.

### VerticalAlignment

```text
ACadSharp.Entities.TextVerticalAlignmentType VerticalAlignment { get; set; }
```

Vertical text justification type.

### WidthFactor

```text
System.Double WidthFactor { get; set; }
```

Relative X scale factor—widt

**Remarks:** This value is also adjusted when fit-type text is used
