# ACadSharp.Entities.Entity

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Entity`

The standard class for a basic CAD entity or a graphical object.

Base type: `ACadSharp.CadObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Entity')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Entity()
```

Documentation inherited from: `base member`.

### ApplyRotation

```text
System.Void ApplyRotation(CSMath.XYZ axis, System.Double rotation)
```

Apply a rotation to this entity.

- `axis`: 
- `rotation`: The angle to rotate around the given axis, in radians.

### ApplyScaling

```text
System.Void ApplyScaling(CSMath.XYZ scale)
```

Apply a scaling transformation to this entity.

- `scale`: 

### ApplyScaling

```text
System.Void ApplyScaling(CSMath.XYZ scale, CSMath.XYZ origin)
```

Apply a scaling transformation to this entity.

- `scale`: 
- `origin`: 

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### ApplyTranslation

```text
System.Void ApplyTranslation(CSMath.XYZ translation)
```

Apply a translation to this entity.

- `translation`: 

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetActiveColor

```text
ACadSharp.Color GetActiveColor()
```

Documentation inherited from: `base member`.

### GetActiveLineType

```text
ACadSharp.Tables.LineType GetActiveLineType()
```

Documentation inherited from: `base member`.

### GetActiveLineWeightType

```text
ACadSharp.LineWeightType GetActiveLineWeightType()
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### MatchProperties

```text
System.Void MatchProperties(ACadSharp.Entities.IEntity entity)
```

Documentation inherited from: `base member`.

### BookColor

```text
ACadSharp.Objects.BookColor BookColor { get; set; }
```

Book color for this entity.

### Color

```text
ACadSharp.Color Color { get; set; }
```

Documentation inherited from: `base member`.

### IsInvisible

```text
System.Boolean IsInvisible { get; set; }
```

Documentation inherited from: `base member`.

### Layer

```text
ACadSharp.Tables.Layer Layer { get; set; }
```

Documentation inherited from: `base member`.

### LineType

```text
ACadSharp.Tables.LineType LineType { get; set; }
```

Documentation inherited from: `base member`.

### LineTypeScale

```text
System.Double LineTypeScale { get; set; }
```

Documentation inherited from: `base member`.

### LineWeight

```text
ACadSharp.LineWeightType LineWeight { get; set; }
```

Documentation inherited from: `base member`.

### Material

```text
ACadSharp.Objects.Material Material { get; set; }
```

Documentation inherited from: `base member`.

### ProxyGeometries

```text
System.Collections.Generic.List[ACadSharp.Entities.ProxyGraphics.IProxyGeometry] ProxyGeometries { get; }
```

Gets the list of proxy geometries for this entity.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Transparency

```text
ACadSharp.Transparency Transparency { get; set; }
```

Documentation inherited from: `base member`.
