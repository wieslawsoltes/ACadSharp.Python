# ACadSharp.IO.ICadWriter

`interface` · `ACadSharp` · CLR name: `ACadSharp.IO.ICadWriter`

Interface for writing a ACadSharp.CadDocument into a stream.

Interfaces: `System.IDisposable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.ICadWriter')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### OnNotification

```text
event ACadSharp.IO.NotificationEventHandler OnNotification
```

Notification event to get information about the writing process.

**Remarks:** The notification system informs about any issue or non critical errors during the writing.

### Write

```text
System.Void Write()
```

Write the ACadSharp.CadDocument into the stream.
