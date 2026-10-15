# CSMath.Quaternion

`struct` · `ACadSharp` · CLR name: `CSMath.Quaternion`

Four dimensional vector which is used to efficiently rotate an object about the (x,y,z) vector by the angle theta, where w = cos(theta/2).

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

Interfaces: `CSMath.IVector`, `System.IEquatable[CSMath.Quaternion]`.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Quaternion')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.Quaternion(CSMath.XYZ vector, System.Double scalarPart)
```

Constructs a Quaternion from the given vector and rotation parts.

- `vector`: The vector part of the Quaternion.
- `scalarPart`: The rotation part of the Quaternion.

### .ctor

```text
CSMath.Quaternion(System.Double x, System.Double y, System.Double z, System.Double w)
```

Constructs a Quaternion from the given components.

- `x`: The X component of the Quaternion.
- `y`: The Y component of the Quaternion.
- `z`: The Z component of the Quaternion.
- `w`: The W component of the Quaternion.

### CreateFromRotationMatrix

```text
static CSMath.Quaternion CreateFromRotationMatrix(CSMath.Matrix4 matrix)
```

Creates a Quaternion from the given rotation matrix.

**Returns:** The created Quaternion.

- `matrix`: The rotation matrix.

### CreateFromYawPitchRoll

```text
static CSMath.Quaternion CreateFromYawPitchRoll(CSMath.XYZ xyz)
```

Creates a new Quaternion from the given yaw, pitch, and roll, in radians.

- `xyz`: X as pitch, Y as yaw and Z as roll

### CreateFromYawPitchRoll

```text
static CSMath.Quaternion CreateFromYawPitchRoll(System.Double pitch, System.Double yaw, System.Double roll)
```

Creates a new Quaternion from the given yaw, pitch, and roll, in radians.

**Remarks:** The values must be in radians

- `pitch`: The pitch angle, around the X-axis.
- `yaw`: The yaw angle, around the Y-axis.
- `roll`: The roll angle, around the Z-axis.

### Equals

```text
System.Boolean Equals(CSMath.Quaternion other)
```

Documentation inherited from: `base member`.

### Equals

```text
System.Boolean Equals(CSMath.Quaternion other, System.Int32 ndecimals)
```

Indicates whether the current object is equal to another object of the same type.

- `other`: 
- `ndecimals`: Number of decimals digits to be set as precision.

### FromAngleAxis

```text
static CSMath.Quaternion FromAngleAxis(System.Double rotation, CSMath.XYZ axis)
```

Creates a quaternion representing a rotation of a specified angle around a given axis.

**Remarks:** The axis parameter should be a unit vector to ensure the resulting quaternion represents a valid rotation. The method assumes a right-handed coordinate system.

**Returns:** A CSMath.Quaternion representing the rotation defined by the specified angle and axis.

- `rotation`: The rotation angle, in radians, to apply around the specified axis.
- `axis`: The axis of rotation, represented as an CSMath.XYZ vector. The vector should be normalized.

### FromRotation

```text
static CSMath.Quaternion FromRotation(CSMath.XYZ orig, CSMath.XYZ dest)
```

Creates a quaternion representing the shortest rotation that aligns the specified origin vector with the destination vector.

**Remarks:** If the origin and destination vectors are opposite, the method selects an arbitrary orthogonal axis for the rotation. Both input vectors should be normalized for accurate results.

**Returns:** A quaternion that rotates the origin vector to align with the destination vector.

- `orig`: The initial direction vector to be rotated. Must be a non-zero vector.
- `dest`: The target direction vector to align with. Must be a non-zero vector.

### ToEulerAngles

```text
CSMath.XYZ ToEulerAngles()
```

Get the Euler angles, in radians, for this quaternion.

### ToMatrix

```text
CSMath.Matrix4 ToMatrix()
```

Create a rotation matrix

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### op_Multiply

```text
static CSMath.XYZ op_Multiply(CSMath.Quaternion q, CSMath.XYZ v)
```

### Dimension

```text
System.UInt32 Dimension { get; }
```

Documentation inherited from: `base member`.

### Identity

```text
static CSMath.Quaternion Identity { get; }
```

Returns a Quaternion representing no rotation.

### Item

```text
System.Double Item[System.Int32 index] { get; set; }
```

Documentation inherited from: `base member`.

### W

```text
System.Double W { get; set; }
```

Specifies the rotation component of the Quaternion.

### X

```text
System.Double X { get; set; }
```

Specifies the X-value of the vector component of the Quaternion.

### Y

```text
System.Double Y { get; set; }
```

Specifies the Y-value of the vector component of the Quaternion.

### Z

```text
System.Double Z { get; set; }
```

Specifies the Z-value of the vector component of the Quaternion.
