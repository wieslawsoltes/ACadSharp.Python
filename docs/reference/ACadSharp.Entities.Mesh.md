# ACadSharp.Entities.Mesh

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Mesh`

Represents a ACadSharp.Entities.Mesh entity.

Object name F:ACadSharp.DxfFileToken.EntityMesh Dxf class name F:ACadSharp.DxfSubclassMarker.Mesh

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Mesh')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Mesh()
```

### AddTextureCoordinate

```text
System.Void AddTextureCoordinate(CSMath.XYZ uvw)
```

Adds a texture coordinate to the mesh. The coordinates are stored in an XRecord in the mesh's extension dictionary.

- `uvw`: The texture coordinate to add.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### BlendCrease

```text
System.Boolean BlendCrease { get; set; }
```

Blend Crease flag

### Edges

```text
System.Collections.Generic.List[ACadSharp.Entities.Mesh.Edge] Edges { get; }
```

Edges of level 0

### Faces

```text
System.Collections.Generic.List[System.Int32[]] Faces { get; }
```

Face list of level 0

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### SubdivisionLevel

```text
System.Int32 SubdivisionLevel { get; set; }
```

Number of subdivision level

### TextureCoordinates

```text
System.Collections.Generic.IEnumerable[CSMath.XYZ] TextureCoordinates { get; set; }
```

Per-vertex texture coordinates (U, V, W). Empty if the mesh has no UV mapping.

**Remarks:** Persisted as an ADSK_XREC_SUBDVERTEXTEXCOORDS XRecord on the mesh extension dictionary, matching the AutoCAD/AcDbSubDMesh convention. The list must have the same length as ACadSharp.Entities.Mesh.Vertices.

### Version

```text
System.Int16 Version { get; set; }
```

Version number.

### Vertices

```text
System.Collections.Generic.List[CSMath.XYZ] Vertices { get; }
```

Vertex count of level 0.
