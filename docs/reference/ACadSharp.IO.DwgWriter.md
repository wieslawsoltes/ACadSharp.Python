# ACadSharp.IO.DwgWriter

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.DwgWriter`

Class for writing a DWG from a ACadSharp.CadDocument.

Base type: `ACadSharp.IO.CadWriterBase[ACadSharp.IO.DwgWriterConfiguration]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IO.ICadWriter`, `System.IDisposable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.DwgWriter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.DwgWriter(System.IO.Stream stream, ACadSharp.CadDocument document)
```

Initializes a new instance of the ACadSharp.IO.DwgWriter class.

- `stream`: 
- `document`: 

### .ctor

```text
ACadSharp.IO.DwgWriter(System.String filename, ACadSharp.CadDocument document)
```

Initializes a new instance of the ACadSharp.IO.DwgWriter class.

- `filename`: 
- `document`: 

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
static System.Void Write(System.IO.Stream stream, ACadSharp.CadDocument document, ACadSharp.IO.DwgWriterConfiguration configuration = null, ACadSharp.IO.NotificationEventHandler notification = null)
```

Write a ACadSharp.CadDocument intio a System.IO.Stream

- `stream`: 
- `document`: 
- `notification`: 

### Write

```text
static System.Void Write(System.String filename, ACadSharp.CadDocument document, ACadSharp.IO.DwgWriterConfiguration configuration = null, ACadSharp.IO.NotificationEventHandler notification = null)
```

Write a ACadSharp.CadDocument into a file

- `filename`: 
- `document`: 
- `configuration`: 
- `notification`: 

### Preview

```text
ACadSharp.DwgPreview Preview { get; set; }
```
