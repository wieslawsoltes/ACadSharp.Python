# ACadSharp.Entities.RasterImage

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.RasterImage`

Represents a ACadSharp.Entities.RasterImage entity.

Object name F:ACadSharp.DxfFileToken.EntityImage Dxf class name F:ACadSharp.DxfSubclassMarker.RasterImage

Base type: `ACadSharp.Entities.CadWipeoutBase`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.RasterImage')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.RasterImage(ACadSharp.Objects.ImageDefinition definition)
```

Initializes a new instance of the ACadSharp.Entities.RasterImage class.

- `definition`: 

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### IsValid

```text
System.Boolean IsValid(ACadSharp.IO.CadFileFormat format, ACadSharp.ACadVersion version, out System.Collections.Generic.IList[System.String] errors)
```

Documentation inherited from: `base member`.

### Definition

```text
ACadSharp.Objects.ImageDefinition Definition { get; set; }
```

Documentation inherited from: `base member`.

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
