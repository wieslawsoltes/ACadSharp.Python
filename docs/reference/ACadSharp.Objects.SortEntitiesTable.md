# ACadSharp.Objects.SortEntitiesTable

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.SortEntitiesTable`

Represents a ACadSharp.Objects.SortEntitiesTable object

Object name F:ACadSharp.DxfFileToken.ObjectSortEntsTable Dxf class name F:ACadSharp.DxfSubclassMarker.SortentsTable

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.SortEntitiesTable.Sorter]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.SortEntitiesTable')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### DictionaryEntryName

```text
static System.String DictionaryEntryName = ACAD_SORTENTS
```

Dictionary entry name for the object ACadSharp.Objects.SortEntitiesTable

### Add

```text
System.Void Add(ACadSharp.Entities.Entity entity, System.UInt64 sorterHandle)
```

Sorter attached to an entity.

- `entity`: Entity in the block to be sorted.
- `sorterHandle`: Sorter handle.

- Raises `System.ArgumentException`: 

### Clear

```text
System.Void Clear()
```

Removes all elements in the collection.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### GetEnumerator

```text
System.Collections.Generic.IEnumerator[ACadSharp.Objects.SortEntitiesTable.Sorter] GetEnumerator()
```

Documentation inherited from: `base member`.

### GetSorterHandle

```text
System.UInt64 GetSorterHandle(ACadSharp.Entities.Entity entity)
```

Get the sorter handle of an entity, if is not in the sorter table it will return the entity's handle.

- `entity`: 

### MoveToBottom

```text
System.Void MoveToBottom(ACadSharp.Entities.Entity entity)
```

Moves the specified entity to the bottom of the draw order.

- `entity`: Entity to move to the bottom.

### MoveToTop

```text
System.Void MoveToTop(ACadSharp.Entities.Entity entity)
```

Moves the specified entity to the top of the draw order.

- `entity`: Entity to move to the top.

### OneStepDown

```text
System.Void OneStepDown(ACadSharp.Entities.Entity entity)
```

Moves the specified entity one step down in the draw order. If the entity is not in the table or is already at the bottom, no action is taken.

- `entity`: Entity to move one step down.

### OneStepUp

```text
System.Void OneStepUp(ACadSharp.Entities.Entity entity)
```

Moves the specified entity one step up in the draw order. If the entity is not in the table or is already at the top, no action is taken.

- `entity`: Entity to move one step up.

### Remove

```text
System.Boolean Remove(ACadSharp.Entities.Entity entity)
```

Removes the first occurrence of a specific object from the sorters table.

- `entity`: 

### BlockOwner

```text
ACadSharp.Tables.BlockRecord BlockOwner { get; }
```

Block owner where the table is applied

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
