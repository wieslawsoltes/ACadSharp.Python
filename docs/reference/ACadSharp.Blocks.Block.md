# ACadSharp.Blocks.Block

`class` · `ACadSharp` · CLR name: `ACadSharp.Blocks.Block`

Represents a ACadSharp.Blocks.Block entity

Object name F:ACadSharp.DxfFileToken.Block Dxf class name F:ACadSharp.DxfSubclassMarker.BlockBegin

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Blocks.Block')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Blocks.Block(ACadSharp.Tables.BlockRecord record)
```

Documentation inherited from: `base member`.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

**Remarks:** Block entities don't have any geometric properties.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

**Remarks:** Cloning a block will also unattached it from the record.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### BasePoint

```text
CSMath.XYZ BasePoint { get; set; }
```

Specifies the insert point of the block.

### BlockOwner

```text
ACadSharp.Tables.BlockRecord BlockOwner { get; }
```

Block record that owns this entity

### Comments

```text
System.String Comments { get; set; }
```

Specifies the comments for the block or drawing.

### Flags

```text
ACadSharp.Blocks.BlockTypeFlags Flags { get; set; }
```

Block active flags.

### IsUnloaded

```text
System.Boolean IsUnloaded { get; set; }
```

Gets or sets a value indicating whether the XRef is unloaded.

**Remarks:** This flag only takes effect if its an external reference.

### Name

```text
System.String Name { get; set; }
```

Specifies the name of the object.

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

### XRefPath

```text
System.String XRefPath { get; set; }
```

Gets the path of the block, document, application, or external reference.
