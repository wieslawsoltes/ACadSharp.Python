# ACadSharp.Tables.Collections.VPortsTable

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.Collections.VPortsTable`

Represents a collection of ACadSharp.Tables.VPort entries.

Base type: `ACadSharp.Tables.Collections.Table[ACadSharp.Tables.VPort]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Tables.VPort]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Tables.VPort]`, `ACadSharp.Tables.Collections.ITable`, `System.Collections.Generic.IEnumerable[ACadSharp.Tables.VPort]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.Collections.VPortsTable')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Add

```text
System.Void Add(ACadSharp.Tables.VPort item)
```

Documentation inherited from: `base member`.

**Remarks:** VPorts allow duplicated entries with the same name, after the first entry, the others will have their ACadSharp.CadObject.Handle as a prefix.

### GetDefaultEntry

```text
ACadSharp.Tables.VPort GetDefaultEntry()
```

Documentation inherited from: `base member`.

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
