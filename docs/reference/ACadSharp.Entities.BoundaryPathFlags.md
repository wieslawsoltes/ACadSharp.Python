# ACadSharp.Entities.BoundaryPathFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.BoundaryPathFlags`

Defines the boundary path type of the hatch.

Bit flag.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.BoundaryPathFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Default

```text
static ACadSharp.Entities.BoundaryPathFlags Default = 0
```

Default.

### Derived

```text
static ACadSharp.Entities.BoundaryPathFlags Derived = 4
```

Derived.

### DoesNotSupportScale

```text
static ACadSharp.Entities.BoundaryPathFlags DoesNotSupportScale = 1024
```

The bounding type does not support scaling.

### Duplicate

```text
static ACadSharp.Entities.BoundaryPathFlags Duplicate = 256
```

Duplicate loop.

### External

```text
static ACadSharp.Entities.BoundaryPathFlags External = 1
```

External.

### ForceAnnoAllVisible

```text
static ACadSharp.Entities.BoundaryPathFlags ForceAnnoAllVisible = 2048
```

Forces all annotatives to be visible.

### IsAnnotative

```text
static ACadSharp.Entities.BoundaryPathFlags IsAnnotative = 512
```

The bounding area is an annotative block.

### IsAnnotativeBlock

```text
static ACadSharp.Entities.BoundaryPathFlags IsAnnotativeBlock = 8192
```

Describes if the hatch is an annotative block.

### NotClosed

```text
static ACadSharp.Entities.BoundaryPathFlags NotClosed = 32
```

Loop is not closed.

### OrientToPaper

```text
static ACadSharp.Entities.BoundaryPathFlags OrientToPaper = 4096
```

Orients hatch loop to paper.

### Outermost

```text
static ACadSharp.Entities.BoundaryPathFlags Outermost = 16
```

Outermost.

### Polyline

```text
static ACadSharp.Entities.BoundaryPathFlags Polyline = 2
```

Polyline.

### SelfIntersecting

```text
static ACadSharp.Entities.BoundaryPathFlags SelfIntersecting = 64
```

Self-intersecting loop.

### TextIsland

```text
static ACadSharp.Entities.BoundaryPathFlags TextIsland = 128
```

Text loop surrounded by an even number of loops.

### Textbox

```text
static ACadSharp.Entities.BoundaryPathFlags Textbox = 8
```

Text box.
