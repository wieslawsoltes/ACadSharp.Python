# ACadSharp.Prototype1b.SchemaIndex

`class` · `ACadSharp` · CLR name: `ACadSharp.Prototype1b.SchemaIndex`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Prototype1b.Segments.IPrototype1bSegment`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Prototype1b.SchemaIndex')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Prototype1b.SchemaIndex()
```

### Header

```text
ACadSharp.Prototype1b.SegmentHeader Header { get; set; }
```

### SchemaNames

```text
System.String[] SchemaNames { get; set; }
```

### SchemaPointer

```text
ACadSharp.Prototype1b.SchemaPropertyPointer[] SchemaPointer { get; set; }
```

### SchemaUnknownPropertyPointer

```text
ACadSharp.Prototype1b.SchemaPropertyPointer[] SchemaUnknownPropertyPointer { get; set; }
```

### Unknown1

```text
System.UInt32 Unknown1 { get; set; }
```

### UnknownIndex1

```text
System.UInt32 UnknownIndex1 { get; set; }
```

### UnknownMagic

```text
System.Int64 UnknownMagic { get; set; }
```

### UnknownPropertyEntryPointer

```text
ACadSharp.Prototype1b.SchemaPropertyPointer[] UnknownPropertyEntryPointer { get; set; }
```
