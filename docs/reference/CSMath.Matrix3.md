# CSMath.Matrix3

`struct` · `ACadSharp` · CLR name: `CSMath.Matrix3`

No upstream type summary is available.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Matrix3')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.Matrix3(CSMath.Matrix4 matrix)
```

### .ctor

```text
CSMath.Matrix3(System.Double m00, System.Double m10, System.Double m20, System.Double m01, System.Double m11, System.Double m21, System.Double m02, System.Double m12, System.Double m22)
```

### Identity

```text
static CSMath.Matrix3 Identity
```

4-dimensional identity matrix.

### M00

```text
System.Double M00
```

Value at column 0, row 0 of the matrix.

### M01

```text
System.Double M01
```

Value at column 0, row 1 of the matrix.

### M02

```text
System.Double M02
```

Value at column 0, row 2 of the matrix.

### M10

```text
System.Double M10
```

Value at column 1, row 0 of the matrix.

### M11

```text
System.Double M11
```

Value at column 1, row 1 of the matrix.

### M12

```text
System.Double M12
```

Value at column 1, row 2 of the matrix.

### M20

```text
System.Double M20
```

Value at column 2, row 0 of the matrix.

### M21

```text
System.Double M21
```

Value at column 2, row 1 of the matrix.

### M22

```text
System.Double M22
```

Value at column 2, row 2 of the matrix.

### Zero

```text
static CSMath.Matrix3 Zero
```

4-dimensional zero matrix.

### ArbitraryAxis

```text
static CSMath.Matrix3 ArbitraryAxis(CSMath.XYZ zAxis)
```

Gets the rotation matrix from the normal vector (extrusion direction) of an entity.

**Returns:** Rotation matrix.

- `zAxis`: Normal vector.

### RotationZ

```text
static CSMath.Matrix3 RotationZ(System.Double angle)
```

Builds a rotation matrix for a rotation around the z-axis.

**Remarks:** Matrix3 adopts the convention of using column vectors to represent a transformation matrix.

**Returns:** The resulting Matrix3 instance.

- `angle`: The counter-clockwise angle in radians.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Transpose

```text
CSMath.Matrix3 Transpose()
```

Obtains the transpose matrix.

**Returns:** Transpose matrix.

### op_Multiply

```text
static CSMath.Matrix3 op_Multiply(CSMath.Matrix3 a, CSMath.Matrix3 b)
```

### op_Multiply

```text
static CSMath.XYZ op_Multiply(CSMath.Matrix3 matrix, CSMath.XYZ value)
```

### Item

```text
System.Double Item[System.Int32 column, System.Int32 row] { get; set; }
```

### Item

```text
System.Double Item[System.Int32 index] { get; set; }
```
