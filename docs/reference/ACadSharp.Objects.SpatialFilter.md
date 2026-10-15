# ACadSharp.Objects.SpatialFilter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.SpatialFilter`

Represents a ACadSharp.Objects.SpatialFilter object.

Object name F:ACadSharp.DxfFileToken.ObjectSpatialFilter Dxf class name F:ACadSharp.DxfSubclassMarker.SpatialFilter

Base type: `ACadSharp.Objects.Filter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.SpatialFilter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.SpatialFilter()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Objects.SpatialFilter(System.String name)
```

Documentation inherited from: `base member`.

### SpatialFilterEntryName

```text
static System.String SpatialFilterEntryName = SPATIAL
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### BackDistance

```text
System.Double BackDistance { get; set; }
```

Back clipping plane distance.

### BoundaryPoints

```text
System.Collections.Generic.List[CSMath.XY] BoundaryPoints { get; set; }
```

Clip boundary definition point (in OCS). Always 2 or more based on an xref scale of 1.

**Remarks:** 2 points = Rectangular clip boundary (lower-left and upper-right) greater than 2 points = Polyline clip boundary

### ClipBackPlane

```text
System.Boolean ClipBackPlane { get; set; }
```

Back clipping plane flag.

### ClipFrontPlane

```text
System.Boolean ClipFrontPlane { get; set; }
```

Front clipping plane flag.

### DisplayBoundary

```text
System.Boolean DisplayBoundary { get; set; }
```

Clip boundary display enabled flag.

### FrontDistance

```text
System.Double FrontDistance { get; set; }
```

Front clipping plane distance.

### InsertTransform

```text
CSMath.Matrix4 InsertTransform { get; set; }
```

This matrix transforms points into the coordinate system of the clip boundary.

### InverseInsertTransform

```text
CSMath.Matrix4 InverseInsertTransform { get; set; }
```

This matrix is the inverse of the original block reference (insert entity) transformation. The original block reference transformation is the one that is applied to all entities in the block when the block reference is regenerated.

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.

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

### Origin

```text
CSMath.XYZ Origin { get; set; }
```

Origin used to define the local coordinate system of the clip boundary.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
