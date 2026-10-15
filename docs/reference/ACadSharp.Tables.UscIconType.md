# ACadSharp.Tables.UscIconType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Tables.UscIconType`

Display Ucs icon

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.UscIconType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Off

```text
static ACadSharp.Tables.UscIconType Off = 0
```

Off; No icon is displayed

### OffOrigin

```text
static ACadSharp.Tables.UscIconType OffOrigin = 2
```

Off; if the icon is turned on, it is displayed at the UCS origin, if possible

### OnLower

```text
static ACadSharp.Tables.UscIconType OnLower = 1
```

On; the icon is displayed only in the lower-left corner of the current viewport or layout

### OnOrigin

```text
static ACadSharp.Tables.UscIconType OnOrigin = 3
```

On; Displays the UCS icon at the origin, if possible.
