# ACadSharp.Header.ObjectSortingFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Header.ObjectSortingFlags`

Bitmask flags to set the various object sorting types.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Header.ObjectSortingFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### All

```text
static ACadSharp.Header.ObjectSortingFlags All = 127
```

Enable all sorting methods.

### Disabled

```text
static ACadSharp.Header.ObjectSortingFlags Disabled = 0
```

Disables SORTENTS.

### Plotting

```text
static ACadSharp.Header.ObjectSortingFlags Plotting = 32
```

Sorts for plotting.

### Postscript

```text
static ACadSharp.Header.ObjectSortingFlags Postscript = 64
```

Sorts for PostScript output.

### Redraw

```text
static ACadSharp.Header.ObjectSortingFlags Redraw = 4
```

Sorts for redraws.

### Regen

```text
static ACadSharp.Header.ObjectSortingFlags Regen = 16
```

Sorts for REGEN commands.

### Selection

```text
static ACadSharp.Header.ObjectSortingFlags Selection = 1
```

Sorts for object selection.

### Slide

```text
static ACadSharp.Header.ObjectSortingFlags Slide = 8
```

Sorts for MSLIDE command slide creation.

### Snap

```text
static ACadSharp.Header.ObjectSortingFlags Snap = 2
```

Sorts for object snap.
