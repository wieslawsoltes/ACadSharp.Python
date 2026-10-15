# ACadSharp.Entities.AttributeBase

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.AttributeBase`

Common base class for ACadSharp.Entities.AttributeEntity and ACadSharp.Entities.AttributeDefinition.

Base type: `ACadSharp.Entities.TextEntity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IText`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.AttributeBase')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.AttributeBase()
```

### AttributeType

```text
ACadSharp.Entities.AttributeType AttributeType { get; set; }
```

Attribute type.

### Flags

```text
ACadSharp.Entities.AttributeFlags Flags { get; set; }
```

Attribute flags.

### IsLocked

```text
System.Boolean IsLocked { get; set; }
```

Gets or sets a value indicating whether the object is currently locked.

### MText

```text
ACadSharp.Entities.MText MText { get; set; }
```

Gets or sets the multi-line text content associated with this object.

### Tag

```text
System.String Tag { get; set; }
```

Specifies the tag string of the object

**Value:** Cannot contain spaces (not applied)

### Version

```text
System.Byte Version { get; set; }
```

### VerticalAlignment

```text
ACadSharp.Entities.TextVerticalAlignmentType VerticalAlignment { get; set; }
```
