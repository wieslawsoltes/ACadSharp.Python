# ACadSharp.Classes.DxfClass

`class` · `ACadSharp` · CLR name: `ACadSharp.Classes.DxfClass`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Classes.DxfClass')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Classes.DxfClass()
```

### DefaultApplicationName

```text
static System.String DefaultApplicationName = ObjectDBX Classes
```

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### ApplicationName

```text
System.String ApplicationName { get; set; }
```

Application name. Posted in Alert box when a class definition listed in this section is not currently loaded.

### ClassNumber

```text
System.Int16 ClassNumber { get; set; }
```

Class number.

### CppClassName

```text
System.String CppClassName { get; set; }
```

C++ class name. Used to bind with software that defines object class behavior; always unique.

### DwgVersion

```text
ACadSharp.ACadVersion DwgVersion { get; set; }
```

### DxfName

```text
System.String DxfName { get; set; }
```

Class DXF record name; always unique.

### InstanceCount

```text
System.Int32 InstanceCount { get; set; }
```

Instance count for a custom class.

### IsAnEntity

```text
System.Boolean IsAnEntity { get; set; }
```

Is-an-entity flag. Set to 1 if class was derived from the AcDbEntity class and can reside in the BLOCKS or ENTITIES section. If 0, instances may appear only in the OBJECTS section

### ItemClassId

```text
System.Int16 ItemClassId { get; set; }
```

Item class id.

**Remarks:** Only effective for dwg.

### ProxyFlags

```text
ACadSharp.Classes.ProxyFlags ProxyFlags { get; set; }
```

Proxy capabilities flag. Bit-coded value that indicates the capabilities of this object as a proxy.

### WasZombie

```text
System.Boolean WasZombie { get; set; }
```

Was-a-proxy flag. Set to 1 if class was not loaded when this DXF file was created, and 0 otherwise.
