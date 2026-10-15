# ACadSharp.Objects.WipeoutFrameType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Objects.WipeoutFrameType`

Controls the display of frames for wipeout objects.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.WipeoutFrameType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### DisplayAndPlotted

```text
static ACadSharp.Objects.WipeoutFrameType DisplayAndPlotted = 1
```

Frames are displayed and plotted.

### DisplayNoPlotted

```text
static ACadSharp.Objects.WipeoutFrameType DisplayNoPlotted = 2
```

Frames are displayed, but not plotted.

### NoDisplayOrPlotted

```text
static ACadSharp.Objects.WipeoutFrameType NoDisplayOrPlotted = 0
```

Frames are not displayed or plotted.

**Remarks:** Frames are temporarily displayed for object selection and selection preview.
