# ACadSharp.Objects.Evaluations.DxfValuePair

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.DxfValuePair`

Represents a pair of values used in evaluation expressions, consisting of a code and its corresponding value.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.DxfValuePair')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.DxfValuePair(ACadSharp.DxfCode code, System.Object value)
```

### Code

```text
ACadSharp.DxfCode Code { get; }
```

### GroupCodeValueType

```text
ACadSharp.GroupCodeValueType GroupCodeValueType { get; }
```

### Value

```text
System.Object Value { get; }
```
