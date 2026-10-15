# ACadSharp.Objects.RasterVariables

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.RasterVariables`

Represents a ACadSharp.Objects.RasterVariables object.

Object name F:ACadSharp.DxfFileToken.ObjectRasterVariables Dxf class name F:ACadSharp.DxfSubclassMarker.RasterVariables

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.RasterVariables')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.RasterVariables()
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

Class version 0.

### DisplayQuality

```text
ACadSharp.Objects.ImageDisplayQuality DisplayQuality { get; set; }
```

Gets or sets the image display quality (screen only).

### IsDisplayFrameShown

```text
System.Boolean IsDisplayFrameShown { get; set; }
```

Gets or sets if the image frame is shown.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Units

```text
ACadSharp.Types.Units.ImageUnits Units { get; set; }
```

AutoCAD units for inserting images. This is what one AutoCAD unit is equal to for the purpose of inserting and scaling images with an associated resolution.
