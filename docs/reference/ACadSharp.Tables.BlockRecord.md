# ACadSharp.Tables.BlockRecord

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.BlockRecord`

Represents a ACadSharp.Tables.BlockRecord entry

Object name F:ACadSharp.DxfFileToken.TableBlockRecord Dxf class name F:ACadSharp.DxfSubclassMarker.BlockRecord

Base type: `ACadSharp.Tables.TableEntry`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.BlockRecord')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.BlockRecord(System.String name)
```

Default constructor.

- `name`: Unique name for this block record.

### .ctor

```text
ACadSharp.Tables.BlockRecord(System.String name, System.String xrefFile, System.Boolean isOverlay = False)
```

Initializes a new instance of the BlockRecord class as an external reference drawing.

**Remarks:** Only DWG files can be used as externally referenced blocks.

- `name`: Block name.
- `xrefFile`: External reference path name.
- `isOverlay`: Specifies if the external reference is an overlay, by default it is set to false.

### AnonymousPrefix

```text
static System.String AnonymousPrefix = *A
```

Prefix used for naming any anonymous block managed by ACadSharp.

### ModelSpaceName

```text
static System.String ModelSpaceName = *Model_Space
```

Default block record name for the model space

### PaperSpaceName

```text
static System.String PaperSpaceName = *Paper_Space
```

Default block record name for the paper space

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

### CreateSortEntitiesTable

```text
ACadSharp.Objects.SortEntitiesTable CreateSortEntitiesTable()
```

Create an entity sorter table for this block.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Get the bounding box for all the entities in the block.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox(System.Boolean ignoreInfinite)
```

Get the bounding box for all the entities in the block.

- `ignoreInfinite`: Ignore infinite entities, default: true

### GetSortedEntities

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.Entity] GetSortedEntities()
```

Get the entities in this block record sorted by it's handle and the sorter assigned if is present.

**Remarks:** If the record is not in a document the entities will not be sorted unless there is a ACadSharp.Tables.BlockRecord.SortEntitiesTable assigned to the block.

### AttributeDefinitions

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.AttributeDefinition] AttributeDefinitions { get; }
```

Attribute definitions in this block

### BlockEnd

```text
ACadSharp.Blocks.BlockEnd BlockEnd { get; }
```

End block entity for this Block record.

### BlockEntity

```text
ACadSharp.Blocks.Block BlockEntity { get; }
```

Block entity for this record.

### CanScale

```text
System.Boolean CanScale { get; set; }
```

Specifies the scaling allowed for the block.

### Entities

```text
ACadSharp.CadObjectCollection[ACadSharp.Entities.Entity] Entities { get; }
```

Entities owned by this block.

**Remarks:** Entities with an owner cannot be added to another block.

### EvaluationGraph

```text
ACadSharp.Objects.Evaluations.EvaluationGraph EvaluationGraph { get; }
```

Gets the evaluation graph for this block if it has dynamic properties attached to it.

### Flags

```text
ACadSharp.Blocks.BlockTypeFlags Flags { get; set; }
```

### HasAttributes

```text
System.Boolean HasAttributes { get; }
```

Flag indicating if the Block has Attributes attached

### IsAnonymous

```text
System.Boolean IsAnonymous { get; set; }
```

Blocks with the anonymous flag set are managed by this library or the editing software, this may affect the entities or the block properties.

### IsDynamic

```text
System.Boolean IsDynamic { get; }
```

Active flag if it has an ACadSharp.Objects.Evaluations.EvaluationGraph attached to it with dynamic expressions.

### IsExplodable

```text
System.Boolean IsExplodable { get; set; }
```

Specifies whether the block can be exploded.

### IsUnloaded

```text
System.Boolean IsUnloaded { get; set; }
```

Gets or sets a value indicating whether the XRef is unloaded.

**Remarks:** This flag only takes effect if its an external reference.

### Layout

```text
ACadSharp.Objects.Layout Layout { get; }
```

Associated Layout.

### ModelSpace

```text
static ACadSharp.Tables.BlockRecord ModelSpace { get; }
```

Create an instance of the *Model_Space block.

**Remarks:** It only can be one Model in each document.

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

### PaperSpace

```text
static ACadSharp.Tables.BlockRecord PaperSpace { get; }
```

Create an instance of the *Paper_Space block.

**Remarks:** This is the default paper space in the document.

### Preview

```text
System.Byte[] Preview { get; set; }
```

DXF: Binary data for bitmap preview.

**Remarks:** Optional

### SortEntitiesTable

```text
ACadSharp.Objects.SortEntitiesTable SortEntitiesTable { get; }
```

Sort entities table for this block record.

### Source

```text
ACadSharp.Tables.BlockRecord Source { get; }
```

Gets the source block. Only present if the block is dynamic and is in the same document as its source.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Units

```text
ACadSharp.Types.Units.UnitsType Units { get; set; }
```

Block insertion units

### Viewports

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.Viewport] Viewports { get; }
```

ViewPorts attached to this block
