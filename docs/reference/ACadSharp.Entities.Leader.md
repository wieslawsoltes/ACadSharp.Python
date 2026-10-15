# ACadSharp.Entities.Leader

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Leader`

Represents a ACadSharp.Entities.Leader entity.

Object name F:ACadSharp.DxfFileToken.EntityLeader Dxf class name F:ACadSharp.DxfSubclassMarker.Leader

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Leader')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Leader()
```

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

### SetDimensionOverride

```text
System.Void SetDimensionOverride(ACadSharp.Tables.DimensionStyle styleOverride)
```

Applies the specified dimension style override to the current leader, updating its extended data to reflect the overridden properties (e.g. arrowhead block, DIMLDRBLK = code 341).

**Remarks:** Only properties that differ between the leader's current style and styleOverride are serialised into the DSTYLE XDATA block, mirroring the behaviour of ACadSharp.Entities.Dimension.SetDimensionOverride(ACadSharp.Tables.DimensionStyle).

- `styleOverride`: The dimension style whose values should override the leader's current style. Only properties with values different from the current style are applied.

### SetStyleOverrideMap

```text
System.Void SetStyleOverrideMap(ACadSharp.DxfClassMap map)
```

Sets the style override mapping for the current leader using the specified DXF class map, writing the entries as ACAD / DSTYLE / { … } extended data.

- `map`: A DXF class map containing the property overrides to apply.

### AnnotationOffset

```text
CSMath.XYZ AnnotationOffset { get; set; }
```

Offset of last leader vertex from annotation placement point.

### ArrowHeadEnabled

```text
System.Boolean ArrowHeadEnabled { get; set; }
```

Arrowhead flag.

### AssociatedAnnotation

```text
ACadSharp.Entities.Entity AssociatedAnnotation { get; }
```

Hard reference to associated annotation (mtext, tolerance, or insert entity).

### BlockOffset

```text
CSMath.XYZ BlockOffset { get; set; }
```

Offset of last leader vertex from block reference insertion point.

### CreationType

```text
ACadSharp.Entities.LeaderCreationType CreationType { get; set; }
```

Leader creation flag, AssociatedAnnotation type.

**Value:** 0 = mtext 1 = tolerance 2 = insert 3 = none (default)

### HasHookline

```text
System.Boolean HasHookline { get; }
```

Hook line flag.

### HookLineDirection

```text
ACadSharp.Entities.HookLineDirection HookLineDirection { get; set; }
```

Hook line direction.

### HorizontalDirection

```text
CSMath.XYZ HorizontalDirection { get; set; }
```

Horizontal direction for leader.

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

### PathType

```text
ACadSharp.Entities.LeaderPathType PathType { get; set; }
```

Leader Path Type.

**Value:** 0 = straight lines 1 = spline

### Style

```text
ACadSharp.Tables.DimensionStyle Style { get; set; }
```

Dimension Style.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### TextHeight

```text
System.Double TextHeight { get; set; }
```

Text annotation height.

### TextWidth

```text
System.Double TextWidth { get; set; }
```

Text annotation width.

### Vertices

```text
System.Collections.Generic.List[CSMath.XYZ] Vertices { get; set; }
```

Vertices in leader.
