# ACadSharp.XData.IExtendedDataHandleReference

`interface` · `ACadSharp` · CLR name: `ACadSharp.XData.IExtendedDataHandleReference`

Interface to define ACadSharp.XData.ExtendedDataRecord that are referencing another ACadSharp.CadObject.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.XData.IExtendedDataHandleReference')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ResolveReference

```text
ACadSharp.CadObject ResolveReference(ACadSharp.CadDocument document)
```

Resolve the reference of for an specific ACadSharp.CadDocument.

- `document`: 

### Value

```text
System.UInt64 Value { get; }
```

ulong value that points to a ACadSharp.IHandledCadObject.Handle.
