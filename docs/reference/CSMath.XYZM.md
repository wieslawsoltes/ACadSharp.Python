# CSMath.XYZM

`struct` · `ACadSharp` · CLR name: `CSMath.XYZM`

No upstream type summary is available.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

Interfaces: `CSMath.IVector`, `System.IEquatable[CSMath.XYZM]`.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.XYZM')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.XYZM(System.Double value)
```

Constructs a vector whose elements are all the single specified value.

- `value`: The element to fill the vector with.

### .ctor

```text
CSMath.XYZM(System.Double x, System.Double y, System.Double z, System.Double m)
```

Constructor with the coordinate components

- `x`: Value of the X-coordinate
- `y`: Value of the Y-coordinate
- `z`: Value of the Z-coordinate
- `m`: Value of the M-coordinate

### AxisM

```text
static CSMath.XYZM AxisM
```

### AxisX

```text
static CSMath.XYZM AxisX
```

### AxisY

```text
static CSMath.XYZM AxisY
```

### AxisZ

```text
static CSMath.XYZM AxisZ
```

### NaN

```text
static CSMath.XYZM NaN
```

### Zero

```text
static CSMath.XYZM Zero
```

### Equals

```text
System.Boolean Equals(CSMath.XYZM other)
```

Documentation inherited from: `base member`.

### Equals

```text
System.Boolean Equals(CSMath.XYZM other, System.Int32 digits)
```

Indicates whether this instance and a specified object are equal with in a specific precison.

- `other`: 
- `digits`: number of decimals

### Equals

```text
System.Boolean Equals(System.Object obj)
```

Documentation inherited from: `base member`.

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
static CSMath.XYZM op_Addition(CSMath.XYZM left, CSMath.XYZM right)
```

Adds two vectors together.

**Returns:** The summed vector.

- `left`: The first source vector.
- `right`: The second source vector.

### op_Division

```text
static CSMath.XYZM op_Division(CSMath.XYZM left, CSMath.XYZM right)
```

Divides the first vector by the second.

**Returns:** The vector resulting from the division.

- `left`: The first source vector.
- `right`: The second source vector.

### op_Division

```text
static CSMath.XYZM op_Division(CSMath.XYZM xyzm, System.Double value)
```

Divides the vector by the given scalar.

**Returns:** The result of the division.

- `xyzm`: The source vector.
- `value`: The scalar value.

### op_Equality

```text
static System.Boolean op_Equality(CSMath.XYZM left, CSMath.XYZM right)
```

Returns a boolean indicating whether the two given vectors are equal.

**Returns:** True if the vectors are equal; False otherwise.

- `left`: The first vector to compare.
- `right`: The second vector to compare.

### op_Inequality

```text
static System.Boolean op_Inequality(CSMath.XYZM left, CSMath.XYZM right)
```

Returns a boolean indicating whether the two given vectors are not equal.

**Returns:** True if the vectors are not equal; False if they are equal.

- `left`: The first vector to compare.
- `right`: The second vector to compare.

### op_Multiply

```text
static CSMath.XYZM op_Multiply(CSMath.XYZM left, CSMath.XYZM right)
```

Multiplies two vectors together.

**Returns:** The product vector.

- `left`: The first source vector.
- `right`: The second source vector.

### op_Multiply

```text
static CSMath.XYZM op_Multiply(CSMath.XYZM left, System.Double scalar)
```

Multiplies a vector by the given scalar.

**Returns:** The scaled vector.

- `left`: The source vector.
- `scalar`: The scalar value.

### op_Multiply

```text
static CSMath.XYZM op_Multiply(System.Double scalar, CSMath.XYZM vector)
```

Multiplies a vector by the given scalar.

**Returns:** The scaled vector.

- `scalar`: The scalar value.
- `vector`: The source vector.

### op_Subtraction

```text
static CSMath.XYZM op_Subtraction(CSMath.XYZM left, CSMath.XYZM right)
```

Subtracts the second vector from the first.

**Returns:** The difference vector.

- `left`: The first source vector.
- `right`: The second source vector.

### op_UnaryNegation

```text
static CSMath.XYZM op_UnaryNegation(CSMath.XYZM value)
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

### M

```text
System.Double M { get; set; }
```

Specifies the M-value of the vector component

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
