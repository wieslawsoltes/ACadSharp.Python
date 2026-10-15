# CSMath.MathHelper

`class` · `ACadSharp` · CLR name: `CSMath.MathHelper`

Provides helper methods and constants for common mathematical operations, including angle conversions, floating-point comparisons, and rounding.

This static class includes constants for frequently used mathematical values and conversion factors between degrees, radians, and gradians. It also offers utility methods for comparing floating-point numbers with a configurable tolerance, normalizing angles, and rounding values. The methods are designed to address common issues with floating-point precision and angle normalization in mathematical computations.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.MathHelper')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### DegToGradFactor

```text
static System.Double DegToGradFactor = 1.1111111111111112
```

Factor for converting an angle between degrees and gradians.

### DegToRadFactor

```text
static System.Double DegToRadFactor = 0.017453292519943295
```

Factor for converting degrees to radians.

### Epsilon

```text
static System.Double Epsilon = 1e-12
```

Default tolerance

### GradToDegFactor

```text
static System.Double GradToDegFactor = 0.9
```

Factor for converting an angle between gradians and degrees.

### GradToRadFactor

```text
static System.Double GradToRadFactor = 0.015707963267948967
```

Factor for converting an angle between gradians and radians.

### HalfPI

```text
static System.Double HalfPI = 1.5707963267948966
```

Equivalent to 90 degrees.

### PI

```text
static System.Double PI = 3.141592653589793
```

Equivalent to 180 degrees.

### RadToDegFactor

```text
static System.Double RadToDegFactor = 57.29577951308232
```

Factor for converting radians to degrees.

### RadToGradFactor

```text
static System.Double RadToGradFactor = 63.66197723675813
```

Factor for converting radians to gradians.

### ThreeHalfPI

```text
static System.Double ThreeHalfPI = 4.71238898038469
```

Equivalent to 270 degrees.

### TwoPI

```text
static System.Double TwoPI = 6.283185307179586
```

Equivalent to 360 degrees.

### Cos

```text
static System.Double Cos(System.Double value)
```

Returns the cosine of specific angle in radians adjusting the value to 0 using F:CSMath.MathHelper.Epsilon as tolerance.

- `value`: 

### DegToGrad

```text
static System.Double DegToGrad(System.Double value)
```

Convert a value from degrees to gradian.

**Returns:** The gradian value.

- `value`: Value in degree.

### DegToRad

```text
static System.Double DegToRad(System.Double value)
```

Convert a value from degree to radian

**Returns:** The radian value

- `value`: Value in degrees

### FixZero

```text
static System.Double FixZero(System.Double number)
```

Returns zero if the specified number is within a small tolerance of zero; otherwise, returns the original number.

**Returns:** Zero if the specified number is considered close enough to zero; otherwise, the original number.

- `number`: The number to evaluate for near-zero equivalence.

### FixZero

```text
static System.Double FixZero(System.Double number, System.Double threshold)
```

Replaces the specified number with zero if it is within the defined threshold.

**Returns:** Zero if the number is within the threshold; otherwise, the original number.

- `number`: The number to evaluate.
- `threshold`: The threshold value for determining if the number is considered zero.

### FixZero

```text
static T FixZero[T](T vector)
```

Returns zero if the specified number is within the given threshold of zero; otherwise, returns the original number.

**Remarks:** This method is useful for normalizing values that are very close to zero due to floating-point precision errors. It can help avoid issues where extremely small values are treated as nonzero in calculations.

**Returns:** Zero if the absolute value of the number is less than or equal to the threshold; otherwise, the original number.

- `number`: The value to evaluate for near-zero equivalence.
- `threshold`: The tolerance within which the number is considered to be zero. Must be non-negative.
- `vector`: The vector to process. Components close to zero will be set to zero.

### FixZero

```text
static T FixZero[T](T vector, System.Double threshold)
```

Returns a new vector in which each component of the input vector is replaced with zero if its absolute value is less than the specified threshold.

**Remarks:** This method does not modify the input vector. The returned vector is a new instance of type T. Use this method to eliminate near-zero noise in vector data.

**Returns:** A new vector of type T with components set to zero if their absolute value is less than the specified threshold; otherwise, the original component value is retained.

- `vector`: The input vector whose components are to be processed.
- `threshold`: The threshold below which a component is considered to be zero. Components with an absolute value less than this value are set to zero.

### GradToDeg

```text
static System.Double GradToDeg(System.Double value)
```

Convert a value from gradian to degrees.

**Returns:** The gradian value.

- `value`: Value in gradians.

### GradToRad

```text
static System.Double GradToRad(System.Double value)
```

Convert a value from gradian to radian.

**Returns:** The gradian value.

- `value`: Value in gradians

### IsAngleInRange

```text
static System.Boolean IsAngleInRange(System.Double angle, System.Double start, System.Double end, System.Double precision = 1e-12)
```

Determines whether a specified angle falls within a given angular range.

**Remarks:** This method normalizes all angles to the range [0, 2π) before comparison. It correctly handles ranges that wrap around the 0/2π boundary. For example, if the start angle is greater than the end angle, the range is considered to span across 0 radians.

**Returns:** true if the angle falls within the specified range (inclusive); otherwise, false.

- `angle`: The angle to test, in radians.
- `start`: The start of the angular range, in radians.
- `end`: The end of the angular range, in radians.
- `precision`: The precision value for the calculation.

### IsEqual

```text
static System.Boolean IsEqual(System.Double a, System.Double b)
```

Checks if a number is equal to another.

**Returns:** True if the numbers are equal within a small tolerance; otherwise, false.

- `a`: Double precision number.
- `b`: Double precision number.

### IsEqual

```text
static System.Boolean IsEqual(System.Double a, System.Double b, System.Double threshold)
```

Checks if a number is equal to another.

**Returns:** True if the numbers are equal within the specified tolerance; otherwise, false.

- `a`: Double precision number.
- `b`: Double precision number.
- `threshold`: Tolerance.

### NormalizeAngle

```text
static System.Double NormalizeAngle(System.Double angle, System.Boolean absolute = True)
```

Normalizes the value of an angle in degrees between 0-360.

**Remarks:** Negative angles will be converted to its positive equivalent.

**Returns:** The equivalent angle in the range 0-360.

- `angle`: Angle in degrees.
- `absolute`: If true, negative angles will be converted to its positive equivalent.

### NormalizeAngleRadians

```text
static System.Double NormalizeAngleRadians(System.Double angle, System.Boolean absolute = True)
```

Normalizes the value of an angle in radians between 0-2π.

**Remarks:** Negative angles will be converted to its positive equivalent when absolute is true.

**Returns:** The equivalent angle in the range 0-2π.

- `angle`: Angle in radians.
- `absolute`: If true, negative angles will be converted to its positive equivalent.

### RadToDeg

```text
static System.Double RadToDeg(System.Double value, System.Boolean normalize = True, System.Boolean absolute = True)
```

Convert a value from radian to degree.

**Returns:** The degree value.

- `value`: Value in radians
- `normalize`: Normalizes the value to a 0-360 range.
- `absolute`: If true, negative values will be converted to its positive equivalent.

### RadToGrad

```text
static System.Double RadToGrad(System.Double value)
```

Convert a value from radian to gradian.

**Returns:** The gradian value.

- `value`: Value in radians.

### RoundToNearest

```text
static System.Double RoundToNearest(System.Double number, System.Double roundTo)
```

Round off a numeric value to the nearest of another value.

**Returns:** The number rounded to the nearest value.

- `number`: Number to round off.
- `roundTo`: The number will be rounded to the nearest of this value.

### Sin

```text
static System.Double Sin(System.Double value)
```

Returns the sine of specific angle in radians adjusting the value to 0 using F:CSMath.MathHelper.Epsilon as tolerance.

**Returns:** The sine of the angle.

- `value`: Angle in radians.
