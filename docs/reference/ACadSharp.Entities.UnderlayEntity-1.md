# ACadSharp.Entities.UnderlayEntity

`class` · `ACadSharp` · CLR name: ``ACadSharp.Entities.UnderlayEntity`1``

Common base class for all underlay entities, like ACadSharp.Entities.PdfUnderlay.

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.UnderlayEntity`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.UnderlayEntity[T](T definition)
```

Initializes a new instance of the ACadSharp.Entities.UnderlayEntity`1 class.

- `definition`: 

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

### ClipBoundaryVertices

```text
System.Collections.Generic.List[CSMath.XY] ClipBoundaryVertices { get; set; }
```

2d points in OCS/ECS.

**Remarks:** If only two, then they are the lower left and upper right corner points of a clip rectangle. If more than two, then they are the vertices of a clipping polygon.

### Contrast

```text
System.Byte Contrast { get; set; }
```

Contrast.

**Remarks:** 0-100; default = 50

### Definition

```text
T Definition { get; set; }
```

The AcDbUnderlayDefinition object.

### Fade

```text
System.Byte Fade { get; set; }
```

Fade.

**Value:** Range: 0 - 100 Default: 0

### Flags

```text
ACadSharp.Entities.UnderlayDisplayFlags Flags { get; set; }
```

Underlay display options.

### InsertPoint

```text
CSMath.XYZ InsertPoint { get; set; }
```

Insertion point(in WCS).

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.

### Rotation

```text
System.Double Rotation { get; set; }
```

Specifies the rotation angle for the object.

**Value:** The rotation angle in radians.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### XScale

```text
System.Double XScale { get; set; }
```

X scale factor.

### YScale

```text
System.Double YScale { get; set; }
```

Y scale factor.

### ZScale

```text
System.Double ZScale { get; set; }
```

Z scale factor.
