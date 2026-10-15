# ACadSharp.IO.DwgReader

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.DwgReader`

Class for reading a DWG file into a ACadSharp.CadDocument.

Base type: `ACadSharp.IO.CadReaderBase[ACadSharp.IO.DwgReaderConfiguration]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IO.ICadReader`, `System.IDisposable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.DwgReader')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.DwgReader(System.IO.Stream stream, ACadSharp.IO.NotificationEventHandler notification = null)
```

Initializes a new instance of the ACadSharp.IO.DwgReader class.

- `stream`: The stream to read from.
- `notification`: Notification handler, sends any message or notification about the reading process.

### .ctor

```text
ACadSharp.IO.DwgReader(System.String filename, ACadSharp.IO.NotificationEventHandler notification = null)
```

Initializes a new instance of the ACadSharp.IO.DwgReader class.

- `filename`: The filename of the file to open.
- `notification`: Notification handler, sends any message or notification about the reading process.

### Read

```text
ACadSharp.CadDocument Read()
```

Documentation inherited from: `base member`.

### Read

```text
static ACadSharp.CadDocument Read(System.IO.Stream stream, ACadSharp.IO.DwgReaderConfiguration configuration, ACadSharp.IO.NotificationEventHandler notification = null)
```

Read a dwg document in a stream.

- `stream`: 
- `configuration`: 
- `notification`: Notification handler, sends any message or notification about the reading process.

### Read

```text
static ACadSharp.CadDocument Read(System.IO.Stream stream, ACadSharp.IO.NotificationEventHandler notification = null)
```

Read a dwg document in a stream.

- `stream`: 
- `notification`: Notification handler, sends any message or notification about the reading process.

### Read

```text
static ACadSharp.CadDocument Read(System.String filename, ACadSharp.IO.DwgReaderConfiguration configuration, ACadSharp.IO.NotificationEventHandler notification = null)
```

Read a dwg document from a file.

- `filename`: 
- `configuration`: 
- `notification`: Notification handler, sends any message or notification about the reading process.

### Read

```text
static ACadSharp.CadDocument Read(System.String filename, ACadSharp.IO.NotificationEventHandler notification = null)
```

Read a dwg document from a file.

- `filename`: 
- `notification`: Notification handler, sends any message or notification about the reading process.

### ReadHeader

```text
ACadSharp.Header.CadHeader ReadHeader()
```

Documentation inherited from: `base member`.

**Remarks:** Refers to AcDb:Header data section.

### ReadPreview

```text
ACadSharp.DwgPreview ReadPreview()
```

Read the preview image of the dwg file.

**Remarks:** Refers to AcDb:Preview data section.

### ReadSummaryInfo

```text
ACadSharp.CadSummaryInfo ReadSummaryInfo()
```

Read the summary info of the dwg file.

**Remarks:** Refers to AcDb:SummaryInfo data section.
