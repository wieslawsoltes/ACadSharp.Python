# ACadSharp.XData.ExtendedDataRecord

`class` · `ACadSharp` · CLR name: `ACadSharp.XData.ExtendedDataRecord`

Defines an ACadSharp.XData.ExtendedData record.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.XData.ExtendedDataRecord')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Create

```text
static ACadSharp.XData.ExtendedDataRecord Create(ACadSharp.GroupCodeValueType groupCode, System.Object value)
```

Creates a new instance of an appropriate ExtendedDataRecord subclass based on the specified group code and value.

**Remarks:** The type of the returned ExtendedDataRecord depends on the group code provided. The value parameter must be compatible with the expected type for the given group code; otherwise, an exception may occur.

**Returns:** An instance of an ExtendedDataRecord subclass representing the provided value for the specified group code.

- `groupCode`: The group code that determines the type of extended data record to create.
- `value`: The value to be encapsulated in the extended data record. The expected type and format depend on the specified group code.

- Raises `System.NotSupportedException`: Thrown if the specified group code is not supported.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Code

```text
ACadSharp.DxfCode Code { get; }
```

Dxf code which defines the value type.

### RawValue

```text
System.Object RawValue { get; }
```

Raw value as an object.
