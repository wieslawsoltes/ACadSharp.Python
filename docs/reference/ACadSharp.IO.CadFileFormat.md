# ACadSharp.IO.CadFileFormat

`enum` · `ACadSharp` · CLR name: `ACadSharp.IO.CadFileFormat`

Represents the file format of a CAD file.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.CadFileFormat')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### DWG

```text
static ACadSharp.IO.CadFileFormat DWG = 1
```

Represents the DWG file format, commonly used for storing two and three-dimensional design data and metadata.

### DXF

```text
static ACadSharp.IO.CadFileFormat DXF = 2
```

Represents a Drawing Exchange Format (DXF) entity or utility for working with DXF files.

### Unknown

```text
static ACadSharp.IO.CadFileFormat Unknown = 0
```

Represents an unknown or unspecified value.
