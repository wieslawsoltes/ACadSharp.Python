# ACadSharp.Objects.VisualStyle

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.VisualStyle`

Represents a ACadSharp.Objects.VisualStyle object

Object name F:ACadSharp.DxfFileToken.ObjectVisualStyle Dxf class name F:ACadSharp.DxfSubclassMarker.VisualStyle

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.VisualStyle')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.VisualStyle()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Objects.VisualStyle(System.String name)
```

Documentation inherited from: `base member`.

### DefaultName

```text
static System.String DefaultName = 2dWireframe
```

Default ACadSharp.Objects.VisualStyle name.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### Brightness

```text
System.Double Brightness { get; set; }
```

### Color

```text
ACadSharp.Color Color { get; set; }
```

Color

### Description

```text
System.String Description { get; set; }
```

Description

### DisplaySettings

```text
System.Int32 DisplaySettings { get; set; }
```

### EdgeApplyStyleFlag

```text
System.Int16 EdgeApplyStyleFlag { get; set; }
```

### EdgeColor

```text
System.Int32 EdgeColor { get; set; }
```

### EdgeCreaseAngle

```text
System.Double EdgeCreaseAngle { get; set; }
```

### EdgeIntersectionColor

```text
ACadSharp.Color EdgeIntersectionColor { get; set; }
```

### EdgeIntersectionLineType

```text
System.Int32 EdgeIntersectionLineType { get; set; }
```

### EdgeIsolineCount

```text
System.Int16 EdgeIsolineCount { get; set; }
```

### EdgeJitter

```text
System.Int32 EdgeJitter { get; set; }
```

### EdgeModifiers

```text
System.Int32 EdgeModifiers { get; set; }
```

### EdgeObscuredColor

```text
ACadSharp.Color EdgeObscuredColor { get; set; }
```

### EdgeObscuredLineType

```text
System.Int32 EdgeObscuredLineType { get; set; }
```

### EdgeOverhang

```text
System.Int32 EdgeOverhang { get; set; }
```

### EdgeSilhouetteColor

```text
ACadSharp.Color EdgeSilhouetteColor { get; set; }
```

### EdgeSilhouetteWidth

```text
System.Int32 EdgeSilhouetteWidth { get; set; }
```

### EdgeStyle

```text
System.Int32 EdgeStyle { get; set; }
```

### EdgeStyleModel

```text
ACadSharp.Objects.EdgeStyleModel EdgeStyleModel { get; set; }
```

### EdgeWidth

```text
System.Int32 EdgeWidth { get; set; }
```

### FaceColorMode

```text
ACadSharp.Objects.FaceColorMode FaceColorMode { get; set; }
```

### FaceLightingModel

```text
ACadSharp.Objects.FaceLightingModelType FaceLightingModel { get; set; }
```

Gets or sets the lighting model used to render the face.

**Remarks:** The lighting model determines how light interacts with the face during rendering, affecting its appearance and shading. Set this property to control the visual style of the face in 3D scenes.

### FaceLightingQuality

```text
ACadSharp.Objects.FaceLightingQualityType FaceLightingQuality { get; set; }
```

### FaceModifiers

```text
ACadSharp.Objects.FaceModifierType FaceModifiers { get; set; }
```

### FaceOpacityLevel

```text
System.Double FaceOpacityLevel { get; set; }
```

Face opacity level

### FaceSpecularLevel

```text
System.Double FaceSpecularLevel { get; set; }
```

Face specular level

### FaceStyleMonoColor

```text
ACadSharp.Color FaceStyleMonoColor { get; set; }
```

Face style mono color

### HaloGap

```text
System.Int16 HaloGap { get; set; }
```

### InternalFlag

```text
System.Boolean InternalFlag { get; }
```

Internal use only flag

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

### OpacityLevel

```text
System.Double OpacityLevel { get; set; }
```

### PrecisionFlag

```text
System.Boolean PrecisionFlag { get; set; }
```

Edge hide precision flag

### RasterFile

```text
System.String RasterFile { get; set; }
```

Raster file name

### ShadowType

```text
System.Int16 ShadowType { get; set; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Type

```text
System.Int32 Type { get; set; }
```

Type
