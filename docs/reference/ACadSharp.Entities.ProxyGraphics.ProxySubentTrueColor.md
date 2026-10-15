# ACadSharp.Entities.ProxyGraphics.ProxySubentTrueColor

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxySubentTrueColor`

Represents proxy graphics data for a subentity with true color information.

This class is used to store color and color method information for proxy graphic subentities. It implements the ACadSharp.Entities.ProxyGraphics.IProxyGeometry interface to provide graphics type information.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxySubentTrueColor')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxySubentTrueColor()
```

### Color

```text
ACadSharp.Color Color { get; set; }
```

Gets or sets the true color for this subentity.

### ColorMethod

```text
ACadSharp.Entities.ProxyGraphics.ProxyColorMethod ColorMethod { get; set; }
```

Gets or sets the color method to be applied to this subentity.

**Remarks:** The default value is F:ACadSharp.Entities.ProxyGraphics.ProxyColorMethod.None.

**Value:** A ACadSharp.Entities.ProxyGraphics.ProxyColorMethod value that specifies how the color should be applied.

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.
