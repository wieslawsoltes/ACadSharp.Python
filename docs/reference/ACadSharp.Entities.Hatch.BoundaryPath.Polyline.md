# ACadSharp.Entities.Hatch.BoundaryPath.Polyline

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Hatch+BoundaryPath+Polyline`

No upstream type summary is available.

Base type: `ACadSharp.Entities.Hatch.BoundaryPath.Edge`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IGeometricEntity`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Hatch+BoundaryPath+Polyline')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Polyline()
```

Initializes a new instance of the Polyline class.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Polyline(ACadSharp.Entities.IPolyline polyline)
```

Initializes a new instance of the Polyline class by copying the vertices and closed state from the specified polyline.

- `polyline`: The source polyline whose vertices and closed state are used to initialize the new instance. Cannot be null.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Polyline(System.Collections.Generic.IEnumerable[CSMath.XYZ] vertices, System.Boolean isClosed = True)
```

Initializes a new instance of the Polyline class with the specified vertices and closure state.

- `vertices`: The collection of points that define the vertices of the polyline. The order of the points determines the sequence of the polyline's segments. Cannot be null or empty.
- `isClosed`: true to create a closed polyline where the last vertex connects to the first; otherwise, false.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.Entities.Hatch.BoundaryPath.Edge Clone()
```

Documentation inherited from: `base member`.

### FindIntersections

```text
System.Collections.Generic.IEnumerable[CSMath.XY] FindIntersections(CSMath.Geometry.Line2D line)
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### ToEntity

```text
ACadSharp.Entities.Entity ToEntity()
```

Documentation inherited from: `base member`.

### Bulges

```text
System.Collections.Generic.IEnumerable[System.Double] Bulges { get; }
```

Bulges applied to each vertice, the number of bulges must be equal to the vertices or empty.

**Remarks:** default value, 0 if not set

### HasBulge

```text
System.Boolean HasBulge { get; }
```

The polyline has bulges with value different than 0.

### IsClosed

```text
System.Boolean IsClosed { get; set; }
```

Is closed flag.

### Type

```text
ACadSharp.Entities.Hatch.BoundaryPath.EdgeType Type { get; }
```

Documentation inherited from: `base member`.

### Vertices

```text
System.Collections.Generic.List[CSMath.XYZ] Vertices { get; }
```

Position values are only X and Y.

**Remarks:** The vertex bulge is stored in the Z component.
