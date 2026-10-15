# ACadSharp.Objects.MultiLeaderStyle

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.MultiLeaderStyle`

Represents a ACadSharp.Objects.MultiLeaderStyle object.

Object name F:ACadSharp.DxfFileToken.ObjectMLeaderStyle Dxf class name F:ACadSharp.DxfSubclassMarker.MLeaderStyle

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MultiLeaderStyle')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.MultiLeaderStyle()
```

Initializes a new instance of the ACadSharp.Objects.MultiLeaderStyle class.

### .ctor

```text
ACadSharp.Objects.MultiLeaderStyle(System.String name)
```

Initializes a new instance of the ACadSharp.Objects.MultiLeaderStyle class and sets the name of this style.

### DefaultName

```text
static System.String DefaultName = Standard
```

Default multiline style name.

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

### AlignSpace

```text
System.Double AlignSpace { get; set; }
```

Align Space

### Arrowhead

```text
ACadSharp.Tables.BlockRecord Arrowhead { get; set; }
```

Gets or sets a ACadSharp.Tables.BlockRecord representing the arrowhead to be displayed with every leader line.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.Arrowhead property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.Arrowhead flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.Arrowhead property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.Arrowhead flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

### ArrowheadSize

```text
System.Double ArrowheadSize { get; set; }
```

Gests or sets the arrowhead size.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.ArrowheadSize property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.ArrowheadSize flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.ArrowheadSize property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.ArrowheadSize flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

### BlockContent

```text
ACadSharp.Tables.BlockRecord BlockContent { get; set; }
```

Gets a ACadSharp.Tables.BlockRecord containing elements to be drawn as content for the multileader.

**Remarks:** Thw standard content block can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.BlockContent property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContent flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### BlockContentColor

```text
ACadSharp.Color BlockContentColor { get; set; }
```

Gets or sets the block-content color.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.BlockContentColor property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContentColor flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### BlockContentConnection

```text
ACadSharp.Entities.BlockContentConnectionType BlockContentConnection { get; set; }
```

Gets or sets a value indicating whether the multileader connects to the content-block extents or to the content-block base point.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.BlockContentConnection property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContentConnection flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### BlockContentRotation

```text
System.Double BlockContentRotation { get; set; }
```

Gets or sets the block content rotation.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.BlockContentRotation property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContentRotation flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### BlockContentScale

```text
CSMath.XYZ BlockContentScale { get; set; }
```

Gets or sets the scale factor for block content.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.BlockContentScale property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContentScale flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### BlockContentScaleX

```text
System.Double BlockContentScaleX { get; set; }
```

Gets or sets the scale factor along the X-axis for the block content.

### BlockContentScaleY

```text
System.Double BlockContentScaleY { get; set; }
```

Gets or sets the scale factor applied to the Y-axis of the block content.

### BlockContentScaleZ

```text
System.Double BlockContentScaleZ { get; set; }
```

Gets or sets the scale factor along the Z-axis for the block content.

### BreakGapSize

```text
System.Double BreakGapSize { get; set; }
```

Break Gap Size

### ContentType

```text
ACadSharp.Objects.LeaderContentType ContentType { get; set; }
```

Gets or sets a value indicating the content type for the multileader.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.ContentType property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.ContentType flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### Default

```text
static ACadSharp.Objects.MultiLeaderStyle Default { get; }
```

Gets the default MultiLeaderStyle

### DefaultTextContents

```text
System.String DefaultTextContents { get; set; }
```

Gests or sets a default text that is to be set when a mutileader is being created with this ACadSharp.Objects.MultiLeaderStyle.

### Description

```text
System.String Description { get; set; }
```

Gets or sets a text containing the description of this ACadSharp.Objects.MultiLeaderStyle.

### EnableBlockContentRotation

```text
System.Boolean EnableBlockContentRotation { get; set; }
```

Gets or sets a value indicating whether rotation of the block content is enabled.

### EnableBlockContentScale

```text
System.Boolean EnableBlockContentScale { get; set; }
```

Gets or sets a value indicating whether scaling of the block content is enabled.

### EnableDogleg

```text
System.Boolean EnableDogleg { get; set; }
```

Gets or sets a value indicating that leader lines are to be drawn with a dogleg.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.EnableDogleg property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.EnableDogleg flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.Note that this setting has no effect when the ACadSharp.Objects.MultiLeaderStyle.TextAttachmentDirection is F:ACadSharp.TextAttachmentDirectionType.Vertical.

### EnableLanding

```text
System.Boolean EnableLanding { get; set; }
```

Gets or sets a value indicating whether landing is enabled.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.EnableLanding property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.EnableLanding flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### FirstSegmentAngleConstraint

```text
System.Double FirstSegmentAngleConstraint { get; set; }
```

Gets or sets a snap angle value for the first leader segment when a leader line is being created for the mutileader.

**Remarks:** This property supports creating and editing a multileader but has no meaning for the display of multileaders.

**Value:** An angle value in radians or zero if no angle contstraint is set.

### IsAnnotative

```text
System.Boolean IsAnnotative { get; set; }
```

Is Annotative

### LandingDistance

```text
System.Double LandingDistance { get; set; }
```

Gets or sets the landing distance, i.e. the length of the dogleg.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.LandingDistance property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LandingDistance flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### LandingGap

```text
System.Double LandingGap { get; set; }
```

Gets or sets the landing gap. This is the distance between the leader end point or, if present, the end of the dogleg and the text label or the content block.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.LandingGap property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LandingGap flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### LeaderDrawOrder

```text
ACadSharp.Objects.LeaderDrawOrderType LeaderDrawOrder { get; set; }
```

DrawLeaderOrder Type

### LeaderLineType

```text
ACadSharp.Tables.LineType LeaderLineType { get; set; }
```

Gets or sets a ACadSharp.Tables.LineType object specifying line-type properties for the musltileader. This setting applies for all leader lines of the multileader.

**Remarks:** This setting can be overridden by the ACadSharp.Entities.MultiLeader.LeaderLineType property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LeaderLineType flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.The setting for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.LineType property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.LineType flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

### LeaderLineWeight

```text
ACadSharp.LineWeightType LeaderLineWeight { get; set; }
```

Gets or sets a value specifying the lineweight to be applied to all leader lines of the multileader.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.LeaderLineWeight property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LeaderLineWeight flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.LineWeight property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.LineWeight flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

### LineColor

```text
ACadSharp.Color LineColor { get; set; }
```

Gets or sets color to be applied all leader lines of the multileader.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.LineColor property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LineColor flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.LineColor property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.LineColor flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

### MaxLeaderSegmentsPoints

```text
System.Int32 MaxLeaderSegmentsPoints { get; set; }
```

Gets or sets the max number of segments when a new leader is being created for a multileader.

**Remarks:** This property supports creating and editing a multileader but has no meaning for the display of multileaders.

### MultiLeaderDrawOrder

```text
ACadSharp.Objects.MultiLeaderDrawOrderType MultiLeaderDrawOrder { get; set; }
```

DrawMLeaderOrder Type

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

### OverwritePropertyValue

```text
System.Boolean OverwritePropertyValue { get; set; }
```

Overwrite Property Value

**Remarks:** Property changed, meaning not totally clear might be set to true if something changed after loading, or might be used to trigger updates in dependent MLeaders. sequence seems to be different in DXF

### PathType

```text
ACadSharp.MultiLeaderPathType PathType { get; set; }
```

Gets or sets a value indicating whether leaders are to be displayed as polyline, a spline curve or invisible. This setting applies for all leader lines of the multileader.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.PathType property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.PathType flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.PathType property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.PathType flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

### ScaleFactor

```text
System.Double ScaleFactor { get; set; }
```

Gets or sets the scale factor for the ACadSharp.Objects.MultiLeaderStyle.ArrowheadSize, ACadSharp.Objects.MultiLeaderStyle.LandingDistance, ACadSharp.Objects.MultiLeaderStyle.LandingGap, ACadSharp.Objects.MultiLeaderStyle.TextHeight, and the elements of ACadSharp.Objects.MultiLeaderStyle.BlockContentScale.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.ScaleFactor property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.ScaleFactor flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### SecondSegmentAngleConstraint

```text
System.Double SecondSegmentAngleConstraint { get; set; }
```

Gets or sets a snap angle value for the second leader segment when a leader line is being created for the mutileader.

**Remarks:** This property supports creating and editing a multileader but has no meaning for the display of multileaders.

**Value:** An angle value in radians or zero if no angle contstraint is set.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### TextAlignAlwaysLeft

```text
System.Boolean TextAlignAlwaysLeft { get; set; }
```

Text Align Always Left

### TextAlignment

```text
ACadSharp.TextAlignmentType TextAlignment { get; set; }
```

Gets or sets the text alignment, i.e. the alignment of text lines if the a multiline text label, relative to the ACadSharp.Objects.MultiLeaderObjectContextData.TextLocation.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.TextAlignment property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextAlignment flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### TextAngle

```text
ACadSharp.TextAngleType TextAngle { get; set; }
```

Gets or sets a value indicating the text angle.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.TextAngle property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextAngle flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### TextAttachmentDirection

```text
ACadSharp.TextAttachmentDirectionType TextAttachmentDirection { get; set; }
```

Gets or sets the Text attachment direction for text or block contents, rename? This property defines whether the leaders attach to the left/right of the content block/text, or attach to the top/bottom.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.TextAttachmentDirection property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextAttachmentDirection flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderRoot.TextAttachmentDirection property when the !:LeaderLinePropertOverrideFlags.TextAttachmentDirection flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

**Value:** A ACadSharp.TextAttachmentDirectionType.

### TextBottomAttachment

```text
ACadSharp.TextAttachmentType TextBottomAttachment { get; set; }
```

Gets or sets the text bottom attachment type. This value controls the position of the connection point of the leader attached to the bottom of the text label.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.TextBottomAttachment property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextBottomAttachment flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.This property is only relevant if ACadSharp.Objects.MultiLeaderStyle.TextAttachmentDirection is F:ACadSharp.TextAttachmentDirectionType.Vertical and a leader attached to the bottom of the text label exists.

**Value:** A ACadSharp.TextAttachmentType having the values 9 = Center, 10 = Underline and Center can be used ("vertical" attachment types).

### TextColor

```text
ACadSharp.Color TextColor { get; set; }
```

Gest or sets the color for the text label of the multileader.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.TextColor property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextColor flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### TextFrame

```text
System.Boolean TextFrame { get; set; }
```

Gets or sets a value indicating that the text label is to be drawn with a frame.

**Remarks:** This value can be overridden by the ACadSharp.Entities.MultiLeader.TextFrame property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextFrame flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### TextHeight

```text
System.Double TextHeight { get; set; }
```

Gets or sets the text height for the text label of the multileader.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.TextHeight property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextHeight flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### TextLeftAttachment

```text
ACadSharp.TextAttachmentType TextLeftAttachment { get; set; }
```

Gets or sets the Text Left Attachment Type. This value controls the position of the connection point of the leader attached to the left side of the text label.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.TextLeftAttachment property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextLeftAttachment flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.This property is only relevant if ACadSharp.Objects.MultiLeaderStyle.TextAttachmentDirection is F:ACadSharp.TextAttachmentDirectionType.Horizontal and a leader attached to the left side of the text label exists.

**Value:** A ACadSharp.TextAttachmentType having the values 0-8 can be used ("horizontal" attachment types).

### TextRightAttachment

```text
ACadSharp.TextAttachmentType TextRightAttachment { get; set; }
```

Gets or sets the Text Right Attachment Type. This value controls the position of the connection point of the leader attached to the right side of the text label.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.TextRightAttachment property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextRightAttachment flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.This property is only relevant if ACadSharp.Objects.MultiLeaderStyle.TextAttachmentDirection is F:ACadSharp.TextAttachmentDirectionType.Horizontal and a leader attached to the right side of the text label exists.

**Value:** A ACadSharp.TextAttachmentType having the values 0-8 can be used ("horizontal" attachment types).

### TextStyle

```text
ACadSharp.Tables.TextStyle TextStyle { get; set; }
```

Gets or sets the ACadSharp.Objects.MultiLeaderStyle.TextStyle to be used to display the text label of the multileader.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.TextStyle property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextStyle flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### TextTopAttachment

```text
ACadSharp.TextAttachmentType TextTopAttachment { get; set; }
```

Gets or sets the text top attachment type. This value controls the position of the connection point of the leader attached to the top of the text label.

**Remarks:** This value can be overridden by the ACadSharp.Objects.MultiLeaderObjectContextData.TextTopAttachment property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextTopAttachment flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.This property is only relevant if ACadSharp.Objects.MultiLeaderStyle.TextAttachmentDirection is F:ACadSharp.TextAttachmentDirectionType.Vertical and a leader attached to the top of the text label exists.

**Value:** A ACadSharp.TextAttachmentType having the values 9 = Center, 10 = Underline and Center can be used ("vertical" attachment types).

### UnknownFlag298

```text
System.Boolean UnknownFlag298 { get; set; }
```

Undocumented in ODS and DXF-ref boolean, found in DXF.
