# ACadSharp.Tables.Collections.Table

`class` · `ACadSharp` · CLR name: ``ACadSharp.Tables.Collections.Table`1``

No upstream type summary is available.

Base type: `ACadSharp.CadObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[T]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[T]`, `ACadSharp.Tables.Collections.ITable`, `System.Collections.Generic.IEnumerable[T]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.Collections.Table`1')
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
System.Void Add(T item)
```

Add a ACadSharp.Tables.TableEntry to the collection, this method triggers E:ACadSharp.Tables.Collections.Table`1.OnAdd

- `item`: 

### AddRange

```text
System.Void AddRange(System.Collections.Generic.IEnumerable[T] items)
```

Add multiple ACadSharp.Tables.TableEntry to the collection, this method triggers E:ACadSharp.Tables.Collections.Table`1.OnAdd

- `items`: 

### Contains

```text
System.Boolean Contains(System.String key)
```

Determines whether the ACadSharp.Tables.Collections.Table`1 contains the specified key.

- `key`: 

### CreateDefaultEntries

```text
System.Void CreateDefaultEntries()
```

Create the default entries for the table if they don't exist

### GetDefaultEntry

```text
T GetDefaultEntry()
```

Gets the default entry for the table.

**Returns:** The default ACadSharp.Tables.TableEntry.

### GetEnumerator

```text
System.Collections.Generic.IEnumerator[T] GetEnumerator()
```

Documentation inherited from: `base member`.

### GetReferences

```text
System.Collections.Generic.IEnumerable[ACadSharp.CadObject] GetReferences(System.String name)
```

Gets the references to a ACadSharp.Tables.TableEntry by name.

**Returns:** An enumerable of ACadSharp.CadObject that reference the specified table entry.

- `name`: The name of the table entry.

### Remove

```text
T Remove(System.String key)
```

Removes a ACadSharp.Tables.TableEntry from the collection, this method triggers E:ACadSharp.Tables.Collections.Table`1.OnRemove

**Returns:** The removed ACadSharp.Tables.TableEntry

- `key`: key in the table

### TryAdd

```text
T TryAdd(T item)
```

Tries to add the item to the collection, if an item with the same name already exists it returns the existing item.

- `item`: 

### TryGetValue

```text
System.Boolean TryGetValue(System.String key, out T item)
```

Gets the value associated with the specified key.

**Returns:** true if the ACadSharp.Tables.Collections.Table`1 contains an element with the specified key; otherwise, false.

- `key`: The key of the value to get.
- `item`: 

### Count

```text
System.Int32 Count { get; }
```

Gets the number of entries in this table

### Item

```text
T Item[System.String name] { get; }
```

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
