# ACadSharp.Entities.Ole2Frame

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Ole2Frame`

Represents a ACadSharp.Entities.Ole2Frame entity.

Object name F:ACadSharp.DxfFileToken.EntityOle2Frame Dxf class name F:ACadSharp.DxfSubclassMarker.Ole2Frame

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Ole2Frame')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Ole2Frame()
```

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### BinaryData

```text
System.Byte[] BinaryData { get; set; }
```

Gets or sets the binary data associated with the object.

### IsPaperSpace

```text
System.Boolean IsPaperSpace { get; set; }
```

Gets or sets a value indicating whether the object resides in paper space.

### LowerRightCorner

```text
CSMath.XYZ LowerRightCorner { get; set; }
```

Gets or sets the lower-right corner of the object in world coordinate system (WCS).

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

### OleObjectType

```text
ACadSharp.Entities.OleObjectType OleObjectType { get; set; }
```

Gets or sets the type of the OLE (Object Linking and Embedding) object.

**Remarks:** The ACadSharp.Entities.Ole2Frame.OleObjectType property specifies the behavior and storage type of the OLE object: F:ACadSharp.Entities.OleObjectType.Link: The object is linked to an external source. F:ACadSharp.Entities.OleObjectType.Embedded: The object is embedded within the current document. F:ACadSharp.Entities.OleObjectType.Static: The object is a static representation.

### SourceApplication

```text
System.String SourceApplication { get; set; }
```

Gets or sets the name of the application that created or modified the associated data.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### UpperLeftCorner

```text
CSMath.XYZ UpperLeftCorner { get; set; }
```

Gets or sets the upper-left corner of the object in world coordinate system (WCS).

### Version

```text
System.Int16 Version { get; }
```

OLE version number.
