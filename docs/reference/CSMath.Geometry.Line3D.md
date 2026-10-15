# CSMath.Geometry.Line3D

`struct` · `ACadSharp` · CLR name: `CSMath.Geometry.Line3D`

No upstream type summary is available.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

Interfaces: `CSMath.Geometry.ILine[CSMath.XYZ]`, `System.IEquatable[CSMath.Geometry.Line3D]`.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Geometry.Line3D')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.Geometry.Line3D(CSMath.XYZ origin, CSMath.XYZ direction)
```

Initialize a new instance of the CSMath.Geometry.Line3D class.

- `origin`: Origin point on the line.
- `direction`: Line direction, must be a none zero vector.

- Raises `System.ArgumentException`: 

### Equals

```text
System.Boolean Equals(CSMath.Geometry.Line3D other)
```

Documentation inherited from: `base member`.

### FindIntersection

```text
CSMath.XYZ FindIntersection(CSMath.Geometry.ILine[CSMath.XYZ] line)
```

Documentation inherited from: `base member`.

### FromPoints

```text
static CSMath.Geometry.Line3D FromPoints(CSMath.XYZ pt1, CSMath.XYZ pt2)
```

Creates a line from 2 points, the first point is the origin and the second point is used to calculate the direction.

**Returns:** A new instance of the CSMath.Geometry.Line3D class.

- `pt1`: The first point, which will be the origin of the line.
- `pt2`: The second point, used to calculate the direction of the line.

### FromSegment3D

```text
static CSMath.Geometry.Line3D FromSegment3D(CSMath.Geometry.Segment3D segment)
```

Creates a line from a segment, the origin of the line will be the origin of the segment and the direction will be the direction of the segment.

**Returns:** A new instance of the CSMath.Geometry.Line3D class.

- `segment`: The 3D segment used to create the line.

### Direction

```text
CSMath.XYZ Direction { get; set; }
```

Documentation inherited from: `base member`.

### Origin

```text
CSMath.XYZ Origin { get; set; }
```

Documentation inherited from: `base member`.
