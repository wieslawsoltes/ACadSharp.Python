# ACadSharp.IObservableCadCollection

`interface` · `ACadSharp` · CLR name: ``ACadSharp.IObservableCadCollection`1``

Events for an observed cad collection.

Interfaces: `System.Collections.Generic.IEnumerable[T]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IObservableCadCollection`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### OnAdd

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnAdd
```

Event triggers when an object is added to the collection.

### OnRemove

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnRemove
```

Event triggers when an object is removed from the collection.
