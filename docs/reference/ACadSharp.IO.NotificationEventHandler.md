# ACadSharp.IO.NotificationEventHandler

`delegate` · `ACadSharp` · CLR name: `ACadSharp.IO.NotificationEventHandler`

Represents the method that handles a notification event raised by an object.

Base type: `System.MulticastDelegate`. Inherited members are documented on their declaring type.

Interfaces: `System.ICloneable`, `System.Runtime.Serialization.ISerializable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.NotificationEventHandler')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.NotificationEventHandler(System.Object object, System.IntPtr method)
```

### BeginInvoke

```text
System.IAsyncResult BeginInvoke(System.Object sender, ACadSharp.IO.NotificationEventArgs e, System.AsyncCallback callback, System.Object object)
```

### EndInvoke

```text
System.Void EndInvoke(System.IAsyncResult result)
```

### Invoke

```text
System.Void Invoke(System.Object sender, ACadSharp.IO.NotificationEventArgs e)
```
