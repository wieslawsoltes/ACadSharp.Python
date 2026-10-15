# ACadSharp.Objects.Collections.MaterialCollection

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Collections.MaterialCollection`

Represents a collection of ACadSharp.Objects.Material objects stored in a CAD dictionary.

Use this collection to access, add, or remove ACadSharp.Objects.Material instances associated with a CAD document. The collection provides dictionary-style access to materials by name.

Base type: `ACadSharp.Objects.Collections.ObjectDictionaryCollection[ACadSharp.Objects.Material]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Objects.Material]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.Material]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.Material]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Collections.MaterialCollection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Collections.MaterialCollection(ACadSharp.Objects.CadDictionary dictionary)
```

Documentation inherited from: `base member`.

### CreateDefaults

```text
System.Void CreateDefaults()
```

Adds the default materials "Global", "ByLayer", and "ByBlock" to the collection if they are not already present.

**Remarks:** This method is typically called to ensure that the collection contains the standard default materials required for typical usage. If any of the default materials already exist in the collection, they are not added again.
