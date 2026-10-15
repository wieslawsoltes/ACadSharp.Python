# ACadSharp.Entities.PolylineFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.PolylineFlags`

Defines the polyline flags.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.PolylineFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ClosedPolygonMeshInN

```text
static ACadSharp.Entities.PolylineFlags ClosedPolygonMeshInN = 32
```

The polygon mesh is closed in the N direction.

### ClosedPolylineOrClosedPolygonMeshInM

```text
static ACadSharp.Entities.PolylineFlags ClosedPolylineOrClosedPolygonMeshInM = 1
```

This is a closed polyline (or a polygon mesh closed in the M direction).

### ContinuousLinetypePattern

```text
static ACadSharp.Entities.PolylineFlags ContinuousLinetypePattern = 128
```

The line type pattern is generated continuously around the vertexes of this polyline.

### CurveFit

```text
static ACadSharp.Entities.PolylineFlags CurveFit = 2
```

Curve-fit vertexes have been added.

### Default

```text
static ACadSharp.Entities.PolylineFlags Default = 0
```

Default, open polyline.

### PolyfaceMesh

```text
static ACadSharp.Entities.PolylineFlags PolyfaceMesh = 64
```

The polyline is a polyface mesh.

### PolygonMesh

```text
static ACadSharp.Entities.PolylineFlags PolygonMesh = 16
```

This is a 3D polygon mesh.

### Polyline3D

```text
static ACadSharp.Entities.PolylineFlags Polyline3D = 8
```

This is a 3D polyline.

### SplineFit

```text
static ACadSharp.Entities.PolylineFlags SplineFit = 4
```

Spline-fit vertexes have been added.
