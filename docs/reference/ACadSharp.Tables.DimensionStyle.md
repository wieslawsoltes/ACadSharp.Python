# ACadSharp.Tables.DimensionStyle

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.DimensionStyle`

Represents a ACadSharp.Tables.DimensionStyle table entry.

Object name F:ACadSharp.DxfFileToken.TableDimstyle Dxf class name F:ACadSharp.DxfSubclassMarker.DimensionStyle

Base type: `ACadSharp.Tables.TableEntry`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.DimensionStyle')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.DimensionStyle(System.String name)
```

Documentation inherited from: `base member`.

### DefaultName

```text
static System.String DefaultName = Standard
```

### StyleOverrideEntryName

```text
static System.String StyleOverrideEntryName = DSTYLE
```

Represents the entry name used for style override data in the underlying storage format.

**Remarks:** This constant can be used when reading from or writing to data sources that require a specific entry name for style overrides. The value is case-sensitive.

### ApplyRounding

```text
System.Double ApplyRounding(System.Double value, System.Boolean isAlternate = False)
```

Apply the rounding of the style to the value.

- `value`: value to apply the style rounding.
- `isAlternate`: flag to indicate to use the alternate rounding.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetAlternateUnitStyleFormat

```text
ACadSharp.Types.Units.UnitStyleFormat GetAlternateUnitStyleFormat()
```

Get the alternate unit style format for this dimension style.

### GetUnitStyleFormat

```text
ACadSharp.Types.Units.UnitStyleFormat GetUnitStyleFormat()
```

Get the unit style format for this dimension style.

### AlternateDimensioningSuffix

```text
System.String AlternateDimensioningSuffix { get; set; }
```

Specifies a text prefix or suffix (or both) to the alternate dimension measurement for all types of dimensions except angular (see DIMAPOST System Variable).

**Remarks:** For instance, if the current units are Architectural, ACadSharp.Tables.DimensionStyle.AlternateUnitDimensioning is on (true), ACadSharp.Tables.DimensionStyle.AlternateUnitScaleFactor is 25.4 (the number of millimeters per inch), ACadSharp.Tables.DimensionStyle.AlternateUnitDecimalPlaces is 2, and AlternateDimensioningSuffix is set to "mm", a distance of 10 units would be displayed as 10"[254.00mm].To turn off an established prefix or suffix (or both), set it to a single period (.).

### AlternateUnitDecimalPlaces

```text
System.Int16 AlternateUnitDecimalPlaces { get; set; }
```

Controls the number of decimal places in alternate units (see DIMALTD System Variable).

**Remarks:** If ACadSharp.Tables.DimensionStyle.AlternateUnitDimensioning is turned on (true), AlternateUnitDecimalPlaces specifies the number of digits displayed to the right of the decimal point in the alternate measurement.

### AlternateUnitDimensioning

```text
System.Boolean AlternateUnitDimensioning { get; set; }
```

Controls the display of alternate units in dimensions (see DIMALT System Variable).

**Value:** true enables alternate units; false disables alternate units.

### AlternateUnitFormat

```text
ACadSharp.Types.Units.LinearUnitFormat AlternateUnitFormat { get; set; }
```

Gets or sets the units format for alternate units of all dimension sub-styles except Angular (see DIMALTU System Variable).

### AlternateUnitRounding

```text
System.Double AlternateUnitRounding { get; set; }
```

Rounds off the alternate dimension units (see DIMALTRND System Variable).

### AlternateUnitScaleFactor

```text
System.Double AlternateUnitScaleFactor { get; set; }
```

Controls the multiplier for alternate units (see DIMALTF System Variable).

**Remarks:** If ACadSharp.Tables.DimensionStyle.AlternateUnitDimensioning is turned on (true), the value of this property (AlternateUnitScaleFactor) multiplies linear dimensions by a factor to produce a value in an alternate system of measurement. The initial value represents the number of millimeters in an inch.

### AlternateUnitToleranceDecimalPlaces

```text
System.Int16 AlternateUnitToleranceDecimalPlaces { get; set; }
```

Gets or sets the number of decimal places for the tolerance values in the alternate units of a dimension (see DIMALTTD System Variable).

### AlternateUnitToleranceZeroHandling

```text
ACadSharp.Tables.ZeroHandling AlternateUnitToleranceZeroHandling { get; set; }
```

Controls suppression of zeros in tolerance values (see DIMALTTZ System Variable).

### AlternateUnitZeroHandling

```text
ACadSharp.Tables.ZeroHandling AlternateUnitZeroHandling { get; set; }
```

Controls the suppression of zeros for alternate unit dimension values (see DIMALTZ System Variable).

### AngularDecimalPlaces

```text
System.Int16 AngularDecimalPlaces { get; set; }
```

Controls the number of precision places displayed in angular dimensions (see DIMADEC System Variable).

**Value:** -1: Angular dimensions display the number of decimal places specified by the ACadSharp.Tables.DimensionStyle.DecimalPlaces property0-8: Specifies the number of decimal places displayed in angular dimensions (independent of the value of the ACadSharp.Tables.DimensionStyle.DecimalPlaces property).

### AngularUnit

```text
ACadSharp.Types.Units.AngularUnitFormat AngularUnit { get; set; }
```

Gets or sets the units format for angular dimensions (see DIMAUNIT System Variable).

### AngularZeroHandling

```text
ACadSharp.Tables.AngularZeroHandling AngularZeroHandling { get; set; }
```

Suppresses zeros for angular dimensions (see DIMAZIN System Variable).

### ArcLengthSymbolPosition

```text
ACadSharp.Tables.ArcLengthSymbolPosition ArcLengthSymbolPosition { get; set; }
```

Controls display of the arc symbol in an arc length dimension (see DIMARCSYM System Variable).

### ArrowBlock

```text
ACadSharp.Tables.BlockRecord ArrowBlock { get; set; }
```

Gets or sets the arrowhead block displayed at the ends of dimension lines (see DIMBLK System Variable).

**Remarks:** Note: Annotative blocks cannot be used as custom arrowheads for dimensions or leaders.

**Value:** A ACadSharp.Tables.BlockRecord that makes up an arrowhead or null if the default, closed-filled arrowhead is to be displayed.

### ArrowSize

```text
System.Double ArrowSize { get; set; }
```

Controls the size of dimension line and leader line arrowheads. Also controls the size of hook lines (see DIMASZ System Variable).

### CenterMarkSize

```text
System.Double CenterMarkSize { get; set; }
```

Controls drawing of circle or arc center marks and centerlines by the DIMCENTER, DIMDIAMETER, and DIMRADIUS commands (see DIMCEN System Variable).

**Remarks:** For DIMDIAMETER and DIMRADIUS, the center mark is drawn only if you place the dimension line outside the circle or arc.

**Value:** 0No center marks or lines are drawn<0Centerlines are drawn>0Center marks are drawn

### CursorUpdate

```text
System.Boolean CursorUpdate { get; set; }
```

Controls options for user-positioned text (see DIMUPT System Variable).

**Value:** false: Cursor controls only the dimension line location.true: Cursor controls both the text position and the dimension line location,

### DecimalPlaces

```text
System.Int16 DecimalPlaces { get; set; }
```

Gets or sets the number of decimal places displayed for the primary units of a dimension (see DIMDEC System Variable).

### DecimalSeparator

```text
System.Char DecimalSeparator { get; set; }
```

Specifies a single-character decimal separator to use when creating dimensions whose unit format is decimal (see DIMDSEP System Variable).

**Remarks:** When prompted, enter a single character at the Command prompt. If dimension units is set to Decimal, the DecimalSeparator character is used instead of the default decimal point. If DecimalSeparator is set to NULL (default value), the decimal point is used as the dimension separator.

### Default

```text
static ACadSharp.Tables.DimensionStyle Default { get; }
```

Gets the default dimension style instance with standard settings.

**Remarks:** Use this property to obtain a baseline dimension style for creating or resetting dimension-related objects. The returned instance uses the default configuration defined by the system.

### DimArrow1

```text
ACadSharp.Tables.BlockRecord DimArrow1 { get; set; }
```

Gets or sets the arrowhead for the first end of the dimension line when ACadSharp.Tables.DimensionStyle.SeparateArrowBlocks is on (true) (see DIMBLK1 System Variable).

**Remarks:** Note: Annotative blocks cannot be used as custom arrowheads for dimensions or leaders.

**Value:** A ACadSharp.Tables.BlockRecord that makes up an arrowhead or null if the default, closed-filled arrowhead is to be displayed.

### DimArrow2

```text
ACadSharp.Tables.BlockRecord DimArrow2 { get; set; }
```

Gets or sets the arrowhead for the first end of the dimension line when ACadSharp.Tables.DimensionStyle.SeparateArrowBlocks is on (true) (see DIMBLK2 System Variable).

**Remarks:** Note: Annotative blocks cannot be used as custom arrowheads for dimensions or leaders.

**Value:** A ACadSharp.Tables.BlockRecord that makes up an arrowhead or null if the default, closed-filled arrowhead is to be displayed.

### DimensionFit

```text
System.Int16 DimensionFit { get; set; }
```

Determines how dimension text and arrows are arranged when space is not sufficient to place both within the extension lines. (see DIMFIT System Variable).

### DimensionLineColor

```text
ACadSharp.Color DimensionLineColor { get; set; }
```

Gets or sets colors to dimension lines, arrowheads, and dimension leader lines (see DIMCLRD System Variable).

**Remarks:** Also controls the color of leader lines created with the LEADER command.

### DimensionLineExtension

```text
System.Double DimensionLineExtension { get; set; }
```

Sets the distance the dimension line extends beyond the extension line when oblique strokes are drawn instead of arrowheads. (see DIMDLE System Variable).

### DimensionLineGap

```text
System.Double DimensionLineGap { get; set; }
```

Gets or sets the distance around the dimension text when the dimension line breaks to accommodate dimension text (see DIMGAP System Variable).

**Remarks:** Also sets the gap between annotation and a hook line created with the LEADER command. If you enter a negative value, DimensionLineGap places a box around the dimension text.The value of DimensionLineGap is also used as the minimum length of each segment of the dimension line. To locate the components of a linear dimension within the extension lines, enough space must be available for both arrowheads (2 x ACadSharp.Tables.DimensionStyle.ArrowSize), both dimension line segments (2 x DimensionLineGap), a gap on either side of the dimension text (another 2 x DimensionLineGap), and the length of the dimension text, which depends on its size and number of decimal places displayed.

### DimensionLineIncrement

```text
System.Double DimensionLineIncrement { get; set; }
```

Controls the spacing of the dimension lines in baseline dimensions (see DIMDLI System Variable).

**Remarks:** Each dimension line is offset from the previous one by this amount, if necessary, to avoid drawing over it. Changes made with DimensionLineIncrement are not applied to existing dimensions.

### DimensionLineWeight

```text
ACadSharp.LineWeightType DimensionLineWeight { get; set; }
```

Assigns line weight to dimension lines (see DIMLWD System Variable).

**Value:** Positive values represent line weight in hundredths of millimeters. (Multiply a value by 2540 to convert values from inches to hundredths of millimeters.)

### DimensionTextArrowFit

```text
ACadSharp.Tables.TextArrowFitType DimensionTextArrowFit { get; set; }
```

Determines how dimension text and arrows are arranged when space is not sufficient to place both within the extension lines. (see DIMATFIT System Variable).

**Remarks:** A leader is added to moved dimension text when ACadSharp.Tables.DimensionStyle.TextMovement is set to F:ACadSharp.Tables.TextMovement.AddLeaderWhenTextMoved.

### DimensionUnit

```text
System.Int16 DimensionUnit { get; set; }
```

DIMUNIT (obsolete, now use DIMLUNIT AND DIMFRAC)

### ExtensionLineColor

```text
ACadSharp.Color ExtensionLineColor { get; set; }
```

Gets or sets colors to extension lines, center marks, and centerlines (see DIMCLRE System Variable).

### ExtensionLineExtension

```text
System.Double ExtensionLineExtension { get; set; }
```

Specifies how far to extend the extension line beyond the dimension line (see DIMEXE System Variable).

### ExtensionLineOffset

```text
System.Double ExtensionLineOffset { get; set; }
```

Specifies how far extension lines are offset from origin points (see DIMEXO System Variable).

**Remarks:** With fixed-length extension lines, this value determines the minimum offset.

### ExtensionLineWeight

```text
ACadSharp.LineWeightType ExtensionLineWeight { get; set; }
```

Assigns line weight to extension lines (see DIMLWE System Variable).

**Value:** Positive values represent line weight in hundredths of millimeters. (Multiply a value by 2540 to convert values from inches to hundredths of millimeters.)

### FixedExtensionLineLength

```text
System.Double FixedExtensionLineLength { get; set; }
```

Sets the total length of the extension lines starting from the dimension line toward the dimension origin (see DIMFXL System Variable).

### FractionFormat

```text
ACadSharp.Tables.FractionFormat FractionFormat { get; set; }
```

Gets or sets the fraction format when ACadSharp.Tables.DimensionStyle.LinearUnitFormat is set to 4 (Architectural) or 5 (Fractional). (see DIMFRAC System Variable).

### GenerateTolerances

```text
System.Boolean GenerateTolerances { get; set; }
```

Appends tolerances to dimension text (see DIMTOL System Variable).

**Remarks:** Setting GenerateTolerances to on (true) turns ACadSharp.Tables.DimensionStyle.LimitsGeneration off (false).

### IsExtensionLineLengthFixed

```text
System.Boolean IsExtensionLineLengthFixed { get; set; }
```

Controls whether extension lines are set to a fixed length (see DIMFXLON System Variable).

**Value:** true when extension lines are set to the length specified by ACadSharp.Tables.DimensionStyle.FixedExtensionLineLength; otherwise, false.

### JoggedRadiusDimensionTransverseSegmentAngle

```text
System.Double JoggedRadiusDimensionTransverseSegmentAngle { get; set; }
```

Determines the angle of the transverse segment of the dimension line in a jogged radius dimension in radians. (see DIMJOGANG System Variable).

**Value:** Jogged radius dimensions are often created when the center point is located off the page. Valid settings range is 5 to 90 degrees.

### LeaderArrow

```text
ACadSharp.Tables.BlockRecord LeaderArrow { get; set; }
```

Specifies the arrow type for leaders (see DIMLDRBLK System Variable).

**Remarks:** Note: Annotative blocks cannot be used as custom arrowheads for dimensions or leaders.

**Value:** A ACadSharp.Tables.BlockRecord that makes up an arrowhead or null if the default, closed-filled arrowhead is to be displayed.

### LimitsGeneration

```text
System.Boolean LimitsGeneration { get; set; }
```

Generates dimension limits as the default text (see DIMLIM System Variable).

**Remarks:** Setting LimitsGeneration to on (true) turns ACadSharp.Tables.DimensionStyle.GenerateTolerances off (false).

### LineType

```text
ACadSharp.Tables.LineType LineType { get; set; }
```

Line type for the main line of the dimension.

### LineTypeExt1

```text
ACadSharp.Tables.LineType LineTypeExt1 { get; set; }
```

Line type for the extension line 1.

### LineTypeExt2

```text
ACadSharp.Tables.LineType LineTypeExt2 { get; set; }
```

Line type for the extension line 2.

### LinearScaleFactor

```text
System.Double LinearScaleFactor { get; set; }
```

Sets a scale factor for linear dimension measurements (see DIMLFAC System Variable).

**Remarks:** All linear dimension distances, including radii, diameters, and coordinates, are multiplied by this LinearScaleFactor before being converted to dimension text. Positive values of LinearScaleFactor are applied to dimensions in both model space and paper space; negative values are applied to paper space only.LinearScaleFactor applies primarily to non-associative dimensions (DIMASSOC set 0 or 1). For non-associative dimensions in paper space, LinearScaleFactor must be set individually for each layout viewport to accommodate viewport scaling.LinearScaleFactor has no effect on angular dimensions, and is not applied to the values held in ACadSharp.Tables.DimensionStyle.Rounding, ACadSharp.Tables.DimensionStyle.MinusTolerance, or ACadSharp.Tables.DimensionStyle.PlusTolerance.

### LinearUnitFormat

```text
ACadSharp.Types.Units.LinearUnitFormat LinearUnitFormat { get; set; }
```

Gets or sets units for all dimension types except Angular (see DIMLUNIT System Variable).

### MinusTolerance

```text
System.Double MinusTolerance { get; set; }
```

Gets or sets the minimum (or lower) tolerance limit for dimension text when ACadSharp.Tables.DimensionStyle.GenerateTolerances or ACadSharp.Tables.DimensionStyle.LimitsGeneration is on (true). (see DIMTM System Variable).

**Remarks:** MinusTolerance accepts signed values. If ACadSharp.Tables.DimensionStyle.GenerateTolerances is on and ACadSharp.Tables.DimensionStyle.PlusTolerance and MinusTolerance are set to the same value, a tolerance value is drawn.If MinusTolerance and ACadSharp.Tables.DimensionStyle.PlusTolerance values differ, the upper tolerance is drawn above the lower, and a plus sign is added to the ACadSharp.Tables.DimensionStyle.PlusTolerance value if it is positive.For MinusTolerance, the program uses the negative of the value you enter (adding a minus sign if you specify a positive number and a plus sign if you specify a negative number).

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

### PlusTolerance

```text
System.Double PlusTolerance { get; set; }
```

Gets or sets the maximum (or upper) tolerance limit for dimension text when ACadSharp.Tables.DimensionStyle.GenerateTolerances or ACadSharp.Tables.DimensionStyle.LimitsGeneration is on (true) (see DIMTP System Variable).

### PostFix

```text
System.String PostFix { get; set; }
```

Specifies a text prefix or suffix (or both) to the dimension measurement (see DIMPOST System Variable).

**Remarks:** For example, to establish a suffix for millimeters, set PostFix to mm; a distance of 19.2 units would be displayed as 19.2 mm.If tolerances are turned on, the suffix is applied to the tolerances as well as to the main dimension.Use <> to indicate placement of the text in relation to the dimension value. For example, enter <> mm to display a 5.0 millimeter radial dimension as "5.0mm". If you entered mm <>, the dimension would be displayed as "mm 5.0". Use the <> mechanism for angular dimensions.

### Prefix

```text
System.String Prefix { get; set; }
```

Gets or sets the prefix based on the ACadSharp.Tables.DimensionStyle.PostFix value.

### Rounding

```text
System.Double Rounding { get; set; }
```

Rounds all dimensioning distances to the specified value (see DIMRND System Variable).

**Remarks:** For instance, if Rounding is set to 0.25, all distances round to the nearest 0.25 unit. If you set the value to 1.0, all distances round to the nearest integer.Note that the number of digits edited after the decimal point depends on the precision set by ACadSharp.Tables.DimensionStyle.DecimalPlaces.This does not apply to angular dimensions.

### ScaleFactor

```text
System.Double ScaleFactor { get; set; }
```

Gets or sets the overall scale factor applied to dimensioning variables that specify sizes, distances, or offsets (see DIMSCALE System Variable).

**Remarks:** This ScaleFactor does not affect measured lengths, coordinates, or angles.Use ScaleFactor to control the overall scale of dimensions. However, if the current dimension style is annotative, ScaleFactor is automatically set to zero and the dimension scale is controlled by the CANNOSCALE system variable. ScaleFactor cannot be set to a non-zero value when using annotative dimensions.Also affects the leader objects with the LEADER command.Use MLEADERSCALE to scale multileader objects created with the MLEADER command.

**Value:** 1.0A reasonable default value is computed based on the scaling between the current model space viewport and paper space. If you are in paper space or model space and not using the paper space feature, the scale factor is 1.0.>0A scale factor is computed that leads text sizes, arrowhead sizes, and other scaled distances to plot at their face values.

### SeparateArrowBlocks

```text
System.Boolean SeparateArrowBlocks { get; set; }
```

Controls the display of dimension line arrowhead blocks (see DIMSAH System Variable).

**Value:** true if arrowhead blocks set by ACadSharp.Tables.DimensionStyle.DimArrow1 and ACadSharp.Tables.DimensionStyle.DimArrow2 shall be used; false if arrowhead block set by ACadSharp.Tables.DimensionStyle.ArrowBlock shall be used.

### Style

```text
ACadSharp.Tables.TextStyle Style { get; set; }
```

Specifies the text style of the dimension (see DIMTXSTY System Variable).

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Suffix

```text
System.String Suffix { get; set; }
```

Gets or sets the suffix based on the ACadSharp.Tables.DimensionStyle.PostFix value.

### SuppressFirstDimensionLine

```text
System.Boolean SuppressFirstDimensionLine { get; set; }
```

Controls suppression of the first dimension line and arrowhead (see DIMSD1 System Variable).

**Value:** true if the first dimension line is to be suppressed; otherwise, false.

### SuppressFirstExtensionLine

```text
System.Boolean SuppressFirstExtensionLine { get; set; }
```

Suppresses display of the first extension line (see DIMSE1 System Variable).

**Value:** true if the first extension line is to be suppressed; otherwise false.

### SuppressOutsideExtensions

```text
System.Boolean SuppressOutsideExtensions { get; set; }
```

Suppresses arrowheads if not enough space is available inside the extension lines (see DIMSOXD System Variable).

**Value:** true if arrowheads are to be suppressed; otherwise, false.

### SuppressSecondDimensionLine

```text
System.Boolean SuppressSecondDimensionLine { get; set; }
```

Controls suppression of the second dimension line and arrowhead (see DIMSD2 System Variable).

**Value:** true if the second dimension line is to be suppressed; otherwise, false.

### SuppressSecondExtensionLine

```text
System.Boolean SuppressSecondExtensionLine { get; set; }
```

Suppresses display of the second extension line (see DIMSE2 System Variable).

**Value:** true if the second extension line is to be suppressed; otherwise false.

### TextBackgroundColor

```text
ACadSharp.Color TextBackgroundColor { get; set; }
```

Sets the color for the text background in dimensions. (see DIMTFILLCLR System Variable).

### TextBackgroundFillMode

```text
ACadSharp.Tables.DimensionTextBackgroundFillMode TextBackgroundFillMode { get; set; }
```

Controls the background of dimension text (see DIMTFILL System Variable).

### TextColor

```text
ACadSharp.Color TextColor { get; set; }
```

Assigns colors to dimension text (see DIMCLRT System Variable).

**Remarks:** The color can be any valid color number.

### TextDirection

```text
ACadSharp.Tables.TextDirection TextDirection { get; set; }
```

Specifies the reading direction of the dimension text (see DIMTXTDIRECTION System Variable).

### TextHeight

```text
System.Double TextHeight { get; set; }
```

Specifies the height of dimension text, unless the current text style has a fixed height (see DIMTXT System Variable).

### TextHorizontalAlignment

```text
ACadSharp.Tables.DimensionTextHorizontalAlignment TextHorizontalAlignment { get; set; }
```

Controls the horizontal positioning of dimension text (see DIMJUST System Variable).

### TextInsideExtensions

```text
System.Boolean TextInsideExtensions { get; set; }
```

Draws text between extension lines (see DIMTIX System Variable).

**Value:** false: For linear and angular dimensions, dimension text is placed inside the extension lines if there is sufficient room.true: Draws dimension text between the extension lines even if it would ordinarily be placed outside those lines. For radius and diameter dimensions, TextInsideExtensions on (true) always forces the dimension text outside the circle or arc.

### TextInsideHorizontal

```text
System.Boolean TextInsideHorizontal { get; set; }
```

Controls the position of dimension text inside the extension lines for all dimension types except Ordinate. (see DIMTIH System Variable).

**Value:** true if the text is to be drawn horizontally; false if the text is to be aligned with the dimension line.

### TextMovement

```text
ACadSharp.Tables.TextMovement TextMovement { get; set; }
```

Sets dimension text movement rules (see DIMTMOVE System Variable).

### TextOutsideExtensions

```text
System.Boolean TextOutsideExtensions { get; set; }
```

Controls whether a dimension line is drawn between the extension lines even when the text is placed outside. (see DIMTOFL System Variable).

**Remarks:** For radius and diameter dimensions, a dimension line is drawn inside the circle or arc when the text, arrowheads, and leader are placed outside.

**Value:** true: Draws dimension lines between the measured points even when arrowheads are placed outside the measured pointsfalse: Does not draw dimension lines between the measured points when arrowheads are placed outside the measured points

### TextOutsideHorizontal

```text
System.Boolean TextOutsideHorizontal { get; set; }
```

Controls the position of dimension text outside the extension lines (see DIMTOH System Variable).

**Value:** true if the text is to be drawn horizontally; false if the text is to be aligned with the dimension line.

### TextVerticalAlignment

```text
ACadSharp.Tables.DimensionTextVerticalAlignment TextVerticalAlignment { get; set; }
```

Controls the vertical position of text in relation to the dimension line (see DIMTAD System Variable).

### TextVerticalPosition

```text
System.Double TextVerticalPosition { get; set; }
```

Controls the vertical position of dimension text above or below the dimension line (see DIMTVP System Variable).

**Remarks:** The TextVerticalPosition value is used when ACadSharp.Tables.DimensionStyle.TextVerticalAlignment is off. The magnitude of the vertical offset of text is the product of the text height and TextVerticalPosition. Setting TextVerticalPosition to 1.0 is equivalent to setting ACadSharp.Tables.DimensionStyle.TextVerticalAlignment to on. The dimension line splits to accommodate the text only if the absolute value of TextVerticalPosition is less than 0.7.

### TickSize

```text
System.Double TickSize { get; set; }
```

Specifies the size of oblique strokes drawn instead of arrowheads for linear, radius, and diameter dimensioning (see DIMTSZ System Variable).

**Value:** 0Draws arrowheads.>0Draws oblique strokes instead of arrowheads. The size of the oblique strokes is determined by this value multiplied by the value of ACadSharp.Tables.DimensionStyle.ScaleFactor.

### ToleranceAlignment

```text
ACadSharp.Tables.ToleranceAlignment ToleranceAlignment { get; set; }
```

Gets or sets the vertical justification for tolerance values relative to the nominal dimension text. (see DIMTOLJ System Variable).

### ToleranceDecimalPlaces

```text
System.Int16 ToleranceDecimalPlaces { get; set; }
```

Gets or sets the number of decimal places to display in tolerance values for the primary units in a dimension (see DIMTDEC System Variable).

### ToleranceScaleFactor

```text
System.Double ToleranceScaleFactor { get; set; }
```

Specifies a scale factor for the text height of fractions and tolerance values relative to the dimension text height, as set by ACadSharp.Tables.DimensionStyle.TextHeight (see DIMTFAC System Variable).

**Remarks:** For example, if ToleranceScaleFactor is set to 1.0, the text height of fractions and tolerances is the same height as the dimension text. If ToleranceScaleFactor is set to 0.7500, the text height of fractions and tolerances is three-quarters the size of dimension text.

### ToleranceZeroHandling

```text
ACadSharp.Tables.ZeroHandling ToleranceZeroHandling { get; set; }
```

Controls the suppression of zeros in tolerance values (see DIMTZIN System Variable).

**Remarks:** Value 0-3 affect feet-and-inch dimensions only.

### ZeroHandling

```text
ACadSharp.Tables.ZeroHandling ZeroHandling { get; set; }
```

Controls the suppression of zeros in the primary unit value (see DIMZIN System Variable).
