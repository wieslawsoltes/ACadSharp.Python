# ACadSharp.Objects.Collections.MLineStyleCollection

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Collections.MLineStyleCollection`

Represents a collection of ACadSharp.Objects.MLineStyle available in the associated CAD dictionary.

This collection provides access to the set of ACadSharp.Objects.MLineStyle objects defined within a CAD dictionary. Use this class to enumerate, retrieve, or manage ACadSharp.Objects.MLineStyle for drawing operations. Changes to the collection affect the styles available for multiline entries in the underlying dictionary.

Base type: `ACadSharp.Objects.Collections.ObjectDictionaryCollection[ACadSharp.Objects.MLineStyle]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Objects.MLineStyle]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.MLineStyle]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.MLineStyle]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Collections.MLineStyleCollection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Collections.MLineStyleCollection(ACadSharp.Objects.CadDictionary dictionary)
```

Documentation inherited from: `base member`.

### CreateDefaults

```text
System.Void CreateDefaults()
```

Adds the default ACadSharp.Objects.MLineStyle to the internal collection if it does not already exist.

**Remarks:** Call this method to ensure that the collection contains the default multiline style. If the default style is already present, this method has no effect.
