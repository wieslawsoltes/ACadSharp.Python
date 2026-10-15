# ACadSharp.Prototype1b.Segments.SegmentIndex

`class` · `ACadSharp` · CLR name: `ACadSharp.Prototype1b.Segments.SegmentIndex`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Prototype1b.Segments.IPrototype1bSegment`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Prototype1b.Segments.SegmentIndex')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Prototype1b.Segments.SegmentIndex()
```

### Header

```text
ACadSharp.Prototype1b.SegmentHeader Header { get; set; }
```

### Pointers

```text
System.Collections.Generic.Dictionary[System.Int32, ACadSharp.Prototype1b.SegmentIndexEntry] Pointers { get; set; }
```
