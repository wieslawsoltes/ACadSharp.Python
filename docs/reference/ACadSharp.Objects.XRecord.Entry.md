# ACadSharp.Objects.XRecord.Entry

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.XRecord+Entry`

Represents a single entry in an ACadSharp.Objects.XRecord object, consisting of a group code and its associated value.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.XRecord+Entry')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### GetReference

```text
ACadSharp.CadObject GetReference()
```

Gets the referenced ACadSharp.CadObject if one is linked and belongs to the same document as the owner.

**Returns:** The referenced ACadSharp.CadObject if a linked object exists and is associated with the same document as the owner; otherwise, null.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Code

```text
System.Int32 Code { get; }
```

Gets the numeric code associated with the current instance.

### GroupCode

```text
ACadSharp.GroupCodeValueType GroupCode { get; }
```

### HasLinkedObject

```text
System.Boolean HasLinkedObject { get; }
```

Gets a value indicating whether this group code is associated with a linked object, such as a handle or object ID.

### Value

```text
System.Object Value { get; set; }
```

Gets or sets the value associated with the current instance.
