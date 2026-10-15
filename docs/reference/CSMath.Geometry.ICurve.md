# CSMath.Geometry.ICurve

`interface` · `ACadSharp` · CLR name: `CSMath.Geometry.ICurve`

No upstream type summary is available.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Geometry.ICurve')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### PolarCoordinateRelativeToCenter

```text
CSMath.XYZ PolarCoordinateRelativeToCenter(System.Double angle)
```

Calculate the local point on the curve for a given angle relative to the center.

**Returns:** A local point on the curve for the given angle relative to the center.

- `angle`: Angle in radians.

### PolygonalVertexes

```text
System.Collections.Generic.List[CSMath.XYZ] PolygonalVertexes(System.Int32 precision)
```

Converts the curve in a list of vertexes.

**Returns:** A list vertexes that represents the curve expressed in object coordinate system.

- `precision`: Number of vertexes generated.

### Center

```text
CSMath.XYZ Center { get; }
```

Specifies the center of the curve.

### RadiusRatio

```text
System.Double RadiusRatio { get; }
```

Ratio of minor axis to major axis.

**Remarks:** Value is 1 for a circle.
