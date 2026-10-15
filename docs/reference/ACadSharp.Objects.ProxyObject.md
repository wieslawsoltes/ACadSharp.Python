# ACadSharp.Objects.ProxyObject

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.ProxyObject`

Represents a ACadSharp.Objects.ProxyObject entity.

Object name F:ACadSharp.DxfFileToken.ObjectProxyObject Dxf class name F:ACadSharp.DxfSubclassMarker.ProxyObject

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`, `ACadSharp.IProxy`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.ProxyObject')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.ProxyObject()
```

### BinaryData

```text
System.IO.Stream BinaryData { get; set; }
```

### ClassId

```text
System.Int32 ClassId { get; }
```

Documentation inherited from: `base member`.

### Data

```text
System.IO.Stream Data { get; set; }
```

Documentation inherited from: `base member`.

### DrawingFormat

```text
System.Int32 DrawingFormat { get; }
```

Object drawing format when it becomes a proxy: Low word is AcDbDwgVersion. High word is MaintenanceReleaseVersion.

### DxfClass

```text
ACadSharp.Classes.DxfClass DxfClass { get; set; }
```

Documentation inherited from: `base member`.

### MaintenanceVersion

```text
System.Int32 MaintenanceVersion { get; set; }
```

Documentation inherited from: `base member`.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### OriginalDataFormatDxf

```text
System.Boolean OriginalDataFormatDxf { get; set; }
```

Documentation inherited from: `base member`.

### ProxyClassId

```text
System.Int32 ProxyClassId { get; }
```

Documentation inherited from: `base member`.

**Remarks:** Always 499

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Version

```text
ACadSharp.ACadVersion Version { get; set; }
```

Documentation inherited from: `base member`.
