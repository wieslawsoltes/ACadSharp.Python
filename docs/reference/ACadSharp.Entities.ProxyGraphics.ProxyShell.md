# ACadSharp.Entities.ProxyGraphics.ProxyShell

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyShell`

Represents a proxy shell entity in a CAD drawing. A proxy shell is a 3D representation of a solid or surface that is not natively supported by the CAD software, allowing for visualization and interaction with the geometry.

Base type: `ACadSharp.Entities.ProxyGraphics.ProxyMeshBase`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyShell')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyShell()
```

### Faces

```text
System.Collections.Generic.List[System.Int32[]] Faces { get; set; }
```

The faces of the shell. Each face is represented by an array of integers, where each integer corresponds to a vertex index in the ACadSharp.Entities.ProxyGraphics.ProxyMeshBase.Vertices list.

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.
