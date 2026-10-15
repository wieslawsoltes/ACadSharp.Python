# ACadSharp.CadSystemVariable

`class` · `ACadSharp` · CLR name: `ACadSharp.CadSystemVariable`

No upstream type summary is available.

Base type: `ACadSharp.DxfPropertyBase[ACadSharp.Attributes.CadSystemVariableAttribute]`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.CadSystemVariable')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.CadSystemVariable(System.Reflection.PropertyInfo property)
```

### GetSystemValue

```text
System.Object GetSystemValue(System.Int32 code, ACadSharp.Header.CadHeader header)
```

Retrieves the value of a system variable from the specified CAD header based on the provided code and reference type.

**Remarks:** The method determines how to retrieve the value based on the reference type associated with the system variable. The returned value may be a direct property, a handle, a name, a count, or a raw value, depending on the context. Callers should cast the result to the expected type based on the variable being accessed.

**Returns:** An object representing the value of the requested system variable. The type and meaning of the returned value depend on the reference type and the specified code.

- `code`: The code identifying the system variable to retrieve. The interpretation of this code depends on the reference type associated with the variable.
- `header`: The CAD header object from which to retrieve the system variable value. Cannot be null.

### GetValue

```text
System.Object GetValue(ACadSharp.Header.CadHeader header)
```

Gets the value of the specified property from the provided ACadSharp.Header.CadHeader instance.

**Returns:** The value of the property for the specified ACadSharp.Header.CadHeader instance.

- `header`: The ACadSharp.Header.CadHeader instance from which to retrieve the property value. Cannot be null.

### Name

```text
System.String Name { get; }
```

Gets the name associated with this attribute.
