# ACadSharp.Exceptions.DxfException

`class` · `ACadSharp` · CLR name: `ACadSharp.Exceptions.DxfException`

No upstream type summary is available.

Base type: `System.Exception`. Inherited members are documented on their declaring type.

Interfaces: `System.Runtime.Serialization.ISerializable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Exceptions.DxfException')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Exceptions.DxfException(System.Int32 code, System.Int64 line)
```

Invalid Dxf code

- `code`: 
- `line`: 

### .ctor

```text
ACadSharp.Exceptions.DxfException(System.String message)
```

### .ctor

```text
ACadSharp.Exceptions.DxfException(System.String message, System.Int64 line)
```

Generic exception

- `message`: 
- `line`: 
