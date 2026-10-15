# ACadSharp.Objects.NonGraphicalObject

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.NonGraphicalObject`

The standard class for a basic CAD non-graphical object.

Base type: `ACadSharp.CadObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.NonGraphicalObject')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.NonGraphicalObject()
```

Default constructor.

### .ctor

```text
ACadSharp.Objects.NonGraphicalObject(System.String name)
```

Initialize a ACadSharp.Objects.NonGraphicalObject with an specific name.

- `name`: 

### OnNameChanged

```text
event System.EventHandler[ACadSharp.OnNameChangedArgs] OnNameChanged
```

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Name

```text
System.String Name { get; set; }
```

Documentation inherited from: `base member`.

**Remarks:** The name of a ACadSharp.Objects.NonGraphicalObject will be used as the name of the entry when the owner is a ACadSharp.Objects.CadDictionary otherwise the name may not be saved if there is no dxf code assigned to the ACadSharp.CadObject.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.
