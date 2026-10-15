# ACadSharp.Tables.TextArrowFitType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Tables.TextArrowFitType`

How dimension text and arrows are arranged when space is not sufficient to place both within the extension lines.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.TextArrowFitType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ArrowsFirst

```text
static ACadSharp.Tables.TextArrowFitType ArrowsFirst = 1
```

Moves arrows first, then text

### BestFit

```text
static ACadSharp.Tables.TextArrowFitType BestFit = 3
```

Moves either text or arrows, whichever fits best

### Both

```text
static ACadSharp.Tables.TextArrowFitType Both = 0
```

Places both text and arrows outside extension lines

### TextFirst

```text
static ACadSharp.Tables.TextArrowFitType TextFirst = 2
```

Moves text first, then arrows
