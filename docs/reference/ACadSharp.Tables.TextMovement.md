# ACadSharp.Tables.TextMovement

`enum` · `ACadSharp` · CLR name: `ACadSharp.Tables.TextMovement`

Text movement rules.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.TextMovement')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### AddLeaderWhenTextMoved

```text
static ACadSharp.Tables.TextMovement AddLeaderWhenTextMoved = 1
```

Adds a leader when dimension text is moved.

### FreeTextPosition

```text
static ACadSharp.Tables.TextMovement FreeTextPosition = 2
```

Allows text to be moved freely without a leader.

### MoveLineWithText

```text
static ACadSharp.Tables.TextMovement MoveLineWithText = 0
```

Moves the dimension line with dimension text.
