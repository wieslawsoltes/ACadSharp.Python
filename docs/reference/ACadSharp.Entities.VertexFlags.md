# ACadSharp.Entities.VertexFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.VertexFlags`

Defines the vertex flags.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.VertexFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### CurveFitTangent

```text
static ACadSharp.Entities.VertexFlags CurveFitTangent = 2
```

Curve-fit tangent defined for this vertex. A curve-fit tangent direction of 0 may be omitted from DXF output but is significant if this bit is set.

### CurveFittingExtraVertex

```text
static ACadSharp.Entities.VertexFlags CurveFittingExtraVertex = 1
```

Extra vertex created by curve-fitting.

### Default

```text
static ACadSharp.Entities.VertexFlags Default = 0
```

Default.

### NotUsed

```text
static ACadSharp.Entities.VertexFlags NotUsed = 4
```

Not used.

### PolyFaceMeshVertex

```text
static ACadSharp.Entities.VertexFlags PolyFaceMeshVertex = 128
```

Polyface mesh vertex.

### PolygonMesh3D

```text
static ACadSharp.Entities.VertexFlags PolygonMesh3D = 64
```

3D polygon mesh.

### PolylineVertex3D

```text
static ACadSharp.Entities.VertexFlags PolylineVertex3D = 32
```

3D polyline vertex.

### SplineFrameControlPoint

```text
static ACadSharp.Entities.VertexFlags SplineFrameControlPoint = 16
```

Spline frame control point.

### SplineVertexFromSplineFitting

```text
static ACadSharp.Entities.VertexFlags SplineVertexFromSplineFitting = 8
```

Spline vertex created by spline-fitting.
