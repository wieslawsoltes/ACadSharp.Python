# ACadSharp.Entities.ProxyGraphics.ProxyExtents

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyExtents`

Represents the extents (bounding box) of proxy graphics.

The extents define the maximum and minimum boundaries of the proxy geometry, providing a rectangular bounding box for the graphics data.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyExtents')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyExtents()
```

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Max

```text
CSMath.XYZ Max { get; set; }
```

Gets or sets the maximum point of the extents bounding box.

**Value:** An CSMath.XYZ representing the maximum corner coordinates.

### Min

```text
CSMath.XYZ Min { get; set; }
```

Gets or sets the minimum point of the extents bounding box.

**Value:** An CSMath.XYZ representing the minimum corner coordinates.
