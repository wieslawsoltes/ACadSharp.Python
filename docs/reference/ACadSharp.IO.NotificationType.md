# ACadSharp.IO.NotificationType

`enum` · `ACadSharp` · CLR name: `ACadSharp.IO.NotificationType`

Defines the type of notification raised during read/write operations.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.NotificationType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Error

```text
static ACadSharp.IO.NotificationType Error = 3
```

An error occurred during the operation.

### None

```text
static ACadSharp.IO.NotificationType None = 0
```

No notification.

### NotImplemented

```text
static ACadSharp.IO.NotificationType NotImplemented = -1
```

The feature is not yet implemented.

### NotSupported

```text
static ACadSharp.IO.NotificationType NotSupported = 1
```

The feature is not supported.

### Warning

```text
static ACadSharp.IO.NotificationType Warning = 2
```

A warning occurred during the operation.
