# ACadSharp.Entities.Dimension

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Dimension`

Represents a ACadSharp.Entities.Dimension entity.

Object name F:ACadSharp.DxfFileToken.EntityDimension Dxf class name F:ACadSharp.DxfSubclassMarker.Dimension

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Dimension')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

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

### GetActiveDimensionStyle

```text
ACadSharp.Tables.DimensionStyle GetActiveDimensionStyle()
```

Retrieves the currently active dimension style, including any style overrides that are applied.

**Remarks:** Use this method to obtain the effective dimension style for rendering or measurement purposes. The returned style reflects all current overrides and can differ from the base style if overrides are set.

**Returns:** A ACadSharp.Tables.DimensionStyle instance representing the active dimension style. If no overrides are present, returns the base style; otherwise, returns a copy of the style with overrides applied.

### GetMeasurementText

```text
System.String GetMeasurementText()
```

Get the measurement text from the actual ACadSharp.Entities.Dimension.Measurement value.

### GetMeasurementText

```text
System.String GetMeasurementText(ACadSharp.Tables.DimensionStyle style)
```

Get the measurement text from the actual ACadSharp.Entities.Dimension.Measurement value.

- `style`: style to apply to the text.

### GetStyleOverrideMap

```text
ACadSharp.DxfClassMap GetStyleOverrideMap()
```

Retrieves a map of style override properties from the extended data, if present and valid.

**Remarks:** This method inspects the extended data for a section identified as a style override ("DSTYLE"). If the section is not present or is malformed, the method returns null. The returned map can be used to access or apply dimension style overrides defined in the extended data.

**Returns:** A ACadSharp.DxfClassMap containing the style override properties if the extended data includes a valid style override section; otherwise, null.

### SetDimensionOverride

```text
System.Void SetDimensionOverride(ACadSharp.Tables.DimensionStyle styleOverride)
```

Applies the specified dimension style override to the current object, updating its extended data to reflect the overridden properties.

**Remarks:** This method updates the object's extended data to record the overridden dimension style properties. Properties that are identical between the current style and the override are not affected. Use this method to persist style overrides for dimension objects in environments that support extended data.

- `styleOverride`: The dimension style containing property values to override the current object's style. Only properties with values different from the current style are applied.

### SetStyleOverrideMap

```text
System.Void SetStyleOverrideMap(ACadSharp.DxfClassMap map)
```

Sets the style override mapping for the current object using the specified DXF class map.

**Remarks:** This method updates the object's extended data to reflect the provided style overrides. Existing style override entries are cleared before applying the new map. Use this method to programmatically control dimension style overrides in the object's extended data.

- `map`: A DXF class map containing the property overrides to apply. Each property in the map defines a style override entry.

### UpdateBlock

```text
System.Void UpdateBlock()
```

Updates the block that represents this dimension.

### AttachmentPoint

```text
ACadSharp.Entities.AttachmentPointType AttachmentPoint { get; set; }
```

Attachment point.

### Block

```text
ACadSharp.Tables.BlockRecord Block { get; set; }
```

Block that contains the entities that make up the dimension picture.

### DefinitionPoint

```text
CSMath.XYZ DefinitionPoint { get; set; }
```

Definition point for the dimension line (in WCS).

### Flags

```text
ACadSharp.Entities.DimensionType Flags { get; }
```

Dimension type.

### FlipArrow1

```text
System.Boolean FlipArrow1 { get; set; }
```

Gets or sets a value indicating whether the first arrow. is to be flipped.

**Remarks:** Arrows are by default drawn inside the extension lines if there is enough space; otherwise, outside. This flag overrules the standard behavior.

**Value:** true if the arrow is to be flipped; otherwise, false.

### FlipArrow2

```text
System.Boolean FlipArrow2 { get; set; }
```

Gets or sets a value indicating whether the second arrow to be flipped.

**Remarks:** Arrows are by default drawn inside the extension lines if there is enough space; otherwise, outside. This flag overrules the standard behavior.

**Value:** true if the arrow is to be flipped; otherwise, false.

### HasStyleOverride

```text
System.Boolean HasStyleOverride { get; }
```

Gets a value indicating whether a style override is present in the extended data.

**Remarks:** Use this property to determine if the object contains custom style information that overrides default styling. This can be useful when rendering or processing objects that may have user-defined appearance settings.

### HorizontalDirection

```text
System.Double HorizontalDirection { get; set; }
```

All dimension types have an optional 51 group code, which indicates the horizontal direction for the dimension entity.The dimension entity determines the orientation of dimension text and lines for horizontal, vertical, and rotated linear dimensions This group value is the negative of the angle between the OCS X axis and the UCS X axis. It is always in the XY plane of the OCS

### InsertionPoint

```text
CSMath.XYZ InsertionPoint { get; set; }
```

Insertion point for clones of a dimension-Baseline and Continue(in OCS).

### IsAngular

```text
System.Boolean IsAngular { get; }
```

Indicates if the dimension is angular or linear.

### IsTextUserDefinedLocation

```text
System.Boolean IsTextUserDefinedLocation { get; set; }
```

Indicates if the dimension text has been positioned at a user-defined location rather than at the default location.

### LineSpacingFactor

```text
System.Double LineSpacingFactor { get; set; }
```

Dimension text-line spacing factor.

**Remarks:** Percentage of default (3-on-5) line spacing to be applied.

**Value:** Valid values range from 0.25 to 4.00

### LineSpacingStyle

```text
ACadSharp.Entities.LineSpacingStyleType LineSpacingStyle { get; set; }
```

Dimension text line-spacing style.

### Measurement

```text
System.Double Measurement { get; }
```

Actual measurement.

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.

### Style

```text
ACadSharp.Tables.DimensionStyle Style { get; set; }
```

Dimension style.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Text

```text
System.String Text { get; set; }
```

Gets or sets an explicit dimension text to be displayed instead of the standard dimension text created from the measurement in the format specified by the dimension-style properties.

**Remarks:** If null or empty, the dimension created from the measurement is to be displayed. If " " (one blank space), the text is to be suppressed. Anything else is drawn as the text.

### TextMiddlePoint

```text
CSMath.XYZ TextMiddlePoint { get; set; }
```

Middle point of dimension text(in OCS).

### TextRotation

```text
System.Double TextRotation { get; set; }
```

Rotation angle of the dimension text away from its default orientation (the direction of the dimension line).

**Remarks:** Optional

### Version

```text
System.Byte Version { get; set; }
```

Version number.
