# ACadSharp.Classes.IDxfClassDefined

`interface` · `ACadSharp` · CLR name: `ACadSharp.Classes.IDxfClassDefined`

Defines a contract for classes that can provide a ACadSharp.Classes.DxfClass instance.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Classes.IDxfClassDefined')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Gets the ACadSharp.Classes.DxfClass instance associated with this class.

**Returns:** The ACadSharp.Classes.DxfClass instance associated with this class.
