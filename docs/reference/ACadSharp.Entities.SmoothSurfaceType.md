# ACadSharp.Entities.SmoothSurfaceType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.SmoothSurfaceType`

Curves and smooth surface type.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.SmoothSurfaceType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### BezierSurface

```text
static ACadSharp.Entities.SmoothSurfaceType BezierSurface = 8
```

Bezier surface.

### Cubic

```text
static ACadSharp.Entities.SmoothSurfaceType Cubic = 6
```

Cubic B-spline curve.

### NoSmooth

```text
static ACadSharp.Entities.SmoothSurfaceType NoSmooth = 0
```

No smooth surface fitted.

### Quadratic

```text
static ACadSharp.Entities.SmoothSurfaceType Quadratic = 5
```

Quadratic B-spline curve.
