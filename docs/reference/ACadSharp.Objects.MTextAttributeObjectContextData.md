# ACadSharp.Objects.MTextAttributeObjectContextData

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.MTextAttributeObjectContextData`

Represents the context data for the multiline text of an ACadSharp.Entities.AttributeEntity in a specific annotation scale.

Base type: `ACadSharp.Objects.AnnotScaleObjectContextData`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MTextAttributeObjectContextData')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.MTextAttributeObjectContextData()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### AlignmentPoint

```text
CSMath.XYZ AlignmentPoint { get; set; }
```

Alignment point of the text.

### AttachmentPoint

```text
ACadSharp.Entities.AttachmentPointType AttachmentPoint { get; set; }
```

Attachment point that defines how the text is aligned relative to the ACadSharp.Objects.MTextAttributeObjectContextData.InsertPoint.

### InsertPoint

```text
CSMath.XYZ InsertPoint { get; set; }
```

Insert point of the text.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### Rotation

```text
System.Double Rotation { get; set; }
```

The rotation angle of the text, in radians.

### Value290

```text
System.Boolean Value290 { get; set; }
```

Unknown flag stored in the DXF code 290.
