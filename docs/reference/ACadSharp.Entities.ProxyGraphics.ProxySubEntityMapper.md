# ACadSharp.Entities.ProxyGraphics.ProxySubEntityMapper

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxySubEntityMapper`

Represents a proxy sub-entity mapper for handling proxy graphics geometry mapping.

This class implements the ACadSharp.Entities.ProxyGraphics.IProxyGeometry interface and provides properties for managing the transformation and tiling parameters of proxy sub-entities in the graphics system.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxySubEntityMapper')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxySubEntityMapper()
```

### AutoTransform

```text
System.Int32 AutoTransform { get; set; }
```

Gets or sets the automatic transformation setting for the proxy sub-entity mapper.

### DummyValue1

```text
System.Int32 DummyValue1 { get; set; }
```

Gets or sets the first dummy value reserved for future use.

### DummyValue2

```text
System.Int32 DummyValue2 { get; set; }
```

Gets or sets the second dummy value reserved for future use.

### DummyValue3

```text
System.Int32 DummyValue3 { get; set; }
```

Gets or sets the third dummy value reserved for future use.

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Projection

```text
System.Int32 Projection { get; set; }
```

Gets or sets the projection setting for the proxy sub-entity mapper.

### UTiling

```text
System.Int32 UTiling { get; set; }
```

Gets or sets the U-direction tiling parameter for the proxy sub-entity mapper.

### VTiling

```text
System.Int32 VTiling { get; set; }
```

Gets or sets the V-direction tiling parameter for the proxy sub-entity mapper.
