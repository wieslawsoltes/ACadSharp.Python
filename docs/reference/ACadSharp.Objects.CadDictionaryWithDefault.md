# ACadSharp.Objects.CadDictionaryWithDefault

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.CadDictionaryWithDefault`

Represents a ACadSharp.Objects.CadDictionaryWithDefault object.

Object name F:ACadSharp.DxfFileToken.ObjectDictionaryWithDefault Dxf class name F:ACadSharp.DxfSubclassMarker.DictionaryWithDefault

Base type: `ACadSharp.Objects.CadDictionary`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.NonGraphicalObject]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.NonGraphicalObject]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.CadDictionaryWithDefault')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.CadDictionaryWithDefault()
```

### .ctor

```text
ACadSharp.Objects.CadDictionaryWithDefault(System.String name, ACadSharp.CadObject defaultEntry)
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### DefaultEntry

```text
ACadSharp.CadObject DefaultEntry { get; set; }
```

Default entry.

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

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
