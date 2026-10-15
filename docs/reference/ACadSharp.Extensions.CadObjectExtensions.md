# ACadSharp.Extensions.CadObjectExtensions

`class` · `ACadSharp` · CLR name: `ACadSharp.Extensions.CadObjectExtensions`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Extensions.CadObjectExtensions')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### CloneTyped

```text
static T CloneTyped[T](T obj)
```

Creates a new object that is a copy of the current instance.

**Remarks:** The copy will be unattached from the document or any reference.

**Returns:** A new object that is a copy of this instance.

- `obj`: 
