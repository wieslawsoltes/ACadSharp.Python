# ACadSharp.Extensions.INamedCadObjectExtensions

`class` · `ACadSharp` · CLR name: `ACadSharp.Extensions.INamedCadObjectExtensions`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Extensions.INamedCadObjectExtensions')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### InvalidCharacters

```text
static System.Char[] InvalidCharacters
```

### HasValidDxfName

```text
static System.Boolean HasValidDxfName(ACadSharp.INamedCadObject namedCadObject, ACadSharp.ACadVersion version = AC1032)
```

Check if the name of the object is valid for dxf format.

- `namedCadObject`: 
- `version`: 
