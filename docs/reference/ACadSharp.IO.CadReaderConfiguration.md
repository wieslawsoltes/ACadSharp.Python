# ACadSharp.IO.CadReaderConfiguration

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.CadReaderConfiguration`

Base configuration for all the ACadSharp.IO.CadReaderBase`1 classes.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.CadReaderConfiguration')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Failsafe

```text
System.Boolean Failsafe { get; set; }
```

The reader will try to continue when an exception is thrown

**Remarks:** The result file may be incomplete or with some objects missing due the error

### KeepUnknownEntities

```text
System.Boolean KeepUnknownEntities { get; set; }
```

The reader will try to read and add to the document all F:ACadSharp.ObjectType.UNLISTED that are linked to a ACadSharp.Classes.DxfClass which may be a proxy or an entity that is not yet supported by ACadSharp, default value is set to false.

**Remarks:** These entities do not contain any geometric information and will be ignored by the writers.

### KeepUnknownNonGraphicalObjects

```text
System.Boolean KeepUnknownNonGraphicalObjects { get; set; }
```

The reader will try to read and add to the document all F:ACadSharp.ObjectType.UNLISTED that are linked to a ACadSharp.Classes.DxfClass which may be a proxy or an NonGraphicalObject that is not yet supported by ACadSharp, default value is set to false.

**Remarks:** These NonGraphicalObjects do not contain any information and will be ignored by the writers.
