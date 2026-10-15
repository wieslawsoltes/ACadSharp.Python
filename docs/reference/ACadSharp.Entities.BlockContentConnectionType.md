# ACadSharp.Entities.BlockContentConnectionType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.BlockContentConnectionType`

The values of this enum indicate how the multileader connects to the content block.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.BlockContentConnectionType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### BasePoint

```text
static ACadSharp.Entities.BlockContentConnectionType BasePoint = 1
```

MultiLeader connects to the block base point.

### BlockExtents

```text
static ACadSharp.Entities.BlockContentConnectionType BlockExtents = 0
```

MultiLeader connects to the block extents.
