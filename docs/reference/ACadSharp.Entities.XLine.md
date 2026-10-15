# ACadSharp.Entities.XLine

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.XLine`

Represents a ACadSharp.Entities.XLine entity.

Object name F:ACadSharp.DxfFileToken.EntityXline Dxf class name F:ACadSharp.DxfSubclassMarker.XLine

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.XLine')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.XLine()
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

Unit direction vector(in WCS).

### FirstPoint

```text
CSMath.XYZ FirstPoint { get; set; }
```

First point(in WCS).

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

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
