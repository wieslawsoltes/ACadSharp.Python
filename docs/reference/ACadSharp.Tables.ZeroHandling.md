# ACadSharp.Tables.ZeroHandling

`enum` · `ACadSharp` · CLR name: `ACadSharp.Tables.ZeroHandling`

Represents suppression of zeros in displaying decimal numbers.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.ZeroHandling')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ShowZeroFeetAndInches

```text
static ACadSharp.Tables.ZeroHandling ShowZeroFeetAndInches = 1
```

Show zero feet and exactly zero inches.

### ShowZeroFeetSuppressZeroInches

```text
static ACadSharp.Tables.ZeroHandling ShowZeroFeetSuppressZeroInches = 2
```

Show zero feet and suppress zero inches.

### SuppressDecimalLeadingAndTrailingZeroes

```text
static ACadSharp.Tables.ZeroHandling SuppressDecimalLeadingAndTrailingZeroes = 12
```

Suppress both leading and trailing zeroes in decimal numbers

### SuppressDecimalLeadingZeroes

```text
static ACadSharp.Tables.ZeroHandling SuppressDecimalLeadingZeroes = 4
```

Suppress leading zeroes in decimal numbers.

### SuppressDecimalTrailingZeroes

```text
static ACadSharp.Tables.ZeroHandling SuppressDecimalTrailingZeroes = 8
```

Suppress trailing zeroes in decimal numbers.

### SuppressZeroFeetAndInches

```text
static ACadSharp.Tables.ZeroHandling SuppressZeroFeetAndInches = 0
```

Suppress zero feet and exactly zero inches.

### SuppressZeroFeetShowZeroInches

```text
static ACadSharp.Tables.ZeroHandling SuppressZeroFeetShowZeroInches = 3
```

Suppress zero feet and show zero inches.
