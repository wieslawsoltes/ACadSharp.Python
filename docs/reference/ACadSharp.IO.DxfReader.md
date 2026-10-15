# ACadSharp.IO.DxfReader

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.DxfReader`

Class for reading a DXF file into a ACadSharp.CadDocument.

Base type: `ACadSharp.IO.CadReaderBase[ACadSharp.IO.DxfReaderConfiguration]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IO.ICadReader`, `System.IDisposable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.DxfReader')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.DxfReader(System.IO.Stream stream, ACadSharp.IO.NotificationEventHandler notification = null)
```

Initializes a new instance of the ACadSharp.IO.DxfReader class

- `stream`: The stream to read from.
- `notification`: Notification handler, sends any message or notification about the reading process.

### .ctor

```text
ACadSharp.IO.DxfReader(System.String filename, ACadSharp.IO.NotificationEventHandler notification = null)
```

Initializes a new instance of the ACadSharp.IO.DxfReader class

- `filename`: The file to open.
- `notification`: Notification handler, sends any message or notification about the reading process.

### Dispose

```text
System.Void Dispose()
```

Documentation inherited from: `base member`.

### IsBinary

```text
System.Boolean IsBinary()
```

Check if the file format is in binary.

### IsBinary

```text
static System.Boolean IsBinary(System.IO.Stream stream, System.Boolean resetPos = False)
```

Check if the file format is in binary.

**Returns:** True if the file format is binary, false otherwise.

- `stream`: The stream to check.
- `resetPos`: Whether to reset the stream position after checking.

### IsBinary

```text
static System.Boolean IsBinary(System.String filename)
```

Check if the file format is in binary.

**Returns:** True if the file format is binary, false otherwise.

- `filename`: Path to the dxf file.

### Read

```text
ACadSharp.CadDocument Read()
```

Documentation inherited from: `base member`.

### Read

```text
static ACadSharp.CadDocument Read(System.IO.Stream stream, ACadSharp.IO.NotificationEventHandler notification = null)
```

Read a dxf document in a stream.

**Returns:** The read ACadSharp.CadDocument.

- `stream`: The stream to read from.
- `notification`: Notification handler, sends any message or notification about the reading process.

### Read

```text
static ACadSharp.CadDocument Read(System.String filename, ACadSharp.IO.DxfReaderConfiguration configuration, ACadSharp.IO.NotificationEventHandler notification = null)
```

Read a dxf document from a file.

**Returns:** The read ACadSharp.CadDocument.

- `filename`: The path to the dxf file.
- `configuration`: The configuration to use while reading the dxf file.
- `notification`: Notification handler, sends any message or notification about the reading process.

### Read

```text
static ACadSharp.CadDocument Read(System.String filename, ACadSharp.IO.NotificationEventHandler notification = null)
```

Read a dxf document from a file

- `filename`: 
- `notification`: Notification handler, sends any message or notification about the reading process.

### ReadEntities

```text
System.Collections.Generic.List[ACadSharp.Entities.Entity] ReadEntities()
```

Read only the entities section in the dxf document

**Remarks:** The entities will be completely independent from each other and linetypes and layers will only have it's name set, all the other properties will be set as default

### ReadHeader

```text
ACadSharp.Header.CadHeader ReadHeader()
```

Documentation inherited from: `base member`.

### ReadTables

```text
ACadSharp.CadDocument ReadTables()
```

Read only the tables section in the dxf document

**Remarks:** The ACadSharp.CadDocument will not contain any entity, only the tables and it's records
