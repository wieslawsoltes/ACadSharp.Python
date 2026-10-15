# ACadSharp.IO.ReadStage

`enum` · `ACadSharp` · CLR name: `ACadSharp.IO.ReadStage`

Represents the stage of a read operation.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.ReadStage')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Build

```text
static ACadSharp.IO.ReadStage Build = 1
```

The building stage where parsed data is assembled into objects.

### Read

```text
static ACadSharp.IO.ReadStage Read = 0
```

The initial reading stage where raw data is parsed from the file.
