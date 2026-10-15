# CSMath.Transform

`class` · `ACadSharp` · CLR name: `CSMath.Transform`

Contains the information for translate/scale/rotation or transform matrix to apply to a geometric shape.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Transform')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.Transform()
```

Default constructor.

### .ctor

```text
CSMath.Transform(CSMath.Matrix4 matrix)
```

Initialize a transform instance with the specified matrix.

- `matrix`: 

### .ctor

```text
CSMath.Transform(CSMath.XYZ translation, CSMath.XYZ scale, CSMath.XYZ rotation)
```

Initialize a transform instance with the specified values.

- `translation`: 
- `scale`: 
- `rotation`: Rotation value in degrees.

### ApplyRotation

```text
CSMath.XYZ ApplyRotation(CSMath.XYZ xyz)
```

### ApplyScale

```text
CSMath.XYZ ApplyScale(CSMath.XYZ xyz)
```

### ApplyTransform

```text
CSMath.XYZ ApplyTransform(CSMath.XYZ xyz, System.Boolean roundZero = True)
```

Apply transform to a CSMath.XYZ.

- `xyz`: 
- `roundZero`: 

### ApplyTranslation

```text
CSMath.XYZ ApplyTranslation(CSMath.XYZ xyz)
```

### CreateRotation

```text
static CSMath.Transform CreateRotation(CSMath.XYZ angles)
```

### CreateRotation

```text
static CSMath.Transform CreateRotation(CSMath.XYZ axis, System.Double angle)
```

### CreateScaling

```text
static CSMath.Transform CreateScaling(CSMath.XYZ scale)
```

### CreateScaling

```text
static CSMath.Transform CreateScaling(CSMath.XYZ scale, CSMath.XYZ origin)
```

### CreateTranslation

```text
static CSMath.Transform CreateTranslation(CSMath.XYZ translation)
```

### TryDecompose

```text
System.Boolean TryDecompose(out CSMath.XYZ translation, out CSMath.XYZ scaling, out CSMath.Quaternion rotation)
```

Try to decompose the transform into it's components.

**Returns:** true, if the decompose has succeeded.

- `translation`: 
- `scaling`: 
- `rotation`: 

### EulerRotation

```text
CSMath.XYZ EulerRotation { get; set; }
```

Rotation in Euler angles, the value is in radians.

### Matrix

```text
CSMath.Matrix4 Matrix { get; }
```

Transform matrix.

### Quaternion

```text
CSMath.Quaternion Quaternion { get; }
```

Rotation represented in quaternion form.

### Scale

```text
CSMath.XYZ Scale { get; set; }
```

Scale applied in the transformation.

### Translation

```text
CSMath.XYZ Translation { get; set; }
```

Rotation in Euler angles, the value is in radians.
