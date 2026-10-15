# ACadSharp.Entities.ProxyGraphics.ProxyRay

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyRay`

Represents a proxy graphics ray entity.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyRay')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyRay()
```

### ConstructionLinePoint

```text
CSMath.XYZ ConstructionLinePoint { get; set; }
```

Gets or sets the construction line point of the ray.

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Point2

```text
CSMath.XYZ Point2 { get; set; }
```

Gets or sets the second point of the ray.
