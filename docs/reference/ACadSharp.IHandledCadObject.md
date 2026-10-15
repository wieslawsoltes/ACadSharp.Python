# ACadSharp.IHandledCadObject

`interface` · `ACadSharp` · CLR name: `ACadSharp.IHandledCadObject`

Defines a CadObject with a unique handle

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IHandledCadObject')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Handle

```text
System.UInt64 Handle { get; }
```

Unique handle for this object in a ACadSharp.CadDocument.
