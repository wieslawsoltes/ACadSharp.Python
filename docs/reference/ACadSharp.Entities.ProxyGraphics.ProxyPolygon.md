# ACadSharp.Entities.ProxyGraphics.ProxyPolygon

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyPolygon`

Represents proxy graphics for a polygon entity.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyPolygon')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyPolygon()
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

Gets or sets the collection of 3D points that define the vertices of the polygon.
