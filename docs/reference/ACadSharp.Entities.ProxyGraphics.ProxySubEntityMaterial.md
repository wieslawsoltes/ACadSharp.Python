# ACadSharp.Entities.ProxyGraphics.ProxySubEntityMaterial

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxySubEntityMaterial`

Represents a proxy sub-entity material in a CAD drawing.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxySubEntityMaterial')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxySubEntityMaterial()
```

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### MaterialHandle

```text
System.UInt64 MaterialHandle { get; set; }
```

Gets or sets the handle of the material.
