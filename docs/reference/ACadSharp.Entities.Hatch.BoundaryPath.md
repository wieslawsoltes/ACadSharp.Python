# ACadSharp.Entities.Hatch.BoundaryPath

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Hatch+BoundaryPath`

Defines a hatch boundary.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IGeometricEntity`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Hatch+BoundaryPath')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath()
```

Initializes a new instance of the BoundaryPath class.

**Remarks:** Subscribes to changes in the Edges collection to keep the BoundaryPath instance updated when the collection is modified.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath(System.Collections.Generic.IEnumerable[ACadSharp.Entities.Entity] entities)
```

Initializes a new instance of the BoundaryPath class using the specified collection of entities.

**Remarks:** The entities provided are added to the Entities collection of the BoundaryPath. The path is marked as derived and external by default.

- `entities`: A collection of Entity objects that define the segments of the boundary path. Cannot be null.

### .ctor

```text
ACadSharp.Entities.Hatch.BoundaryPath(System.Collections.Generic.IEnumerable[ACadSharp.Entities.Hatch.BoundaryPath.Edge] edges)
```

Initializes a new instance of the BoundaryPath class with the specified collection of edges.

- `edges`: A collection of Edge objects that define the boundary path. Cannot be null.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.Entities.Hatch.BoundaryPath Clone()
```

Documentation inherited from: `base member`.

### FindIntersections

```text
System.Collections.Generic.IEnumerable[CSMath.XY] FindIntersections(CSMath.Geometry.Line2D line)
```

Finds the intersection points between the boundary path and a given line. The method iterates through each edge in the boundary path and collects the intersection points with the specified line, returning them as an enumerable collection of XY coordinates.

**Returns:** An enumerable collection of XY coordinates representing the intersection points.

- `line`: The line to check for intersections with the boundary path.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### GetPoints

```text
System.Collections.Generic.IEnumerable[CSMath.XYZ] GetPoints(System.Int32 precision = 256)
```

Retrieves the points of the specified boundary as a sequence of the specified vector type.

**Returns:** An System.Collections.Generic.IEnumerable`1 containing the points of the polyline, including interpolated points for arcs.

- `precision`: The number of points to generate for each arc segment. Must be equal to or greater than 2.

### UpdateEdges

```text
System.Void UpdateEdges()
```

Updates the collection of edges to reflect the current set of entities in the boundary definition.

**Remarks:** This method clears the existing edges and reconstructs them based on the current entities. It should be called after modifying the entities collection to ensure the edges remain consistent with the boundary definition.

- Raises `System.ArgumentException`: Thrown if an entity in the collection is not of a supported type. Only Arc, Circle, Ellipse, Line, Polyline2D, Polyline3D, and Spline entities are allowed as hatch boundary elements.

### Edges

```text
System.Collections.ObjectModel.ObservableCollection[ACadSharp.Entities.Hatch.BoundaryPath.Edge] Edges { get; }
```

Edges that form the boundary.

### Entities

```text
System.Collections.Generic.List[ACadSharp.Entities.Entity] Entities { get; set; }
```

Source boundary objects.

### Flags

```text
ACadSharp.Entities.BoundaryPathFlags Flags { get; set; }
```

Boundary path type flag

### IsPolyline

```text
System.Boolean IsPolyline { get; }
```

Flag that indicates that this boundary path is formed by a polyline.
