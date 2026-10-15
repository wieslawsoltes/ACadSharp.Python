# ACadSharp.CadValue

`class` · `ACadSharp` · CLR name: `ACadSharp.CadValue`

Represents a value entry used in CAD objects.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.CadValue')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.CadValue()
```

### SetValue

```text
System.Void SetValue(System.Object value)
```

Sets the value of the current object, converting or validating the input as required by the current value type.

**Remarks:** The type of the value parameter must match the requirements of the current value type. If the value type is XY or XYZ, the value is converted to the appropriate coordinate type. Supplying a value of an incorrect type will result in an exception.

- `value`: The value to assign. The expected type depends on the current value type: for XY or XYZ, an object implementing IVector; for Long, an int; for Double, a double; for Date, a DateTime; for Handle, an IHandledCadObject; for String or General, a string.

- Raises `System.InvalidOperationException`: Thrown if the current value type does not support assignment or if the value type is unknown.

### SetValue

```text
System.Void SetValue(System.Object value, ACadSharp.CadValueType valueType)
```

Sets the value and specifies its type for the current instance.

- `value`: The value to assign. The type of this object must be compatible with the specified value type.
- `valueType`: The type that describes how the value should be interpreted.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Flags

```text
System.Int32 Flags { get; set; }
```

Gets or sets the flags associated with this value.

### Format

```text
System.String Format { get; set; }
```

Gets or sets the format string used to display the value.

### FormattedValue

```text
System.String FormattedValue { get; set; }
```

Gets or sets the formatted string representation of the value.

### IsEmpty

```text
System.Boolean IsEmpty { get; set; }
```

Gets or sets a value indicating whether this ACadSharp.CadValue is empty.

**Remarks:** This property reads and writes the least significant bit of ACadSharp.CadValue.Flags.

### Units

```text
ACadSharp.CadValueUnitType Units { get; set; }
```

Gets or sets the unit type for this value.

### Value

```text
System.Object Value { get; }
```

Gets or sets the underlying value object. The actual type depends on ACadSharp.CadValue.ValueType.

### ValueType

```text
ACadSharp.CadValueType ValueType { get; set; }
```

Gets or sets the data type of ACadSharp.CadValue.Value.
