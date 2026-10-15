# ACadSharp.DxfPropertyBase

`class` · `ACadSharp` · CLR name: ``ACadSharp.DxfPropertyBase`1``

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.DxfPropertyBase`1')
```

This is an open generic type with 1 parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### GetRawValue

```text
System.Object GetRawValue(ACadSharp.CadObject obj)
```

### SetValue

```text
System.Void SetValue[TCadObject](System.Int32 code, TCadObject obj, System.Object value)
```

Sets the value of a specified property on a CAD object, converting the value as needed based on the property's type.

**Remarks:** This method supports setting values for various property types, including vectors (CSMath.XY and CSMath.XYZ), colors (ACadSharp.Color), margins (ACadSharp.Objects.PaperMargin), transparency (ACadSharp.Transparency), and other primitive or enum types. The behavior of the method depends on the property's type and the provided code.

- `code`: A code that determines how the value should be interpreted or applied. The interpretation of this code depends on the property's type.
- `obj`: The CAD object whose property value is being set. Cannot be null.
- `value`: The value to set for the property. The value will be converted to the appropriate type based on the property's type.

### SetValue

```text
System.Void SetValue[TCadObject](TCadObject obj, System.Object value)
```

Set the value for the property using the AssignedCode

- `obj`: 
- `value`: 

- Raises `System.InvalidOperationException`: 

### AssignedCode

```text
System.Int32 AssignedCode { get; }
```

Gets the code currently assigned to this instance.

**Remarks:** If an explicit assigned code is not set, the value is determined based on the associated DXF codes. If there is exactly one DXF code, that code is returned; otherwise, an invalid code value is returned.

### DxfCodes

```text
System.Int32[] DxfCodes { get; }
```

Gets the collection of DXF group codes associated with the attribute data.

**Remarks:** DXF group codes identify the type and meaning of each value in the attribute data according to the DXF specification. The order of codes in the array corresponds to the order of values in the attribute data.

### GroupCode

```text
ACadSharp.GroupCodeValueType GroupCode { get; }
```

Gets the group code value associated with this instance.

### ReferenceType

```text
ACadSharp.DxfReferenceType ReferenceType { get; }
```

Gets the type of reference associated with the attribute.

### StoredValue

```text
System.Object StoredValue { get; set; }
```

Gets or sets the value associated with the current group code, using the appropriate type based on the group code definition.

**Remarks:** The type of the value must match the expected type for the group code as determined by the DXF specification. Assigning a value of an incorrect type will result in an exception. Supported types include string, numeric types, boolean, byte arrays, and custom handled objects, depending on the group code. When setting this property, the value is automatically converted or validated according to the group code's requirements.
