# ACadSharp.Objects.Collections.GroupCollection

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Collections.GroupCollection`

No upstream type summary is available.

Base type: `ACadSharp.Objects.Collections.ObjectDictionaryCollection[ACadSharp.Objects.Group]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Objects.Group]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.Group]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.Group]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Collections.GroupCollection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Collections.GroupCollection(ACadSharp.Objects.CadDictionary dictionary)
```

### Add

```text
System.Void Add(ACadSharp.Objects.Group entry)
```

Documentation inherited from: `base member`.

### CreateGroup

```text
ACadSharp.Objects.Group CreateGroup(System.Collections.Generic.IEnumerable[ACadSharp.Entities.Entity] entities)
```

Creates a group with a collection of entities.

**Remarks:** The entities must be assigned to the owner ACadSharp.CadDocument of this collection.

- `entities`: 

### CreateGroup

```text
ACadSharp.Objects.Group CreateGroup(System.String name, System.Collections.Generic.IEnumerable[ACadSharp.Entities.Entity] entities)
```

Creates a group with a collection of entities.

**Remarks:** The entities must be assigned to the owner ACadSharp.CadDocument of this collection.

- `name`: 
- `entities`: 
