# CSMath.Geometry.CurveExtensions

`class` · `ACadSharp` · CLR name: `CSMath.Geometry.CurveExtensions`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Geometry.CurveExtensions')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### PolarCoordinate

```text
static CSMath.XYZ PolarCoordinate(System.Double angle, CSMath.XYZ center, CSMath.XYZ normal, CSMath.XYZ startPoint, System.Double ratio = 1.0)
```

Find a coordinate in a curve.

- `angle`: 
- `center`: 
- `normal`: 
- `startPoint`: 
- `ratio`: 

### PolygonalVertexes

```text
static System.Collections.Generic.List[CSMath.XYZ] PolygonalVertexes(System.Double length, CSMath.XYZ center, System.Double startAngle, System.Double endAngle, System.Double radius, CSMath.XYZ normal)
```

Converts a curve into a list of vertexes.

- `length`: 
- `center`: 
- `startAngle`: 
- `endAngle`: 
- `radius`: 
- `normal`: 

### PolygonalVertexes

```text
static System.Collections.Generic.List[CSMath.XYZ] PolygonalVertexes(System.Int32 precision, CSMath.XYZ center, System.Double startAngle, System.Double endAngle, CSMath.XYZ normal, CSMath.XYZ majorAxisPoint, System.Double ratio = 1.0)
```

Converts an elliptical curve into a list of vertexes.

- `precision`: 
- `center`: 
- `startAngle`: 
- `endAngle`: 
- `normal`: 
- `majorAxisPoint`: 
- `ratio`: 

- Raises `System.ArgumentOutOfRangeException`: 

### PolygonalVertexes

```text
static System.Collections.Generic.List[CSMath.XYZ] PolygonalVertexes(System.Int32 precision, CSMath.XYZ center, System.Double startAngle, System.Double endAngle, System.Double radius, CSMath.XYZ normal)
```

Converts a curve into a list of vertexes.

- `precision`: 
- `center`: 
- `startAngle`: 
- `endAngle`: 
- `radius`: 
- `normal`: 

- Raises `System.ArgumentOutOfRangeException`: 
