# ACadSharp.Tables.ViewModeType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Tables.ViewModeType`

No upstream type summary is available.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.ViewModeType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### BackClipping

```text
static ACadSharp.Tables.ViewModeType BackClipping = 4
```

Back clipping

### Follow

```text
static ACadSharp.Tables.ViewModeType Follow = 8
```

### FrontClipping

```text
static ACadSharp.Tables.ViewModeType FrontClipping = 2
```

Front clipping

### FrontClippingZ

```text
static ACadSharp.Tables.ViewModeType FrontClippingZ = 16
```

Front clipping not at the camera

**Remarks:** If turned on, FRONTZ determines the front clipping plane. If turned off, FRONTZ is ignored, and the front clipping plane passes through the camera point. This setting is ignored if the front-clipping bit 2 is turned off.

### Off

```text
static ACadSharp.Tables.ViewModeType Off = 0
```

Off

### PerspectiveView

```text
static ACadSharp.Tables.ViewModeType PerspectiveView = 1
```

Perspective view
