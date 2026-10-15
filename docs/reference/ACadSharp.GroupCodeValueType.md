# ACadSharp.GroupCodeValueType

`enum` · `ACadSharp` · CLR name: `ACadSharp.GroupCodeValueType`

Group codes define the type of the associated value as an integer, a floating-point number, or a string, according to the following table of group code ranges.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.GroupCodeValueType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Bool

```text
static ACadSharp.GroupCodeValueType Bool = 10
```

### Byte

```text
static ACadSharp.GroupCodeValueType Byte = 4
```

### Chunk

```text
static ACadSharp.GroupCodeValueType Chunk = 11
```

### Comment

```text
static ACadSharp.GroupCodeValueType Comment = 12
```

Comment (string)

**Remarks:** Code range : 999

### Double

```text
static ACadSharp.GroupCodeValueType Double = 3
```

Double-precision floating-point value

**Remarks:** Code range : 40-59 | 110-119 | 120-129 | 130-139 | 210-239

### ExtendedDataChunk

```text
static ACadSharp.GroupCodeValueType ExtendedDataChunk = 14
```

### ExtendedDataDouble

```text
static ACadSharp.GroupCodeValueType ExtendedDataDouble = 16
```

### ExtendedDataHandle

```text
static ACadSharp.GroupCodeValueType ExtendedDataHandle = 15
```

### ExtendedDataInt16

```text
static ACadSharp.GroupCodeValueType ExtendedDataInt16 = 17
```

### ExtendedDataInt32

```text
static ACadSharp.GroupCodeValueType ExtendedDataInt32 = 18
```

### ExtendedDataString

```text
static ACadSharp.GroupCodeValueType ExtendedDataString = 13
```

### Handle

```text
static ACadSharp.GroupCodeValueType Handle = 8
```

String representing hexadecimal (hex) handle value

**Remarks:** Code range : 105

### Int16

```text
static ACadSharp.GroupCodeValueType Int16 = 5
```

### Int32

```text
static ACadSharp.GroupCodeValueType Int32 = 6
```

### Int64

```text
static ACadSharp.GroupCodeValueType Int64 = 7
```

### None

```text
static ACadSharp.GroupCodeValueType None = 0
```

### ObjectId

```text
static ACadSharp.GroupCodeValueType ObjectId = 9
```

### Point3D

```text
static ACadSharp.GroupCodeValueType Point3D = 2
```

Double precision 3D point value

**Remarks:** Code range : 10-39

### String

```text
static ACadSharp.GroupCodeValueType String = 1
```

String

**Remarks:** Code range : 0-9
