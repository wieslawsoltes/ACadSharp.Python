# ACadSharp.Entities.Hatch.BoundaryPath.Line

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Hatch+BoundaryPath+Line`

No upstream type summary is available.

Base type: `ACadSharp.Entities.Hatch.BoundaryPath.Edge`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IGeometricEntity`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Hatch+BoundaryPath+Line')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Line()
```

Initializes a new instance of the Line class.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath.Line(ACadSharp.Entities.Line line)
```

Initializes a new instance of the Line class using the specified line entity.

- `line`: The line entity from which to initialize the start and end points. Cannot be null.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
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

### ToSegment2D

```text
CSMath.Geometry.Segment2D ToSegment2D()
```

### End

```text
CSMath.XY End { get; set; }
```

Endpoint (in OCS)

### Start

```text
CSMath.XY Start { get; set; }
```

Start point (in OCS)

### Type

```text
ACadSharp.Entities.Hatch.BoundaryPath.EdgeType Type { get; }
```
