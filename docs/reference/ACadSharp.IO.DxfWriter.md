# ACadSharp.IO.DxfWriter

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.DxfWriter`

Class for writing a DXF from a ACadSharp.CadDocument.

Base type: `ACadSharp.IO.CadWriterBase[ACadSharp.IO.DxfWriterConfiguration]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IO.ICadWriter`, `System.IDisposable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.DxfWriter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.DxfWriter(System.IO.Stream stream, ACadSharp.CadDocument document, System.Boolean binary = False)
```

Initializes a new instance of the ACadSharp.IO.DxfWriter class.

- `stream`: The stream to write into
- `document`: 
- `binary`: 

### .ctor

```text
ACadSharp.IO.DxfWriter(System.String filename, ACadSharp.CadDocument document, System.Boolean binary = False)
```

Initializes a new instance of the ACadSharp.IO.DxfWriter class.

- `filename`: The file to write into.
- `document`: 
- `binary`: 

### Dispose

```text
System.Void Dispose()
```

Documentation inherited from: `base member`.

### Write

```text
System.Void Write()
```

Documentation inherited from: `base member`.

### Write

```text
static System.Void Write(System.IO.Stream stream, ACadSharp.CadDocument document, System.Boolean binary = False, ACadSharp.IO.DxfWriterConfiguration configuration = null, ACadSharp.IO.NotificationEventHandler notification = null)
```

Write a ACadSharp.CadDocument into a System.IO.Stream.

- `stream`: 
- `document`: 
- `binary`: 
- `configuration`: 
- `notification`: 

### Write

```text
static System.Void Write(System.String filename, ACadSharp.CadDocument document, System.Boolean binary = False, ACadSharp.IO.DxfWriterConfiguration configuration = null, ACadSharp.IO.NotificationEventHandler notification = null)
```

Write a ACadSharp.CadDocument into a file.

- `filename`: 
- `document`: 
- `binary`: 
- `configuration`: 
- `notification`: 

### IsBinary

```text
System.Boolean IsBinary { get; }
```

Flag indicating if the dxf will be writen as a binary file
