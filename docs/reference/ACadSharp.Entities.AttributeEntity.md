# ACadSharp.Entities.AttributeEntity

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.AttributeEntity`

Represents a ACadSharp.Entities.AttributeEntity entity.

Object name F:ACadSharp.DxfFileToken.EntityAttribute Dxf class name F:ACadSharp.DxfSubclassMarker.Attribute

Base type: `ACadSharp.Entities.AttributeBase`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IText`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.AttributeEntity')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.AttributeEntity()
```

Default constructor.

### .ctor

```text
ACadSharp.Entities.AttributeEntity(ACadSharp.Entities.AttributeDefinition definition)
```

Create an instance of an attribute based on a definition.

- `definition`: 

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
