# ACadSharp.Entities.ProxyGraphics.ProxyPolylineWithNormal

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyPolylineWithNormal`

Represents a proxy graphics polyline entity with an associated normal vector.

This class extends ACadSharp.Entities.ProxyGraphics.ProxyPolyline to include normal vector information, which defines the plane in which the polyline lies in 3D space.

Base type: `ACadSharp.Entities.ProxyGraphics.ProxyPolyline`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyPolylineWithNormal')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyPolylineWithNormal()
```

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.
