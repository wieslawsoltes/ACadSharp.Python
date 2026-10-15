# ACadSharp.IO.CadObjectData

`struct` · `ACadSharp` · CLR name: `ACadSharp.IO.CadObjectData`

Represents metadata and associated information for a CAD object, including its handle, type, name, ownership, and optional entity data.

This struct provides a read-only view of key properties for a CAD object, which may be used for serialization, inspection, or referencing objects within a CAD database. All properties are immutable after construction.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.CadObjectData')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.CadObjectData(ACadSharp.CadObject cadObject, System.Nullable[System.UInt64] ownerHandle = null, System.Nullable[System.UInt64] xDictHandle = null, System.Nullable[ACadSharp.IO.EntityData] entityData = null)
```

Initializes a new instance of the ACadSharp.IO.CadObjectData struct from the specified ACadSharp.CadObject.

- `cadObject`: The CAD object from which to extract handle, type, and name information.
- `ownerHandle`: The optional handle of the owning object.
- `xDictHandle`: The optional handle of the extension dictionary.
- `entityData`: The optional entity-specific data to associate with this object.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### EntityData

```text
System.Nullable[ACadSharp.IO.EntityData] EntityData { get; }
```

Gets the optional entity-specific data associated with this CAD object.

### Handle

```text
System.UInt64 Handle { get; }
```

Gets the unique handle that identifies this CAD object within the database.

### Name

```text
System.String Name { get; }
```

Gets the name of the CAD object, if it implements ACadSharp.INamedCadObject; otherwise, null.

### ObjectName

```text
System.String ObjectName { get; }
```

Gets the name of the CAD object type, which can be used to determine the specific type of object.

### OwnerHandle

```text
System.Nullable[System.UInt64] OwnerHandle { get; }
```

Gets the handle of the owner object, or null if no owner is specified.

### XDictHandle

```text
System.Nullable[System.UInt64] XDictHandle { get; }
```

Gets the handle of the extension dictionary associated with this object, or null if none is assigned.
