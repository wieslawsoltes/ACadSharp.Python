# ACadSharp.DxfProperty

`class` · `ACadSharp` · CLR name: `ACadSharp.DxfProperty`

Represents a property of a CAD object that is associated with one or more DXF codes and provides access to its value and related metadata.

Use the DxfProperty class to map object properties to DXF codes for serialization or processing within DXF-based workflows. The property referenced must be decorated with the DxfCodeValueAttribute. This class supports retrieving DXF code collections, accessing property values from CAD objects, and generating extended data records for use in DXF files.

Base type: `ACadSharp.DxfPropertyBase[ACadSharp.Attributes.DxfCodeValueAttribute]`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.DxfProperty')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.DxfProperty(ACadSharp.DxfProperty value)
```

Initializes a new instance of the DxfProperty class by copying the property information from the specified DxfProperty instance.

- `value`: The DxfProperty instance from which to copy property information. Cannot be null.

### .ctor

```text
ACadSharp.DxfProperty(System.Int32 code, System.Reflection.PropertyInfo property)
```

Creates a dxf property referenced to an object property

**Remarks:** The property must have the ACadSharp.Attributes.DxfCodeValueAttribute

- `code`: assigned value for this property, only useful if the property has multiple codes assigned
- `property`: 

- Raises `System.ArgumentException`: 

### .ctor

```text
ACadSharp.DxfProperty(System.Reflection.PropertyInfo property)
```

Creates a dxf property referenced to an object property

**Remarks:** The property must have the ACadSharp.Attributes.DxfCodeValueAttribute

- `property`: 

- Raises `System.ArgumentException`: 

### GetCollectionCodes

```text
ACadSharp.DxfCode[] GetCollectionCodes()
```

Gets the collection of DXF codes associated with the property, if defined.

**Remarks:** Use this method to retrieve custom DXF code mappings specified by the ACadSharp.Attributes.DxfCollectionCodeValueAttribute on the property. Returns null if the attribute is not present.

**Returns:** An array of ACadSharp.DxfCode values representing the collection codes for the property; or null if no collection codes are defined.

### GetValue

```text
System.Object GetValue[TCadObject](TCadObject obj)
```

Gets the value of the specified property from the given CAD object.

**Returns:** The value of the property for the specified CAD object.

- `obj`: The CAD object instance from which to retrieve the property value. Cannot be null.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### ToXDataRecords

```text
System.Collections.Generic.IEnumerable[ACadSharp.XData.ExtendedDataRecord] ToXDataRecords()
```

Creates a collection of extended data records representing the current object's assigned code and stored value.

**Remarks:** The returned collection always contains at most two records: one for the assigned code and one for the stored value, if present.

**Returns:** An enumerable collection of ACadSharp.XData.ExtendedDataRecord objects containing the assigned code and stored value. Returns an empty collection if the stored value is null.
