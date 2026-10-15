# ACadSharp.Entities.ProxyGraphics.VertexTraits

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.VertexTraits`

Represents the traits of a vertex in proxy graphics.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.VertexTraits')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.VertexTraits()
```

### Normals

```text
System.Collections.Generic.List[CSMath.XYZ] Normals { get; set; }
```

Gets or sets the list of normals associated with the vertex.

### Orientation

```text
System.Int32 Orientation { get; set; }
```

Gets or sets the orientation of the vertex.
