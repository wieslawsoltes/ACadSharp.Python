# ACadSharp.Objects.Collections.TableStyleCollection

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Collections.TableStyleCollection`

Represents a collection of named ACadSharp.Objects.TableStyle definitions stored in a CAD dictionary.

This collection provides access to individual ACadSharp.Objects.TableStyle definitions by name and supports enumeration of all table styles in the associated CAD dictionary. Modifications to the collection are reflected in the underlying dictionary.

Base type: `ACadSharp.Objects.Collections.ObjectDictionaryCollection[ACadSharp.Objects.TableStyle]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Objects.TableStyle]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.TableStyle]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.TableStyle]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Collections.TableStyleCollection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Collections.TableStyleCollection(ACadSharp.Objects.CadDictionary dictionary)
```

Documentation inherited from: `base member`.

### CreateDefaults

```text
System.Void CreateDefaults()
```

Adds the default ACadSharp.Objects.TableStyle to the collection if it does not already exist.

**Remarks:** Call this method to ensure that the collection contains a default style entry. If the default style is already present, this method has no effect.
