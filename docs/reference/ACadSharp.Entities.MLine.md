# ACadSharp.Entities.MLine

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.MLine`

Represents a ACadSharp.Entities.MLine entity.

Object name F:ACadSharp.DxfFileToken.EntityMLine Dxf class name F:ACadSharp.DxfSubclassMarker.MLine

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.MLine')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.MLine()
```

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

### Flags

```text
ACadSharp.Entities.MLineFlags Flags { get; set; }
```

Flags.

### Justification

```text
ACadSharp.Entities.MLineJustification Justification { get; set; }
```

Justification.

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

### ScaleFactor

```text
System.Double ScaleFactor { get; set; }
```

Scale factor.

### StartPoint

```text
CSMath.XYZ StartPoint { get; set; }
```

Start point(in WCS).

### Style

```text
ACadSharp.Objects.MLineStyle Style { get; set; }
```

MLine Style.

**Remarks:** Name reference: String of up to 32 characters.The name of the style used for this mline. An entry for this style must exist in the MLINESTYLE dictionary. Do not modify this field without also updating the associated entry in the MLINESTYLE dictionary

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Vertices

```text
System.Collections.Generic.List[ACadSharp.Entities.MLine.Vertex] Vertices { get; }
```

Vertices in the MLine.
