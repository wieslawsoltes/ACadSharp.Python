# ACadSharp.Objects.Collections.MLeaderStyleCollection

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Collections.MLeaderStyleCollection`

Represents a collection of ACadSharp.Objects.MultiLeaderStyle objects within a CAD dictionary.

This collection provides access to ACadSharp.Objects.MultiLeaderStyles stored in the underlying CAD dictionary. It enables enumeration, retrieval, and management of ACadSharp.Objects.MultiLeaderStyle definitions used for annotative entities in a drawing.

Base type: `ACadSharp.Objects.Collections.ObjectDictionaryCollection[ACadSharp.Objects.MultiLeaderStyle]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Objects.MultiLeaderStyle]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.MultiLeaderStyle]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.MultiLeaderStyle]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Collections.MLeaderStyleCollection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Collections.MLeaderStyleCollection(ACadSharp.Objects.CadDictionary dictionary)
```

Documentation inherited from: `base member`.

### CreateDefaults

```text
System.Void CreateDefaults()
```

Adds the default ACadSharp.Objects.MultiLeaderStyle to the collection if it does not already exist.

**Remarks:** Call this method to ensure that the collection contains a default style entry. If the default style is already present, this method has no effect.
