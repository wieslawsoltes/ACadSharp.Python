# ACadSharp.Entities.ProxyGraphics.ProxySubentLineTypeScale

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxySubentLineTypeScale`

Represents a proxy graphics entity that defines the line type scale for a subentity.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxySubentLineTypeScale')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxySubentLineTypeScale()
```

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### LineTypeScale

```text
System.Double LineTypeScale { get; set; }
```

Gets or sets the line type scale for the subentity.
