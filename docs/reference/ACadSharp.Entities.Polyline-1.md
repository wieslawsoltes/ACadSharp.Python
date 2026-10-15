# ACadSharp.Entities.Polyline

`class` · `ACadSharp` · CLR name: ``ACadSharp.Entities.Polyline`1``

Represents a ACadSharp.Entities.Polyline`1 entity.

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IPolyline`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Polyline`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Polyline[T]()
```

Default constructor.

### .ctor

```text
ACadSharp.Entities.Polyline[T](System.Collections.Generic.IEnumerable[T] vertices, System.Boolean isClosed)
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

### Elevation

```text
System.Double Elevation { get; set; }
```

Documentation inherited from: `base member`.

### EndWidth

```text
System.Double EndWidth { get; set; }
```

End width.

### Flags

```text
ACadSharp.Entities.PolylineFlags Flags { get; set; }
```

Polyline flags.

### IsClosed

```text
System.Boolean IsClosed { get; set; }
```

Documentation inherited from: `base member`.

### Layer

```text
ACadSharp.Tables.Layer Layer { get; set; }
```

Documentation inherited from: `base member`.

### LineType

```text
ACadSharp.Tables.LineType LineType { get; set; }
```

Documentation inherited from: `base member`.

### MatchVerticesEntityProperties

```text
System.Boolean MatchVerticesEntityProperties { get; set; }
```

Gets or sets a value indicating whether entity properties in the ACadSharp.Entities.Vertex should be equals to the polyline when adding vertices or modifying the polyline properties.

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

### SmoothSurface

```text
ACadSharp.Entities.SmoothSurfaceType SmoothSurface { get; set; }
```

Curves and smooth surface type.

### StartWidth

```text
System.Double StartWidth { get; set; }
```

Start width.

### Thickness

```text
System.Double Thickness { get; set; }
```

Documentation inherited from: `base member`.

### Vertices

```text
ACadSharp.SeqendCollection[T] Vertices { get; }
```

Vertices that form this polyline.

**Remarks:** Each ACadSharp.Entities.Vertex has it's own unique handle.
