# CSMath.XY

`struct` · `ACadSharp` · CLR name: `CSMath.XY`

No upstream type summary is available.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

Interfaces: `CSMath.IVector`, `System.IEquatable[CSMath.XY]`.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.XY')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.XY(System.Double value)
```

Constructs a vector whose components are all the single specified value.

- `value`: The element to fill the vector with.

### .ctor

```text
CSMath.XY(System.Double x, System.Double y)
```

Constructor with the coordinate components

- `x`: Value of the X-coordinate
- `y`: Value of the Y-coordinate

### AxisX

```text
static CSMath.XY AxisX
```

### AxisY

```text
static CSMath.XY AxisY
```

### NaN

```text
static CSMath.XY NaN
```

### Zero

```text
static CSMath.XY Zero
```

### Cross

```text
static System.Double Cross(CSMath.XY xy1, CSMath.XY xy2)
```

Computes the cross product of two coordinates.

**Returns:** The cross product.

- `xy1`: The first coordinate.
- `xy2`: The second coordinate.

### Equals

```text
System.Boolean Equals(CSMath.XY other)
```

Documentation inherited from: `base member`.

### Equals

```text
System.Boolean Equals(CSMath.XY other, System.Int32 digits)
```

Indicates whether this instance and a specified object are equal with in a specific precison.

- `other`: 
- `digits`: number of decimals

### Equals

```text
System.Boolean Equals(System.Object obj)
```

Documentation inherited from: `base member`.

### GetAngle

```text
System.Double GetAngle()
```

Get the angle formed by the components of this vector.

**Returns:** Angle in radians.

### GetAngle

```text
System.Double GetAngle(CSMath.XY v)
```

Obtains the angle of a line defined by two points.

**Returns:** Angle in radians.

- `v`: Point defining the line.

### GetHashCode

```text
System.Int32 GetHashCode()
```

Documentation inherited from: `base member`.

### Perpendicular

```text
CSMath.XY Perpendicular()
```

Get the perpendicular vector.

### Polar

```text
CSMath.XY Polar(System.Double distance, System.Double angle)
```

Obtains the polar point of another point.

**Returns:** The polar point of the specified point.

- `distance`: Distance from point u.
- `angle`: Angle in radians.

### Polar

```text
static CSMath.XY Polar(CSMath.XY u, System.Double distance, System.Double angle)
```

Obtains the polar point of another point.

**Returns:** The polar point of the specified point.

- `u`: Reference point.
- `distance`: Distance from point u.
- `angle`: Angle in radians.

### Rotate

```text
static CSMath.XY Rotate(CSMath.XY value, System.Double angle)
```

Rotates a vector.

**Returns:** The rotated vector.

- `value`: 
- `angle`: Rotation angles in radians.

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
static CSMath.XY op_Addition(CSMath.XY left, CSMath.XY right)
```

Adds two vectors together.

**Returns:** The summed vector.

- `left`: The first source vector.
- `right`: The second source vector.

### op_Division

```text
static CSMath.XY op_Division(CSMath.XY XY, System.Double value)
```

Divides the vector by the given scalar.

**Returns:** The result of the division.

- `XY`: The source vector.
- `value`: The scalar value.

### op_Division

```text
static CSMath.XY op_Division(CSMath.XY XY, System.Single value)
```

Divides the vector by the given scalar.

**Returns:** The result of the division.

- `XY`: The source vector.
- `value`: The scalar value.

### op_Division

```text
static CSMath.XY op_Division(CSMath.XY left, CSMath.XY right)
```

Divides the first vector by the second.

**Returns:** The vector resulting from the division.

- `left`: The first source vector.
- `right`: The second source vector.

### op_Equality

```text
static System.Boolean op_Equality(CSMath.XY left, CSMath.XY right)
```

Returns a boolean indicating whether the two given vectors are equal.

**Returns:** True if the vectors are equal; False otherwise.

- `left`: The first vector to compare.
- `right`: The second vector to compare.

### op_Explicit

```text
static CSMath.XY op_Explicit(CSMath.XYZ xyz)
```

### op_Inequality

```text
static System.Boolean op_Inequality(CSMath.XY left, CSMath.XY right)
```

Returns a boolean indicating whether the two given vectors are not equal.

**Returns:** True if the vectors are not equal; False if they are equal.

- `left`: The first vector to compare.
- `right`: The second vector to compare.

### op_Multiply

```text
static CSMath.XY op_Multiply(CSMath.XY left, CSMath.XY right)
```

Multiplies two vectors together.

**Returns:** The product vector.

- `left`: The first source vector.
- `right`: The second source vector.

### op_Multiply

```text
static CSMath.XY op_Multiply(CSMath.XY left, System.Double scalar)
```

Multiplies a vector by the given scalar.

**Returns:** The scaled vector.

- `left`: The source vector.
- `scalar`: The scalar value.

### op_Multiply

```text
static CSMath.XY op_Multiply(System.Double scalar, CSMath.XY vector)
```

Multiplies a vector by the given scalar.

**Returns:** The scaled vector.

- `scalar`: The scalar value.
- `vector`: The source vector.

### op_Subtraction

```text
static CSMath.XY op_Subtraction(CSMath.XY left, CSMath.XY right)
```

Subtracts the second vector from the first.

**Returns:** The difference vector.

- `left`: The first source vector.
- `right`: The second source vector.

### op_UnaryNegation

```text
static CSMath.XY op_UnaryNegation(CSMath.XY value)
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
