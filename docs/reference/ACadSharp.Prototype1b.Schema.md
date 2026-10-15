# ACadSharp.Prototype1b.Schema

`class` · `ACadSharp` · CLR name: `ACadSharp.Prototype1b.Schema`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Prototype1b.Schema')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Prototype1b.Schema()
```

### ACIS

```text
static System.String ACIS = AcDb3DSolid_ASM_Data
```

### HANDLE_ATTRIBUTE

```text
static System.String HANDLE_ATTRIBUTE = AcDbDs::HandleAttributeSchema
```

### INDEXED_PROPERTY

```text
static System.String INDEXED_PROPERTY = AcDbDs::IndexedPropertySchema
```

### LEGACY

```text
static System.String LEGACY = AcDbDs::LegacySchema
```

### THUMBNAIL

```text
static System.String THUMBNAIL = AcDb_Thumbnail_Schema
```

### TREATED_AS_OBJECT_DATA

```text
static System.String TREATED_AS_OBJECT_DATA = AcDbDs::TreatedAsObjectDataSchema
```

### Index

```text
System.UInt32 Index { get; set; }
```

### Indices

```text
System.UInt64[] Indices { get; set; }
```

### Name

```text
System.String Name { get; set; }
```

### Properties

```text
ACadSharp.Prototype1b.SchemaProperty[] Properties { get; set; }
```
