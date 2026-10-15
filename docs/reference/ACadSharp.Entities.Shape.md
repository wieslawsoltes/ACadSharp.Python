# ACadSharp.Entities.Shape

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Shape`

Represents a ACadSharp.Entities.Shape entity.

Object name F:ACadSharp.DxfFileToken.EntityShape Dxf class name F:ACadSharp.DxfSubclassMarker.Shape

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Shape')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Shape(ACadSharp.Tables.TextStyle textStyle)
```

Initializes a shape by the ACadSharp.Tables.TextStyle

- `textStyle`: Text style with the flag ACadSharp.Tables.TextStyle.IsShapeFile

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

### InsertionPoint

```text
CSMath.XYZ InsertionPoint { get; set; }
```

Insertion point (in WCS).

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

Oblique angle.

### RelativeXScale

```text
System.Double RelativeXScale { get; set; }
```

Relative X scale factor.

### Rotation

```text
System.Double Rotation { get; set; }
```

Rotation angle.

### ShapeStyle

```text
ACadSharp.Tables.TextStyle ShapeStyle { get; set; }
```

Shape name.

### Size

```text
System.Double Size { get; set; }
```

Size.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Thickness

```text
System.Double Thickness { get; set; }
```

Thickness.
