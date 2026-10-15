# ACadSharp.Objects.PlotSettings

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.PlotSettings`

Represents a ACadSharp.Objects.PlotSettings object

Object name F:ACadSharp.DxfFileToken.ObjectPlotSettings Dxf class name F:ACadSharp.DxfSubclassMarker.PlotSettings

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.PlotSettings')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.PlotSettings()
```

### .ctor

```text
ACadSharp.Objects.PlotSettings(System.String name)
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### DenominatorScale

```text
System.Double DenominatorScale { get; set; }
```

Denominator of custom print scale: drawing units

### Flags

```text
ACadSharp.Objects.PlotFlags Flags { get; set; }
```

Plot layout flags

### NumeratorScale

```text
System.Double NumeratorScale { get; set; }
```

Numerator of custom print scale: real world(paper) units

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

### PageName

```text
System.String PageName { get; set; }
```

Page Setup name

### PaperHeight

```text
System.Double PaperHeight { get; set; }
```

Physical paper height in millimeters.

### PaperImageOrigin

```text
CSMath.XY PaperImageOrigin { get; set; }
```

Paper image origin

### PaperImageOriginX

```text
System.Double PaperImageOriginX { get; set; }
```

Paper image origin: X value

### PaperImageOriginY

```text
System.Double PaperImageOriginY { get; set; }
```

Paper image origin: Y value

### PaperRotation

```text
ACadSharp.Objects.PlotRotation PaperRotation { get; set; }
```

Plot paper rotation.

### PaperSize

```text
System.String PaperSize { get; set; }
```

Paper size

### PaperUnits

```text
ACadSharp.Objects.PlotPaperUnits PaperUnits { get; set; }
```

Plot paper units.

### PaperWidth

```text
System.Double PaperWidth { get; set; }
```

Physical paper width in millimeters.

### PlotOriginX

```text
System.Double PlotOriginX { get; set; }
```

Plot origin: X value of origin offset in millimeters

### PlotOriginY

```text
System.Double PlotOriginY { get; set; }
```

Plot origin: Y value of origin offset in millimeters

### PlotType

```text
ACadSharp.Objects.PlotType PlotType { get; set; }
```

Portion of paper space to output to the media

### PlotViewName

```text
System.String PlotViewName { get; set; }
```

Plot view name

### PrintScale

```text
System.Double PrintScale { get; }
```

Gets the scale factor.

### ScaledFit

```text
ACadSharp.Objects.ScaledType ScaledFit { get; set; }
```

Standard scale type

### ShadePlotDPI

```text
System.Int16 ShadePlotDPI { get; set; }
```

Shade plot custom DPI.

**Remarks:** Only applied when the ShadePlot resolution level is set to 5 (Custom)

**Value:** Valid shade plot DPI values range from 100 to 23767.

### ShadePlotIDHandle

```text
System.UInt64 ShadePlotIDHandle { get; set; }
```

ShadePlot ID/Handle(optional)

### ShadePlotMode

```text
ACadSharp.Objects.ShadePlotMode ShadePlotMode { get; set; }
```

Plot shade mode.

### ShadePlotResolutionMode

```text
ACadSharp.Objects.ShadePlotResolutionMode ShadePlotResolutionMode { get; set; }
```

Plot resolution.

### StandardScale

```text
System.Double StandardScale { get; set; }
```

A floating point scale factor that represents the standard scale value specified in code 75.

### StyleSheet

```text
System.String StyleSheet { get; set; }
```

Current style sheet

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### SystemPrinterName

```text
System.String SystemPrinterName { get; set; }
```

Name of system printer or plot configuration file

### UnprintableMargin

```text
ACadSharp.Objects.PaperMargin UnprintableMargin { get; set; }
```

Size, in millimeters, of unprintable margins of paper

### WindowLowerLeftX

```text
System.Double WindowLowerLeftX { get; set; }
```

Plot window area: X value of lower-left window corner

### WindowLowerLeftY

```text
System.Double WindowLowerLeftY { get; set; }
```

Plot window area: Y value of upper-right window corner

### WindowUpperLeftX

```text
System.Double WindowUpperLeftX { get; set; }
```

Plot window area: X value of lower-left window corner

### WindowUpperLeftY

```text
System.Double WindowUpperLeftY { get; set; }
```

Plot window area: Y value of upper-right window corner
