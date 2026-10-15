# ACadSharp.Objects.Collections.ObjectDictionaryCollection

`class` · `ACadSharp` · CLR name: ``ACadSharp.Objects.Collections.ObjectDictionaryCollection`1``

Object collection linked to a dictionary.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[T]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[T]`, `System.Collections.Generic.IEnumerable[T]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Collections.ObjectDictionaryCollection`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### OnAdd

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnAdd
```

### OnRemove

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnRemove
```

### Add

```text
System.Void Add(T entry)
```

Add an entry to the collection

- `entry`: 

### Clear

```text
System.Void Clear()
```

Removes all keys and values from the ACadSharp.Objects.Collections.ObjectDictionaryCollection`1.

### ContainsKey

```text
System.Boolean ContainsKey(System.String key)
```

Determines whether the ACadSharp.Objects.Collections.ObjectDictionaryCollection`1 contains the specified key.

- `key`: The key to locate in the ACadSharp.Objects.Collections.ObjectDictionaryCollection`1

### GetEntry

```text
T GetEntry(System.String name)
```

Retrieves the entry associated with the specified name.

**Returns:** The entry associated with the specified name.

- `name`: The name of the entry to locate. Cannot be null.

### GetEnumerator

```text
System.Collections.Generic.IEnumerator[T] GetEnumerator()
```

Documentation inherited from: `base member`.

### GetReferences

```text
System.Collections.Generic.IEnumerable[ACadSharp.CadObject] GetReferences(System.String name)
```

Retrieves the references associated with the specified name.

**Returns:** An enumerable collection of CAD objects that reference the specified entry.

- `name`: The name of the entry whose references are to be retrieved.

### Remove

```text
System.Boolean Remove(System.String name)
```

Remove an entry from the collection.

**Returns:** true if the entry was successfully removed; otherwise, false.

- `name`: The name of the entry to remove.

### Remove

```text
System.Boolean Remove(System.String name, out T entry)
```

Remove an entry from the collection.

**Returns:** true if the entry was successfully removed; otherwise, false.

- `name`: The name of the entry to remove.
- `entry`: When this method returns, contains the entry that was removed, if the removal was successful; otherwise, the default value for the type of the entry parameter.

### TryAdd

```text
T TryAdd(T item)
```

Documentation inherited from: `base member`.

### TryGet

```text
System.Boolean TryGet(System.String name, out T entry)
```

Attempts to retrieve the entry associated with the specified name.

**Returns:** true if an entry with the specified name is found; otherwise, false.

- `name`: The name of the entry to locate. Cannot be null.
- `entry`: When this method returns, contains the entry associated with the specified name, if the name is found; otherwise, the default value for the type of the entry parameter. This parameter is passed uninitialized.

### Document

```text
ACadSharp.CadDocument Document { get; }
```

### Handle

```text
System.UInt64 Handle { get; }
```

Documentation inherited from: `base member`.

### Item

```text
T Item[System.String key] { get; }
```
