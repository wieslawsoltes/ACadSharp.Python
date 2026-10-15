# ACadSharp.Entities.ProxyGraphics.ProxyMeshBase

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyMeshBase`

Represents a proxy mesh geometry in AutoCAD.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyMeshBase')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### EdgeTraits

```text
ACadSharp.Entities.ProxyGraphics.EdgeTraits EdgeTraits { get; set; }
```

Gets or sets the traits associated with the edges of the mesh.

### FaceTraits

```text
ACadSharp.Entities.ProxyGraphics.FaceTraits FaceTraits { get; set; }
```

Gets or sets the traits associated with the faces of the mesh.

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### VertexTraits

```text
ACadSharp.Entities.ProxyGraphics.VertexTraits VertexTraits { get; set; }
```

Gets or sets the traits associated with the vertices of the mesh.

### Vertices

```text
System.Collections.Generic.List[CSMath.XYZ] Vertices { get; set; }
```

Gets or sets the list of vertices that define the mesh geometry.
