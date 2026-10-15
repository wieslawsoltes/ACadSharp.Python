# ACadSharp.XData.ExtendedDataRecord

`class` · `ACadSharp` · CLR name: ``ACadSharp.XData.ExtendedDataRecord`1``

Defines a typed ACadSharp.XData.ExtendedData record.

Base type: `ACadSharp.XData.ExtendedDataRecord`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.XData.ExtendedDataRecord`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Value

```text
T Value { get; set; }
```

Value for this record.
