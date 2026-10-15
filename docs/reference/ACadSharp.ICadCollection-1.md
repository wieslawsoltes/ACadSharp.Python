# ACadSharp.ICadCollection

`interface` · `ACadSharp` · CLR name: ``ACadSharp.ICadCollection`1``

A collection of CAD objects.

Interfaces: `System.Collections.Generic.IEnumerable[T]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.ICadCollection`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### TryAdd

```text
T TryAdd(T item)
```

Tries to add the item to the collection, if an item with the same name already exists it returns the existing item.

**Returns:** The added item or the existing item with the same name.

- `item`: The item to add to the collection.
