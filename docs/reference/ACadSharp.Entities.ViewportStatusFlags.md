# ACadSharp.Entities.ViewportStatusFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.ViewportStatusFlags`

viewport status flags

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ViewportStatusFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### AdaptiveGridDisplay

```text
static ACadSharp.Entities.ViewportStatusFlags AdaptiveGridDisplay = 524288
```

Enable adaptive grid display.

### BackClipping

```text
static ACadSharp.Entities.ViewportStatusFlags BackClipping = 4
```

Enables back clipping.

### CurrentlyAlwaysEnabled

```text
static ACadSharp.Entities.ViewportStatusFlags CurrentlyAlwaysEnabled = 32768
```

Currently always enabled.

### DisplayGridBeyondDrawingLimits

```text
static ACadSharp.Entities.ViewportStatusFlags DisplayGridBeyondDrawingLimits = 262144
```

Enables the display of the grid beyond the drawing limits.

### FastZoom

```text
static ACadSharp.Entities.ViewportStatusFlags FastZoom = 128
```

Enables fast zoom.

### FrontClipNotAtEye

```text
static ACadSharp.Entities.ViewportStatusFlags FrontClipNotAtEye = 16
```

Enables front clip not at eye.

### FrontClipping

```text
static ACadSharp.Entities.ViewportStatusFlags FrontClipping = 2
```

Enables front clipping.

### GridMode

```text
static ACadSharp.Entities.ViewportStatusFlags GridMode = 512
```

Enables grid mode.

### HidePlotMode

```text
static ACadSharp.Entities.ViewportStatusFlags HidePlotMode = 2048
```

Enables hide plot mode.

### IsoPairRight

```text
static ACadSharp.Entities.ViewportStatusFlags IsoPairRight = 8192
```

If set and IsoPairTop is not set, then isopair right is enabled.

### IsoPairTop

```text
static ACadSharp.Entities.ViewportStatusFlags IsoPairTop = 4096
```

If set and IsoPairRight is not set, then isopair top is enabled. If both IsoPairTop and IsoPairRight are set, then isopair left is enabled

### IsometricSnapStyle

```text
static ACadSharp.Entities.ViewportStatusFlags IsometricSnapStyle = 1024
```

Enables isometric snap style.

### NonRectangularClipping

```text
static ACadSharp.Entities.ViewportStatusFlags NonRectangularClipping = 65536
```

Enables non-rectangular clipping.

### PerspectiveMode

```text
static ACadSharp.Entities.ViewportStatusFlags PerspectiveMode = 1
```

Enables perspective mode.

### SnapMode

```text
static ACadSharp.Entities.ViewportStatusFlags SnapMode = 256
```

Enables snap mode.

### SubdivisionGridBelowSpacing

```text
static ACadSharp.Entities.ViewportStatusFlags SubdivisionGridBelowSpacing = 1048576
```

Enables subdivision of the grid below the set grid spacing when the grid display is adaptive.

### UcsFollow

```text
static ACadSharp.Entities.ViewportStatusFlags UcsFollow = 8
```

Enables UCS follow.

### UcsIconAtOrigin

```text
static ACadSharp.Entities.ViewportStatusFlags UcsIconAtOrigin = 64
```

Enables UCS icon at origin.

### UcsIconVisibility

```text
static ACadSharp.Entities.ViewportStatusFlags UcsIconVisibility = 32
```

Enables UCS icon visibility.

### ViewportOff

```text
static ACadSharp.Entities.ViewportStatusFlags ViewportOff = 131072
```

Turns the viewport off.

### ViewportZoomLocking

```text
static ACadSharp.Entities.ViewportStatusFlags ViewportZoomLocking = 16384
```

Enables viewport zoom locking.
