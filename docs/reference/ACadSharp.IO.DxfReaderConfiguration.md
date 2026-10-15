# ACadSharp.IO.DxfReaderConfiguration

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.DxfReaderConfiguration`

Configuration for reading DXF files.

Base type: `ACadSharp.IO.CadReaderConfiguration`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.DxfReaderConfiguration')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.DxfReaderConfiguration()
```

### ClearCache

```text
System.Boolean ClearCache { get; set; }
```

Clears the cache after the reading

### CreateDefaults

```text
System.Boolean CreateDefaults { get; set; }
```

Create the defaults at the end of the reading operation.
