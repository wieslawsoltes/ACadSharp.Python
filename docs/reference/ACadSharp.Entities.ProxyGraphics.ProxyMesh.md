# ACadSharp.Entities.ProxyGraphics.ProxyMesh

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyMesh`

Represents a proxy mesh graphics entity in AutoCAD.

Base type: `ACadSharp.Entities.ProxyGraphics.ProxyMeshBase`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyMesh')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyMesh()
```

### ColumnCount

```text
System.Int32 ColumnCount { get; set; }
```

Gets or sets the number of columns in the mesh.

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### RowCount

```text
System.Int32 RowCount { get; set; }
```

Gets or sets the number of rows in the mesh.
