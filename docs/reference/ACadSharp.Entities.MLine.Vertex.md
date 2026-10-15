# ACadSharp.Entities.MLine.Vertex

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.MLine+Vertex`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.MLine+Vertex')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.MLine.Vertex()
```

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.Entities.MLine.Vertex Clone()
```

Documentation inherited from: `base member`.

### Direction

```text
CSMath.XYZ Direction { get; set; }
```

Direction vector of segment starting at this vertex

### Miter

```text
CSMath.XYZ Miter { get; set; }
```

Direction vector of miter at this vertex

### Position

```text
CSMath.XYZ Position { get; set; }
```

Vertex coordinates

### Segments

```text
System.Collections.Generic.List[ACadSharp.Entities.MLine.Vertex.Segment] Segments { get; set; }
```

Segments in MLineStyle definition
