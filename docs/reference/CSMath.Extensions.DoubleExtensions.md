# CSMath.Extensions.DoubleExtensions

`class` · `ACadSharp` · CLR name: `CSMath.Extensions.DoubleExtensions`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.Extensions.DoubleExtensions')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### IsZero

```text
static System.Boolean IsZero(System.Double value)
```

Determines whether the specified double is zero, using a default threshold for comparison.

**Returns:** True if the number is zero within the default threshold; otherwise, false.

- `value`: The double value to evaluate.

### IsZero

```text
static System.Boolean IsZero(System.Double value, System.Double threshold)
```

Determines whether the specified double is zero, using a custom threshold for comparison.

**Returns:** True if the number is zero within the specified threshold; otherwise, false.

- `value`: The double value to evaluate.
- `threshold`: The custom threshold for comparison.
