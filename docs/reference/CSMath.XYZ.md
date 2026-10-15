# CSMath.XYZ

`struct` · `ACadSharp` · CLR name: `CSMath.XYZ`

No upstream type summary is available.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

Interfaces: `CSMath.IVector`, `System.IEquatable[CSMath.XYZ]`.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.XYZ')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.XYZ(System.Double value)
```

Constructs a vector whose elements are all the single specified value.

- `value`: The element to fill the vector with.

### .ctor

```text
CSMath.XYZ(System.Double x, System.Double y, System.Double z)
```

Constructor with the coordinate components

- `x`: Value of the X-coordinate
- `y`: Value of the Y-coordinate
- `z`: Value of the Z-coordinate

### AxisX

```text
static CSMath.XYZ AxisX
```

### AxisY

```text
static CSMath.XYZ AxisY
```

### AxisZ

```text
static CSMath.XYZ AxisZ
```

### NaN

```text
static CSMath.XYZ NaN
```

### Zero

```text
static CSMath.XYZ Zero
```

### Cross

```text
static CSMath.XYZ Cross(CSMath.XYZ xyz1, CSMath.XYZ xyz2)
```

Computes the cross product of two coordinates.

**Returns:** The cross product.

- `xyz1`: The first coordinate.
- `xyz2`: The second coordinate.

### Equals

```text
System.Boolean Equals(CSMath.XYZ other)
```

Documentation inherited from: `base member`.

### Equals

```text
System.Boolean Equals(CSMath.XYZ other, System.Int32 digits)
```

Indicates whether this instance and a specified object are equal with in a specific precision.

**Returns:** true if the objects are equal within the specified precision; otherwise, false.

- `other`: The object to compare with the current instance.
- `digits`: The number of decimal places to consider for equality.

### Equals

```text
System.Boolean Equals(System.Object obj)
```

Documentation inherited from: `base member`.

### FindNormal

```text
static CSMath.XYZ FindNormal(CSMath.XYZ point1, CSMath.XYZ point2, CSMath.XYZ point3)
```

Finds the normal vector of a plane defined by three points.

**Returns:** The normal vector of the plane.

- `point1`: The first point defining the plane.
- `point2`: The second point defining the plane.
- `point3`: The third point defining the plane.

### GetAngle

```text
System.Double GetAngle(CSMath.XYZ dir)
```

Calculates the angle, in radians, between this vector and the specified vector.

**Remarks:** If either vector has zero length, the result may not be meaningful. The method returns 0 if the vectors are parallel and point in the same direction, and π if they are parallel and point in opposite directions.

**Returns:** The angle, in radians, between this vector and dir. The value is in the range [0, π].

- `dir`: The vector to which the angle is measured.

### GetAngle

```text
System.Double GetAngle(CSMath.XYZ dir, CSMath.XYZ normal)
```

Calculates the signed angle, in radians, between this vector and the specified direction vector, using the given normal to determine the sign.

**Remarks:** The returned angle is measured in the plane defined by this vector and dir, with the sign determined by the right-hand rule using normal. If the vectors are parallel, the angle is 0 or π depending on their direction.

**Returns:** The signed angle, in radians, between this vector and dir. The value is in the range [0, 2π].

- `dir`: The direction vector to which the angle is measured.
- `normal`: The normal vector that defines the orientation of the plane in which the angle is measured. The sign of the angle is determined based on the direction of this normal.

### GetHashCode

```text
System.Int32 GetHashCode()
```

Documentation inherited from: `base member`.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### ToString

```text
System.String ToString(System.IFormatProvider cultureInfo)
```

Converts the numeric value of this instance to its equivalent string representation using the specified culture-specific format information.

**Returns:** The string representation of the value of this instance as specified by provider.

- `cultureInfo`: An object that supplies culture-specific formatting information.

### op_Addition

```text
static CSMath.XYZ op_Addition(CSMath.XYZ left, CSMath.XYZ right)
```

Adds two vectors together.

**Returns:** The summed vector.

- `left`: The first source vector.
- `right`: The second source vector.

### op_Division

```text
static CSMath.XYZ op_Division(CSMath.XYZ left, CSMath.XYZ right)
```

Divides the first vector by the second.

**Returns:** The vector resulting from the division.

- `left`: The first source vector.
- `right`: The second source vector.

### op_Division

```text
static CSMath.XYZ op_Division(CSMath.XYZ xyz, System.Double value)
```

Divides the vector by the given scalar.

**Returns:** The result of the division.

- `xyz`: The source vector.
- `value`: The scalar value.

### op_Division

```text
static CSMath.XYZ op_Division(CSMath.XYZ xyz, System.Single value)
```

Divides the vector by the given scalar.

**Returns:** The result of the division.

- `xyz`: The source vector.
- `value`: The scalar value.

### op_Equality

```text
static System.Boolean op_Equality(CSMath.XYZ left, CSMath.XYZ right)
```

Returns a boolean indicating whether the two given vectors are equal.

**Returns:** True if the vectors are equal; False otherwise.

- `left`: The first vector to compare.
- `right`: The second vector to compare.

### op_Explicit

```text
static CSMath.XYZ op_Explicit(CSMath.XY xy)
```

### op_Inequality

```text
static System.Boolean op_Inequality(CSMath.XYZ left, CSMath.XYZ right)
```

Returns a boolean indicating whether the two given vectors are not equal.

**Returns:** True if the vectors are not equal; False if they are equal.

- `left`: The first vector to compare.
- `right`: The second vector to compare.

### op_Multiply

```text
static CSMath.XYZ op_Multiply(CSMath.XYZ left, CSMath.XYZ right)
```

Multiplies two vectors together.

**Returns:** The product vector.

- `left`: The first source vector.
- `right`: The second source vector.

### op_Multiply

```text
static CSMath.XYZ op_Multiply(CSMath.XYZ left, System.Double scalar)
```

Multiplies a vector by the given scalar.

**Returns:** The scaled vector.

- `left`: The source vector.
- `scalar`: The scalar value.

### op_Multiply

```text
static CSMath.XYZ op_Multiply(System.Double scalar, CSMath.XYZ vector)
```

Multiplies a vector by the given scalar.

**Returns:** The scaled vector.

- `scalar`: The scalar value.
- `vector`: The source vector.

### op_Subtraction

```text
static CSMath.XYZ op_Subtraction(CSMath.XYZ left, CSMath.XYZ right)
```

Subtracts the second vector from the first.

**Returns:** The difference vector.

- `left`: The first source vector.
- `right`: The second source vector.

### op_UnaryNegation

```text
static CSMath.XYZ op_UnaryNegation(CSMath.XYZ value)
```

Negates a given vector.

**Returns:** The negated vector.

- `value`: The source vector.

### Dimension

```text
System.UInt32 Dimension { get; }
```

Documentation inherited from: `base member`.

### Item

```text
System.Double Item[System.Int32 index] { get; set; }
```

Documentation inherited from: `base member`.

### X

```text
System.Double X { get; set; }
```

Specifies the X-value of the vector component

### Y

```text
System.Double Y { get; set; }
```

Specifies the Y-value of the vector component

### Z

```text
System.Double Z { get; set; }
```

Specifies the Z-value of the vector component
