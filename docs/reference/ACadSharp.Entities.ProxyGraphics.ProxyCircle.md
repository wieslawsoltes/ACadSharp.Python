# ACadSharp.Entities.ProxyGraphics.ProxyCircle

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyCircle`

Represents a proxy circle geometry entity.

A proxy circle is a graphical representation of a circle defined by its center point, radius, and normal vector. It implements the ACadSharp.Entities.ProxyGraphics.IProxyGeometry interface to provide geometry information for proxy graphics objects.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyCircle')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyCircle()
```

### Center

```text
CSMath.XYZ Center { get; set; }
```

Gets or sets the center point of the circle in 3D space.

**Value:** An CSMath.XYZ coordinate representing the center of the circle.

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.

### Radius

```text
System.Double Radius { get; set; }
```

Gets or sets the radius of the circle.

**Value:** A double value representing the distance from the center to the circle's edge. Must be a positive value.
