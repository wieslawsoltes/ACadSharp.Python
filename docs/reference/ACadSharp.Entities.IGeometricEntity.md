# ACadSharp.Entities.IGeometricEntity

`interface` · `ACadSharp` · CLR name: `ACadSharp.Entities.IGeometricEntity`

Objects with geometric properties that can be processed in a drawing.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.IGeometricEntity')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Apply a transform matrix to this entity.

- `transform`: 

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Gets the bounding box aligned with the axis XYZ that occupies this entity.

**Returns:** The bounding box where this entity resides.
