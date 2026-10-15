# ACadSharp.IO.NotificationEventArgs

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.NotificationEventArgs`

Provides data for notification events, including the message, notification type, and any associated exception.

Use this class with event handlers to receive detailed information about notifications, such as informational messages, warnings, or errors. The properties expose the notification message, its type, and an optional exception if the notification is related to an error condition.

Base type: `System.EventArgs`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.NotificationEventArgs')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.NotificationEventArgs(System.String message, ACadSharp.IO.NotificationType notificationType = None, System.Exception exception = null)
```

### Exception

```text
System.Exception Exception { get; }
```

Gets the exception that caused the current operation to fail.

### Message

```text
System.String Message { get; }
```

Gets the message.

### NotificationType

```text
ACadSharp.IO.NotificationType NotificationType { get; }
```

Gets the type of notification.
