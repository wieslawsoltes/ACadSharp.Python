# ACadSharp.Entities.ProxyGraphics.ProxyText

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyText`

Represents proxy graphics for a text entity.

This class implements the ACadSharp.Entities.ProxyGraphics.IProxyGeometry interface to provide geometric information for text objects in a proxy graphics representation.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyText')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyText()
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

### StartPoint

```text
CSMath.XYZ StartPoint { get; set; }
```

Gets or sets the starting point of the text.

### Text

```text
System.String Text { get; set; }
```

Gets or sets the text string content.

### TextDirection

```text
CSMath.XYZ TextDirection { get; set; }
```

Gets or sets the direction vector of the text.

### WidthFactor

```text
System.Double WidthFactor { get; set; }
```

Gets or sets the width factor of the text.
