# ACadSharp.Types.Units.UnitStyleFormat

`class` · `ACadSharp` · CLR name: `ACadSharp.Types.Units.UnitStyleFormat`

Represents the parameters to convert linear and angular units to its string representation.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Types.Units.UnitStyleFormat')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Types.Units.UnitStyleFormat()
```

Initializes a new instance of the UnitStyleFormat class.

### GetZeroHandlingFormat

```text
System.String GetZeroHandlingFormat(System.Boolean isAngular = False)
```

Get the string format based on the zero handling of the style.

- `isAngular`: 

### ToArchitectural

```text
System.String ToArchitectural(System.Double value)
```

Converts a value into its feet and fractional inches string representation.

**Returns:** A string that represents the value in feet and fractional inches.

- `value`: 

### ToDecimal

```text
System.String ToDecimal(System.Double value, System.Boolean isAngular = False)
```

Converts a value into its decimal string representation.

**Returns:** A string that represents the value in decimal units.

- `value`: 
- `isAngular`: 

### ToDegrees

```text
System.String ToDegrees(System.Double angle)
```

Converts an angle value in degrees string representation.

**Returns:** A string that represents the value in degrees

- `angle`: Angle value in radians.

### ToDegreesMinutesSeconds

```text
System.String ToDegreesMinutesSeconds(System.Double angle)
```

Converts an angle value in degrees into its degrees, minutes and seconds string representation.

**Returns:** A string that represents the value in degrees, minutes and seconds

- `angle`: Angle value in radians.

### ToEngineering

```text
System.String ToEngineering(System.Double value)
```

Converts a value into its feet and decimal inches string representation.

**Returns:** A string that represents the value in feet and decimal inches.

- `value`: Must be in inches.

### ToFractional

```text
System.String ToFractional(System.Double value)
```

Converts a value into its fractional string representation.

**Returns:** A string that represents the value in fractional units.

- `value`: 

### ToGradians

```text
System.String ToGradians(System.Double angle)
```

Converts an angle value in radians into its gradians string representation.

**Returns:** A string that represents the angle in gradians.

- `angle`: The angle value in radians.

### ToRadians

```text
System.String ToRadians(System.Double angle)
```

Converts an angle value in radians into its string representation.

**Returns:** A string that represents the angle in radians.

- `angle`: The angle value in radians.

### ToScientific

```text
System.String ToScientific(System.Double value)
```

Converts a value into its scientific string representation.

**Returns:** A string that represents the length in scientific units.

- `value`: The length value.

### AngularDecimalPlaces

```text
System.Int16 AngularDecimalPlaces { get; set; }
```

Gets or sets the number of decimal places for angular units.

### AngularZeroHandling

```text
ACadSharp.Tables.AngularZeroHandling AngularZeroHandling { get; set; }
```

Gets or sets the suppression of zeros in the angular values.

### DecimalSeparator

```text
System.String DecimalSeparator { get; set; }
```

Gets or set the decimal separator.

### DegreesSymbol

```text
System.String DegreesSymbol { get; set; }
```

Gets or set the angle degrees symbol.

### FeetInchesSeparator

```text
System.String FeetInchesSeparator { get; set; }
```

Gets or sets the separator between feet and inches.

### FeetSymbol

```text
System.String FeetSymbol { get; set; }
```

Gets or set the feet symbol.

### FractionHeightScale

```text
System.Double FractionHeightScale { get; set; }
```

Gets or sets the scale of fractions relative to dimension text height.

### FractionType

```text
ACadSharp.Tables.FractionFormat FractionType { get; set; }
```

Gets or sets the fraction format for architectural or fractional units.

**Remarks:** Horizontal stacking Diagonal stacking Not stacked (for example, 1/2)

### GradiansSymbol

```text
System.String GradiansSymbol { get; set; }
```

Gets or set the angle gradians symbol.

### InchesSymbol

```text
System.String InchesSymbol { get; set; }
```

Gets or set the inches symbol.

### LinearDecimalPlaces

```text
System.Int16 LinearDecimalPlaces { get; set; }
```

Gets or sets the number of decimal places for linear units.

**Remarks:** For architectural and fractional the precision used for the minimum fraction is 1/2^LinearDecimalPlaces.

### LinearZeroHandling

```text
ACadSharp.Tables.ZeroHandling LinearZeroHandling { get; set; }
```

Gets or sets the suppression of zeros in the linear values.

### MinutesSymbol

```text
System.String MinutesSymbol { get; set; }
```

Gets or set the angle minutes symbol.

### RadiansSymbol

```text
System.String RadiansSymbol { get; set; }
```

Gets or set the angle radians symbol.

### SecondsSymbol

```text
System.String SecondsSymbol { get; set; }
```

Gets or set the angle seconds symbol.

### SuppressAngularLeadingZeros

```text
System.Boolean SuppressAngularLeadingZeros { get; }
```

Suppresses leading zeros in angular decimal dimensions (for example, 0.5000 becomes .5000).

### SuppressAngularTrailingZeros

```text
System.Boolean SuppressAngularTrailingZeros { get; }
```

Suppresses trailing zeros in angular decimal dimensions (for example, 12.5000 becomes 12.5).

### SuppressLinearLeadingZeros

```text
System.Boolean SuppressLinearLeadingZeros { get; }
```

Suppresses leading zeros in linear decimal dimensions (for example, 0.5000 becomes .5000).

### SuppressLinearTrailingZeros

```text
System.Boolean SuppressLinearTrailingZeros { get; }
```

Suppresses trailing zeros in linear decimal dimensions (for example, 12.5000 becomes 12.5).

### SuppressZeroFeet

```text
System.Boolean SuppressZeroFeet { get; }
```

Suppresses zero feet in architectural dimensions.

### SuppressZeroInches

```text
System.Boolean SuppressZeroInches { get; }
```

Suppresses zero inches in architectural dimensions.
