# ACadSharp.Entities.HatchGradientPattern

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.HatchGradientPattern`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.HatchGradientPattern')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.HatchGradientPattern()
```

### .ctor

```text
ACadSharp.Entities.HatchGradientPattern(System.String name)
```

### Clone

```text
ACadSharp.Entities.HatchGradientPattern Clone()
```

### Angle

```text
System.Double Angle { get; set; }
```

Rotation angle in radians for gradients (default = 0, 0)

### ColorTint

```text
System.Double ColorTint { get; set; }
```

Color tint value used by dialog code (default = 0, 0; range is 0.0 to 1.0). The color tint value is a gradient color and controls the degree of tint in the dialog when the Hatch group code 452 is set to 1.

### Colors

```text
System.Collections.Generic.List[ACadSharp.Entities.GradientColor] Colors { get; set; }
```

Colors in the gradient

**Remarks:** 0 = Solid hatch 2 = Gradient

### Enabled

```text
System.Boolean Enabled { get; set; }
```

Indicates solid hatch or gradient

### IsSingleColorGradient

```text
System.Boolean IsSingleColorGradient { get; set; }
```

Records how colors were defined and is used only by dialog code

**Remarks:** 0 = Two-color gradient 1 = Single-color gradient

### Name

```text
System.String Name { get; set; }
```

Name of the gradient

### Shift

```text
System.Double Shift { get; set; }
```

Gradient definition; corresponds to the Centered option on the Gradient Tab of the Boundary Hatch and Fill dialog box. Each gradient has two definitions, shifted and non-shifted. A Shift value describes the blend of the two definitions that should be used. A value of 0.0 means only the non-shifted version should be used, and a value of 1.0 means that only the shifted version should be used.
