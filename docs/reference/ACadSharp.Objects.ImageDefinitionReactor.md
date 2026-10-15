# ACadSharp.Objects.ImageDefinitionReactor

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.ImageDefinitionReactor`

Represents a ACadSharp.Objects.ImageDefinitionReactor object. This object is for internal use only.

Object name F:ACadSharp.DxfFileToken.ObjectImageDefinitionReactor Dxf class name F:ACadSharp.DxfSubclassMarker.RasterImageDefReactor

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.ImageDefinitionReactor')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### ClassVersion

```text
System.Int32 ClassVersion { get; set; }
```

Class version 2.

### Image

```text
ACadSharp.Entities.RasterImage Image { get; set; }
```

Object ID for associated image object.

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
