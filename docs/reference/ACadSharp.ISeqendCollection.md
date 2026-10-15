# ACadSharp.ISeqendCollection

`interface` · `ACadSharp` · CLR name: `ACadSharp.ISeqendCollection`

No upstream type summary is available.

Interfaces: `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.ISeqendCollection')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### OnSeqendAdded

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnSeqendAdded
```

### OnSeqendRemoved

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnSeqendRemoved
```

### Seqend

```text
ACadSharp.Entities.Seqend Seqend { get; }
```
