# ACadSharp.Entities.OleObjectType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.OleObjectType`

No upstream type summary is available.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.OleObjectType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Embedded

```text
static ACadSharp.Entities.OleObjectType Embedded = 2
```

The object is embedded within the current document.

### Link

```text
static ACadSharp.Entities.OleObjectType Link = 1
```

The object is linked to an external source.

### Static

```text
static ACadSharp.Entities.OleObjectType Static = 3
```

The object is a static representation.
