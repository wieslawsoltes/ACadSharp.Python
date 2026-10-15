# ACadSharp.Objects.XRecord

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.XRecord`

Represents a ACadSharp.Objects.XRecord object.

Object name F:ACadSharp.DxfFileToken.ObjectXRecord Dxf class name F:ACadSharp.DxfSubclassMarker.XRecord Is not recommended to modify, add or remove entries to an XRecord unless you know what consequences will cause in the document.

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.XRecord')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.XRecord()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Objects.XRecord(System.String name)
```

Documentation inherited from: `base member`.

### Clear

```text
System.Void Clear()
```

Clears all entries from the collection.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### CreateEntry

```text
ACadSharp.Objects.XRecord.Entry CreateEntry(System.Int32 code, System.Object value)
```

Adds a new entry with the specified code and value to the collection.

**Returns:** The newly created ACadSharp.Objects.XRecord.Entry object.

- `code`: The integer code that identifies the entry. The value should be unique within the collection.
- `value`: The value to associate with the entry. Can be any object, including null.

### CloningFlags

```text
ACadSharp.Objects.DictionaryCloningFlags CloningFlags { get; set; }
```

Duplicate record cloning flag (determines how to merge duplicate entries)

### Entries

```text
System.Collections.Generic.IEnumerable[ACadSharp.Objects.XRecord.Entry] Entries { get; }
```

Gets the collection of ACadSharp.Objects.XRecord.Entry objects associated with this ACadSharp.Objects.XRecord.

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
