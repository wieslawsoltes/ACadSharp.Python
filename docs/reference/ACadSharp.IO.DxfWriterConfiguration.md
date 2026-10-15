# ACadSharp.IO.DxfWriterConfiguration

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.DxfWriterConfiguration`

Configuration for writing DWG files.

Base type: `ACadSharp.IO.CadWriterConfiguration`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.DxfWriterConfiguration')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.DxfWriterConfiguration()
```

### Variables

```text
static System.String[] Variables
```

Variables that must be writen in a dxf file

### AddHeaderVariable

```text
System.Void AddHeaderVariable(System.String name)
```

Add a Header variable name to be added in the dxf document

**Remarks:** The name of the variable must exist in ACadSharp.Header.CadHeader.GetHeaderMap

- `name`: 

- Raises `System.ArgumentException`: 

### RemoveHeaderVariable

```text
System.Boolean RemoveHeaderVariable(System.String name)
```

Remove a Header variable name so is not added in the dxf document

**Remarks:** The name cannot be a in the F:ACadSharp.IO.DxfWriterConfiguration.Variables list

- `name`: 

- Raises `System.ArgumentException`: 

### DecimalPrecision

```text
System.Nullable[System.Int32] DecimalPrecision { get; set; }
```

Gets or sets the double precision for writing the DXF file. If set to null, the default "R" format precision will be used.

### HeaderVariables

```text
System.Collections.Generic.IEnumerable[System.String] HeaderVariables { get; }
```

Header variables to write in the dxf file

### WriteAllHeaderVariables

```text
System.Boolean WriteAllHeaderVariables { get; set; }
```

Flag to write all the header variables in the dxf file

**Remarks:** Some variables are version sensitive, writing all the variables may cause a crash in other applications, to write an specific variable add it to the ACadSharp.IO.DxfWriterConfiguration.AddHeaderVariable(System.String) set

**Value:** false

### WriteOptionalValues

```text
System.Boolean WriteOptionalValues { get; set; }
```

Write the Dxf optional values.

**Remarks:** The values are marked with the attribute flag F:ACadSharp.DxfReferenceType.Optional.

**Value:** default: true
