# ACadSharp.Entities.ProxyGraphics.ProxyCircularArc3Pt

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.ProxyCircularArc3Pt`

Represents a proxy circular arc defined by three points in 3D space.

This class is used to store graphics representation data for a circular arc that is defined by three points. The arc type indicates the specific variation of the arc representation.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.ProxyGraphics.IProxyGeometry`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.ProxyCircularArc3Pt')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.ProxyCircularArc3Pt()
```

### ArcType

```text
System.Int32 ArcType { get; set; }
```

Gets or sets the arc type.

**Value:** An integer representing the type of arc.

### GraphicsType

```text
ACadSharp.Entities.ProxyGraphics.GraphicsType GraphicsType { get; }
```

Documentation inherited from: `base member`.

### Point1

```text
CSMath.XYZ Point1 { get; set; }
```

Gets or sets the first point of the circular arc in 3D space.

**Value:** An CSMath.XYZ coordinate representing the first point.

### Point2

```text
CSMath.XYZ Point2 { get; set; }
```

Gets or sets the second point of the circular arc in 3D space.

**Value:** An CSMath.XYZ coordinate representing the second point.

### Point3

```text
CSMath.XYZ Point3 { get; set; }
```

Gets or sets the third point of the circular arc in 3D space.

**Value:** An CSMath.XYZ coordinate representing the third point.
