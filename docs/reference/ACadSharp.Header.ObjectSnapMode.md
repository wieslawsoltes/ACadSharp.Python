# ACadSharp.Header.ObjectSnapMode

`enum` · `ACadSharp` · CLR name: `ACadSharp.Header.ObjectSnapMode`

Object snap mode AcDb::OsnapMask

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Header.ObjectSnapMode')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### AllModes

```text
static ACadSharp.Header.ObjectSnapMode AllModes = 16383
```

All snapping modes on

### ApparentIntersection

```text
static ACadSharp.Header.ObjectSnapMode ApparentIntersection = 2048
```

Snap to apparent intersections in the view

### Center

```text
static ACadSharp.Header.ObjectSnapMode Center = 4
```

Snap to center of circles, arcs. and polyline arc segments

### ClearsAllObjectSnaps

```text
static ACadSharp.Header.ObjectSnapMode ClearsAllObjectSnaps = 1024
```

Clears all object snaps

### EndPoint

```text
static ACadSharp.Header.ObjectSnapMode EndPoint = 1
```

Snap to end point of lines, arcs, and to polyline vertices

### Extension

```text
static ACadSharp.Header.ObjectSnapMode Extension = 4096
```

Snap to extensions of lines

### Insertion

```text
static ACadSharp.Header.ObjectSnapMode Insertion = 64
```

Snap to insertion points of blocks, texts, and images.

### Intersection

```text
static ACadSharp.Header.ObjectSnapMode Intersection = 32
```

Snap to intersections of any two drawing objects

### MidPoint

```text
static ACadSharp.Header.ObjectSnapMode MidPoint = 2
```

Snap to mid point of lines, arcs, and polyline segments

### Nearest

```text
static ACadSharp.Header.ObjectSnapMode Nearest = 512
```

Snap to the nearest point on a drawing object

### Node

```text
static ACadSharp.Header.ObjectSnapMode Node = 8
```

Snap to the center of point objects

### None

```text
static ACadSharp.Header.ObjectSnapMode None = 0
```

Switch off all snapping modes

### Parallel

```text
static ACadSharp.Header.ObjectSnapMode Parallel = 8192
```

Parallel lines

### Perpendicular

```text
static ACadSharp.Header.ObjectSnapMode Perpendicular = 128
```

Snap to points which form a perpendicular with the selected object.

### Quadrant

```text
static ACadSharp.Header.ObjectSnapMode Quadrant = 16
```

Snap to circle quadrant points at 0°, 90°, 180°, and 270°.

### SwitchedOff

```text
static ACadSharp.Header.ObjectSnapMode SwitchedOff = 16384
```

Switch off snapping

### Tangent

```text
static ACadSharp.Header.ObjectSnapMode Tangent = 256
```

Snap to tangent points
