# ACadSharp.Entities.HatchPattern.Line

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.HatchPattern+Line`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.HatchPattern+Line')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.HatchPattern.Line()
```

### Clone

```text
ACadSharp.Entities.HatchPattern.Line Clone()
```

Clones this line.

### ToLine2D

```text
CSMath.Geometry.Line2D ToLine2D()
```

### Angle

```text
System.Double Angle { get; set; }
```

Pattern line angle.

### BasePoint

```text
CSMath.XY BasePoint { get; set; }
```

Pattern line base point.

### DashLengths

```text
System.Collections.Generic.List[System.Double] DashLengths { get; set; }
```

Gets or sets the dash lengths of the pattern line. A negative value represents a space, zero a dot, and a positive value a line segment.

### Direction

```text
CSMath.XY Direction { get; }
```

Gets the direction vector of the pattern line based on the specified angle.

### LineOffset

```text
System.Double LineOffset { get; }
```

Perpendicular distance for the next line to be located.

### Offset

```text
CSMath.XY Offset { get; set; }
```

Gets or sets the local displacements between lines of the same family.

### Shift

```text
System.Double Shift { get; }
```

Gets the horizontal shift of the offset after applying the specified angle transformation.
