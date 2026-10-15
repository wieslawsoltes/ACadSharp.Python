# ACadSharp.Tables.VPort

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.VPort`

Represents a ACadSharp.Tables.VPort table entry

Object name F:ACadSharp.DxfFileToken.TableVport Dxf class name F:ACadSharp.DxfSubclassMarker.VPort

Base type: `ACadSharp.Tables.TableEntry`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.VPort')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.VPort()
```

### .ctor

```text
ACadSharp.Tables.VPort(System.String name)
```

### DefaultName

```text
static System.String DefaultName = *Active
```

### Clone

```text
ACadSharp.CadObject Clone()
```

### AmbientColor

```text
ACadSharp.Color AmbientColor { get; set; }
```

Ambient color(only output when non-black)

### AspectRatio

```text
System.Double AspectRatio { get; set; }
```

Aspect ratio

### BackClippingPlane

```text
System.Double BackClippingPlane { get; set; }
```

Back clipping plane(offset from target point)

### BaseUcs

```text
ACadSharp.Tables.UCS BaseUcs { get; set; }
```

Base Ucs

**Remarks:** AcDbUCSTableRecord of base UCS if UCS is orthographic(79 code is non-zero). If not present and 79 code is non-zero, then base UCS is taken to be WORLD

### BottomLeft

```text
CSMath.XY BottomLeft { get; set; }
```

Lower-left corner of viewport

### Brightness

```text
System.Double Brightness { get; set; }
```

Brightness

### Center

```text
CSMath.XY Center { get; set; }
```

View center point(in DCS)

### CircleZoomPercent

```text
System.Int16 CircleZoomPercent { get; set; }
```

Circle sides

### Contrast

```text
System.Double Contrast { get; set; }
```

Contrast

### Default

```text
static ACadSharp.Tables.VPort Default { get; }
```

### DefaultLighting

```text
ACadSharp.Tables.DefaultLightingType DefaultLighting { get; set; }
```

Default Lighting type

### Direction

```text
CSMath.XYZ Direction { get; set; }
```

View direction from target point(in WCS)

### Elevation

```text
System.Double Elevation { get; set; }
```

Elevation

### FrontClippingPlane

```text
System.Double FrontClippingPlane { get; set; }
```

Front clipping plane(offset from target point)

### GridFlags

```text
ACadSharp.Tables.GridFlags GridFlags { get; set; }
```

Grid flags

### GridSpacing

```text
CSMath.XY GridSpacing { get; set; }
```

Grid spacing X and Y

### IsometricSnap

```text
System.Boolean IsometricSnap { get; set; }
```

Snap style

### LensLength

```text
System.Double LensLength { get; set; }
```

Lens length

### MinorGridLinesPerMajorGridLine

```text
System.Int16 MinorGridLinesPerMajorGridLine { get; set; }
```

Major grid lines

### NamedUcs

```text
ACadSharp.Tables.UCS NamedUcs { get; set; }
```

Named Ucs

**Remarks:** AcDbUCSTableRecord if UCS is a named UCS.If not present, then UCS is unnamed

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

### Origin

```text
CSMath.XYZ Origin { get; set; }
```

UCS origin

### OrthographicType

```text
ACadSharp.OrthographicType OrthographicType { get; set; }
```

Orthographic type of UCS

### RenderMode

```text
ACadSharp.RenderMode RenderMode { get; set; }
```

Render mode

### ShowGrid

```text
System.Boolean ShowGrid { get; set; }
```

Grid on/off

### SnapBasePoint

```text
CSMath.XY SnapBasePoint { get; set; }
```

Snap base point(in DCS)

### SnapIsoPair

```text
System.Int16 SnapIsoPair { get; set; }
```

Snap style

### SnapOn

```text
System.Boolean SnapOn { get; set; }
```

Snap on/off

### SnapRotation

```text
System.Double SnapRotation { get; set; }
```

Snap rotation angle

### SnapSpacing

```text
CSMath.XY SnapSpacing { get; set; }
```

Snap spacing X and Y

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Target

```text
CSMath.XYZ Target { get; set; }
```

View target point(in WCS)

### TopRight

```text
CSMath.XY TopRight { get; set; }
```

Upper-right corner of viewport

### TwistAngle

```text
System.Double TwistAngle { get; set; }
```

View twist angle

### UcsIconDisplay

```text
ACadSharp.Tables.UscIconType UcsIconDisplay { get; set; }
```

UCSICON setting

### UseDefaultLighting

```text
System.Boolean UseDefaultLighting { get; set; }
```

Default Lighting On flag

### ViewHeight

```text
System.Double ViewHeight { get; set; }
```

View height

### ViewMode

```text
ACadSharp.Tables.ViewModeType ViewMode { get; set; }
```

View mode(see VIEWMODE system variable)

### VisualStyle

```text
ACadSharp.Objects.VisualStyle VisualStyle { get; set; }
```

Visual style object (optional)

**Remarks:** (optional)

### XAxis

```text
CSMath.XYZ XAxis { get; set; }
```

UCS X-axis

### YAxis

```text
CSMath.XYZ YAxis { get; set; }
```

UCS Y-axis
