# ACadSharp.Entities.Insert

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Insert`

Represents a ACadSharp.Entities.Insert entity.

Object name F:ACadSharp.DxfFileToken.EntityInsert Dxf class name F:ACadSharp.DxfSubclassMarker.Insert

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Insert')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Insert(ACadSharp.Tables.BlockRecord block)
```

Constructor to reference an insert to a block record

- `block`: Block Record to reference

- Raises `System.ArgumentNullException`: 

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

### Explode

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.Entity] Explode()
```

Returns an enumerable collection of entities representing the exploded contents of the block, with all entities transformed into the current coordinate system.

**Remarks:** The returned entities are clones or converted equivalents of the original block entities, with geometric transformations applied. For example, arcs and circles are converted to their corresponding geometric representations. The original block and its entities remain unchanged.

**Returns:** An enumerable collection of ACadSharp.Entities.Entity objects that make up the exploded block. Each entity is transformed according to the block's transform. The collection may be empty if the block contains no entities.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### GetTransform

```text
CSMath.Transform GetTransform()
```

Get the transform that will be applied to the entities in the ACadSharp.Tables.BlockRecord when this entity is processed. This accounts for the block base point so the inserted geometry lands in the expected position.

### IsValid

```text
System.Boolean IsValid(ACadSharp.IO.CadFileFormat format, ACadSharp.ACadVersion version, out System.Collections.Generic.IList[System.String] errors)
```

Documentation inherited from: `base member`.

### UpdateAttributes

```text
System.Void UpdateAttributes()
```

Updates all attribute definitions contained in the block reference as ACadSharp.Entities.AttributeDefinition entities in the insert.

**Remarks:** This will update the attributes based on their ACadSharp.Entities.AttributeBase.Tag.

### Attributes

```text
ACadSharp.SeqendCollection[ACadSharp.Entities.AttributeEntity] Attributes { get; }
```

Attributes from the block reference

**Remarks:** If an attribute should be added in this collection a definition will be added into the block reference as well

### Block

```text
ACadSharp.Tables.BlockRecord Block { get; }
```

Gets the insert block definition.

### ColumnCount

```text
System.UInt16 ColumnCount { get; set; }
```

Column count

### ColumnSpacing

```text
System.Double ColumnSpacing { get; set; }
```

Column spacing

### HasAttributes

```text
System.Boolean HasAttributes { get; }
```

True if the insert has attribute entities in it

### HasDynamicSubclass

```text
System.Boolean HasDynamicSubclass { get; }
```

Documentation inherited from: `base member`.

### InsertPoint

```text
CSMath.XYZ InsertPoint { get; set; }
```

A 3D WCS coordinate representing the insertion or origin point.

### IsMultiple

```text
System.Boolean IsMultiple { get; }
```

Specifies the rotation angle for the object.

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

### Rotation

```text
System.Double Rotation { get; set; }
```

Specifies the rotation angle for the object.

**Value:** The rotation angle in radians.

### RowCount

```text
System.UInt16 RowCount { get; set; }
```

Row count

### RowSpacing

```text
System.Double RowSpacing { get; set; }
```

Row spacing

### SpatialFilter

```text
ACadSharp.Objects.SpatialFilter SpatialFilter { get; set; }
```

Gets or set the spatial filter entry for this ACadSharp.Entities.Insert entity.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### XScale

```text
System.Double XScale { get; set; }
```

X scale factor.

### YScale

```text
System.Double YScale { get; set; }
```

Y scale factor.

### ZScale

```text
System.Double ZScale { get; set; }
```

Z scale factor.
