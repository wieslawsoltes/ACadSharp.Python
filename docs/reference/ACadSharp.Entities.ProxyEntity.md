# ACadSharp.Entities.ProxyEntity

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyEntity`

Represents a ACadSharp.Entities.ProxyEntity entity.

Object name F:ACadSharp.DxfFileToken.EntityProxyEntity Dxf class name F:ACadSharp.DxfSubclassMarker.ProxyEntity

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IProxy`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyEntity')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyEntity()
```

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### ClassId

```text
System.Int32 ClassId { get; }
```

Application dxf class ID.

### Data

```text
System.IO.Stream Data { get; set; }
```

Documentation inherited from: `base member`.

**Remarks:** No DxfCodeValue: the DXF reader has no handler for code 311 on an entity.

### DrawingFormat

```text
System.Int32 DrawingFormat { get; }
```

Object drawing format when it becomes a proxy: Low word is AcDbDwgVersion. High word is MaintenanceReleaseVersion.

### DxfClass

```text
ACadSharp.Classes.DxfClass DxfClass { get; set; }
```

### MaintenanceVersion

```text
System.Int32 MaintenanceVersion { get; set; }
```

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

**Remarks:** Always 498

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
