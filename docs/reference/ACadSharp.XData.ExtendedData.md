# ACadSharp.XData.ExtendedData

`class` · `ACadSharp` · CLR name: `ACadSharp.XData.ExtendedData`

Extended data linked to an ACadSharp.Tables.AppId.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.XData.ExtendedData')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.XData.ExtendedData()
```

Default constructor.

### .ctor

```text
ACadSharp.XData.ExtendedData(System.Collections.Generic.IEnumerable[ACadSharp.XData.ExtendedDataRecord] records)
```

Initialize an instance of ACadSharp.XData.ExtendedData with a collection of records.

- `records`: Records to add to the ACadSharp.XData.ExtendedData.

### AddControlStrings

```text
System.Void AddControlStrings()
```

Make sure that the first and last record are ACadSharp.XData.ExtendedDataControlString.

**Remarks:** The first control string must be the opening one and the last one closing.

### Records

```text
System.Collections.Generic.List[ACadSharp.XData.ExtendedDataRecord] Records { get; }
```

Records contained in this Extended Data instance.
