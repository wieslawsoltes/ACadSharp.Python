# ACadSharp.Objects.Collections.LayoutCollection

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Collections.LayoutCollection`

Represents a collection of named ACadSharp.Objects.Layout definitions stored in a CAD dictionary.

This collection provides access to individual ACadSharp.Objects.Layout definitions by name and supports enumeration of all layouts in the associated CAD dictionary. Modifications to the collection are reflected in the underlying dictionary.

Base type: `ACadSharp.Objects.Collections.ObjectDictionaryCollection[ACadSharp.Objects.Layout]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Objects.Layout]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.Layout]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.Layout]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Collections.LayoutCollection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Collections.LayoutCollection(ACadSharp.Objects.CadDictionary dictionary)
```

Documentation inherited from: `base member`.

### Remove

```text
System.Boolean Remove(System.String name, out ACadSharp.Objects.Layout entry)
```

Documentation inherited from: `base member`.
