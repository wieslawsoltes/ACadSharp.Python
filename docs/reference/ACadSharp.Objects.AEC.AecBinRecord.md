# ACadSharp.Objects.AEC.AecBinRecord

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.AEC.AecBinRecord`

Represents an AcAecBinRecord object used by AEC (Architecture, Engineering and Construction) entities.

AcAecBinRecord objects store the actual geometry and property data for AEC entities like AEC_WALL, AEC_DOOR, AEC_WINDOW, etc. The parent AEC entity contains a reference to this object which holds the actual data in a proprietary binary format.

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.AEC.AecBinRecord')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.AEC.AecBinRecord()
```

### BinaryData

```text
System.Byte[] BinaryData { get; set; }
```

Binary data containing the actual AEC object properties. The format is proprietary and undocumented.

### Name

```text
System.String Name { get; set; }
```

Optional name/identifier for this binary record.

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

### Version

```text
System.Int32 Version { get; set; }
```

Version number of the binary record format.
