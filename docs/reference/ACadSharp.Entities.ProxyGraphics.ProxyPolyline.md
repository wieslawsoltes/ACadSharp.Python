# ACadSharp.Entities.ProxyGraphics.ProxyPolyline

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyPolyline`

Represents proxy graphics for a polyline entity.

This class implements the ACadSharp.Entities.ProxyGraphics.IProxyGeometry interface to provide geometric representation of a polyline defined by a collection of 3D points.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyPolyline')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyPolyline()
```

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Points

```text
System.Collections.Generic.List[CSMath.XYZ] Points { get; set; }
```

Gets or sets the collection of 3D points that define the vertices of the polyline.

**Value:** A System.Collections.Generic.List`1 of CSMath.XYZ coordinates representing the polyline vertices.
