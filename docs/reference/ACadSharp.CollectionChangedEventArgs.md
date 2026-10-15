# ACadSharp.CollectionChangedEventArgs

`class` · `ACadSharp` · CLR name: `ACadSharp.CollectionChangedEventArgs`

No upstream type summary is available.

Base type: `System.EventArgs`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.CollectionChangedEventArgs')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.CollectionChangedEventArgs(ACadSharp.CadObject item)
```

Initializes a new instance of the ACadSharp.CollectionChangedEventArgs class with the specified item that is being added or removed from the collection.

- `item`: The item that is being added or removed from the collection.

### Cancel

```text
System.Boolean Cancel { get; set; }
```

Gets or sets a value indicating whether the current operation should be canceled.

**Remarks:** This property is used by the OnBeforeAdd and OnBeforeRemove events to cancel the add or remove operation.

### Item

```text
ACadSharp.CadObject Item { get; }
```

Item that is beeing added or removed from the collection
