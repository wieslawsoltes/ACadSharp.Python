# ACadSharp.Entities.ProxyGraphics.ProxyPushClip

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyPushClip`

Represents a proxy push clip graphics object for CAD proxy graphics operations.

This class defines clipping boundaries and transformations for proxy graphics rendering, including front/back clip planes and boundary definitions in 3D space.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyPushClip')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyPushClip()
```

### BackClip

```text
System.Double BackClip { get; set; }
```

Gets or sets the back clipping plane distance.

**Value:** A double representing the back clip distance in drawing units.

### BackClipOn

```text
System.Boolean BackClipOn { get; set; }
```

Gets or sets a value indicating whether the back clipping plane is enabled.

**Value:** true if back clipping is active; otherwise, false.

### ClipBoundary

```text
System.Collections.Generic.List[CSMath.XY] ClipBoundary { get; set; }
```

Gets or sets the collection of 2D points that define the clip boundary polygon.

**Value:** A System.Collections.Generic.List`1 of CSMath.XY coordinates representing boundary points.

### ClipBoundaryOrigin

```text
CSMath.XYZ ClipBoundaryOrigin { get; set; }
```

Gets or sets the origin point of the clip boundary in 3D space.

**Value:** An CSMath.XYZ coordinate representing the clip boundary origin.

### ClipBoundaryTransformMatrix

```text
CSMath.Matrix4 ClipBoundaryTransformMatrix { get; set; }
```

Gets or sets the transformation matrix applied to the clip boundary.

**Value:** A CSMath.Matrix4 representing the clip boundary transformation.

### DrawBoundary

```text
System.Boolean DrawBoundary { get; set; }
```

Gets or sets a value indicating whether the clip boundary should be drawn.

**Value:** true if the boundary should be rendered; otherwise, false.

### Extrusion

```text
CSMath.XYZ Extrusion { get; set; }
```

Gets or sets the extrusion direction vector.

**Value:** An CSMath.XYZ vector representing the extrusion direction.

### FrontClip

```text
System.Double FrontClip { get; set; }
```

Gets or sets the front clipping plane distance.

**Value:** A double representing the front clip distance in drawing units.

### FrontClipOn

```text
System.Boolean FrontClipOn { get; set; }
```

Gets or sets a value indicating whether the front clipping plane is enabled.

**Value:** true if front clipping is active; otherwise, false.

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### InverseBlockTransformMatrix

```text
CSMath.Matrix4 InverseBlockTransformMatrix { get; set; }
```

Gets or sets the inverse block transformation matrix.

**Value:** A CSMath.Matrix4 representing the inverse transformation of the block.

### PointCount

```text
System.Int32 PointCount { get; set; }
```

Gets or sets the number of points defining the clip boundary polygon.

**Value:** An integer representing the point count.
