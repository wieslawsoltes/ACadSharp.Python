# ACadSharp.Objects.AecCleanupGroup

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.AecCleanupGroup`

Represents an AcAecCleanupGroup object used by AEC Wall entities.

AcAecCleanupGroup objects manage wall cleanup operations, which control how walls join and interact with each other at intersections and endpoints. Object name: AEC_CLEANUP_GROUP

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.AecCleanupGroup')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.AecCleanupGroup()
```

Default constructor.

### .ctor

```text
ACadSharp.Objects.AecCleanupGroup(System.String name)
```

Initialize an ACadSharp.Objects.AecCleanupGroup with a specific name.

- `name`: Name of the cleanup group.

### Description

```text
System.String Description { get; set; }
```

Description of the cleanup group.

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

### RawData

```text
System.Byte[] RawData { get; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Version

```text
System.Int32 Version { get; set; }
```

AEC cleanup group version number.
