# ACadSharp.Entities.ProxyGraphics.ProxyXLine

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyXLine`

Represents a proxy geometry element for an infinite line (X-line) in CAD graphics.

An X-line is a geometric element that extends infinitely in both directions along the line defined by two points. This class implements the ACadSharp.Entities.ProxyGraphics.IProxyGeometry interface for graphics rendering purposes.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyXLine')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyXLine()
```

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Point1

```text
CSMath.XYZ Point1 { get; set; }
```

Gets or sets the first point that defines the position and direction of the X-line.

**Remarks:** Combined with CSMath.XYZ, this point defines the infinite line direction.

### Point2

```text
CSMath.XYZ Point2 { get; set; }
```

Gets or sets the second point that defines the position and direction of the X-line.

**Remarks:** Combined with CSMath.XYZ, this point defines the infinite line direction.
