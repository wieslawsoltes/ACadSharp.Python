# ACadSharp.Entities.ProxyGraphics.TrueTypeFontDescriptor

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.TrueTypeFontDescriptor`

Represents a descriptor for TrueType font properties used in proxy graphics.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.TrueTypeFontDescriptor')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.TrueTypeFontDescriptor()
```

### Charset

```text
System.Byte Charset { get; set; }
```

Gets or sets the character set for the font.

### FontFilename

```text
System.String FontFilename { get; set; }
```

Gets or sets the filename or path of the TrueType font file.

### IsBold

```text
System.Boolean IsBold { get; set; }
```

Gets or sets a value indicating whether the font is bold.

### IsItalic

```text
System.Boolean IsItalic { get; set; }
```

Gets or sets a value indicating whether the font is italic.

### PitchAndFamily

```text
System.Byte PitchAndFamily { get; set; }
```

Gets or sets the pitch and family information for the font.

### Typeface

```text
System.String Typeface { get; set; }
```

Gets or sets the typeface name of the font.
