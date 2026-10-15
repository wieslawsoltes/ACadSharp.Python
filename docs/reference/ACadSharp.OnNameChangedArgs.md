# ACadSharp.OnNameChangedArgs

`class` · `ACadSharp` · CLR name: `ACadSharp.OnNameChangedArgs`

No upstream type summary is available.

Base type: `System.EventArgs`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.OnNameChangedArgs')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.OnNameChangedArgs(System.String oldName, System.String newName)
```

### NewName

```text
System.String NewName { get; }
```

New name to be assign at the object

### OldName

```text
System.String OldName { get; }
```

Old object name
