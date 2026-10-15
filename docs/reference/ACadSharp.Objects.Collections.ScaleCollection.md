# ACadSharp.Objects.Collections.ScaleCollection

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Collections.ScaleCollection`

Represents a collection of named ACadSharp.Objects.Scale objects within a CAD dictionary.

This collection provides access to individual ACadSharp.Objects.Scale definitions by name and supports enumeration of all scales in the associated CAD dictionary. Modifications to the collection are reflected in the underlying dictionary.

Base type: `ACadSharp.Objects.Collections.ObjectDictionaryCollection[ACadSharp.Objects.Scale]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Objects.Scale]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.Scale]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.Scale]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Collections.ScaleCollection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Collections.ScaleCollection(ACadSharp.Objects.CadDictionary dictionary)
```

Documentation inherited from: `base member`.

### CreateDefaults

```text
System.Void CreateDefaults()
```

Populates the collection with a standard set of default ACadSharp.Objects.Scale definitions commonly used in technical drawings if they do not already exist.

**Remarks:** This method adds a predefined set of scales to the collection if they are not already present. Calling this method multiple times has no effect on existing entries.
