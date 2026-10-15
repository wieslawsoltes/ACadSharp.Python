# ACadSharp.Entities.Vertex

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Vertex`

Represents a base type for Vertex entities.

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IVertex`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Vertex')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

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

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Bulge

```text
System.Double Bulge { get; set; }
```

Documentation inherited from: `base member`.

### CurveTangent

```text
System.Double CurveTangent { get; set; }
```

Curve fit tangent direction.

### EndWidth

```text
System.Double EndWidth { get; set; }
```

Ending width.

### Flags

```text
ACadSharp.Entities.VertexFlags Flags { get; set; }
```

Vertex flags.

### Id

```text
System.Int32 Id { get; set; }
```

Vertex identifier.

### Location

```text
CSMath.XYZ Location { get; set; }
```

Location point (in OCS when 2D, and WCS when 3D).

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### StartWidth

```text
System.Double StartWidth { get; set; }
```

Starting width
