# ACadSharp.Entities.ProxyGraphics.EdgeTraits

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.EdgeTraits`

Represents the traits and properties of edges in proxy graphics.

This class extends ACadSharp.Entities.ProxyGraphics.PrimitiveTraits to provide edge-specific characteristics used in the representation of proxy graphic entities in AutoCAD documents.

Base type: `ACadSharp.Entities.ProxyGraphics.PrimitiveTraits`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.EdgeTraits')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.EdgeTraits()
```

### LineTypeHandles

```text
System.Collections.Generic.List[System.UInt64] LineTypeHandles { get; }
```

Gets the collection of line type handles associated with this edge.

**Value:** A System.Collections.Generic.List`1 of unsigned 64-bit integers representing handles to line types.
