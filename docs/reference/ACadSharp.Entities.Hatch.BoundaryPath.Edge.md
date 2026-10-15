# ACadSharp.Entities.Hatch.BoundaryPath.Edge

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Hatch+BoundaryPath+Edge`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IGeometricEntity`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Hatch+BoundaryPath+Edge')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.Entities.Hatch.BoundaryPath.Edge Clone()
```

Creates a new object that is a copy of the current instance.

### FindIntersections

```text
System.Collections.Generic.IEnumerable[CSMath.XY] FindIntersections(CSMath.Geometry.Line2D line)
```

Find the intersection points between this edge and a line. The line is expressed in the object coordinate system of the edge.

**Returns:** An enumerable of intersection points.

- `line`: The line to find intersections with.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### ToEntity

```text
ACadSharp.Entities.Entity ToEntity()
```

Create the equivalent entity for this Edge.

### Type

```text
ACadSharp.Entities.Hatch.BoundaryPath.EdgeType Type { get; }
```

Edge type.
