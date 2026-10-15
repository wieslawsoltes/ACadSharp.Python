# ACadSharp.Classes.DxfClassCollection

`class` · `ACadSharp` · CLR name: `ACadSharp.Classes.DxfClassCollection`

Represents a collection of ACadSharp.Classes.DxfClass objects.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `System.Collections.Generic.ICollection[ACadSharp.Classes.DxfClass]`, `System.Collections.Generic.IEnumerable[ACadSharp.Classes.DxfClass]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Classes.DxfClassCollection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Classes.DxfClassCollection(ACadSharp.CadDocument document)
```

Initializes a new instance of the ACadSharp.Classes.DxfClassCollection class.

- `document`: The CAD document associated with this collection.

### Add

```text
System.Void Add(ACadSharp.Classes.DxfClass item)
```

Add a dxf class to the collection if the ACadSharp.Classes.DxfClass.DxfName is not present.

- `item`: The dxf class to add.

### AddOrUpdate

```text
System.Void AddOrUpdate(ACadSharp.Classes.DxfClass item)
```

Add a dxf class to the collection or updates the existing one if the ACadSharp.Classes.DxfClass.DxfName is already in the collection.

- `item`: The dxf class to add or update.

### Clear

```text
System.Void Clear()
```

Documentation inherited from: `base member`.

### Contains

```text
System.Boolean Contains(ACadSharp.Classes.DxfClass item)
```

Documentation inherited from: `base member`.

### Contains

```text
System.Boolean Contains(System.String dxfname)
```

Determines whether the Collection contains a specific ACadSharp.Classes.DxfClass.DxfName.

**Returns:** true if the Collection contains an element with the specified name; otherwise, false.

- `dxfname`: The name of the dxf class to check.

### CopyTo

```text
System.Void CopyTo(ACadSharp.Classes.DxfClass[] array, System.Int32 arrayIndex)
```

Documentation inherited from: `base member`.

### GetByClassNumber

```text
ACadSharp.Classes.DxfClass GetByClassNumber(System.Int16 id)
```

Gets the dxf class associated with ACadSharp.Classes.DxfClass.ClassNumber.

- `id`: 

### GetByName

```text
ACadSharp.Classes.DxfClass GetByName(System.String dxfname)
```

Gets the dxf class associated with ACadSharp.Classes.DxfClass.DxfName.

- `dxfname`: 

### GetEnumerator

```text
System.Collections.Generic.IEnumerator[ACadSharp.Classes.DxfClass] GetEnumerator()
```

Documentation inherited from: `base member`.

### IncreaseInstanceCount

```text
System.Void IncreaseInstanceCount(ACadSharp.Classes.DxfClass dxfClass)
```

Increases the instance count of a dxf class in the collection. If the dxf class is not present, it adds it to the collection with an initial instance count of 1.

- `dxfClass`: The dxf class whose instance count is to be increased.

### Remove

```text
System.Boolean Remove(ACadSharp.Classes.DxfClass item)
```

Documentation inherited from: `base member`.

### ResetClassNumbers

```text
System.Void ResetClassNumbers()
```

Resets the class numbers of all ACadSharp.Classes.DxfClass objects in the collection to a default value starting from 500.

### TryAdd

```text
System.Boolean TryAdd(ACadSharp.Classes.DxfClass item)
```

Attempts to add a dxf class to the collection if the ACadSharp.Classes.DxfClass.DxfName is not present.

**Returns:** true if the dxf class was added successfully; otherwise, false.

- `item`: The dxf class to add.

### TryGetByClassNumber

```text
System.Boolean TryGetByClassNumber(System.Int16 id, out ACadSharp.Classes.DxfClass result)
```

Gets the dxf class associated with ACadSharp.Classes.DxfClass.ClassNumber.

- `id`: 
- `result`: 

### TryGetByName

```text
System.Boolean TryGetByName(System.String dxfname, out ACadSharp.Classes.DxfClass result)
```

Gets the dxf class associated with ACadSharp.Classes.DxfClass.DxfName.

**Returns:** true if the Collection contains an element with the specified key; otherwise, false.

- `dxfname`: 
- `result`: 

### UpdateDxfClasses

```text
System.Void UpdateDxfClasses()
```

Updates the DXF class collection in the document with a predefined set of class definitions and resets class numbers.

### Count

```text
System.Int32 Count { get; }
```

Documentation inherited from: `base member`.

### IsReadOnly

```text
System.Boolean IsReadOnly { get; }
```

Documentation inherited from: `base member`.
