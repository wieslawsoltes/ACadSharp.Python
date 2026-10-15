# ACadSharp.Objects.GeoData.GeoMeshPoint

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.GeoData+GeoMeshPoint`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.GeoData+GeoMeshPoint')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.GeoData.GeoMeshPoint()
```

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Destination

```text
CSMath.XY Destination { get; set; }
```

Coordinate of destination mesh point

### Source

```text
CSMath.XY Source { get; set; }
```

Coordinate of source mesh point.
