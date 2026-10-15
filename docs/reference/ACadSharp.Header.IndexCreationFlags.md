# ACadSharp.Header.IndexCreationFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Header.IndexCreationFlags`

Controls whether layer and spatial indexes are created and saved in drawing files

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Header.IndexCreationFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### LayerAndSpatialIndex

```text
static ACadSharp.Header.IndexCreationFlags LayerAndSpatialIndex = 3
```

Layer and spatial indexes are created

### LayerIndex

```text
static ACadSharp.Header.IndexCreationFlags LayerIndex = 1
```

Layer index is created

### NoIndex

```text
static ACadSharp.Header.IndexCreationFlags NoIndex = 0
```

No indexes are created

### SpatialIndex

```text
static ACadSharp.Header.IndexCreationFlags SpatialIndex = 2
```

Spatial index is created
