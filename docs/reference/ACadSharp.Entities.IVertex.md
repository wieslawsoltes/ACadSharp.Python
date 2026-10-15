# ACadSharp.Entities.IVertex

`interface` · `ACadSharp` · CLR name: `ACadSharp.Entities.IVertex`

No upstream type summary is available.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.IVertex')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Bulge

```text
System.Double Bulge { get; set; }
```

The bulge is the tangent of one fourth the included angle for an arc segment, made negative if the arc goes clockwise from the start point to the endpoint.A bulge of 0 indicates a straight segment, and a bulge of 1 is a semicircle

### Location

```text
CSMath.IVector Location { get; set; }
```

Location point (in OCS when 2D, and WCS when 3D)
