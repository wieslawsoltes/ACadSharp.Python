# ACadSharp.Entities.LwPolyline.Vertex

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.LwPolyline+Vertex`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IVertex`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.LwPolyline+Vertex')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.LwPolyline.Vertex()
```

### .ctor

```text
ACadSharp.Entities.LwPolyline.Vertex(CSMath.XY location)
```

### .ctor

```text
ACadSharp.Entities.LwPolyline.Vertex(System.Double x, System.Double y)
```

### Clone

```text
ACadSharp.Entities.LwPolyline.Vertex Clone()
```

Documentation inherited from: `base member`.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Bulge

```text
System.Double Bulge { get; set; }
```

The bulge is the tangent of one fourth the included angle for an arc segment, made negative if the arc goes clockwise from the start point to the endpoint.A bulge of 0 indicates a straight segment, and a bulge of 1 is a semicircle

### CurveTangent

```text
System.Double CurveTangent { get; set; }
```

Curve fit tangent direction

### EndWidth

```text
System.Double EndWidth { get; set; }
```

Ending width

### Flags

```text
ACadSharp.Entities.VertexFlags Flags { get; set; }
```

Vertex flags

### Id

```text
System.Int32 Id { get; set; }
```

Vertex identifier

### Location

```text
CSMath.XY Location { get; set; }
```

Vertex coordinates (in OCS)

### StartWidth

```text
System.Double StartWidth { get; set; }
```

Starting width
