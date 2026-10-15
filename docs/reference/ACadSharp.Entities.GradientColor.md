# ACadSharp.Entities.GradientColor

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.GradientColor`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.GradientColor')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.GradientColor()
```

### Clone

```text
ACadSharp.Entities.GradientColor Clone()
```

### Color

```text
ACadSharp.Color Color { get; set; }
```

Color for this gradient

### Value

```text
System.Double Value { get; set; }
```

Gradient value

**Value:** The value must be in the range 0-1
