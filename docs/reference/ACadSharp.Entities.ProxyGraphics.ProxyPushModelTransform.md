# ACadSharp.Entities.ProxyGraphics.ProxyPushModelTransform

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyPushModelTransform`

Represents a proxy graphics push model transform.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyPushModelTransform')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyPushModelTransform()
```

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### TransformationMatrix

```text
CSMath.Matrix4 TransformationMatrix { get; set; }
```

Gets or sets the transformation matrix.
