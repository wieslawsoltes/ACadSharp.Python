# ACadSharp.Entities.ProxyGraphics.ProxyCircularArc

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyCircularArc`

Represents a proxy circular arc graphic element.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyCircularArc')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyCircularArc()
```

### ArcType

```text
System.Int32 ArcType { get; set; }
```

Gets or sets the type of the arc.

### Center

```text
CSMath.XYZ Center { get; set; }
```

Gets or sets the center point of the circular arc.

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

Gets or sets the radius of the circular arc.

### StartVectorDirection

```text
CSMath.XYZ StartVectorDirection { get; set; }
```

Gets or sets the direction vector from the center to the start point of the arc.

### SweepAngle

```text
System.Double SweepAngle { get; set; }
```

Gets or sets the sweep angle of the arc in radians.
