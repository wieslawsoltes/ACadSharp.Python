# ACadSharp.Entities.ProxyGraphics.ProxyText2

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyText2`

Represents text geometry information for proxy objects in AutoCAD drawings.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyText2')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyText2()
```

### BigFontFilename

```text
System.String BigFontFilename { get; set; }
```

Gets or sets the filename of the big font file used for the text.

### FontFilename

```text
System.String FontFilename { get; set; }
```

Gets or sets the filename of the font file used for the text.

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

Gets or sets a value indicating whether the text is overlined.

### IsRaw

```text
System.Boolean IsRaw { get; set; }
```

Gets or sets a value indicating whether special patterns (e.g., %%) are not supposed to be interpreted.

### IsUnderlined

```text
System.Boolean IsUnderlined { get; set; }
```

Gets or sets a value indicating whether the text is underlined.

### IsUpsideDown

```text
System.Boolean IsUpsideDown { get; set; }
```

Gets or sets a value indicating whether the text is displayed upside down (rotated 180 degrees).

### IsVertical

```text
System.Boolean IsVertical { get; set; }
```

Gets or sets a value indicating whether the text is displayed vertically.

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Gets or sets the normal vector of the text plane.

### ObliqueAngle

```text
System.Double ObliqueAngle { get; set; }
```

Gets or sets the oblique angle of the text in degrees.

### StartPoint

```text
CSMath.XYZ StartPoint { get; set; }
```

Gets or sets the starting point of the text in world coordinates.

### Text

```text
System.String Text { get; set; }
```

Gets or sets the text content to be displayed.

### TextDirection

```text
CSMath.XYZ TextDirection { get; set; }
```

Gets or sets the direction vector of the text along the baseline.

### TextLength

```text
System.Int32 TextLength { get; set; }
```

Gets or sets the length of the text in characters, or -1 if the text is zero terminated.

### TrackingPercentage

```text
System.Double TrackingPercentage { get; set; }
```

Gets or sets the tracking percentage, which controls the spacing between characters.

### WidthFactor

```text
System.Double WidthFactor { get; set; }
```

Gets or sets the width factor that scales the text horizontally.
