# ACadSharp.INamedCadObject

`interface` · `ACadSharp` · CLR name: `ACadSharp.INamedCadObject`

Defines a CadObject with a unique name.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.INamedCadObject')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### OnNameChanged

```text
event System.EventHandler[ACadSharp.OnNameChangedArgs] OnNameChanged
```

### Name

```text
System.String Name { get; }
```

Name identifier for this object.

**Remarks:** All named entries are case insensitive.
