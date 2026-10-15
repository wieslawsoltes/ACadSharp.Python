# ACadSharp.Entities.Surface

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Surface`

Represents a ACadSharp.Entities.Surface entity.

Object name F:ACadSharp.DxfFileToken.EntitySurface Dxf class name F:ACadSharp.DxfSubclassMarker.Surface

Base type: `ACadSharp.Entities.ModelerGeometry`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Surface')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Surface()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
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

### UIsolines

```text
System.Int16 UIsolines { get; set; }
```

Number of U isolines.

### VIsolines

```text
System.Int16 VIsolines { get; set; }
```

Number of V isolines.
