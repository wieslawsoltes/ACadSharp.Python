# ACadSharp.IO.CadWriterBase

`class` · `ACadSharp` · CLR name: ``ACadSharp.IO.CadWriterBase`1``

Base class for the CAD writers.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IO.ICadWriter`, `System.IDisposable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.CadWriterBase`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### OnNotification

```text
event ACadSharp.IO.NotificationEventHandler OnNotification
```

Documentation inherited from: `base member`.

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

### Configuration

```text
T Configuration { get; set; }
```

Configuration for the writer.
