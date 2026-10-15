# ACadSharp.Objects.MaterialIlluminationModel

`enum` · `ACadSharp` · CLR name: `ACadSharp.Objects.MaterialIlluminationModel`

Shader chosen to evaluate the illumination of a ACadSharp.Objects.Material. Mirrors the ODA-side OdGiMaterialTraits::IlluminationModel enum.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MaterialIlluminationModel')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### BlinnShader

```text
static ACadSharp.Objects.MaterialIlluminationModel BlinnShader = 0
```

### MetalShader

```text
static ACadSharp.Objects.MaterialIlluminationModel MetalShader = 1
```
