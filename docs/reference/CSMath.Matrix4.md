# CSMath.Matrix4

`struct` · `ACadSharp` · CLR name: `CSMath.Matrix4`

4x4 Matrix

Matrix organization: |m00|m10|m20|m30| |m01|m11|m21|m31| |m02|m12|m22|m32| |m03|m13|m23|m33|

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Matrix4')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.Matrix4(System.Double m00, System.Double m10, System.Double m20, System.Double m30, System.Double m01, System.Double m11, System.Double m21, System.Double m31, System.Double m02, System.Double m12, System.Double m22, System.Double m32, System.Double m03, System.Double m13, System.Double m23, System.Double m33)
```

### .ctor

```text
CSMath.Matrix4(System.Double[] elements)
```

### Identity

```text
static CSMath.Matrix4 Identity
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

### M03

```text
System.Double M03
```

Value at column 0, row 3 of the matrix.

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

### M13

```text
System.Double M13
```

Value at column 1, row 3 of the matrix.

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

### M23

```text
System.Double M23
```

Value at column 2, row 3 of the matrix.

### M30

```text
System.Double M30
```

Value at column 3, row 0 of the matrix.

### M31

```text
System.Double M31
```

Value at column 3, row 1 of the matrix.

### M32

```text
System.Double M32
```

Value at column 3, row 2 of the matrix.

### M33

```text
System.Double M33
```

Value at column 3, row 3 of the matrix.

### Zero

```text
static CSMath.Matrix4 Zero
```

4-dimensional zero matrix.

### CreateFromAxisAngle

```text
static CSMath.Matrix4 CreateFromAxisAngle(CSMath.XYZ axis, System.Double angle)
```

Creates a matrix that rotates around an arbitrary vector.

**Returns:** The rotation matrix.

- `axis`: The axis to rotate around.
- `angle`: The angle to rotate around the given axis, in radians.

### CreateFromQuaternion

```text
static CSMath.Matrix4 CreateFromQuaternion(CSMath.Quaternion quaternion)
```

Creates a rotation matrix from the given Quaternion rotation value.

**Returns:** The rotation matrix.

- `quaternion`: The source Quaternion.

### CreateRotationMatrix

```text
static CSMath.Matrix4 CreateRotationMatrix(CSMath.XYZ angles)
```

### CreateRotationMatrix

```text
static CSMath.Matrix4 CreateRotationMatrix(System.Double x, System.Double y, System.Double z)
```

Creates a rotation matrix.

- `x`: 
- `y`: 
- `z`: 

### CreateScale

```text
static CSMath.Matrix4 CreateScale(CSMath.XYZ scale)
```

Creates a scaling matrix.

**Returns:** The scaling matrix.

- `scale`: The vector containing the amount to scale by on each axis.

### CreateScale

```text
static CSMath.Matrix4 CreateScale(CSMath.XYZ scale, CSMath.XYZ centerPoint)
```

Creates a scaling matrix with a center point.

**Returns:** The scaling matrix.

- `scale`: The vector containing the amount to scale by on each axis.
- `centerPoint`: The center point.

### CreateScale

```text
static CSMath.Matrix4 CreateScale(System.Double scale)
```

Creates a uniform scaling matrix that scales equally on each axis.

**Returns:** The scaling matrix.

- `scale`: The uniform scaling factor.

### CreateScale

```text
static CSMath.Matrix4 CreateScale(System.Double scale, CSMath.XYZ centerPoint)
```

Creates a uniform scaling matrix that scales equally on each axis with a center point.

**Returns:** The scaling matrix.

- `scale`: The uniform scaling factor.
- `centerPoint`: The center point.

### CreateScalingMatrix

```text
static CSMath.Matrix4 CreateScalingMatrix(System.Double x, System.Double y, System.Double z)
```

Builds a matrix that scales along the x-axis, y-axis, and z-axis.

### CreateTranslation

```text
static CSMath.Matrix4 CreateTranslation(CSMath.XYZ position)
```

Creates a translation matrix.

**Returns:** The translation matrix.

- `position`: The amount to translate in each axis.

### CreateTranslation

```text
static CSMath.Matrix4 CreateTranslation(System.Double xPosition, System.Double yPosition, System.Double zPosition)
```

Creates a translation matrix.

**Returns:** The translation matrix.

- `xPosition`: The amount to translate on the X-axis.
- `yPosition`: The amount to translate on the Y-axis.
- `zPosition`: The amount to translate on the Z-axis.

### Equals

```text
System.Boolean Equals(System.Object obj)
```

Documentation inherited from: `base member`.

### GetArbitraryAxis

```text
static CSMath.Matrix4 GetArbitraryAxis(CSMath.XYZ xaxis, CSMath.XYZ zaxis)
```

Gets the rotation matrix from the normal vector.

**Returns:** Rotation matrix.

- `xaxis`: X axis.
- `zaxis`: Normal vector.

### GetArbitraryAxis

```text
static CSMath.Matrix4 GetArbitraryAxis(CSMath.XYZ zaxis)
```

Gets the rotation matrix from the normal vector.

**Returns:** Rotation matrix.

- `zaxis`: Normal vector.

### GetCols

```text
System.Collections.Generic.List[CSMath.XYZM] GetCols()
```

Gets the matrix columns.

### GetDeterminant

```text
System.Double GetDeterminant()
```

Calculates the determinant of the matrix.

**Returns:** The determinant of the matrix.

### GetHashCode

```text
System.Int32 GetHashCode()
```

Documentation inherited from: `base member`.

### GetRows

```text
System.Collections.Generic.List[CSMath.XYZM] GetRows()
```

Gets the matrix rows.

### Inverse

```text
static System.Boolean Inverse(CSMath.Matrix4 matrix, out CSMath.Matrix4 result)
```

Attempts to calculate the inverse of the given matrix. If successful, result will contain the inverted matrix.

**Returns:** True if the source matrix could be inverted; False otherwise.

- `matrix`: The source matrix to invert.
- `result`: If successful, contains the inverted matrix.

### Multiply

```text
static CSMath.Matrix4 Multiply(CSMath.Matrix4 a, CSMath.Matrix4 b)
```

Multiplies two matrices.

**Returns:** A new instance containing the result.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Transpose

```text
CSMath.Matrix4 Transpose()
```

Transposes the rows and columns of this matrix.

**Returns:** The transposed matrix.

### op_Multiply

```text
static CSMath.Matrix4 op_Multiply(CSMath.Matrix4 a, CSMath.Matrix4 b)
```

Multiplies two matrices.

**Returns:** A new instance containing the result.

### op_Multiply

```text
static CSMath.XYZ op_Multiply(CSMath.Matrix4 matrix, CSMath.XYZ value)
```

Multiply the matrix and a coordinate

**Returns:** Result matrix

- `matrix`: 
- `value`: 

### op_Multiply

```text
static CSMath.XYZM op_Multiply(CSMath.Matrix4 matrix, CSMath.XYZM v)
```

Multiply the matrix and XYZM

**Returns:** Result matrix

- `matrix`: 
- `v`: 

### Item

```text
System.Double Item[System.Int32 column, System.Int32 row] { get; set; }
```

### Item

```text
System.Double Item[System.Int32 index] { get; set; }
```
