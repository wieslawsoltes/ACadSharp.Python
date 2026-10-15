# ACadSharp.Objects.Group

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Group`

Represents a ACadSharp.Objects.Group object.

Object name F:ACadSharp.DxfFileToken.TableGroup Dxf class name F:ACadSharp.DxfSubclassMarker.Group

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Group')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Group()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Objects.Group(System.String name)
```

Documentation inherited from: `base member`.

### Add

```text
System.Void Add(ACadSharp.Entities.Entity entity)
```

Add an entity to the group.

- `entity`: 

### AddRange

```text
System.Void AddRange(System.Collections.Generic.IEnumerable[ACadSharp.Entities.Entity] entities)
```

Add multiple entities into the group.

- `entities`: 

### Clear

```text
System.Void Clear()
```

Removes all entities in the group.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### Remove

```text
System.Boolean Remove(ACadSharp.Entities.Entity entity)
```

Removes the entity from the group.

- `entity`: 

### Description

```text
System.String Description { get; set; }
```

Group description.

### Entities

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.Entity] Entities { get; }
```

Entities in this group.

**Remarks:** Hard-pointer handle to entity in group.

### IsUnnamed

```text
System.Boolean IsUnnamed { get; }
```

If the group has an automatic generated name.

**Remarks:** The name for an unnamed group will be managed by the ACadSharp.Objects.Collections.GroupCollection.

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

### Selectable

```text
System.Boolean Selectable { get; set; }
```

If the group is selectable.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
