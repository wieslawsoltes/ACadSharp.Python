# ACadSharp.Entities.Hatch

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Hatch`

Represents a ACadSharp.Entities.Hatch entity.

Object name F:ACadSharp.DxfFileToken.EntityHatch Dxf class name F:ACadSharp.DxfSubclassMarker.Hatch

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Hatch')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Hatch()
```

Documentation inherited from: `base member`.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### Explode

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.Entity] Explode()
```

Explode the hatch edges into the equivalent entities.

**Returns:** A collection of entities representing the exploded hatch edges.

### ExplodePattern

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.Line] ExplodePattern()
```

Explode the hatch pattern into the equivalent entities.

**Returns:** A collection of entities representing the exploded hatch pattern.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### Elevation

```text
System.Double Elevation { get; set; }
```

The current elevation of the object.

### GradientColor

```text
ACadSharp.Entities.HatchGradientPattern GradientColor { get; set; }
```

Gradient color pattern, if exists.

### IsAssociative

```text
System.Boolean IsAssociative { get; set; }
```

Associativity flag.

### IsDouble

```text
System.Boolean IsDouble { get; set; }
```

Hatch pattern double flag (pattern fill only)

### IsSolid

```text
System.Boolean IsSolid { get; set; }
```

Solid fill flag

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.

### Paths

```text
System.Collections.Generic.List[ACadSharp.Entities.Hatch.BoundaryPath] Paths { get; set; }
```

Boundary paths (loops).

### Pattern

```text
ACadSharp.Entities.HatchPattern Pattern { get; set; }
```

Pattern of this hatch.

**Value:** Default value: SOLID pattern.

### PatternAngle

```text
System.Double PatternAngle { get; set; }
```

Hatch pattern angle (pattern fill only).

### PatternScale

```text
System.Double PatternScale { get; set; }
```

Hatch pattern scale or spacing(pattern fill only).

### PatternType

```text
ACadSharp.Entities.HatchPatternType PatternType { get; set; }
```

Hatch pattern type

### PixelSize

```text
System.Double PixelSize { get; set; }
```

Pixel size used to determine the density to perform various intersection and ray casting operations in hatch pattern computation for associative hatches and hatches created with the Flood method of hatching

### SeedPoints

```text
System.Collections.Generic.List[CSMath.XY] SeedPoints { get; set; }
```

Seed points codes (in OCS)

### Style

```text
ACadSharp.Entities.HatchStyleType Style { get; set; }
```

Hatch style.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
