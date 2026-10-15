# ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText2

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText2`

Represents proxy graphics for Unicode text rendering in AutoCAD graphics. This class encapsulates all properties necessary to render and transform Unicode text geometry, including font information, styling attributes, positioning, and text-specific transformations.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText2')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText2()
```

### BigFontFilename

```text
System.String BigFontFilename { get; set; }
```

Gets or sets the filename of the big font file used for rendering the text.

### FontDescriptor

```text
ACadSharp.Entities.ProxyGraphics.TrueTypeFontDescriptor FontDescriptor { get; set; }
```

Gets or sets the TrueType font descriptor that defines the font characteristics for text rendering.

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Height

```text
System.Double Height { get; set; }
```

Gets or sets the height of the text in drawing units.

### IsBackwards

```text
System.Boolean IsBackwards { get; set; }
```

Gets or sets a value indicating whether the text is displayed backwards (mirrored horizontally).

### IsOverlined

```text
System.Boolean IsOverlined { get; set; }
```

Gets or sets a value indicating whether the text is displayed with an overline.

### IsRaw

```text
System.Boolean IsRaw { get; set; }
```

Gets or sets a value indicating whether special text patterns (e.g., %%, %%p, %%c) are interpreted as formatting codes. If true, special patterns are not interpreted and are rendered as literal text.

### IsUnderlined

```text
System.Boolean IsUnderlined { get; set; }
```

Gets or sets a value indicating whether the text is displayed with an underline.

### IsUpsideDown

```text
System.Boolean IsUpsideDown { get; set; }
```

Gets or sets a value indicating whether the text is displayed upside down (rotated 180 degrees).

### IsVertical

```text
System.Boolean IsVertical { get; set; }
```

Gets or sets a value indicating whether the text is oriented vertically.

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.

### ObliqueAngle

```text
System.Double ObliqueAngle { get; set; }
```

Gets or sets the oblique angle in degrees, creating an italic-like slant effect on the text.

### StartPoint

```text
CSMath.XYZ StartPoint { get; set; }
```

Gets or sets the starting point (insertion point) of the text in drawing coordinates.

### Text

```text
System.String Text { get; set; }
```

Gets or sets the text string to be rendered.

### TextDirection

```text
CSMath.XYZ TextDirection { get; set; }
```

Gets or sets the direction vector in which the text flows, defining the text's horizontal orientation.

### TextLength

```text
System.Int32 TextLength { get; set; }
```

Gets or sets the length of the text in characters. A value of -1 indicates the text is zero-terminated.

### TrackingPercentage

```text
System.Double TrackingPercentage { get; set; }
```

Gets or sets the tracking percentage, which controls the spacing between characters as a percentage of the text height.

### WidthFactor

```text
System.Double WidthFactor { get; set; }
```

Gets or sets the width factor that scales the text horizontally. A value of 1.0 represents normal width.
