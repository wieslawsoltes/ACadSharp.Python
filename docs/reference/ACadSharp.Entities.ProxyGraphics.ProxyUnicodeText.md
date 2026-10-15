# ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText`

Represents Unicode text as a proxy graphics entity.

This class is used to store and manage the properties of Unicode text within proxy graphics, including positioning, orientation, sizing, and the actual text content.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText()
```

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Height

```text
System.Double Height { get; set; }
```

Gets or sets the height of the text.

**Value:** The text height as a double value.

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.

### ObliqueAngle

```text
System.Double ObliqueAngle { get; set; }
```

Gets or sets the oblique angle of the text in radians.

**Value:** The oblique angle as a double value.

### StartPoint

```text
CSMath.XYZ StartPoint { get; set; }
```

Gets or sets the starting point of the text.

**Value:** An CSMath.XYZ point representing the text's starting position.

### Text

```text
System.String Text { get; set; }
```

Gets or sets the text content.

**Value:** A string containing the Unicode text.

### TextDirection

```text
CSMath.XYZ TextDirection { get; set; }
```

Gets or sets the text direction vector.

**Value:** An CSMath.XYZ vector representing the direction of the text.

### WidthFactor

```text
System.Double WidthFactor { get; set; }
```

Gets or sets the width factor of the text.

**Value:** The width factor as a double value, where 1.0 is normal width.
