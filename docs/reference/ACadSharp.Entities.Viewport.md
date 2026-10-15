# ACadSharp.Entities.Viewport

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Viewport`

Represents a ACadSharp.Entities.Viewport entity.

Object name F:ACadSharp.DxfFileToken.EntityViewport Dxf class name F:ACadSharp.DxfSubclassMarker.Viewport

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Viewport')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Viewport()
```

### ASDK_XREC_ANNOTATION_SCALE_INFO

```text
static System.String ASDK_XREC_ANNOTATION_SCALE_INFO = ASDK_XREC_ANNOTATION_SCALE_INFO
```

### PaperViewId

```text
static System.Int32 PaperViewId = 1
```

Paper view Id, it indicates that the viewport acts as a paper size.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### GetModelBoundingBox

```text
CSMath.BoundingBox GetModelBoundingBox()
```

Gets the bounding box of this viewport in the model space.

### SelectEntities

```text
System.Collections.Generic.List[ACadSharp.Entities.Entity] SelectEntities(System.Boolean includePartial = True)
```

Gets all the entities from the model that are in the view of the viewport.

### ActiveStatus

```text
System.Int16 ActiveStatus { get; set; }
```

Gets or sets the active status code.

**Remarks:** -1 = On, but is fully off screen, or is one of the viewports that is not active because the $MAXACTVP count is currently being exceeded. 0 = Off 'positive value' = On and active.The value indicates the order of stacking for the viewports, where 1 is the active viewport, 2 is the next, and so forth

### AmbientLightColor

```text
ACadSharp.Color AmbientLightColor { get; set; }
```

Ambient light color.Write only if not black color.

### BackClipPlane

```text
System.Double BackClipPlane { get; set; }
```

Back clip plane Z value.

### Boundary

```text
ACadSharp.Entities.Entity Boundary { get; set; }
```

Hard-pointer ID/handle to entity that serves as the viewport's clipping boundary (only present if viewport is non-rectangular)

### Brightness

```text
System.Double Brightness { get; set; }
```

View brightness

### Center

```text
CSMath.XYZ Center { get; set; }
```

Center point(in WCS).

### CircleZoomPercent

```text
System.Int16 CircleZoomPercent { get; set; }
```

Circle zoom percent

### Contrast

```text
System.Double Contrast { get; set; }
```

View contrast

### DefaultLightingType

```text
ACadSharp.Entities.LightingType DefaultLightingType { get; set; }
```

Default lighting type.

**Remarks:** 0 = One distant light 1 = Two distant lights

### DisplayUcsIcon

```text
System.Boolean DisplayUcsIcon { get; set; }
```

Display UCS icon at UCS origin flag

**Remarks:** Controls whether UCS icon represents viewport UCS or current UCS(these will be different if UCSVP is 1 and viewport is not active). However, this field is currently being ignored and the icon always represents the viewport UCS

### Elevation

```text
System.Double Elevation { get; set; }
```

Viewport elevation

### FrontClipPlane

```text
System.Double FrontClipPlane { get; set; }
```

Front clip plane Z value.

### FrozenLayers

```text
System.Collections.Generic.List[ACadSharp.Tables.Layer] FrozenLayers { get; }
```

Frozen layer object ID/handle(multiple entries may exist)

### GridSpacing

```text
CSMath.XY GridSpacing { get; set; }
```

Grid spacing

### Height

```text
System.Double Height { get; set; }
```

Height in paper space units.

### Id

```text
System.Int16 Id { get; }
```

Viewport ID.

**Remarks:** The first value for a PaperSpace will represent the paper image in the screen.

### LensLength

```text
System.Double LensLength { get; set; }
```

Perspective lens length

### MajorGridLineFrequency

```text
System.Int16 MajorGridLineFrequency { get; set; }
```

Frequency of major grid lines compared to minor grid lines

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

### RenderMode

```text
ACadSharp.RenderMode RenderMode { get; set; }
```

Render mode

### RepresentsPaper

```text
System.Boolean RepresentsPaper { get; }
```

Flag that set for those viewports that represent the paper in the view.

**Remarks:** A paper viewport is only for boundaries only, does not visualize anything.

### Scale

```text
ACadSharp.Objects.Scale Scale { get; set; }
```

Scale assigned for this viewport.

### ScaleFactor

```text
System.Double ScaleFactor { get; }
```

Scale factor applied in this viewport.

**Remarks:** Represents the scale applied to all the entities in the model when are visualized in the paper.

### ShadePlotMode

```text
ACadSharp.Objects.ShadePlotMode ShadePlotMode { get; set; }
```

Orthographic type of UCS

### SnapAngle

```text
System.Double SnapAngle { get; set; }
```

Snap angle

### SnapBase

```text
CSMath.XY SnapBase { get; set; }
```

Snap base point

### SnapSpacing

```text
CSMath.XY SnapSpacing { get; set; }
```

Snap spacing

### Status

```text
ACadSharp.Entities.ViewportStatusFlags Status { get; set; }
```

Viewport status.

### StyleSheetName

```text
System.String StyleSheetName { get; set; }
```

Plot style sheet name assigned to this viewport

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### TwistAngle

```text
System.Double TwistAngle { get; set; }
```

View twist angle

### UcsOrigin

```text
CSMath.XYZ UcsOrigin { get; set; }
```

UCS origin

### UcsOrthographicType

```text
ACadSharp.OrthographicType UcsOrthographicType { get; set; }
```

Orthographic type of UCS

### UcsPerViewport

```text
System.Boolean UcsPerViewport { get; set; }
```

UCS per viewport flag

**Remarks:** 0 = The UCS will not change when this viewport becomes active. 1 = This viewport stores its own UCS which will become the current UCS whenever the viewport is activated

### UcsXAxis

```text
CSMath.XYZ UcsXAxis { get; set; }
```

UCS X-axis

### UcsYAxis

```text
CSMath.XYZ UcsYAxis { get; set; }
```

UCS Y-axis

### UseDefaultLighting

```text
System.Boolean UseDefaultLighting { get; set; }
```

Default lighting flag.On when no user lights are specified.

### ViewCenter

```text
CSMath.XY ViewCenter { get; set; }
```

View center point(in DCS).

### ViewDirection

```text
CSMath.XYZ ViewDirection { get; set; }
```

View direction vector(in WCS)

### ViewHeight

```text
System.Double ViewHeight { get; set; }
```

View height(in model space units).

### ViewTarget

```text
CSMath.XYZ ViewTarget { get; set; }
```

View target point(in WCS)

### ViewWidth

```text
System.Double ViewWidth { get; }
```

View width (in model space units).

### VisualStyle

```text
ACadSharp.Objects.VisualStyle VisualStyle { get; set; }
```

Visual style

### Width

```text
System.Double Width { get; set; }
```

Width in paper space units.
