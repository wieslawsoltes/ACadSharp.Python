# ACadSharp.Prototype1b.DataStorage

`class` · `ACadSharp` · CLR name: `ACadSharp.Prototype1b.DataStorage`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Prototype1b.DataStorage')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Prototype1b.DataStorage()
```

### ContainsDataWithHandle

```text
System.Boolean ContainsDataWithHandle(System.UInt64 handle)
```

Checks if a data entry with the given handle exists in the ACadSharp.Prototype1b.DataStorage

**Returns:** Whether or not a data entry with the given handle exists

- `handle`: The handle to check

### GetDataByHandle

```text
System.Byte[] GetDataByHandle(System.UInt64 handle)
```

Get the bytes of the file stored by a data field with the given handle. If the entry references file blobs, they will be resolved.

**Returns:** The bytes of the resolved data entry

- `handle`: The handle of the data entry to resolve

- Raises `System.Collections.Generic.KeyNotFoundException`: 

### GetSchemaByName

```text
ACadSharp.Prototype1b.Schema GetSchemaByName(System.String name)
```

### GetSchemaData

```text
System.Collections.Generic.List[ACadSharp.Prototype1b.DataEntry] GetSchemaData(ACadSharp.Prototype1b.Schema schema)
```

### GetSchemaData

```text
System.Collections.Generic.List[ACadSharp.Prototype1b.DataEntry] GetSchemaData(System.String schemaName)
```

Get all ACadSharp.Prototype1b.DataEntry fields referenced by the given schema. Known schema names are available as constants in the ACadSharp.Prototype1b.Schema class. To get all ACIS data stored in the ACadSharp.Prototype1b.DataStorage for example, pass F:ACadSharp.Prototype1b.Schema.ACIS as schemaName

**Returns:** A list of all data entries referenced by the given schema

- `schemaName`: The schema name to get all data entries for

### ResolveDataEntry

```text
System.Byte[] ResolveDataEntry(ACadSharp.Prototype1b.DataEntry entry)
```

Resolve the bytes of the provided ACadSharp.Prototype1b.DataEntry. If the entry references file blobs, they will be resolved.

**Returns:** The bytes of the resolved data entry

- `entry`: The data entry to resolve

### TryGetDataByHandle

```text
System.Boolean TryGetDataByHandle(System.UInt64 handle, out System.Byte[] data)
```

Get the bytes of the file stored by a data field with the given handle. If the entry references file blobs, they will be resolved.

**Returns:** true when the handle was found and data contains data otherwise false

- `handle`: The handle of the data entry to resolve
- `data`: The bytes of the resolved data entry

### Blobs

```text
System.Collections.Generic.List[ACadSharp.Prototype1b.Segments.Blob01] Blobs { get; set; }
```

Blobs of bytes referenced to by ACadSharp.Prototype1b.DataStorage.DataFields. Embedded files larger than 0x40000 bytes will be split into one or more blobs

### DataFields

```text
System.Collections.Generic.List[ACadSharp.Prototype1b.Segments.DataField] DataFields { get; set; }
```

Fields containing data entries with bytes of embedded files, or references to ACadSharp.Prototype1b.DataStorage.Blobs

### FileHeader

```text
ACadSharp.Prototype1b.FileHeader FileHeader { get; set; }
```

General information about the header of the ACadSharp.Prototype1b.DataStorage and Prototype_1b section

### IndexPointers

```text
ACadSharp.Prototype1b.DataStoragePointers IndexPointers { get; set; }
```

Pointers to individual segments of the Prototype_1b section referenced to by the ACadSharp.Prototype1b.DataStorage.FileHeader

### Item

```text
System.Byte[] Item[ACadSharp.Entities.ModelerGeometry geometry] { get; }
```

Get the bytes of an embedded file for the given ACadSharp.Entities.ModelerGeometry.

**Returns:** The bytes of the embedded file

- `geometry`: The entity to get the stored file data for

### Item

```text
System.Byte[] Item[System.UInt64 handle] { get; }
```

Get the bytes of an embedded file with a given handle. This can be the handle of a ACadSharp.Entities.ModelerGeometry referencing an ACIS file or a handle for a thunbnail

**Returns:** The bytes of the embedded file

- `handle`: The handle of the data entry to get

### PreviousSave

```text
ACadSharp.Prototype1b.PreviousSave PreviousSave { get; set; }
```

Information about file state at last revision

### SchemaFields

```text
System.Collections.Generic.List[ACadSharp.Prototype1b.Segments.SchemaData] SchemaFields { get; set; }
```

All registered Schemes

### SchemaSearch

```text
ACadSharp.Prototype1b.SchemaSearch SchemaSearch { get; set; }
```

The search object to get the data entries associated with schema entries
