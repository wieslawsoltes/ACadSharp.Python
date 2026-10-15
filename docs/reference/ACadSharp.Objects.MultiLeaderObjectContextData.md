# ACadSharp.Objects.MultiLeaderObjectContextData

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.MultiLeaderObjectContextData`

This class represents a subset ob the properties of the MLeaderAnnotContext object, that are embedded into the MultiLeader entity.

Base type: `ACadSharp.Objects.AnnotScaleObjectContextData`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MultiLeaderObjectContextData')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.MultiLeaderObjectContextData()
```

Initializes a new instance of a ACadSharp.Objects.MultiLeaderObjectContextData.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### ArrowheadSize

```text
System.Double ArrowheadSize { get; set; }
```

Gets or sets the arrowhead size (see ACadSharp.Objects.MultiLeaderStyle.Arrowhead) for every leader line. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.ArrowheadSize flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.ArrowheadSize property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.ArrowheadSize flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.ArrowheadSize). Values should be equal, the value of this property is assumed to be used.

**Value:** The value returned is the value entered in AutoCAD multiplied with the ACadSharp.Objects.MultiLeaderObjectContextData.ScaleFactor.

### BackgroundFillColor

```text
ACadSharp.Color BackgroundFillColor { get; set; }
```

Background fill color

### BackgroundFillEnabled

```text
System.Boolean BackgroundFillEnabled { get; set; }
```

Is background fill enabled

### BackgroundMaskFillOn

```text
System.Boolean BackgroundMaskFillOn { get; set; }
```

Is background mask fill on

### BackgroundScaleFactor

```text
System.Double BackgroundScaleFactor { get; set; }
```

Background scale factor

### BackgroundTransparency

```text
System.Int32 BackgroundTransparency { get; set; }
```

Background transparency

### BaseDirection

```text
CSMath.XYZ BaseDirection { get; set; }
```

Base direction

### BasePoint

```text
CSMath.XYZ BasePoint { get; set; }
```

Base point

### BaseVertical

```text
CSMath.XYZ BaseVertical { get; set; }
```

Base vertical

### BlockContent

```text
ACadSharp.Tables.BlockRecord BlockContent { get; set; }
```

Gets a ACadSharp.Tables.BlockRecord containing elements to be drawn as content for the multileader.

### BlockContentColor

```text
ACadSharp.Color BlockContentColor { get; set; }
```

Gets or sets the block-content color. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContentColor flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.BlockContentColor). Values should be equal, the value of this property is assumed to be used.

### BlockContentConnection

```text
ACadSharp.Entities.BlockContentConnectionType BlockContentConnection { get; set; }
```

Gets or sets a value indicating whether the multileader connects to the content-block extents or to the content-block base point. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContentConnection flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.BlockContentConnection). Values should be equal, the value of this property is assumed to be used.

### BlockContentLocation

```text
CSMath.XYZ BlockContentLocation { get; set; }
```

Gets or sets the location of the block content of the multileader.

**Remarks:** This location is evaluated by AutoCAD from the ACadSharp.Objects.MultiLeaderObjectContextData.BlockContentConnection.

### BlockContentNormal

```text
CSMath.XYZ BlockContentNormal { get; set; }
```

Gets or sets the normal vector for the block content of the multileader.

### BlockContentRotation

```text
System.Double BlockContentRotation { get; set; }
```

Gets or sets the rotation of the block content of the multileader.

**Remarks:** This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.BlockContentRotation). Values should be equal, the value of this property is assumed to be used.

**Value:** The rotation angle in radians.

### BlockContentScale

```text
CSMath.XYZ BlockContentScale { get; set; }
```

Gets or sets the scale factor for block content. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContentScale flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.BlockContentScale). Values should be equal, the value of this property is assumed to be used.

### BoundaryHeight

```text
System.Double BoundaryHeight { get; set; }
```

Boundary height (DXF Reference: TextHeight) Value seems to be always zero.

### BoundaryWidth

```text
System.Double BoundaryWidth { get; set; }
```

Boundary width (DXF Reference: TextWidth) Value seems to be always zero.

### ColumnFlowReversed

```text
System.Boolean ColumnFlowReversed { get; set; }
```

Column flow reversed

### ColumnGutter

```text
System.Double ColumnGutter { get; set; }
```

Column gutter

### ColumnSizes

```text
System.Collections.Generic.IList[System.Double] ColumnSizes { get; }
```

Get a list of column sizes

### ColumnType

```text
System.Int16 ColumnType { get; set; }
```

Column type (ODA writes 0)

### ColumnWidth

```text
System.Double ColumnWidth { get; set; }
```

Column width

### ContentBasePoint

```text
CSMath.XYZ ContentBasePoint { get; set; }
```

Gets or sets the content base point. This point is identical with the landing end point of the first leader.

**Remarks:** This point

### Direction

```text
CSMath.XYZ Direction { get; set; }
```

Direction

### FlowDirection

```text
ACadSharp.FlowDirectionType FlowDirection { get; set; }
```

Gets or sets a value indicating the flow direction.

### HasContentsBlock

```text
System.Boolean HasContentsBlock { get; set; }
```

Gets or sets a value indicating that the multileader has a content block.

### HasTextContents

```text
System.Boolean HasTextContents { get; set; }
```

Gets or sets a value indicating that the mutileader has a text label.

### LandingGap

```text
System.Double LandingGap { get; set; }
```

Gets or sets the landing gap (see ACadSharp.Objects.MultiLeaderStyle.LandingGap). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LandingGap flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

### LeaderRoots

```text
System.Collections.Generic.IList[ACadSharp.Objects.MultiLeaderObjectContextData.LeaderRoot] LeaderRoots { get; }
```

Gets the list of ACadSharp.Objects.MultiLeaderObjectContextData.LeaderRoot objects of the multileader.

**Remarks:** A ACadSharp.Entities.MultiLeader can have one or two leader roots having one ore more leader lines each.

### LineSpacing

```text
ACadSharp.LineSpacingStyle LineSpacing { get; set; }
```

Gets or sets the line spacing style for the display of the text label.

### LineSpacingFactor

```text
System.Double LineSpacingFactor { get; set; }
```

Gets or sets the line-spacing factor for the display of the text label.

### NormalReversed

```text
System.Boolean NormalReversed { get; set; }
```

Is normal reversed?

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

### ScaleFactor

```text
System.Double ScaleFactor { get; set; }
```

Gets or sets a scale factor (see ACadSharp.Objects.MultiLeaderStyle.ScaleFactor). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.ScaleFactor flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property). The scale factor is applied by AutoCAD.

**Remarks:** The following properties entered in AutoCAD are multiplied with this scale factor: ACadSharp.Objects.MultiLeaderObjectContextData.ArrowheadSize, ACadSharp.Entities.MultiLeader.LandingDistance, ACadSharp.Objects.MultiLeaderObjectContextData.LandingGap, ACadSharp.Objects.MultiLeaderObjectContextData.TextHeight, and the elements of ACadSharp.Objects.MultiLeaderObjectContextData.BlockContentScale. The ACadSharp.Objects.MultiLeaderObjectContextData.ContentBasePoint is adjusted.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### TextAlignment

```text
ACadSharp.TextAlignmentType TextAlignment { get; set; }
```

Gets or sets the text alignment, i.e. the alignment of text lines if the a multiline text label, relative to the ACadSharp.Objects.MultiLeaderObjectContextData.TextLocation. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextAlignment flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** This property contains the alignment value specified in AutoCAD rather than ACadSharp.Entities.MultiLeader.TextAlignment and seems always to be consistent with ACadSharp.Objects.MultiLeaderObjectContextData.TextAttachmentPoint.Note that when changing this value the ACadSharp.Objects.MultiLeaderObjectContextData.TextLocation must be changed accordingly.

### TextAttachmentPoint

```text
ACadSharp.TextAttachmentPointType TextAttachmentPoint { get; set; }
```

Gets or sets a value indicating the text attachment point.

**Remarks:** In the Open Design Specification this property is documented as Alignment, in DXF reference as Text Attachment. It is not clear what the meaning of this property is in contrast to the ACadSharp.Objects.MultiLeaderObjectContextData.TextAlignment property. The value seems to be always consistent.This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.TextAttachmentPoint). Values should be equal, the value of this property is assumed to be used.

### TextBottomAttachment

```text
ACadSharp.TextAttachmentType TextBottomAttachment { get; set; }
```

Gets or sets the text bottom attachment type (see ACadSharp.Objects.MultiLeaderStyle.TextBottomAttachment). This property override the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextBottomAttachment flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.TextBottomAttachment). Values should be equal, the value of this property is assumed to be used.

**Value:** A ACadSharp.TextAttachmentType having the values 9 = Center, 10 = Underline and Center can be used ("vertical" attachment types).

### TextColor

```text
ACadSharp.Color TextColor { get; set; }
```

Gets or sets the color for the display of the text label

### TextHeight

```text
System.Double TextHeight { get; set; }
```

Get or sets the text height for the lext label of the multileader (see ACadSharp.Objects.MultiLeaderStyle.TextHeight). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextHeight flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Value:** The value returned is the value entered in AutoCAD multiplied with the ACadSharp.Objects.MultiLeaderObjectContextData.ScaleFactor.

### TextHeightAutomatic

```text
System.Boolean TextHeightAutomatic { get; set; }
```

Is text height automatic?

### TextLabel

```text
System.String TextLabel { get; set; }
```

Gets or sets a string containg the text tat is to be dispayed a s text label of the multileader.

**Remarks:** The string may contain MTEXT markups to specify new-lines, font, size, style, etc.

### TextLeftAttachment

```text
ACadSharp.TextAttachmentType TextLeftAttachment { get; set; }
```

Gets or sets the text top attachment type (see ACadSharp.Objects.MultiLeaderStyle.TextLeftAttachment). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextLeftAttachment flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.TextLeftAttachment). Values should be equal, the value of this property is assumed to be used.

**Value:** A ACadSharp.TextAttachmentType having the values 0-8 can be used ("horizontal" attachment types).

### TextLocation

```text
CSMath.XYZ TextLocation { get; set; }
```

Gets or sets the location of the text label of the multileader.

### TextNormal

```text
CSMath.XYZ TextNormal { get; set; }
```

Gets or sets the normal vector for the text label of the multileader.

### TextRightAttachment

```text
ACadSharp.TextAttachmentType TextRightAttachment { get; set; }
```

Gets or sets the text top attachment type (see ACadSharp.Objects.MultiLeaderStyle.TextRightAttachment). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextRightAttachment flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.TextRightAttachment). Values should be equal, the value of this property is assumed to be used.

**Value:** A ACadSharp.TextAttachmentType having the values 0-8 can be used ("horizontal" attachment types).

### TextRotation

```text
System.Double TextRotation { get; set; }
```

Gets or sets the rotation of the text label of the multileader.

**Value:** The rotation angle in radians.

### TextStyle

```text
ACadSharp.Tables.TextStyle TextStyle { get; set; }
```

Gets or sets the ACadSharp.Objects.MultiLeaderObjectContextData.TextStyle to be used to display the text label of the multileader. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextStyle flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.TextStyle). Values should be equal, the value of this property is assumed to be used.

### TextTopAttachment

```text
ACadSharp.TextAttachmentType TextTopAttachment { get; set; }
```

Gets or sets the text top attachment type (see ACadSharp.Objects.MultiLeaderStyle.TextTopAttachment). This property override the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextTopAttachment flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.TextTopAttachment). Values should be equal, the value of this property is assumed to be used.

**Value:** A ACadSharp.TextAttachmentType having the values 9 = Center, 10 = Underline and Center can be used ("vertical" attachment types).

### TransformationMatrix

```text
CSMath.Matrix4 TransformationMatrix { get; set; }
```

Gets a array of 16 doubles containing the complete transformation matrix.

**Remarks:** Order of transformation is: Rotation, OCS to WCS (using normal vector), Scaling (using scale vector), Translation (using location)

### WordBreak

```text
System.Boolean WordBreak { get; set; }
```

Word break
