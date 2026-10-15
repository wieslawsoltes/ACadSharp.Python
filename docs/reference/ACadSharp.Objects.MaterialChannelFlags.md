# ACadSharp.Objects.MaterialChannelFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Objects.MaterialChannelFlags`

Material channel-enable flags. Each bit toggles whether the renderer considers the corresponding channel data on the ACadSharp.Objects.Material. Mirrors the ODA-side OdGiMaterialTraits::ChannelFlags enum.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MaterialChannelFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### None

```text
static ACadSharp.Objects.MaterialChannelFlags None = 0
```

### UseAll

```text
static ACadSharp.Objects.MaterialChannelFlags UseAll = 127
```

### UseBump

```text
static ACadSharp.Objects.MaterialChannelFlags UseBump = 16
```

### UseDiffuse

```text
static ACadSharp.Objects.MaterialChannelFlags UseDiffuse = 1
```

### UseNormalMap

```text
static ACadSharp.Objects.MaterialChannelFlags UseNormalMap = 64
```

### UseOpacity

```text
static ACadSharp.Objects.MaterialChannelFlags UseOpacity = 8
```

### UseReflection

```text
static ACadSharp.Objects.MaterialChannelFlags UseReflection = 4
```

### UseRefraction

```text
static ACadSharp.Objects.MaterialChannelFlags UseRefraction = 32
```

### UseSpecular

```text
static ACadSharp.Objects.MaterialChannelFlags UseSpecular = 2
```
