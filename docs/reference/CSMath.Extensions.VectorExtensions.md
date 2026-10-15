# CSMath.Extensions.VectorExtensions

`class` · `ACadSharp` · CLR name: `CSMath.Extensions.VectorExtensions`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Extensions.VectorExtensions')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Add

```text
static T Add[T](T left, T right)
```

Adds two vectors together.

**Returns:** The summed vector.

- `left`: The first source vector.
- `right`: The second source vector.

### AngleBetweenVectors

```text
static System.Double AngleBetweenVectors[T](T v, T u)
```

Angle between two CSMath.IVector.

**Remarks:** The CSMath.IVector must be vectors, not points.

- `v`: The first CSMath.IVector.
- `u`: The second CSMath.IVector.

### Convert

```text
static T Convert[T](CSMath.IVector v)
```

Converts an CSMath.IVector into an equivalent CSMath.IVector

- `v`: 

### CopyValues

```text
static T CopyValues[T](T v, CSMath.IVector source)
```

Copy the component values from a source using the smallest dimension of both parameters

**Returns:** A copy of the CSMath.IVector with the copied components

- `v`: 
- `source`: 

### DistanceFrom

```text
static System.Double DistanceFrom[T](T v, T u)
```

Distance between two CSMath.IVector.

- `v`: 
- `u`: 

### Divide

```text
static T Divide[T](T left, System.Double scalar)
```

Divides a vector with an scalar.

### Divide

```text
static T Divide[T](T left, T right)
```

Divides the first vector by the second.

**Returns:** The vector resulting from the division.

- `left`: The first source vector.
- `right`: The second source vector.

### Dot

```text
static System.Double Dot[T](T left, T right)
```

Returns the dot product of two vectors.

**Returns:** The dot product.

- `left`: The first vector.
- `right`: The second vector.

### GetLength

```text
static System.Double GetLength[T](T vector)
```

Returns the length of the vector.

**Returns:** The vector's length.

### GetLengthSquared

```text
static System.Double GetLengthSquared[T](T vector)
```

Calculates the sum of the squares of the vector's components.

**Remarks:** This method does not compute the square root of the sum. To obtain the actual length (magnitude) of the vector, use Math.Sqrt on the returned value. This method is useful for performance-sensitive scenarios where comparing squared lengths is sufficient.

**Returns:** The sum of the squares of all components of the vector. This value represents the squared length (magnitude) of the vector.

- `vector`: The vector whose squared length is to be calculated. Must not be null.

### IsEqual

```text
static System.Boolean IsEqual[T](T left, T right)
```

Returns a boolean indicating whether the two given vectors are equal.

**Returns:** True if the vectors are equal; False otherwise.

- `left`: The first vector to compare.
- `right`: The second vector to compare.

### IsEqual

```text
static System.Boolean IsEqual[T](T left, T right, System.Int32 ndecimals)
```

Returns a boolean indicating whether the two given vectors are equal.

**Returns:** True if the vectors are equal; False otherwise.

- `left`: The first vector to compare.
- `right`: The second vector to compare.
- `ndecimals`: Number of decimals digits to be set as precision.

### IsNaN

```text
static System.Boolean IsNaN[T](T v)
```

Returns a value indicating if any component of the specified vector evaluates to a value that is not a number F:System.Double.NaN.

**Returns:** Returns true if any component of the specified vector evaluates to F:System.Double.NaN; otherwise, false.

- `v`: 

### IsNormalized

```text
static System.Boolean IsNormalized[T](T v)
```

Gets a value indicating whether the CSMath.IVector is normalized, or not.

### IsParallel

```text
static System.Boolean IsParallel[T](T left, T right)
```

Returns a boolean indicating whether the two given vectors are parallel.

- `left`: The first vector.
- `right`: The second vector.

### IsPerpendicular

```text
static System.Boolean IsPerpendicular[T](T left, T right)
```

Returns a boolean indicating whether the two given vectors are perpendicular.

- `left`: The first vector.
- `right`: The second vector.

### IsZero

```text
static System.Boolean IsZero[T](T v)
```

Returns true if the magnitude of the CSMath.IVector is zero.

- `v`: 

### Mid

```text
static T Mid[T](T start, T end)
```

Calculates the middle point between a start and end.

**Returns:** Middle point.

- `start`: Start point.
- `end`: End point.

### Multiply

```text
static T Multiply[T](T left, System.Double scalar)
```

Multiplies a vector with an scalar.

**Returns:** The product vector.

- `left`: The first source vector.
- `scalar`: The second source vector.

### Multiply

```text
static T Multiply[T](T left, T right)
```

Multiplies two vectors together.

**Returns:** The product vector.

- `left`: The first source vector.
- `right`: The second source vector.

### Normalize

```text
static T Normalize[T](T vector)
```

Returns a vector with the same direction as the given vector, but with a length of 1.

**Returns:** The normalized vector.

- `vector`: The vector to normalize.

### Round

```text
static T Round[T](T vector)
```

Round the vector components

- `vector`: 

### Round

```text
static T Round[T](T vector, System.Int32 digits)
```

Round the vector components

- `vector`: 
- `digits`: The number of fractional digits in the return value

### RoundZero

```text
static T RoundZero[T](T vector, System.Double threshold = 1e-12)
```

Round the zeros within the threshold defined by F:CSMath.MathHelper.Epsilon.

- `vector`: 
- `threshold`: 

### Subtract

```text
static T Subtract[T](T left, T right)
```

Subtracts the second vector from the first.

**Returns:** The difference vector.

- `left`: The first source vector.
- `right`: The second source vector.

### ToEnumerable

```text
static System.Collections.Generic.IEnumerable[System.Double] ToEnumerable[T](T v)
```

Get an enumerable with the components of the CSMath.IVector

- `v`: 
