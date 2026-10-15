# ACadSharp.Tables.TableEntry

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.TableEntry`

No upstream type summary is available.

Base type: `ACadSharp.CadObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.TableEntry')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.TableEntry(System.String name)
```

Default constructor.

- `name`: Name for the entry, must be unique is added to a ACadSharp.CadDocument.

- Raises `System.ArgumentNullException`: 

### OnNameChanged

```text
event System.EventHandler[ACadSharp.OnNameChangedArgs] OnNameChanged
```

Event occurs when the ACadSharp.Tables.TableEntry.Name changes.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### IsValid

```text
System.Boolean IsValid(ACadSharp.IO.CadFileFormat format, ACadSharp.ACadVersion version, out System.Collections.Generic.IList[System.String] errors)
```

Documentation inherited from: `base member`.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Flags

```text
ACadSharp.Tables.StandardFlags Flags { get; set; }
```

Standard flags

### Name

```text
System.String Name { get; set; }
```

Specifies the name of the object

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
