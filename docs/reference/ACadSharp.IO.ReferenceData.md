# ACadSharp.IO.ReferenceData

`struct` · `ACadSharp` · CLR name: `ACadSharp.IO.ReferenceData`

Represents a reference to a CAD object identified by a name and/or handle.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.ReferenceData')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.ReferenceData(System.String name, System.Nullable[System.UInt64] handle)
```

Initializes a new instance of the ACadSharp.IO.ReferenceData struct.

- `name`: The name of the referenced object.
- `handle`: The handle of the referenced object.

### Handle

```text
System.Nullable[System.UInt64] Handle { get; }
```

Gets the handle of the referenced object.

### Name

```text
System.String Name { get; }
```

Gets the name of the referenced object.
