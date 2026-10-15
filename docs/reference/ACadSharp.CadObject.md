# ACadSharp.CadObject

`class` · `ACadSharp` · CLR name: `ACadSharp.CadObject`

Represents an element in a CadDocument.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.CadObject')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.CadObject()
```

Default constructor.

### AddReactor

```text
System.Void AddReactor(ACadSharp.CadObject reactor)
```

Add a reactor object linked to this one.

**Remarks:** The ACadSharp.CadObject and its reactors must be in the same ACadSharp.CadDocument to be valid.

- `reactor`: 

### CleanReactors

```text
System.Void CleanReactors()
```

Removes any reactor object that doesn't belong to the same ACadSharp.CadDocument as this ACadSharp.CadObject.

### Clone

```text
ACadSharp.CadObject Clone()
```

Creates a new object that is a copy of the current instance.

**Remarks:** The copy will be unattached from the document or any reference.

**Returns:** A new object that is a copy of this instance.

### CreateExtendedDictionary

```text
ACadSharp.Objects.CadDictionary CreateExtendedDictionary()
```

Creates the extended dictionary if null.

**Returns:** The ACadSharp.Objects.CadDictionary attached to this ACadSharp.CadObject

### IsValid

```text
System.Boolean IsValid(ACadSharp.IO.CadFileFormat format, ACadSharp.ACadVersion version)
```

Determines whether the object is valid and can be written in a CAD file.

**Returns:** True if the object is valid; otherwise, false.

- `format`: The CAD file format.
- `version`: The CAD version.

### IsValid

```text
System.Boolean IsValid(ACadSharp.IO.CadFileFormat format, ACadSharp.ACadVersion version, out System.Collections.Generic.IList[System.String] errors)
```

Determines whether the object is valid and can be written in a CAD file.

**Returns:** True if the object is valid; otherwise, false.

- `format`: The CAD file format.
- `version`: The CAD version.
- `errors`: A list of errors found during the validation.

### RemoveReactor

```text
System.Boolean RemoveReactor(ACadSharp.CadObject reactor)
```

Remove a reactor linked to this object.

- `reactor`: 

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Document

```text
ACadSharp.CadDocument Document { get; }
```

Document where this element belongs.

### ExtendedData

```text
ACadSharp.XData.ExtendedDataDictionary ExtendedData { get; }
```

Extended data attached to this object.

### Handle

```text
System.UInt64 Handle { get; }
```

Documentation inherited from: `base member`.

**Remarks:** If the value is 0 the object is not assigned to a document or a parent.

### HasDynamicSubclass

```text
System.Boolean HasDynamicSubclass { get; }
```

Flag that indicates if this object has a dynamic dxf sublcass.

### ObjectName

```text
System.String ObjectName { get; }
```

The CAD class name of an object.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Get the object type.

### Owner

```text
ACadSharp.IHandledCadObject Owner { get; }
```

Soft-pointer ID/handle to owner object.

### Reactors

```text
System.Collections.Generic.IEnumerable[ACadSharp.CadObject] Reactors { get; }
```

Objects that are attached to this object.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Object Subclass marker.

### XDictionary

```text
ACadSharp.Objects.CadDictionary XDictionary { get; }
```

Extended Dictionary object.

**Remarks:** An extended dictionary can be created using ACadSharp.CadObject.CreateExtendedDictionary.
