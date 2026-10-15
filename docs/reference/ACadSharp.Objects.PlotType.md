# ACadSharp.Objects.PlotType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Objects.PlotType`

Defines the portion of paper space to output to the media

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.PlotType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### DrawingExtents

```text
static ACadSharp.Objects.PlotType DrawingExtents = 1
```

Drawing extents

### DrawingLimits

```text
static ACadSharp.Objects.PlotType DrawingLimits = 2
```

Drawing limits

### LastScreenDisplay

```text
static ACadSharp.Objects.PlotType LastScreenDisplay = 0
```

Last screen display

### LayoutInformation

```text
static ACadSharp.Objects.PlotType LayoutInformation = 5
```

Layout information

### View

```text
static ACadSharp.Objects.PlotType View = 3
```

View specified by the plot view name

### Window

```text
static ACadSharp.Objects.PlotType Window = 4
```

Window specified by the upper-right and bottom-left window corners
