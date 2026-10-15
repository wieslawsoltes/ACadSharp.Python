# ACadSharp.SeqendCollection

`class` · `ACadSharp` · CLR name: ``ACadSharp.SeqendCollection`1``

Represents a collection of ACadSharp.CadObject ended by a ACadSharp.Entities.Seqend entity.

Base type: `ACadSharp.CadObjectCollection[T]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IObservableCadCollection[T]`, `ACadSharp.ISeqendCollection`, `System.Collections.Generic.IEnumerable[T]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.SeqendCollection`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.SeqendCollection[T](ACadSharp.CadObject owner)
```

### OnSeqendAdded

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnSeqendAdded
```

### OnSeqendRemoved

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnSeqendRemoved
```

### Add

```text
System.Void Add(T item)
```

Documentation inherited from: `base member`.

### Remove

```text
System.Boolean Remove(T item)
```

Documentation inherited from: `base member`.

### Seqend

```text
ACadSharp.Entities.Seqend Seqend { get; }
```

Sequence end entity for dxf.
