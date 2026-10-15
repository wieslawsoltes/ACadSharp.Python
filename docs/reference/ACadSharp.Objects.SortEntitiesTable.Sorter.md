# ACadSharp.Objects.SortEntitiesTable.Sorter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.SortEntitiesTable+Sorter`

Entity sorter based in their position in the collection.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable[ACadSharp.Objects.SortEntitiesTable.Sorter]`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.SortEntitiesTable+Sorter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.SortEntitiesTable.Sorter(ACadSharp.Entities.Entity entity, System.UInt64 handle)
```

Sorter constructor with the entity and handle.

- `entity`: Entity in the block to be sorted.
- `handle`: Sorter handle.

### CompareTo

```text
System.Int32 CompareTo(ACadSharp.Objects.SortEntitiesTable.Sorter other)
```

Documentation inherited from: `base member`.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Entity

```text
ACadSharp.Entities.Entity Entity { get; set; }
```

Entity to set the order to.

### SortHandle

```text
System.UInt64 SortHandle { get; set; }
```

Sorter handle, if this doesn't point to an entity, the value will match with ACadSharp.Objects.SortEntitiesTable.Sorter.Entity's handle.
