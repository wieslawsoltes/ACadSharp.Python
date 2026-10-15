# ACadSharp.IO.ICadReader

`interface` · `ACadSharp` · CLR name: `ACadSharp.IO.ICadReader`

Common interface for the different Cad readers.

Interfaces: `System.IDisposable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.ICadReader')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### OnNotification

```text
event ACadSharp.IO.NotificationEventHandler OnNotification
```

Notification event to get information about the reading process.

**Remarks:** The notification system informs about any issue or non critical errors during the reading.

### OnProgress

```text
event ACadSharp.IO.ProgressEventHandler OnProgress
```

Occurs when progress is reported during a long-running operation.

**Remarks:** Subscribe to this event to receive updates about the progress of the associated operation.

### Read

```text
ACadSharp.CadDocument Read()
```

Read the cad document.

### ReadHeader

```text
ACadSharp.Header.CadHeader ReadHeader()
```

Read the Cad header section of the file.
