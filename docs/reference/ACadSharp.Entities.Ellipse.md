# ACadSharp.Entities.Ellipse

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Ellipse`

Represents a ACadSharp.Entities.Ellipse entity.

Object name F:ACadSharp.DxfFileToken.EntityEllipse Dxf class name F:ACadSharp.DxfSubclassMarker.Ellipse

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`, `CSMath.Geometry.ICurve`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Ellipse')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Ellipse()
```

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### GetEndVertices

```text
System.Void GetEndVertices(out CSMath.XYZ start, out CSMath.XYZ end)
```

Get end vertices of the ellipse, if ACadSharp.Entities.Ellipse.IsFullEllipse is set, the point will be the same.

- `start`: 
- `end`: 

### IsValid

```text
System.Boolean IsValid(ACadSharp.IO.CadFileFormat format, ACadSharp.ACadVersion version, out System.Collections.Generic.IList[System.String] errors)
```

Documentation inherited from: `base member`.

### PolarCoordinateRelativeToCenter

```text
CSMath.XYZ PolarCoordinateRelativeToCenter(System.Double angle)
```

Documentation inherited from: `base member`.

### PolygonalVertexes

```text
System.Collections.Generic.List[CSMath.XYZ] PolygonalVertexes(System.Int32 precision)
```

Documentation inherited from: `base member`.

### Center

```text
CSMath.XYZ Center { get; set; }
```

Center point (in WCS).

### EndParameter

```text
System.Double EndParameter { get; set; }
```

End parameter.

**Value:** The valid range is 0 to 2 * PI.

### IsFullEllipse

```text
System.Boolean IsFullEllipse { get; }
```

Flag that indicates weather this ellipse is closed or not.

### MajorAxis

```text
System.Double MajorAxis { get; }
```

Length of the major axis.

### MajorAxisEndPoint

```text
CSMath.XYZ MajorAxisEndPoint { get; set; }
```

Endpoint of major axis, relative to the center (in WCS).

**Remarks:** Axis X is set as default.

### MinorAxis

```text
System.Double MinorAxis { get; }
```

Length of the minor axis.

### MinorAxisEndPoint

```text
CSMath.XYZ MinorAxisEndPoint { get; }
```

Endpoint of minor axis, relative to the center (in WCS).

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.

### RadiusRatio

```text
System.Double RadiusRatio { get; set; }
```

Ratio of minor axis to major axis.

### Rotation

```text
System.Double Rotation { get; }
```

Rotation of the major axis from the world X axis.

### StartParameter

```text
System.Double StartParameter { get; set; }
```

Start parameter.

**Value:** The valid range is 0 to 2 * PI.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Thickness

```text
System.Double Thickness { get; set; }
```

Specifies the distance a 2D object is extruded above or below its elevation.
