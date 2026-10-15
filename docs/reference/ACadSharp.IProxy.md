# ACadSharp.IProxy

`interface` · `ACadSharp` · CLR name: `ACadSharp.IProxy`

Represents a proxy object containing custom data.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IProxy')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ClassId

```text
System.Int32 ClassId { get; }
```

Application object's class ID.

### Data

```text
System.IO.Stream Data { get; set; }
```

Gets or sets the retained data of the original object.

### DxfClass

```text
ACadSharp.Classes.DxfClass DxfClass { get; set; }
```

Application object's class.

### MaintenanceVersion

```text
System.Int32 MaintenanceVersion { get; set; }
```

### OriginalDataFormatDxf

```text
System.Boolean OriginalDataFormatDxf { get; set; }
```

Original custom object data format.

### ProxyClassId

```text
System.Int32 ProxyClassId { get; }
```

Proxy object class ID.

### Version

```text
ACadSharp.ACadVersion Version { get; set; }
```
