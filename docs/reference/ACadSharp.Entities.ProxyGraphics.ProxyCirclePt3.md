# ACadSharp.Entities.ProxyGraphics.ProxyCirclePt3

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyCirclePt3`

Represents a proxy graphics circle defined by three points.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyCirclePt3')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyCirclePt3()
```

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Point1

```text
CSMath.XYZ Point1 { get; set; }
```

Gets or sets the first point that defines the circle.

### Point2

```text
CSMath.XYZ Point2 { get; set; }
```

Gets or sets the second point that defines the circle.

### Point3

```text
CSMath.XYZ Point3 { get; set; }
```

Gets or sets the third point that defines the circle.
