# ACadSharp.Entities.MultiLeader

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.MultiLeader`

Represents a ACadSharp.Entities.MultiLeader entity.

Object name F:ACadSharp.DxfFileToken.EntityMultiLeader Dxf class name F:ACadSharp.DxfSubclassMarker.MultiLeader

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.MultiLeader')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.MultiLeader()
```

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

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### Arrowhead

```text
ACadSharp.Tables.BlockRecord Arrowhead { get; set; }
```

Gets or sets a ACadSharp.Tables.BlockRecord representing the arrowhead (see ACadSharp.Objects.MultiLeaderStyle.Arrowhead) to be displayed with every leader line. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.Arrowhead flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.Arrowhead property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.Arrowhead flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

### ArrowheadSize

```text
System.Double ArrowheadSize { get; set; }
```

Gets or sets the arrowhead size (see ACadSharp.Objects.MultiLeaderStyle.Arrowhead) for every leader line when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.ArrowheadSize flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.ArrowheadSize property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.ArrowheadSize flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.ArrowheadSize is assumed to be used.

### BlockAttributes

```text
System.Collections.Generic.IList[ACadSharp.Entities.MultiLeader.BlockAttribute] BlockAttributes { get; }
```

### BlockContent

```text
ACadSharp.Tables.BlockRecord BlockContent { get; set; }
```

Gets a ACadSharp.Tables.BlockRecord containing elements to be drawn as content for the multileader. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContent flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.BlockContent is assumed to be used.

### BlockContentColor

```text
ACadSharp.Color BlockContentColor { get; set; }
```

Gets or sets the block-content color. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContentColor flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.BlockContentColor is assumed to be used.

### BlockContentConnection

```text
ACadSharp.Entities.BlockContentConnectionType BlockContentConnection { get; set; }
```

Gets or sets a value indicating whether the multileader connects to the content-block extents or to the content-block base point when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContentConnection flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.BlockContentConnection is assumed to be used.

### BlockContentRotation

```text
System.Double BlockContentRotation { get; set; }
```

Gets or sets the rotation of the block content of the multileader.

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.BlockContentRotation is assumed to be used.

### BlockContentScale

```text
CSMath.XYZ BlockContentScale { get; set; }
```

Gets or sets the scale factor for block content. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.BlockContentScale flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.BlockContentScale is assumed to be used.

### ContentType

```text
ACadSharp.Objects.LeaderContentType ContentType { get; set; }
```

Gets or sets a value indicating whether the content of this ACadSharp.Entities.MultiLeader is a text label, a content block, or a tolerance.

### ContextData

```text
ACadSharp.Objects.MultiLeaderObjectContextData ContextData { get; }
```

Gets the embedded ACadSharp.Objects.MultiLeaderObjectContextData object contains the multileader content (block/text) and the leaders.

**Remarks:** The embedded ACadSharp.Objects.MultiLeaderObjectContextData object is used if the ACadSharp.Entities.MultiLeader.EnableAnnotationScale property is false. If ACadSharp.Entities.MultiLeader.EnableAnnotationScale is true an alternate ACadSharp.Objects.MultiLeaderObjectContextData object with the respective scaling value that is linked via the ACadSharp.CadObject.XDictionary property.Note: The properties of the various ACadSharp.Objects.MultiLeaderObjectContextData objects are currently not synchronized.

### EnableAnnotationScale

```text
System.Boolean EnableAnnotationScale { get; set; }
```

Enable Annotation Scale

### EnableDogleg

```text
System.Boolean EnableDogleg { get; set; }
```

Gets or sets a value indicating that leader lines of this ACadSharp.Entities.MultiLeader are to be drawn with a dogleg (see ACadSharp.Objects.MultiLeaderStyle.EnableDogleg). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.EnableDogleg flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### EnableLanding

```text
System.Boolean EnableLanding { get; set; }
```

Gets or sets a value indicating whether landing is enabled. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.EnableLanding flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### ExtendedToText

```text
System.Boolean ExtendedToText { get; set; }
```

Leader extended to text

### LandingDistance

```text
System.Double LandingDistance { get; set; }
```

Gets or sets the landing distance, i.e. the length of the dogleg, for this ACadSharp.Entities.MultiLeader. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LandingDistance flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** There is only one field for the landing distance in the multileader property grid. The value entered arrives in this property and the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderRoot.LandingDistance property. If two leader roots exist both receive the same value. I seems F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LandingDistance flag is never set.

### LeaderLineType

```text
ACadSharp.Tables.LineType LeaderLineType { get; set; }
```

Gets or sets ACadSharp.Tables.LineType of the leader lines of this ACadSharp.Entities.MultiLeader (see ACadSharp.Objects.MultiLeaderStyle.LeaderLineType). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LeaderLineType flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** The setting for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.LineType property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.LineType flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

### LeaderLineWeight

```text
ACadSharp.LineWeightType LeaderLineWeight { get; set; }
```

Gets or sets a value specifying the line weight to be applied to all leader lines of this ACadSharp.Entities.MultiLeader (see ACadSharp.Objects.MultiLeaderStyle.LeaderLineWeight). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LeaderLineWeight flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.LineWeight property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.LineWeight flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

### LineColor

```text
ACadSharp.Color LineColor { get; set; }
```

Gets or sets color of the leader lines of this ACadSharp.Entities.MultiLeader (see ACadSharp.Objects.MultiLeaderStyle.LineColor). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.LineColor flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.LineColor property when the F:ACadSharp.Objects.LeaderLinePropertOverrideFlags.LineColor flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

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

### PathType

```text
ACadSharp.MultiLeaderPathType PathType { get; set; }
```

Gets or sets a value indicating the path type of this ACadSharp.Entities.MultiLeader (see ACadSharp.Objects.MultiLeaderStyle.PathType). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.PathType flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

### PropertyOverrideFlags

```text
ACadSharp.Entities.MultiLeaderPropertyOverrideFlags PropertyOverrideFlags { get; set; }
```

Gets or sets a value containing a list of flags indicating which multileader properties specified by the associated ACadSharp.Objects.MultiLeaderStyle are to be overridden by properties specified by this ACadSharp.Entities.MultiLeader or the attached ACadSharp.Objects.MultiLeaderObjectContextData.

### ScaleFactor

```text
System.Double ScaleFactor { get; set; }
```

Gets or sets a scale factor (see ACadSharp.Objects.MultiLeaderStyle.ScaleFactor). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.ScaleFactor flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property). The scale factor is applied by AutoCAD.

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.ScaleFactor is assumed to be relevant.

### Style

```text
ACadSharp.Objects.MultiLeaderStyle Style { get; set; }
```

Gets a ACadSharp.Objects.MultiLeaderStyle providing reusable style information for this ACadSharp.Entities.MultiLeader.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### TextAligninIPE

```text
System.Int16 TextAligninIPE { get; set; }
```

Text Align in IPE (meaning unknown)

### TextAlignment

```text
ACadSharp.TextAlignmentType TextAlignment { get; set; }
```

Gets or sets the text alignement type.

**Remarks:** The Open Design Specification for DWG documents this property as Unknown, DXF reference as Text Aligment Type. Available DWG and DXF sample documents saved by AutoCAD return always 0=Left.This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.TextAlignment is assumed to be used.

### TextAngle

```text
ACadSharp.TextAngleType TextAngle { get; set; }
```

Gets or sets a value indicating the text angle. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextAngle flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

### TextAttachmentDirection

```text
ACadSharp.TextAttachmentDirectionType TextAttachmentDirection { get; set; }
```

Gets or sets the Text attachment direction for text or block contents. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextAttachmentDirection flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** This property defines whether the leaders attach to the left/right of the content block/text, or attach to the top/bottom.The value for all leader lines can be overridden for each individual leader line by the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderRoot.TextAttachmentDirection property when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextAttachmentDirection flag is set in the ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.OverrideFlags property.

**Value:** A ACadSharp.TextAttachmentDirectionType.

### TextAttachmentPoint

```text
ACadSharp.TextAttachmentPointType TextAttachmentPoint { get; set; }
```

Gets or sets a value indicating the text attachment point.

**Remarks:** The Open Design Specification for DWG files documents this property as Justification, the DXF reference as Text Attachments point.This property is also exposed by the ACadSharp.Entities.MultiLeader class (ACadSharp.Entities.MultiLeader.TextAttachmentPoint). The ACadSharp.Objects.MultiLeaderObjectContextData.TextAttachmentPoint property always has the same value and seems to have the respective value as ACadSharp.Objects.MultiLeaderObjectContextData.TextAlignment. The ACadSharp.Objects.MultiLeaderObjectContextData.TextAttachmentPoint property is to be used.

### TextBottomAttachment

```text
ACadSharp.TextAttachmentType TextBottomAttachment { get; set; }
```

Gets or sets the text bottom attachment type (see ACadSharp.Objects.MultiLeaderStyle.TextBottomAttachment). This property override the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextBottomAttachment flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.TextBottomAttachment is assumed to be used.

**Value:** A ACadSharp.TextAttachmentType having the values 9 = Center, 10 = Underline and Center can be used ("vertical" attachment types).

### TextColor

```text
ACadSharp.Color TextColor { get; set; }
```

Gets or sets the color for the display of the text label. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextColor flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.TextColor is assumed to be used.

### TextDirectionNegative

```text
System.Boolean TextDirectionNegative { get; set; }
```

Text Direction Negative

### TextFrame

```text
System.Boolean TextFrame { get; set; }
```

Gets or sets a value indicating that the text label is to be drawn with a frame. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextFrame flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

### TextLeftAttachment

```text
ACadSharp.TextAttachmentType TextLeftAttachment { get; set; }
```

Gets or sets the text left attachment type (see ACadSharp.Objects.MultiLeaderStyle.TextLeftAttachment). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextLeftAttachment flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.TextLeftAttachment is assumed to be used.

**Value:** A ACadSharp.TextAttachmentType having the values 0-8 can be used ("horizontal" attachment types).

### TextRightAttachment

```text
ACadSharp.TextAttachmentType TextRightAttachment { get; set; }
```

Gets or sets the text right attachment type (see ACadSharp.Objects.MultiLeaderStyle.TextRightAttachment). This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextRightAttachment flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.TextRightAttachment is assumed to be used.

**Value:** A ACadSharp.TextAttachmentType having the values 0-8 can be used ("horizontal" attachment types).

### TextStyle

```text
ACadSharp.Tables.TextStyle TextStyle { get; set; }
```

Gets or sets the ACadSharp.Entities.MultiLeader.TextStyle to be used to display the text label of this ACadSharp.Entities.MultiLeader. This property overrides the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextStyle flag is set in the ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property.

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class (ACadSharp.Objects.MultiLeaderObjectContextData.TextStyle). Values should be equal, the ACadSharp.Objects.MultiLeaderObjectContextData.TextStyle is assumed to be used.

### TextTopAttachment

```text
ACadSharp.TextAttachmentType TextTopAttachment { get; set; }
```

Gets or sets the text top attachment type (see ACadSharp.Objects.MultiLeaderStyle.TextTopAttachment). This property override the value from ACadSharp.Objects.MultiLeaderStyle when the F:ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.TextTopAttachment flag is set (see ACadSharp.Entities.MultiLeader.PropertyOverrideFlags property).

**Remarks:** This property is also exposed by the ACadSharp.Objects.MultiLeaderObjectContextData class. Values should be equal, the value ACadSharp.Objects.MultiLeaderObjectContextData.TextTopAttachment is assumed to be used.

**Value:** A ACadSharp.TextAttachmentType having the values 9 = Center, 10 = Underline and Center can be used ("vertical" attachment types).
