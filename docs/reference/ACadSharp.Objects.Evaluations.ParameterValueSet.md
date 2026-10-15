# ACadSharp.Objects.Evaluations.ParameterValueSet

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.ParameterValueSet`

Represents the value set of a dynamic block parameter, which defines the allowed values for the parameter.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.ParameterValueSet')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.ParameterValueSet()
```

### AllowedValues

```text
System.Collections.Generic.List[System.Double] AllowedValues { get; }
```

Discrete list of allowed values.

### Increment

```text
System.Double Increment { get; set; }
```

Distance increment between two allowed values.

### Maximum

```text
System.Double Maximum { get; set; }
```

Maximum allowed value.

### Minimum

```text
System.Double Minimum { get; set; }
```

Minimum allowed value.

### Type

```text
ACadSharp.Objects.Evaluations.ParameterValueSetType Type { get; set; }
```

Gets or sets the type of the value set, which can be a discrete list, a range, or a combination of both.
