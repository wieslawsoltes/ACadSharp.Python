# ACadSharp.Header.CadHeader

`class` · `ACadSharp` · CLR name: `ACadSharp.Header.CadHeader`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Header.CadHeader')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Header.CadHeader()
```

### .ctor

```text
ACadSharp.Header.CadHeader(ACadSharp.ACadVersion version)
```

### .ctor

```text
ACadSharp.Header.CadHeader(ACadSharp.CadDocument document)
```

### GetHeaderMap

```text
static System.Collections.Generic.Dictionary[System.String, ACadSharp.CadSystemVariable] GetHeaderMap()
```

Gets a map of all the system variables and it's codes

### GetValue

```text
System.Object GetValue(System.String systemvar)
```

### GetValues

```text
System.Collections.Generic.Dictionary[ACadSharp.DxfCode, System.Object] GetValues(System.String systemvar)
```

Get the primitive values in each dxf code

**Returns:** dictionary with the codes and values

- `systemvar`: 

### SetValue

```text
System.Void SetValue(System.String systemvar, System.Object[] values)
```

Set a value of a system variable by name

- `systemvar`: name of the system var
- `values`: parameters for the constructor of the value

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### AngleBase

```text
System.Double AngleBase { get; set; }
```

Sets the zero (0) base angle with respect to the current UCS.

**Remarks:** System variable ANGBASE

### AngularDirection

```text
ACadSharp.Types.Units.AngularDirection AngularDirection { get; set; }
```

Sets the direction of positive angles.

**Remarks:** System variable ANGDIR.

### AngularUnit

```text
ACadSharp.Types.Units.AngularUnitFormat AngularUnit { get; set; }
```

Sets units for angles.

**Remarks:** System variable AUNITS.

### AngularUnitPrecision

```text
System.Int16 AngularUnitPrecision { get; set; }
```

Sets the display precision for angular units and coordinates.

**Remarks:** System variable AUPREC.

**Value:** Valid values are from 0 to 8.

### ArrowBlockName

```text
System.String ArrowBlockName { get; set; }
```

Arrow block name for leaders

**Remarks:** System variable DIMLDRBLK

### AssociatedDimensions

```text
System.Boolean AssociatedDimensions { get; set; }
```

**Remarks:** System variable DIMASO Obsolete; see DIMASSOC

### AttributeVisibility

```text
ACadSharp.Header.AttributeVisibilityMode AttributeVisibility { get; set; }
```

Controls display of attributes.

**Remarks:** System variable ATTMODE.

### BlipMode

```text
System.Boolean BlipMode { get; set; }
```

System variable BLIPMODE ??

### CameraDisplayObjects

```text
System.Boolean CameraDisplayObjects { get; set; }
```

**Remarks:** System variable CAMERADISPLAY

### CameraHeight

```text
System.Double CameraHeight { get; set; }
```

**Remarks:** System variable CAMERAHEIGHT

### ChamferAngle

```text
System.Double ChamferAngle { get; set; }
```

Sets the chamfer angle when CHAMMODE is set to 1.

**Remarks:** System variable CHAMFERD.

### ChamferDistance1

```text
System.Double ChamferDistance1 { get; set; }
```

Sets the first chamfer distance when CHAMMODE is set to 0.

**Remarks:** System variable CHAMFERA.

### ChamferDistance2

```text
System.Double ChamferDistance2 { get; set; }
```

Sets the second chamfer distance when CHAMMODE is set to 0.

**Remarks:** System variable CHAMFERB.

### ChamferLength

```text
System.Double ChamferLength { get; set; }
```

Sets the chamfer length when CHAMMODE is set to 1.

**Remarks:** System variable CHAMFERC.

### CodePage

```text
System.String CodePage { get; set; }
```

Drawing code page.

**Remarks:** System variable DWGCODEPAGE

### CreateDateTime

```text
System.DateTime CreateDateTime { get; set; }
```

Local date/time of drawing creation (see Special Handling of Date/Time Variables).

**Remarks:** System variable TDCREATE.

### CreateEllipseAsPolyline

```text
System.Boolean CreateEllipseAsPolyline { get; set; }
```

Controls the ellipse type created with ELLIPSE.

**Remarks:** System variable PELLIPSE.

### CurrentDimensionStyle

```text
ACadSharp.Tables.DimensionStyle CurrentDimensionStyle { get; }
```

Gets the current dimension style applied to the document or the default dimension style if no document is loaded.

### CurrentDimensionStyleName

```text
System.String CurrentDimensionStyleName { get; set; }
```

Dimension style name.

**Remarks:** System variable DIMSTYLE

### CurrentEntityColor

```text
ACadSharp.Color CurrentEntityColor { get; set; }
```

Current entity color number.

**Remarks:** System variable CECOLOR.

### CurrentEntityLineWeight

```text
ACadSharp.LineWeightType CurrentEntityLineWeight { get; set; }
```

Line weight of new objects

**Remarks:** System variable CELWEIGHT

### CurrentEntityLinetypeScale

```text
System.Double CurrentEntityLinetypeScale { get; set; }
```

Current entity linetype scale.

**Remarks:** System variable CELTSCALE.

### CurrentEntityPlotStyle

```text
ACadSharp.Header.EntityPlotStyleType CurrentEntityPlotStyle { get; set; }
```

Plot style type of new objects

**Remarks:** System variable CEPSNTYPE

### CurrentLayer

```text
ACadSharp.Tables.Layer CurrentLayer { get; }
```

Gets the current layer associated with the document. If the document is null, returns the default layer.

**Remarks:** This property retrieves the layer based on the current layer name from the document's layer collection, if a document is available. If no document is associated, it returns the default layer stored internally.

### CurrentLayerName

```text
System.String CurrentLayerName { get; set; }
```

Sets the current layer.

**Remarks:** System variable CLAYER

### CurrentLineType

```text
ACadSharp.Tables.LineType CurrentLineType { get; }
```

Gets the current line type associated with the document or the default line type if no document is set.

### CurrentLineTypeName

```text
System.String CurrentLineTypeName { get; set; }
```

Sets the linetype of new objects.

**Remarks:** System variable CELTYPE.

### CurrentMLineStyle

```text
ACadSharp.Objects.MLineStyle CurrentMLineStyle { get; }
```

### CurrentMLineStyleName

```text
System.String CurrentMLineStyleName { get; set; }
```

Current multiline style name.

**Remarks:** System variable CMLSTYLE.

### CurrentMultiLineJustification

```text
ACadSharp.Entities.VerticalAlignmentType CurrentMultiLineJustification { get; set; }
```

Current multi line justification.

**Remarks:** System variable CMLJUST.

### CurrentMultilineScale

```text
System.Double CurrentMultilineScale { get; set; }
```

Current multiline scale.

**Remarks:** System variable CMLSCALE.

### CurrentTextStyle

```text
ACadSharp.Tables.TextStyle CurrentTextStyle { get; }
```

Gets the current text style applied to the document or the default text style if no document is loaded.

### CurrentTextStyleName

```text
System.String CurrentTextStyleName { get; set; }
```

Sets the name of the current text style.

**Remarks:** System variable TEXTSTYLE.

### DgnUnderlayFramesVisibility

```text
System.Char DgnUnderlayFramesVisibility { get; set; }
```

**Remarks:** System variable DGNFRAME

### DimensionAltMzf

```text
System.Double DimensionAltMzf { get; set; }
```

Undocumented

**Remarks:** System variable DIMALTMZF

### DimensionAltMzs

```text
System.String DimensionAltMzs { get; set; }
```

Undocumented

**Remarks:** System variable DIMALTMZS

### DimensionAlternateDimensioningSuffix

```text
System.String DimensionAlternateDimensioningSuffix { get; set; }
```

Alternate dimensioning suffix

**Remarks:** System variable DIMAPOST

### DimensionAlternateUnitDecimalPlaces

```text
System.Int16 DimensionAlternateUnitDecimalPlaces { get; set; }
```

Alternate unit decimal places

**Remarks:** System variable DIMALTD

### DimensionAlternateUnitDimensioning

```text
System.Boolean DimensionAlternateUnitDimensioning { get; set; }
```

Alternate unit dimensioning performed if nonzero

**Remarks:** System variable DIMALT

### DimensionAlternateUnitFormat

```text
ACadSharp.Types.Units.LinearUnitFormat DimensionAlternateUnitFormat { get; set; }
```

Units format for alternate units of all dimension style family members except angular

**Remarks:** System variable DIMALTU

### DimensionAlternateUnitRounding

```text
System.Double DimensionAlternateUnitRounding { get; set; }
```

Determines rounding of alternate units

**Remarks:** System variable DIMALTRND

### DimensionAlternateUnitScaleFactor

```text
System.Double DimensionAlternateUnitScaleFactor { get; set; }
```

Alternate unit scale factor

**Remarks:** System variable DIMALTF

### DimensionAlternateUnitToleranceDecimalPlaces

```text
System.Int16 DimensionAlternateUnitToleranceDecimalPlaces { get; set; }
```

Number of decimal places for tolerance values of an alternate units dimension

**Remarks:** System variable DIMALTTD

### DimensionAlternateUnitToleranceZeroHandling

```text
ACadSharp.Tables.ZeroHandling DimensionAlternateUnitToleranceZeroHandling { get; set; }
```

Controls suppression of zeros for alternate tolerance values

**Remarks:** System variable DIMALTTZ

### DimensionAlternateUnitZeroHandling

```text
ACadSharp.Tables.ZeroHandling DimensionAlternateUnitZeroHandling { get; set; }
```

Controls suppression of zeros for alternate unit dimension values

**Remarks:** System variable DIMALTZ

### DimensionAngularDimensionDecimalPlaces

```text
System.Int16 DimensionAngularDimensionDecimalPlaces { get; set; }
```

Number of precision places displayed in angular dimensions

**Remarks:** System variable DIMADEC

### DimensionAngularUnit

```text
ACadSharp.Types.Units.AngularUnitFormat DimensionAngularUnit { get; set; }
```

Angle format for angular dimensions

**Remarks:** System variable DIMAUNIT

### DimensionAngularZeroHandling

```text
ACadSharp.Tables.AngularZeroHandling DimensionAngularZeroHandling { get; set; }
```

Controls suppression of zeros for angular dimensions

**Remarks:** System variable DIMAZIN

### DimensionArcLengthSymbolPosition

```text
ACadSharp.Tables.ArcLengthSymbolPosition DimensionArcLengthSymbolPosition { get; set; }
```

Undocumented

**Remarks:** System variable DIMARCSYM

### DimensionArrowSize

```text
System.Double DimensionArrowSize { get; set; }
```

Dimensioning arrow size

**Remarks:** System variable DIMASZ

### DimensionAssociativity

```text
ACadSharp.Header.DimensionAssociation DimensionAssociativity { get; set; }
```

Controls the associativity of dimension objects

**Remarks:** System variable DIMASSOC

### DimensionBlockName

```text
System.String DimensionBlockName { get; set; }
```

Arrow block name

**Remarks:** System variable DIMBLK

### DimensionBlockNameFirst

```text
System.String DimensionBlockNameFirst { get; set; }
```

First arrow block name

**Remarks:** System variable DIMBLK1

### DimensionBlockNameSecond

```text
System.String DimensionBlockNameSecond { get; set; }
```

Second arrow block name

**Remarks:** System variable DIMBLK2

### DimensionCenterMarkSize

```text
System.Double DimensionCenterMarkSize { get; set; }
```

Size of center mark/lines

**Remarks:** System variable DIMCEN

### DimensionCursorUpdate

```text
System.Boolean DimensionCursorUpdate { get; set; }
```

Cursor functionality for user-positioned text

**Remarks:** System variable DIMUPT

### DimensionDecimalPlaces

```text
System.Int16 DimensionDecimalPlaces { get; set; }
```

Number of decimal places for the tolerance values of a primary units dimension

**Remarks:** System variable DIMDEC

### DimensionDecimalSeparator

```text
System.Char DimensionDecimalSeparator { get; set; }
```

Single-character decimal separator used when creating dimensions whose unit format is decimal

**Remarks:** System variable DIMLUNIT

### DimensionDimensionTextArrowFit

```text
ACadSharp.Tables.TextArrowFitType DimensionDimensionTextArrowFit { get; set; }
```

Controls dimension text and arrow placement when space is not sufficient to place both within the extension lines

**Remarks:** System variable DIMATFIT

### DimensionExtensionLineColor

```text
ACadSharp.Color DimensionExtensionLineColor { get; set; }
```

Dimension extension line color override.

**Remarks:** System variable DIMCLRE

### DimensionExtensionLineExtension

```text
System.Double DimensionExtensionLineExtension { get; set; }
```

Extension line extension override.

**Remarks:** System variable DIMEXE

### DimensionExtensionLineOffset

```text
System.Double DimensionExtensionLineOffset { get; set; }
```

Extension line offset override.

**Remarks:** System variable DIMEXO

### DimensionFit

```text
System.Int16 DimensionFit { get; set; }
```

**Remarks:** System variable DIMFIT

### DimensionFixedExtensionLineLength

```text
System.Double DimensionFixedExtensionLineLength { get; set; }
```

Undocumented

**Remarks:** System variable DIMFXL

### DimensionFractionFormat

```text
ACadSharp.Tables.FractionFormat DimensionFractionFormat { get; set; }
```

Undocumented

**Remarks:** System variable DIMFRAC

### DimensionGenerateTolerances

```text
System.Boolean DimensionGenerateTolerances { get; set; }
```

Vertical justification for tolerance values override.

**Remarks:** System variable DIMTOL

### DimensionIsExtensionLineLengthFixed

```text
System.Boolean DimensionIsExtensionLineLengthFixed { get; set; }
```

Undocumented

**Remarks:** System variable DIMFXLON

### DimensionJoggedRadiusDimensionTransverseSegmentAngle

```text
System.Double DimensionJoggedRadiusDimensionTransverseSegmentAngle { get; set; }
```

Undocumented

**Remarks:** System variable DIMJOGANG

### DimensionLimitsGeneration

```text
System.Boolean DimensionLimitsGeneration { get; set; }
```

Dimension limits generated if nonzero override.

**Remarks:** System variable DIMLIM

### DimensionLineColor

```text
ACadSharp.Color DimensionLineColor { get; set; }
```

Dimension line color

**Remarks:** System variable DIMCLRD

### DimensionLineExtension

```text
System.Double DimensionLineExtension { get; set; }
```

Dimension line extension

**Remarks:** System variable DIMDLE

### DimensionLineGap

```text
System.Double DimensionLineGap { get; set; }
```

Undocumented

**Remarks:** System variable DIMGAP

### DimensionLineIncrement

```text
System.Double DimensionLineIncrement { get; set; }
```

Dimension line increment

**Remarks:** System variable DIMDLI

### DimensionLineType

```text
System.String DimensionLineType { get; set; }
```

Undocumented

**Remarks:** System variable DIMLTYPE

### DimensionLineWeight

```text
ACadSharp.LineWeightType DimensionLineWeight { get; set; }
```

Dimension line lineweight

**Remarks:** System variable DIMLWD

### DimensionLinearScaleFactor

```text
System.Double DimensionLinearScaleFactor { get; set; }
```

Linear measurements scale factor override.

**Remarks:** System variable DIMLFAC

### DimensionLinearUnitFormat

```text
ACadSharp.Types.Units.LinearUnitFormat DimensionLinearUnitFormat { get; set; }
```

Sets units for all dimension types except Angular

**Remarks:** System variable DIMLUNIT

### DimensionMinusTolerance

```text
System.Double DimensionMinusTolerance { get; set; }
```

Minus tolerance

**Remarks:** System variable DIMTM

### DimensionMzf

```text
System.Double DimensionMzf { get; set; }
```

Undocumented

**Remarks:** System variable DIMMZF

### DimensionMzs

```text
System.String DimensionMzs { get; set; }
```

Undocumented

**Remarks:** System variable DIMMZS

### DimensionPlusTolerance

```text
System.Double DimensionPlusTolerance { get; set; }
```

Plus tolerance

**Remarks:** System variable DIMTP

### DimensionPostFix

```text
System.String DimensionPostFix { get; set; }
```

Undocumented

**Remarks:** System variable DIMPOST

### DimensionRounding

```text
System.Double DimensionRounding { get; set; }
```

Rounding value for dimension distances

**Remarks:** System variable DIMRND

### DimensionScaleFactor

```text
System.Double DimensionScaleFactor { get; set; }
```

Overall dimensioning scale factor

**Remarks:** System variable DIMSCALE

### DimensionSeparateArrowBlocks

```text
System.Boolean DimensionSeparateArrowBlocks { get; set; }
```

Use separate arrow blocks if nonzero

**Remarks:** System variable DIMSAH

### DimensionSuppressFirstDimensionLine

```text
System.Boolean DimensionSuppressFirstDimensionLine { get; set; }
```

Suppression of first extension line.

**Remarks:** System variable DIMSD1

### DimensionSuppressFirstExtensionLine

```text
System.Boolean DimensionSuppressFirstExtensionLine { get; set; }
```

First extension line suppressed if nonzero

**Remarks:** System variable DIMSE1

### DimensionSuppressOutsideExtensions

```text
System.Boolean DimensionSuppressOutsideExtensions { get; set; }
```

Suppress outside-extensions dimension lines if nonzero

**Remarks:** System variable DIMSOXD

### DimensionSuppressSecondDimensionLine

```text
System.Boolean DimensionSuppressSecondDimensionLine { get; set; }
```

Suppression of second extension line

**Remarks:** System variable DIMSD2

### DimensionSuppressSecondExtensionLine

```text
System.Boolean DimensionSuppressSecondExtensionLine { get; set; }
```

Second extension line suppressed if nonzero

**Remarks:** System variable DIMSE2

### DimensionTex1

```text
System.String DimensionTex1 { get; set; }
```

Undocumented

**Remarks:** System variable DIMLTEX1

### DimensionTex2

```text
System.String DimensionTex2 { get; set; }
```

Undocumented

**Remarks:** System variable DIMLTEX2

### DimensionTextBackgroundColor

```text
ACadSharp.Color DimensionTextBackgroundColor { get; set; }
```

Undocumented

**Remarks:** System variable DIMTFILLCLR

### DimensionTextBackgroundFillMode

```text
ACadSharp.Tables.DimensionTextBackgroundFillMode DimensionTextBackgroundFillMode { get; set; }
```

Undocumented

**Remarks:** System variable DIMTFILL

### DimensionTextColor

```text
ACadSharp.Color DimensionTextColor { get; set; }
```

Dimension text color

**Remarks:** System variable DIMCLRT

### DimensionTextDirection

```text
ACadSharp.Tables.TextDirection DimensionTextDirection { get; set; }
```

Undocumented

**Remarks:** System variable DIMTXTDIRECTION

### DimensionTextHeight

```text
System.Double DimensionTextHeight { get; set; }
```

Dimensioning text height

**Remarks:** System variable DIMTXT

### DimensionTextHorizontalAlignment

```text
ACadSharp.Tables.DimensionTextHorizontalAlignment DimensionTextHorizontalAlignment { get; set; }
```

Horizontal dimension text position

**Remarks:** System variable DIMJUST

### DimensionTextInsideExtensions

```text
System.Boolean DimensionTextInsideExtensions { get; set; }
```

Force text inside extensions if nonzero

**Remarks:** System variable DIMTIX

### DimensionTextInsideHorizontal

```text
System.Boolean DimensionTextInsideHorizontal { get; set; }
```

Text inside horizontal if nonzero

**Remarks:** System variable DIMTIH

### DimensionTextMovement

```text
ACadSharp.Tables.TextMovement DimensionTextMovement { get; set; }
```

Dimension text movement rules decimal

**Remarks:** System variable DIMTMOVE

### DimensionTextOutsideExtensions

```text
System.Boolean DimensionTextOutsideExtensions { get; set; }
```

If text is outside the extension lines, dimension lines are forced between the extension lines if nonzero

**Remarks:** System variable DIMTOFL

### DimensionTextOutsideHorizontal

```text
System.Boolean DimensionTextOutsideHorizontal { get; set; }
```

Text outside horizontal if nonzero

**Remarks:** System variable DIMTOH

### DimensionTextStyle

```text
ACadSharp.Tables.TextStyle DimensionTextStyle { get; }
```

Gets the current dimension text style applied to the document or the default dimension text style if no document is loaded.

### DimensionTextStyleName

```text
System.String DimensionTextStyleName { get; set; }
```

Dimension text style

**Remarks:** System variable DIMTXSTY

### DimensionTextVerticalAlignment

```text
ACadSharp.Tables.DimensionTextVerticalAlignment DimensionTextVerticalAlignment { get; set; }
```

Text above dimension line if nonzero

**Remarks:** System variable DIMTAD

### DimensionTextVerticalPosition

```text
System.Double DimensionTextVerticalPosition { get; set; }
```

Text vertical position

**Remarks:** System variable DIMTVP

### DimensionTickSize

```text
System.Double DimensionTickSize { get; set; }
```

Dimensioning tick size

**Remarks:** System variable DIMTSZ

### DimensionToleranceAlignment

```text
ACadSharp.Tables.ToleranceAlignment DimensionToleranceAlignment { get; set; }
```

Vertical justification for tolerance values

**Remarks:** System variable DIMTOLJ

### DimensionToleranceDecimalPlaces

```text
System.Int16 DimensionToleranceDecimalPlaces { get; set; }
```

Number of decimal places to display the tolerance values

**Remarks:** System variable DIMTDEC

### DimensionToleranceScaleFactor

```text
System.Double DimensionToleranceScaleFactor { get; set; }
```

Dimension tolerance display scale factor

**Remarks:** System variable DIMTFAC

### DimensionToleranceZeroHandling

```text
ACadSharp.Tables.ZeroHandling DimensionToleranceZeroHandling { get; set; }
```

Controls suppression of zeros for tolerance values

**Remarks:** System variable DIMTZIN

### DimensionUnit

```text
System.Int16 DimensionUnit { get; set; }
```

Controls suppression of zeros for alternate unit dimension values

**Remarks:** System variable DIMUNIT

### DimensionZeroHandling

```text
ACadSharp.Tables.ZeroHandling DimensionZeroHandling { get; set; }
```

Controls suppression of zeros for primary unit values

**Remarks:** System variable DIMZIN

### DimensionstyleOverrides

```text
ACadSharp.Tables.DimensionStyle DimensionstyleOverrides { get; }
```

Get the ACadSharp.Tables.DimensionStyle override for this document.

### DisplayLightGlyphs

```text
System.Char DisplayLightGlyphs { get; set; }
```

**Remarks:** System variable LIGHTGLYPHDISPLAY

### DisplayLineWeight

```text
System.Boolean DisplayLineWeight { get; set; }
```

Controls whether the lineweights of objects are displayed. 0 = Lineweight is not displayed 1 = Lineweight is displayed

**Remarks:** System variable LWDISPLAY

### DisplaySilhouetteCurves

```text
System.Boolean DisplaySilhouetteCurves { get; set; }
```

Controls display of silhouette edges of 3D solid and surface objects in the Wireframe or 2D Wireframe visual styles.

**Remarks:** System variable DISPSILH.

### Document

```text
ACadSharp.CadDocument Document { get; }
```

Document where this header resides

### DraftAngleFirstCrossSection

```text
System.Double DraftAngleFirstCrossSection { get; set; }
```

**Remarks:** System variable LOFTANG1

### DraftAngleSecondCrossSection

```text
System.Double DraftAngleSecondCrossSection { get; set; }
```

**Remarks:** System variable LOFTANG2

### DraftMagnitudeFirstCrossSection

```text
System.Double DraftMagnitudeFirstCrossSection { get; set; }
```

**Remarks:** System variable LOFTMAG1

### DraftMagnitudeSecondCrossSection

```text
System.Double DraftMagnitudeSecondCrossSection { get; set; }
```

**Remarks:** System variable LOFTMAG2

### Dw3DPrecision

```text
System.Double Dw3DPrecision { get; set; }
```

**Remarks:** System variable 3DDWFPREC

### DwgUnderlayFramesVisibility

```text
System.Char DwgUnderlayFramesVisibility { get; set; }
```

**Remarks:** System variable DWFFRAME

### Elevation

```text
System.Double Elevation { get; set; }
```

Current elevation set by ELEV command

**Remarks:** System variable ELEVATION

### EndCaps

```text
System.Int16 EndCaps { get; set; }
```

Line weight end-caps setting for new objects

**Remarks:** System variable ENDCAPS

### EntitySortingFlags

```text
ACadSharp.Header.ObjectSortingFlags EntitySortingFlags { get; set; }
```

Controls the object sorting methods

**Remarks:** System variable SORTENTS

### ExtendedNames

```text
System.Boolean ExtendedNames { get; set; }
```

Controls symbol table naming

**Remarks:** System variable EXTNAMES

### ExtensionLineWeight

```text
ACadSharp.LineWeightType ExtensionLineWeight { get; set; }
```

Extension line lineweight

**Remarks:** System variable DIMLWE

### ExternalReferenceClippingBoundaryType

```text
ACadSharp.Header.XClipFrameType ExternalReferenceClippingBoundaryType { get; set; }
```

Determines whether xref clipping boundaries are visible or plotted in the current drawing.

**Remarks:** System variable XCLIPFRAME

### FacetResolution

```text
System.Double FacetResolution { get; set; }
```

Adjusts the smoothness of shaded and rendered objects, rendered shadows, and objects with hidden lines removed.

**Remarks:** System variable FACETRES.

**Value:** Valid values are from 0.01 to 10.0.

### FillMode

```text
System.Boolean FillMode { get; set; }
```

Specifies whether hatches and fills, 2D solids, and wide polylines are filled in.

**Remarks:** System variable FILLMODE.

### FilletRadius

```text
System.Double FilletRadius { get; set; }
```

Stores the current fillet radius for 2D objects.

**Remarks:** System variable FILLETRAD.

### FingerPrintGuid

```text
System.String FingerPrintGuid { get; }
```

Set at creation time, uniquely identifies a particular drawing

**Remarks:** System variable FINGERPRINTGUID

### HaloGapPercentage

```text
System.Byte HaloGapPercentage { get; set; }
```

Specifies a gap to be displayed where an object is hidden by another object; the value is specified as a percent of one unit and is independent of the zoom level.A haloed line is shortened at the point where it is hidden when HIDE or the Hidden option of SHADEMODE is used

**Remarks:** System variable HALOGAP

### HandleSeed

```text
System.UInt64 HandleSeed { get; }
```

Next available handle.

**Remarks:** System variable HANDSEED.

### HideText

```text
System.Byte HideText { get; set; }
```

Specifies HIDETEXT system variable

**Remarks:** System variable HIDETEXT

### HyperLinkBase

```text
System.String HyperLinkBase { get; set; }
```

Path for all relative hyperlinks in the drawing. If null, the drawing path is used

**Remarks:** System variable HYPERLINKBASE

### IndexCreationFlags

```text
ACadSharp.Header.IndexCreationFlags IndexCreationFlags { get; set; }
```

Controls whether layer and spatial indexes are created and saved in drawing files

**Remarks:** System variable INDEXCTL

### InsUnits

```text
ACadSharp.Types.Units.UnitsType InsUnits { get; set; }
```

Default drawing units for blocks

**Remarks:** System variable INSUNITS

### InterfereColor

```text
ACadSharp.Color InterfereColor { get; set; }
```

Represents the ACI color index of the "interference objects" created during the INTERFERE command. Default value is 1

**Remarks:** System variable INTERFERECOLOR

### IntersectionDisplay

```text
System.Byte IntersectionDisplay { get; set; }
```

### JoinStyle

```text
System.Int16 JoinStyle { get; set; }
```

Line weight joint setting for new objects

**Remarks:** System variable JOINSTYLE

### LastSavedBy

```text
System.String LastSavedBy { get; set; }
```

Displays the name of the last person who modified the file

**Remarks:** System variable LASTSAVEDBY

### Latitude

```text
System.Double Latitude { get; set; }
```

Specifies the latitude of the drawing model in decimal format.

**Remarks:** System variable LATITUDE

### LensLength

```text
System.Double LensLength { get; set; }
```

**Remarks:** System variable LENSLENGTH

### LimitCheckingOn

```text
System.Boolean LimitCheckingOn { get; set; }
```

Controls whether you can create objects outside the grid limits.

**Remarks:** System variable LIMCHECK.

### LineTypeScale

```text
System.Double LineTypeScale { get; set; }
```

Sets the global linetype scale factor.

**Remarks:** System variable LTSCALE.

### LinearUnitFormat

```text
ACadSharp.Types.Units.LinearUnitFormat LinearUnitFormat { get; set; }
```

Sets the linear units format for creating objects.

**Remarks:** System variable LUNITS.

### LinearUnitPrecision

```text
System.Int16 LinearUnitPrecision { get; set; }
```

Sets the display precision for linear units and coordinates.

**Remarks:** System variable LUPREC.

**Value:** Valid values are from 0 to 8.

### LoadOLEObject

```text
System.Boolean LoadOLEObject { get; set; }
```

**Remarks:** System variable OLESTARTUP

### LoftedObjectNormals

```text
System.Char LoftedObjectNormals { get; set; }
```

**Remarks:** System variable LOFTNORMALS

### Longitude

```text
System.Double Longitude { get; set; }
```

Specifies the longitude of the drawing model in decimal format.

**Remarks:** System variable LONGITUDE

### MaintenanceVersion

```text
System.Int16 MaintenanceVersion { get; }
```

Maintenance version number(should be ignored)

**Remarks:** System variable ACADMAINTVER.

### MaxViewportCount

```text
System.Int16 MaxViewportCount { get; set; }
```

Sets the maximum number of viewports that can be active at one time in a layout.

**Remarks:** System variable MAXACTVP.

### MeasurementUnits

```text
ACadSharp.Header.MeasurementUnits MeasurementUnits { get; set; }
```

Controls whether the current drawing uses imperial or metric hatch pattern and linetype files.

**Remarks:** System variable MEASUREMENT

### MenuFileName

```text
System.String MenuFileName { get; set; }
```

Name of menu file.

**Remarks:** System variable MENU.

### MirrorText

```text
System.Boolean MirrorText { get; set; }
```

Controls how MIRROR reflects text.

**Remarks:** System variable MIRRTEXT.

### ModelSpaceExtMax

```text
CSMath.XYZ ModelSpaceExtMax { get; set; }
```

X, Y, and Z drawing extents upper-right corner(in WCS)

**Remarks:** System variable EXTMAX

### ModelSpaceExtMin

```text
CSMath.XYZ ModelSpaceExtMin { get; set; }
```

X, Y, and Z drawing extents lower-left corner (in WCS)

**Remarks:** System variable EXTMIN

### ModelSpaceInsertionBase

```text
CSMath.XYZ ModelSpaceInsertionBase { get; set; }
```

Insertion base set by BASE command(in WCS)

**Remarks:** System variable INSBASE

### ModelSpaceLimitsMax

```text
CSMath.XY ModelSpaceLimitsMax { get; set; }
```

XY drawing limits upper-right corner (in WCS)

**Remarks:** System variable LIMMAX

### ModelSpaceLimitsMin

```text
CSMath.XY ModelSpaceLimitsMin { get; set; }
```

XY drawing limits lower-left corner (in WCS)

**Remarks:** System variable LIMMIN

### ModelSpaceOrigin

```text
CSMath.XYZ ModelSpaceOrigin { get; set; }
```

Origin of current UCS(in WCS)

**Remarks:** System variable UCSORG

### ModelSpaceOrthographicBackDOrigin

```text
CSMath.XYZ ModelSpaceOrthographicBackDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing model space UCS to BACK when PUCSBASE is set to WORLD

**Remarks:** System variable UCSORGBACK

### ModelSpaceOrthographicBottomDOrigin

```text
CSMath.XYZ ModelSpaceOrthographicBottomDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing model space UCS to BOTTOM when PUCSBASE is set to WORLD

**Remarks:** System variable UCSORGBOTTOM

### ModelSpaceOrthographicFrontDOrigin

```text
CSMath.XYZ ModelSpaceOrthographicFrontDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing model space UCS to FRONT when PUCSBASE is set to WORLD

**Remarks:** System variable UCSORGFRONT

### ModelSpaceOrthographicLeftDOrigin

```text
CSMath.XYZ ModelSpaceOrthographicLeftDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing model space UCS to LEFT when PUCSBASE is set to WORLD

**Remarks:** System variable UCSORGLEFT

### ModelSpaceOrthographicRightDOrigin

```text
CSMath.XYZ ModelSpaceOrthographicRightDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing model space UCS to RIGHT when PUCSBASE is set to WORLD

**Remarks:** System variable UCSORGRIGHT

### ModelSpaceOrthographicTopDOrigin

```text
CSMath.XYZ ModelSpaceOrthographicTopDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing model space UCS to TOP when PUCSBASE is set to WORLD

**Remarks:** System variable UCSORGTOP

### ModelSpaceUcs

```text
ACadSharp.Tables.UCS ModelSpaceUcs { get; }
```

### ModelSpaceUcsBase

```text
ACadSharp.Tables.UCS ModelSpaceUcsBase { get; }
```

### ModelSpaceXAxis

```text
CSMath.XYZ ModelSpaceXAxis { get; set; }
```

Direction of the current UCS X axis (in WCS)

**Remarks:** System variable UCSXDIR

### ModelSpaceYAxis

```text
CSMath.XYZ ModelSpaceYAxis { get; set; }
```

Direction of the current UCS Y axis (in WCS)

**Remarks:** System variable UCSYDIR

### NorthDirection

```text
System.Double NorthDirection { get; set; }
```

**Remarks:** System variable NORTHDIRECTION

### NumberOfSplineSegments

```text
System.Int16 NumberOfSplineSegments { get; set; }
```

Sets the number of line segments to be generated for each spline-fit polyline generated by the Spline option of the PEDIT command.

**Remarks:** System variable SPLINESEGS.

### ObjectSnapMode

```text
ACadSharp.Header.ObjectSnapMode ObjectSnapMode { get; set; }
```

Sets running object snaps.

**Remarks:** System variable OSMODE.

### ObscuredColor

```text
ACadSharp.Color ObscuredColor { get; set; }
```

### ObscuredType

```text
System.Byte ObscuredType { get; set; }
```

**Remarks:** System variable OBSCUREDLTYPE

### OrthoMode

```text
System.Boolean OrthoMode { get; set; }
```

Constrains cursor movement to the perpendicular.

**Remarks:** System variable ORTHOMODE.

### PaperSpaceBaseName

```text
System.String PaperSpaceBaseName { get; set; }
```

Name of the UCS that defines the origin and orientation of orthographic UCS settings (paper space only)

**Remarks:** System variable PUCSBASE

### PaperSpaceElevation

```text
System.Double PaperSpaceElevation { get; set; }
```

Current elevation set by ELEV command

**Remarks:** System variable PELEVATION

### PaperSpaceExtMax

```text
CSMath.XYZ PaperSpaceExtMax { get; set; }
```

X, Y, and Z drawing extents upper-right corner(in WCS).

**Remarks:** System variable PEXTMAX.

### PaperSpaceExtMin

```text
CSMath.XYZ PaperSpaceExtMin { get; set; }
```

X, Y, and Z drawing extents lower-left corner (in WCS).

**Remarks:** System variable PEXTMIN.

### PaperSpaceInsertionBase

```text
CSMath.XYZ PaperSpaceInsertionBase { get; set; }
```

Paper space insertion base point.

**Remarks:** System variable PINSBASE.

### PaperSpaceLimitsChecking

```text
System.Boolean PaperSpaceLimitsChecking { get; set; }
```

Limits checking in paper space when nonzero.

**Remarks:** System variable PLIMCHECK.

### PaperSpaceLimitsMax

```text
CSMath.XY PaperSpaceLimitsMax { get; set; }
```

XY drawing limits upper-right corner (in WCS).

**Remarks:** System variable PLIMMAX.

### PaperSpaceLimitsMin

```text
CSMath.XY PaperSpaceLimitsMin { get; set; }
```

XY drawing limits lower-left corner(in WCS).

**Remarks:** System variable PLIMMIN.

### PaperSpaceLineTypeScaling

```text
ACadSharp.Header.SpaceLineTypeScaling PaperSpaceLineTypeScaling { get; set; }
```

Controls paper space linetype scaling.

**Remarks:** System variable PSLTSCALE.

### PaperSpaceName

```text
System.String PaperSpaceName { get; set; }
```

Current paper space UCS name

**Remarks:** System variable PUCSNAME

### PaperSpaceOrthographicBackDOrigin

```text
CSMath.XYZ PaperSpaceOrthographicBackDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing paper space UCS to BACK when PUCSBASE is set to WORLD

**Remarks:** System variable PUCSORGBACK

### PaperSpaceOrthographicBottomDOrigin

```text
CSMath.XYZ PaperSpaceOrthographicBottomDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing paper space UCS to BOTTOM when PUCSBASE is set to WORLD

**Remarks:** System variable PUCSORGBOTTOM

### PaperSpaceOrthographicFrontDOrigin

```text
CSMath.XYZ PaperSpaceOrthographicFrontDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing paper space UCS to FRONT when PUCSBASE is set to WORLD

**Remarks:** System variable PUCSORGFRONT

### PaperSpaceOrthographicLeftDOrigin

```text
CSMath.XYZ PaperSpaceOrthographicLeftDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing paper space UCS to LEFT when PUCSBASE is set to WORLD

**Remarks:** System variable PUCSORGLEFT

### PaperSpaceOrthographicRightDOrigin

```text
CSMath.XYZ PaperSpaceOrthographicRightDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing paper space UCS to RIGHT when PUCSBASE is set to WORLD

**Remarks:** System variable PUCSORGRIGHT

### PaperSpaceOrthographicTopDOrigin

```text
CSMath.XYZ PaperSpaceOrthographicTopDOrigin { get; set; }
```

Point which becomes the new UCS origin after changing paper space UCS to TOP when PUCSBASE is set to WORLD

**Remarks:** System variable PUCSORGTOP

### PaperSpaceUcs

```text
ACadSharp.Tables.UCS PaperSpaceUcs { get; }
```

### PaperSpaceUcsBase

```text
ACadSharp.Tables.UCS PaperSpaceUcsBase { get; }
```

### PaperSpaceUcsOrigin

```text
CSMath.XYZ PaperSpaceUcsOrigin { get; set; }
```

Origin of current UCS (in WCS)

**Remarks:** System variable PUCSORG

### PaperSpaceUcsXAxis

```text
CSMath.XYZ PaperSpaceUcsXAxis { get; set; }
```

Direction of the current UCS X axis (in WCS)

**Remarks:** System variable PUCSXDIR

### PaperSpaceUcsYAxis

```text
CSMath.XYZ PaperSpaceUcsYAxis { get; set; }
```

Direction of the current UCS Y aYis (in WCS)

**Remarks:** System variable PUCSYDIR

### PlotStyleMode

```text
System.Int16 PlotStyleMode { get; set; }
```

Indicates whether the current drawing is in a Color-Dependent or Named Plot Style mode

**Remarks:** System variable PSTYLEMODE

### PointDisplayMode

```text
System.Int16 PointDisplayMode { get; set; }
```

Controls how point objects are displayed.

**Remarks:** System variable PDMODE.

### PointDisplaySize

```text
System.Double PointDisplaySize { get; set; }
```

Sets the display size for point objects.

**Remarks:** System variable PDSIZE.

### PolylineLineTypeGeneration

```text
System.Boolean PolylineLineTypeGeneration { get; set; }
```

Governs the generation of linetype patterns around the vertices of a 2D polyline: 1 = Linetype is generated in a continuous pattern around vertices of the polyline 0 = Each segment of the polyline starts and ends with a dash

**Remarks:** System variable PLINEGEN

### PolylineWidthDefault

```text
System.Double PolylineWidthDefault { get; set; }
```

Stores the default polyline width.

**Remarks:** System variable PLINEWID.

### ProjectName

```text
System.String ProjectName { get; set; }
```

Assigns a project name to the current drawing. Used when an external reference or image is not found on its original path. The project name points to a section in the registry that can contain one or more search paths for each project name defined. Project names and their search directories are created from the Files tab of the Options dialog box

**Remarks:** System variable PROJECTNAME

### ProxyGraphics

```text
System.Boolean ProxyGraphics { get; set; }
```

Specifies whether images of proxy objects are saved in the drawing.

**Remarks:** System variable PROXYGRAPHICS.

### QuickTextMode

```text
System.Boolean QuickTextMode { get; set; }
```

Quick Text mode on if nonzero

**Remarks:** System variable QTEXTMODE.

### RegenerationMode

```text
System.Boolean RegenerationMode { get; set; }
```

Obsolete. Controls automatic regeneration of the drawing.

**Remarks:** System variable REGENMODE.

### RequiredVersions

```text
System.Int64 RequiredVersions { get; set; }
```

The default value is 0. Read only.

**Remarks:** System variable REQUIREDVERSIONS Only in F:ACadSharp.ACadVersion.AC1024 or above

### RetainXRefDependentVisibilitySettings

```text
System.Boolean RetainXRefDependentVisibilitySettings { get; set; }
```

Controls the properties of xref-dependent layers: 0 = Don't retain xref-dependent visibility settings 1 = Retain xref-dependent visibility settings

**Remarks:** System variable VISRETAIN.

### ShadeDiffuseToAmbientPercentage

```text
System.Int16 ShadeDiffuseToAmbientPercentage { get; set; }
```

Sets the ratio of diffuse reflective light to ambient light.

**Remarks:** System variable SHADEDIF.

**Value:** range 1-100

### ShadeEdge

```text
ACadSharp.Header.ShadeEdgeType ShadeEdge { get; set; }
```

Controls the shading of edges.

**Remarks:** System variable SHADEDGE.

### ShadowMode

```text
ACadSharp.Header.ShadowMode ShadowMode { get; set; }
```

Shadow mode for a 3D object

**Remarks:** System variable CSHADOW

### ShadowPlaneLocation

```text
System.Double ShadowPlaneLocation { get; set; }
```

Location of the ground shadow plane. This is a Z axis ordinate

**Remarks:** System variable SHADOWPLANELOCATION

### ShowModelSpace

```text
System.Boolean ShowModelSpace { get; set; }
```

Determines whether the Model tab or the most-recently accessed named layout tab is active.

**Remarks:** System variable TILEMODE.

### ShowSolidsHistory

```text
System.Char ShowSolidsHistory { get; set; }
```

**Remarks:** System variable SHOWHIST

### ShowSplineControlPoints

```text
System.Boolean ShowSplineControlPoints { get; set; }
```

Controls the display of helixes and smoothed mesh objects.

**Remarks:** System variable SPLFRAME.

### SketchIncrement

```text
System.Double SketchIncrement { get; set; }
```

Sketch record increment.

**Remarks:** System variable SKETCHINC.

### SketchPolylines

```text
System.Boolean SketchPolylines { get; set; }
```

Determines the object type created by the SKETCH command.

**Remarks:** System variable SKPOLY.

### SolidLoftedShape

```text
System.Int16 SolidLoftedShape { get; set; }
```

**Remarks:** System variable LOFTPARAM

### SolidsRetainHistory

```text
System.Char SolidsRetainHistory { get; set; }
```

**Remarks:** System variable SOLIDHIST

### SpatialIndexMaxTreeDepth

```text
System.Int16 SpatialIndexMaxTreeDepth { get; set; }
```

Specifies the maximum depth, that is, the number of times the tree-structured spatial index can divide into branches.

**Remarks:** System variable TREEDEPTH.

### SplineType

```text
ACadSharp.Header.SplineType SplineType { get; set; }
```

Sets the type of curve generated by the Spline option of the PEDIT command.

**Remarks:** System variable SPLINETYPE.

### StackedTextAlignment

```text
System.Int16 StackedTextAlignment { get; }
```

**Remarks:** System variable TSTACKALIGN, default = 1(not present in DXF)

### StackedTextSizePercentage

```text
System.Int16 StackedTextSizePercentage { get; }
```

**Remarks:** TSTACKSIZE, default = 70(not present in DXF)

### StepSize

```text
System.Double StepSize { get; set; }
```

Specifies the size of each step when in walk or fly mode, in drawing units.

**Remarks:** System variable STEPSIZE

### StepsPerSecond

```text
System.Double StepsPerSecond { get; set; }
```

Specifies the number of steps taken per second when you are in walk or fly mode.

**Remarks:** System variable STEPSPERSEC

**Value:** Valid values are from 1 to 30.

### StyleSheetName

```text
System.String StyleSheetName { get; set; }
```

**Remarks:** System variable STYLESHEET

### SurfaceDensityU

```text
System.Int16 SurfaceDensityU { get; set; }
```

Surface density (for PEDIT Smooth) in M direction.

**Remarks:** System variable SURFU.

### SurfaceDensityV

```text
System.Int16 SurfaceDensityV { get; set; }
```

Surface density(for PEDIT Smooth) in N direction.

**Remarks:** System variable SURFV.

### SurfaceIsolineCount

```text
System.Int16 SurfaceIsolineCount { get; set; }
```

Specifies the number of contour lines displayed on the curved surfaces of 3D solids.

**Remarks:** System variable ISOLINES.

**Value:** Valid values are from 0 to 2047.

### SurfaceMeshTabulationCount1

```text
System.Int16 SurfaceMeshTabulationCount1 { get; set; }
```

Number of mesh tabulations in first direction.

**Remarks:** System variable SURFTAB1.

### SurfaceMeshTabulationCount2

```text
System.Int16 SurfaceMeshTabulationCount2 { get; set; }
```

Number of mesh tabulations in second direction.

**Remarks:** System variable SURFTAB2.

### SurfaceType

```text
System.Int16 SurfaceType { get; set; }
```

Surface type for PEDIT Smooth.

**Remarks:** System variable SURFTYPE.

### SweptSolidHeight

```text
System.Double SweptSolidHeight { get; set; }
```

**Remarks:** System variable PSOLHEIGHT

### SweptSolidWidth

```text
System.Double SweptSolidWidth { get; set; }
```

**Remarks:** System variable PSOLWIDTH

### TextHeightDefault

```text
System.Double TextHeightDefault { get; set; }
```

Sets the default text height when creating new text objects.

**Remarks:** System variable TEXTSIZE.

### TextQuality

```text
System.Int16 TextQuality { get; set; }
```

Sets the resolution of TrueType text for plotting and rendering.

**Remarks:** System variable TEXTQLTY.

**Value:** Valid values are from 1 to 100.

### ThicknessDefault

```text
System.Double ThicknessDefault { get; set; }
```

Sets the default 3D thickness property when creating 2D geometric objects.

**Remarks:** System variable THICKNESS.

### TimeZone

```text
System.Int32 TimeZone { get; set; }
```

Sets the time zone for the sun in the drawing.

**Remarks:** The values in the table are expressed as hours and minutes away from Greenwich Mean Time. You can also change this value in the Geographic Location dialog box when you set or edit geographic location information for the drawing file. System variable TIMEZONE

### TotalEditingTime

```text
System.TimeSpan TotalEditingTime { get; set; }
```

Cumulative editing time for this drawing(see Special Handling of Date/Time Variables)

**Remarks:** System variable TDINDWG

### TraceWidthDefault

```text
System.Double TraceWidthDefault { get; set; }
```

Default trace width.

**Remarks:** System variable TRACEWID.

### UcsBaseName

```text
System.String UcsBaseName { get; set; }
```

Name of the UCS that defines the origin and orientation of orthographic UCS settings

**Remarks:** System variable UCSBASE

### UcsName

```text
System.String UcsName { get; set; }
```

Name of current UCS

**Remarks:** System variable UCSNAME

### UnitMode

```text
System.Int16 UnitMode { get; set; }
```

Controls the display format for units.

**Remarks:** System variable UNITMODE.

### UniversalCreateDateTime

```text
System.DateTime UniversalCreateDateTime { get; set; }
```

Universal date/time the drawing was created(see Special Handling of Date/Time Variables).

**Remarks:** System variable TDUCREATE.

### UniversalUpdateDateTime

```text
System.DateTime UniversalUpdateDateTime { get; set; }
```

Universal date/time of the last update/save(see Special Handling of Date/Time Variables).

**Remarks:** System variable TDUUPDATE.

### UpdateDateTime

```text
System.DateTime UpdateDateTime { get; set; }
```

Local date/time of last drawing update(see Special Handling of Date/Time Variables).

**Remarks:** System variable TDUPDATE.

### UpdateDimensionsWhileDragging

```text
System.Boolean UpdateDimensionsWhileDragging { get; set; }
```

System variable DIMSHO

### UserDouble1

```text
System.Double UserDouble1 { get; set; }
```

Real variable intended for use by third-party developers.

**Remarks:** System variable USERR1.

### UserDouble2

```text
System.Double UserDouble2 { get; set; }
```

Real variable intended for use by third-party developers.

**Remarks:** System variable USERR2.

### UserDouble3

```text
System.Double UserDouble3 { get; set; }
```

Real variable intended for use by third-party developers.

**Remarks:** System variable USERR3.

### UserDouble4

```text
System.Double UserDouble4 { get; set; }
```

Real variable intended for use by third-party developers.

**Remarks:** System variable USERR4.

### UserDouble5

```text
System.Double UserDouble5 { get; set; }
```

Real variable intended for use by third-party developers.

**Remarks:** System variable USERR5.

### UserElapsedTimeSpan

```text
System.TimeSpan UserElapsedTimeSpan { get; set; }
```

User-elapsed timer

**Remarks:** System variable TDUSRTIMER

### UserShort1

```text
System.Int16 UserShort1 { get; set; }
```

Integer variable intended for use by third-party developers.

**Remarks:** System variable USERI1.

### UserShort2

```text
System.Int16 UserShort2 { get; set; }
```

Integer variable intended for use by third-party developers.

**Remarks:** System variable USERI2.

### UserShort3

```text
System.Int16 UserShort3 { get; set; }
```

Integer variable intended for use by third-party developers.

**Remarks:** System variable USERI3.

### UserShort4

```text
System.Int16 UserShort4 { get; set; }
```

Integer variable intended for use by third-party developers.

**Remarks:** System variable USERI4.

### UserShort5

```text
System.Int16 UserShort5 { get; set; }
```

Integer variable intended for use by third-party developers.

**Remarks:** System variable USERI5.

### UserTimer

```text
System.Boolean UserTimer { get; set; }
```

Controls the user timer for the drawing.

**Remarks:** System variable USRTIMER.

### Version

```text
ACadSharp.ACadVersion Version { get; set; }
```

### VersionGuid

```text
System.String VersionGuid { get; }
```

Uniquely identifies a particular version of a drawing. Updated when the drawing is modified

**Remarks:** System variable VERSIONGUID

### VersionString

```text
System.String VersionString { get; set; }
```

The Drawing database version number.

**Remarks:** System variable ACADVER.

### ViewportDefaultViewScaleFactor

```text
System.Double ViewportDefaultViewScaleFactor { get; set; }
```

View scale factor for new viewports.

**Remarks:** System variable PSVPSCALE.

### WorldView

```text
System.Boolean WorldView { get; set; }
```

Determines whether input to the DVIEW and VPOINT commands is relative to the WCS (default) or the current UCS.

**Remarks:** System variable WORLDVIEW.

### XEdit

```text
System.Boolean XEdit { get; set; }
```

Controls whether the current drawing can be edited in-place when being referenced by another drawing

**Remarks:** System variable XEDIT
