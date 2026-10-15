# ACadSharp.Objects.Collections.ColorCollection

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Collections.ColorCollection`

Represents a collection of named ACadSharp.Objects.BookColor definitions stored in a CAD dictionary.

This collection provides access to individual ACadSharp.Objects.BookColor definitions by name and supports enumeration of all colors in the associated CAD dictionary. Modifications to the collection are reflected in the underlying dictionary.

Base type: `ACadSharp.Objects.Collections.ObjectDictionaryCollection[ACadSharp.Objects.BookColor]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Objects.BookColor]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.BookColor]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.BookColor]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Collections.ColorCollection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Collections.ColorCollection(ACadSharp.Objects.CadDictionary dictionary)
```

Documentation inherited from: `base member`.
