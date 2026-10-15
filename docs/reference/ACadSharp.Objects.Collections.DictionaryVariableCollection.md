# ACadSharp.Objects.Collections.DictionaryVariableCollection

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Collections.DictionaryVariableCollection`

Represents a collection of named ACadSharp.Objects.DictionaryVariable stored as key-value pairs, providing methods to add, update, and retrieve variable values by name.

This collection is typically used to manage custom variables within a CAD dictionary context. Variable names are case-insensitive and must be unique within the collection. Adding a variable with an existing name updates its value.

Base type: `ACadSharp.Objects.Collections.ObjectDictionaryCollection[ACadSharp.Objects.DictionaryVariable]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.ICadCollection[ACadSharp.Objects.DictionaryVariable]`, `ACadSharp.IHandledCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.DictionaryVariable]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.DictionaryVariable]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Collections.DictionaryVariableCollection')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Collections.DictionaryVariableCollection(ACadSharp.Objects.CadDictionary dictionary)
```

Documentation inherited from: `base member`.

### AddOrUpdateVariable

```text
System.Void AddOrUpdateVariable(System.String name, System.String value)
```

Adds a variable with the specified name and value to the collection. If a variable with the same name already exists, its value is updated.

- `name`: The name of the variable to add or update. Cannot be null.
- `value`: The value to assign to the variable. Can be null.

### AddVariable

```text
System.Void AddVariable(System.String name, System.String value)
```

Adds a new variable with the specified name and value to the collection if a variable with the same name does not already exist.

- `name`: The name of the variable to add. Cannot be null or empty.
- `value`: The value to assign to the variable. Can be null or empty.

### CreateDefaults

```text
System.Void CreateDefaults()
```

Creates and adds default variables to the collection.

**Remarks:** Call this method to ensure that the collection contains the standard default variables. Calling this method multiple times has no effect on existing entries.

### GetValue

```text
System.String GetValue(System.String name)
```

Retrieves the value associated with the specified variable name.

**Returns:** The value of the variable if found; otherwise, null.

- `name`: The name of the variable whose value to retrieve. Cannot be null.
