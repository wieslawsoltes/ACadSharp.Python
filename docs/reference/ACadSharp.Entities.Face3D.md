# ACadSharp.Entities.Face3D

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Face3D`

Represents a ACadSharp.Entities.Face3D entity.

Object name F:ACadSharp.DxfFileToken.Entity3DFace Dxf class name F:ACadSharp.DxfSubclassMarker.Face3d

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Face3D')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Face3D()
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

### FirstCorner

```text
CSMath.XYZ FirstCorner { get; set; }
```

First corner(in WCS).

### Flags

```text
ACadSharp.Entities.InvisibleEdgeFlags Flags { get; set; }
```

Invisible edge flags.

### FourthCorner

```text
CSMath.XYZ FourthCorner { get; set; }
```

Fourth corner(in WCS).

**Remarks:** If only three corners are entered, this is the same as the third corner

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

### SecondCorner

```text
CSMath.XYZ SecondCorner { get; set; }
```

Second corner(in WCS).

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### ThirdCorner

```text
CSMath.XYZ ThirdCorner { get; set; }
```

Third corner(in WCS).
