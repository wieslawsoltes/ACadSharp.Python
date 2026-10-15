# ACadSharp.Entities.ProxyGraphics.ProxySubentLineType

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxySubentLineType`

Represents a proxy subentity line type.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxySubentLineType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxySubentLineType()
```

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### IsByBlock

```text
System.Boolean IsByBlock { get; }
```

Defines if the color is defined by block.

### IsByLayer

```text
System.Boolean IsByLayer { get; }
```

Defines if the color is defined by layer.

### LineTypeIndex

```text
System.UInt32 LineTypeIndex { get; set; }
```
