# DXF and DWG I/O

## Reading and writing

`DxfReader`, `DxfWriter`, `DwgReader` and `DwgWriter` are the upstream types, including their configuration classes and overloads. Pass filesystem paths as strings.

```python
from acadsharp.io import DxfReader, DxfWriter, DwgReader, DwgWriter

cad = DxfReader.Read("source.dxf")
DxfWriter.Write("ascii.dxf", cad)
DxfWriter.Write("binary.dxf", cad, True)
DwgWriter.Write("converted.dwg", cad)
copy = DwgReader.Read("converted.dwg")
```

A drawing's `Header.Version` controls its CAD version. Reader and writer version support, unsupported objects and fidelity limits follow ACadSharp. Consult the pinned upstream README's compatibility matrix and collect notifications when processing unfamiliar drawings.

## Notifications

Readers and writers can report unsupported or malformed content without necessarily failing the whole operation. Retain the notification handler for the duration of the call.

```python
import acadsharp
acadsharp.load()
from ACadSharp.IO import DxfReader, NotificationEventHandler

messages = []

def on_notification(sender, event):
    messages.append(str(event.Message))

handler = NotificationEventHandler(on_notification)
cad = DxfReader.Read("source.dxf", handler)
for message in messages:
    print(message)
```

Use the notification types and signatures listed in the [reference](reference/index.md) if you need notification severity or exceptions. Python callbacks execute inside managed operations; keep handlers short and retain references until the operation completes.

## Reader configuration and deterministic disposal

The instance API exposes reader-specific methods such as reading only a header or tables. Dispose readers and writers explicitly when using instances:

```python
from acadsharp.io import DxfReader, DxfReaderConfiguration

reader = DxfReader("source.dxf")
try:
    reader.Configuration = DxfReaderConfiguration()
    cad = reader.Read()
finally:
    reader.Dispose()
```

The static convenience methods manage their own reader/writer lifetime. The instance forms also accept .NET `System.IO.Stream` instances. Python file objects and `io.BytesIO` are not .NET streams; use `System.IO.MemoryStream` and `System.Array[System.Byte]` when exchanging bytes across the boundary. The reader or writer may own and close the supplied stream; inspect upstream semantics before using it afterward.

## Exceptions

Managed exceptions propagate through Python.NET and can be caught from Python. Avoid suppressing exceptions or notifications when evaluating file fidelity. A successfully written file should still be re-read and checked for the entities and properties your application depends on.

## Known upstream round-trip behavior

The pinned DXF writer does not serialize `CadDocument.SummaryInfo.Title`; the DWG writer does. The managed test suite checks this distinction explicitly. Evaluate preservation of metadata separately from entity geometry when selecting an output format.
