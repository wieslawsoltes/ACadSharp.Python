# ACadSharp.Entities.IPolyline

`interface` · `ACadSharp` · CLR name: `ACadSharp.Entities.IPolyline`

No upstream type summary is available.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.IPolyline')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Elevation

```text
System.Double Elevation { get; set; }
```

The current elevation of the object.

### IsClosed

```text
System.Boolean IsClosed { get; set; }
```

Indicates that the polyline is closed.

### Thickness

```text
System.Double Thickness { get; set; }
```

Specifies the distance a 2D object is extruded above or below its elevation.

### Vertices

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.IVertex] Vertices { get; }
```

Vertices that form the Polyline.
