# ACadSharp.CadObjectCollection

`class` · `ACadSharp` · CLR name: ``ACadSharp.CadObjectCollection`1``

Collection formed by ACadSharp.CadObject managed by an owner.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IObservableCadCollection[T]`, `System.Collections.Generic.IEnumerable[T]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.CadObjectCollection`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.CadObjectCollection[T](ACadSharp.CadObject owner)
```

Default constructor for a ACadSharp.CadObjectCollection`1 with it's owner assigned.

- `owner`: Owner of the collection.

### OnAdd

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnAdd
```

Documentation inherited from: `base member`.

### OnBeforeRemove

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnBeforeRemove
```

Occurs before an item is removed from the collection.

**Remarks:** Subscribers can use this event to perform actions or validation before the removal operation completes. To cancel the removal, handle the event and set the appropriate property on the event arguments if supported.

### OnRemove

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnRemove
```

Documentation inherited from: `base member`.

### Add

```text
System.Void Add(T item)
```

Add a ACadSharp.CadObject to the collection, this method triggers E:ACadSharp.CadObjectCollection`1.OnAdd.

- `item`: 

- Raises `System.ArgumentException`: 
- Raises `System.ArgumentNullException`: 

### AddRange

```text
System.Void AddRange(System.Collections.Generic.IEnumerable[T] items)
```

Add multiple ACadSharp.CadObject to the collection, this method triggers E:ACadSharp.CadObjectCollection`1.OnAdd.

- `items`: 

### Clear

```text
System.Void Clear()
```

Removes all elements from the Collection.

### GetEnumerator

```text
System.Collections.Generic.IEnumerator[T] GetEnumerator()
```

Documentation inherited from: `base member`.

### Remove

```text
System.Boolean Remove(T item)
```

Removes the specified item from the collection.

**Remarks:** If an event handler for the removal is registered and cancels the operation, the item will not be removed. After successful removal, the item's owner is set to null and a removal event is raised.

**Returns:** true if the item was successfully removed; otherwise, false.

- `item`: The item to remove from the collection.

### Remove

```text
System.Void Remove(System.Collections.Generic.IEnumerable[T] items)
```

Removes multiple items from the collection.

- `items`: The items to remove.

### Count

```text
System.Int32 Count { get; }
```

Gets the number of elements that are contained in the collection.

### Item

```text
T Item[System.Int32 index] { get; }
```

### Owner

```text
ACadSharp.CadObject Owner { get; }
```

Owner of the collection.
