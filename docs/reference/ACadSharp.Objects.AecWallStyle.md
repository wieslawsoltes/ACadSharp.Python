# ACadSharp.Objects.AecWallStyle

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.AecWallStyle`

Represents an AcAecWallStyle object used by AEC Wall entities.

AcAecWallStyle objects define wall style properties such as components, materials, and other wall construction parameters used by AEC_WALL entities. These objects are stored in the DWG file and referenced by wall entities. Object name: AEC_WALL_STYLE

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.AecWallStyle')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.AecWallStyle()
```

Default constructor.

### .ctor

```text
ACadSharp.Objects.AecWallStyle(System.String name)
```

Initialize an ACadSharp.Objects.AecWallStyle with a specific name.

- `name`: Name of the wall style.

### RawData

```text
System.Byte[] RawData
```

### Description

```text
System.String Description { get; set; }
```

Description of the wall style.

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

### Version

```text
System.Int32 Version { get; set; }
```

AEC wall style version number.
