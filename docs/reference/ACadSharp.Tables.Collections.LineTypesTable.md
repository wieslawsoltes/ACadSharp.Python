# ACadSharp.Tables.Collections.LineTypesTable

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.Collections.LineTypesTable`

Represents a collection of ACadSharp.Tables.LineType entries.

Base type: `ACadSharp.Tables.Collections.Table[ACadSharp.Tables.LineType]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Tables.LineType]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Tables.LineType]`, `ACadSharp.Tables.Collections.ITable`, `System.Collections.Generic.IEnumerable[ACadSharp.Tables.LineType]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.Collections.LineTypesTable')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### GetDefaultEntry

```text
ACadSharp.Tables.LineType GetDefaultEntry()
```

Documentation inherited from: `base member`.

### ByBlock

```text
ACadSharp.Tables.LineType ByBlock { get; }
```

Get the ByBlock entry in the table

### ByLayer

```text
ACadSharp.Tables.LineType ByLayer { get; }
```

Get the ByLayer entry in the table

### Continuous

```text
ACadSharp.Tables.LineType Continuous { get; }
```

Get the Continuous entry in the table

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
