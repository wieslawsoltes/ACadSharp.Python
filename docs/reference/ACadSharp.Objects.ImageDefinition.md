# ACadSharp.Objects.ImageDefinition

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.ImageDefinition`

Represents a ACadSharp.Objects.ImageDefinition object.

Object name F:ACadSharp.DxfFileToken.ObjectImageDefinition Dxf class name F:ACadSharp.DxfSubclassMarker.RasterImageDef

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.ImageDefinition')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.ImageDefinition()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Objects.ImageDefinition(System.String name)
```

Documentation inherited from: `base member`.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### ClassVersion

```text
System.Int32 ClassVersion { get; }
```

Class version

### DefaultSize

```text
CSMath.XY DefaultSize { get; set; }
```

Default size of one pixel in AutoCAD units

### FileName

```text
System.String FileName { get; set; }
```

File name of image

### IsLoaded

```text
System.Boolean IsLoaded { get; set; }
```

Image-is-loaded flag.

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

### Size

```text
CSMath.XY Size { get; set; }
```

Image size in pixels

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Units

```text
ACadSharp.Objects.ResolutionUnit Units { get; set; }
```

Resolution units.
