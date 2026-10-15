# ACadSharp.IO.CadReaderFactory

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.CadReaderFactory`

Provides factory methods for creating CAD file readers based on file format.

Use this class to obtain an appropriate ICadReader instance for supported CAD file types such as DWG and DXF. The factory selects the correct reader implementation based on the file extension. This class does not validate file existence or content; it only inspects the file extension.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.CadReaderFactory')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### CreateReader

```text
static ACadSharp.IO.ICadReader CreateReader(System.String filename, ACadSharp.IO.NotificationEventHandler notification = null)
```

Creates an ACadSharp.IO.ICadReader instance for the specified CAD file format.

**Remarks:** Supported file formats include DWG and DXF. The method selects the appropriate reader based on the file extension.

**Returns:** An ACadSharp.IO.ICadReader instance capable of reading the specified CAD file.

- `filename`: The path to the CAD file to read. The file extension determines the reader type. Must not be null or empty.
- `notification`: An optional event handler for receiving notifications during the reading process. Can be null if no notifications are needed.

- Raises `System.NotSupportedException`: Thrown if the file extension is not supported.

### GetFileFormat

```text
static ACadSharp.IO.CadFileFormat GetFileFormat(System.String filename)
```

Determines the CAD file format based on the file extension of the specified filename.

**Remarks:** The method does not validate whether the file exists or whether the file content matches the extension. Only the file extension is considered when determining the format.

**Returns:** A value of the CadFileFormat enumeration that corresponds to the file's extension. Returns F:ACadSharp.IO.CadFileFormat.DWG for ".dwg" files, F:ACadSharp.IO.CadFileFormat.DXF for ".dxf" files, or F:ACadSharp.IO.CadFileFormat.Unknown if the extension is not recognized.

- `filename`: The path or name of the file whose format is to be identified. The file extension is used to determine the format.
