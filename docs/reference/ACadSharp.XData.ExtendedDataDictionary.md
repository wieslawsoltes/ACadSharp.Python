# ACadSharp.XData.ExtendedDataDictionary

`class` · `ACadSharp` · CLR name: `ACadSharp.XData.ExtendedDataDictionary`

Dictionary containing all the extended data for a giving ACadSharp.CadObject, each entry is identified with an ACadSharp.Tables.AppId key that identifies the application that has added the collection of Extended Data (XData) into the object.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[ACadSharp.Tables.AppId, ACadSharp.XData.ExtendedData]]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.XData.ExtendedDataDictionary')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.XData.ExtendedDataDictionary(ACadSharp.CadObject owner)
```

Default constructor.

- `owner`: 

### Add

```text
System.Void Add(ACadSharp.Tables.AppId app)
```

Add an empty entry of ExtendedData for a given ACadSharp.Tables.AppId.

- `app`: 

### Add

```text
System.Void Add(ACadSharp.Tables.AppId app, ACadSharp.XData.ExtendedData extendedData)
```

Add ExtendedData for a specific ACadSharp.Tables.AppId to the Dictionary.

- `app`: 
- `extendedData`: 

### Add

```text
System.Void Add(ACadSharp.Tables.AppId app, System.Collections.Generic.IEnumerable[ACadSharp.XData.ExtendedDataRecord] records)
```

Add ExtendedData for a specific ACadSharp.Tables.AppId to the Dictionary.

- `app`: The AppId object.
- `records`: The ExtendedData records.

### Add

```text
System.Void Add(System.String appName)
```

Adds a new application with the specified name.

- `appName`: The name of the application to add. Cannot be null or empty.

### Add

```text
System.Void Add(System.String appName, ACadSharp.XData.ExtendedData extendedData)
```

Adds an application and its associated extended data to the collection.

- `appName`: The name of the application to add. Cannot be null or empty.
- `extendedData`: The extended data associated with the application. Cannot be null.

### Clear

```text
System.Void Clear()
```

Clear all Dictionary entries.

### ContainsKey

```text
System.Boolean ContainsKey(ACadSharp.Tables.AppId app)
```

Check whether a given AppId is in the Dictionary.

- `app`: The AppId object.

### ContainsKeyName

```text
System.Boolean ContainsKeyName(System.String name)
```

Check whether a given AppId is in the Dictionary.

- `name`: The AppId name.

### Get

```text
ACadSharp.XData.ExtendedData Get(ACadSharp.Tables.AppId app)
```

Get ExtendedData for a specific ACadSharp.Tables.AppId from the Dictionary.

- `app`: The AppId object.

### Get

```text
ACadSharp.XData.ExtendedData Get(System.String name)
```

Get the Extended data for a given ACadSharp.Tables.AppId name.

- `name`: 

### GetEnumerator

```text
System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[ACadSharp.Tables.AppId, ACadSharp.XData.ExtendedData]] GetEnumerator()
```

Documentation inherited from: `base member`.

### GetExtendedDataByName

```text
System.Collections.Generic.IDictionary[System.String, ACadSharp.XData.ExtendedData] GetExtendedDataByName()
```

Get the different extended data by it's name.

### TryAdd

```text
ACadSharp.XData.ExtendedData TryAdd(System.String appName, ACadSharp.XData.ExtendedData extendedData)
```

Adds the specified extended data for the given application name if it does not already exist, and returns the stored extended data.

**Remarks:** If extended data for the specified application name already exists, this method does not overwrite it. Use this method to ensure that only one instance of extended data is associated with each application name.

**Returns:** The existing extended data associated with the specified application name if it was already present; otherwise, the newly added extended data.

- `appName`: The name of the application to associate with the extended data. Cannot be null.
- `extendedData`: The extended data to add if no data is already associated with the specified application name. Cannot be null.

### TryGet

```text
System.Boolean TryGet(ACadSharp.Tables.AppId app, out ACadSharp.XData.ExtendedData value)
```

Try to get ExtendedData for a specific ACadSharp.Tables.AppId from the Dictionary.

- `app`: The AppId object.
- `value`: ExtendedData object.

### TryGet

```text
System.Boolean TryGet(System.String name, out ACadSharp.XData.ExtendedData value)
```

Try to get ExtendedData for a specific ACadSharp.Tables.AppId name from the Dictionary.

**Returns:** true, if found.

- `name`: The AppId name.
- `value`: ExtendedData object.

### Document

```text
ACadSharp.CadDocument Document { get; }
```

### Owner

```text
ACadSharp.CadObject Owner { get; }
```

Owner of the Extended Data dictionary.
