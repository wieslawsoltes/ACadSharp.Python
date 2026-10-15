# ACadSharp.Objects.DimensionAssociation.OsnapPointRef

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.DimensionAssociation+OsnapPointRef`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.DimensionAssociation+OsnapPointRef')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.DimensionAssociation.OsnapPointRef()
```

### Geometry

```text
ACadSharp.CadObject Geometry { get; set; }
```

Gets or sets the associated geometry object.

### GeometryParameter

```text
System.Double GeometryParameter { get; set; }
```

Gets or sets the geometry parameter used for the Near object snap (Osnap).

### GsMarker

```text
System.Int32 GsMarker { get; set; }
```

Gets or sets the graphics system marker (GsMarker) associated with the main object.

### HasLastPointRef

```text
System.Boolean HasLastPointRef { get; set; }
```

### IntersectionGsMarker

```text
System.Int32 IntersectionGsMarker { get; set; }
```

### IntersectionSubType

```text
ACadSharp.Objects.SubentType IntersectionSubType { get; set; }
```

### ObjectOsnapType

```text
ACadSharp.Objects.ObjectOsnapType ObjectOsnapType { get; set; }
```

Gets or sets the object snap type associated with the entity.

### OsnapPoint

```text
CSMath.XYZ OsnapPoint { get; set; }
```

Gets or sets the object snap (Osnap) point in world coordinate system (WCS).

**Remarks:** The Osnap point is used to specify precise locations on geometry for object snapping operations.

### SubentType

```text
ACadSharp.Objects.SubentType SubentType { get; set; }
```

Gets or sets the type of the rotated dimension, indicating whether it is parallel or perpendicular.
