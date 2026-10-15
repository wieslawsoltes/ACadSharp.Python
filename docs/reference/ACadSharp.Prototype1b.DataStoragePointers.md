# ACadSharp.Prototype1b.DataStoragePointers

`class` · `ACadSharp` · CLR name: `ACadSharp.Prototype1b.DataStoragePointers`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Prototype1b.DataStoragePointers')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Prototype1b.DataStoragePointers()
```

### DataIndex

```text
ACadSharp.Prototype1b.DataIndex DataIndex { get; set; }
```

### FreeSpace

```text
ACadSharp.Prototype1b.Segments.FreeSpace FreeSpace { get; set; }
```

Empty areas inside the file which are filled with zeros for the most part

### SchemaIndex

```text
ACadSharp.Prototype1b.SchemaIndex SchemaIndex { get; set; }
```

### SegmentIndex

```text
ACadSharp.Prototype1b.Segments.SegmentIndex SegmentIndex { get; set; }
```
