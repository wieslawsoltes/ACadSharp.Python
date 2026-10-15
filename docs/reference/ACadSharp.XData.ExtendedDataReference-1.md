# ACadSharp.XData.ExtendedDataReference

`class` · `ACadSharp` · CLR name: ``ACadSharp.XData.ExtendedDataReference`1``

No upstream type summary is available.

Base type: `ACadSharp.XData.ExtendedDataRecord[System.UInt64]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.XData.IExtendedDataHandleReference`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.XData.ExtendedDataReference`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ResolveReference

```text
T ResolveReference(ACadSharp.CadDocument document)
```

Resolve the reference of for an specific ACadSharp.CadDocument.

- `document`: 
