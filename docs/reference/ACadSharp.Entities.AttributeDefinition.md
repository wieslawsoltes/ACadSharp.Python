# ACadSharp.Entities.AttributeDefinition

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.AttributeDefinition`

Represents a ACadSharp.Entities.AttributeDefinition entity.

Object name F:ACadSharp.DxfFileToken.EntityAttributeDefinition Dxf class name F:ACadSharp.DxfSubclassMarker.AttributeDefinition

Base type: `ACadSharp.Entities.AttributeBase`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IText`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.AttributeDefinition')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.AttributeDefinition()
```

Initializes a new instance of the AttributeDefinition class.

### .ctor

```text
ACadSharp.Entities.AttributeDefinition(ACadSharp.Entities.AttributeEntity entity)
```

Initializes a new instance of the AttributeDefinition class using the specified attribute entity.

- `entity`: The attribute entity whose properties are used to initialize the new AttributeDefinition instance. Cannot be null.

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

### Prompt

```text
System.String Prompt { get; set; }
```

Prompt text for this attribute.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
