# ACadSharp.IO.DwgReaderConfiguration

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.DwgReaderConfiguration`

Configuration for reading DWG files.

Base type: `ACadSharp.IO.CadReaderConfiguration`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.DwgReaderConfiguration')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.DwgReaderConfiguration()
```

### CrcCheck

```text
System.Boolean CrcCheck { get; set; }
```

Use the Standard Cycling Redundancy Check to verify the integrity of the file, default value is set to false.

**Remarks:** DWG file format uses a modification of a standard Cyclic Redundancy Check as an error detecting mechanism, if this flag is enabled the reader will perform this verification to detect any possible error, but it will greatly increase the reading time.

### IgnoreProxyGraphics

```text
System.Boolean IgnoreProxyGraphics { get; set; }
```

If set to true the reader will skip the proxy graphics section.

**Value:** default: true

### ReadSummaryInfo

```text
System.Boolean ReadSummaryInfo { get; set; }
```

If set to false the reader will skip the summary info section.

**Value:** default: true
