# ACadSharp.Prototype1b.SegmentHeader

`class` · `ACadSharp` · CLR name: `ACadSharp.Prototype1b.SegmentHeader`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Prototype1b.SegmentHeader')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Prototype1b.SegmentHeader()
```

### SIZE

```text
static System.UInt32 SIZE = 48
```

The size of the segment header. The ACadSharp.Prototype1b.SegmentHeader.Name is always 6 characters long and the ACadSharp.Prototype1b.SegmentHeader.AlignmentBytes is always 8 bytes long.

### AlignmentBytes

```text
System.Byte[] AlignmentBytes { get; set; }
```

### DataStorageRevision

```text
System.Int32 DataStorageRevision { get; set; }
```

### IsBlob

```text
System.Int32 IsBlob { get; set; }
```

### Name

```text
System.String Name { get; set; }
```

### ObjectDataAlignmentOffset

```text
System.Int32 ObjectDataAlignmentOffset { get; set; }
```

### SegmentIndex

```text
System.UInt32 SegmentIndex { get; set; }
```

### SegmentSize

```text
System.UInt32 SegmentSize { get; set; }
```

### Signature

```text
System.Int16 Signature { get; set; }
```

### SystemDataAlignmentOffset

```text
System.Int32 SystemDataAlignmentOffset { get; set; }
```

### Unknown1

```text
System.Int32 Unknown1 { get; set; }
```

### Unknown2

```text
System.Int32 Unknown2 { get; set; }
```
