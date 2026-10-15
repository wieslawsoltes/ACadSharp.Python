# ACadSharp.Entities.DimensionType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Entities.DimensionType`

Dimension type flags.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.DimensionType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Aligned

```text
static ACadSharp.Entities.DimensionType Aligned = 1
```

Aligned.

### Angular

```text
static ACadSharp.Entities.DimensionType Angular = 2
```

Angular 2 lines.

### Angular3Point

```text
static ACadSharp.Entities.DimensionType Angular3Point = 5
```

Angular 3 points.

### BlockReference

```text
static ACadSharp.Entities.DimensionType BlockReference = 32
```

Indicates that the block reference(group code 2) is referenced by this dimension only.

### Diameter

```text
static ACadSharp.Entities.DimensionType Diameter = 3
```

Diameter.

### Linear

```text
static ACadSharp.Entities.DimensionType Linear = 0
```

Rotated, horizontal, or vertical.

### Ordinate

```text
static ACadSharp.Entities.DimensionType Ordinate = 6
```

Ordinate.

### OrdinateTypeX

```text
static ACadSharp.Entities.DimensionType OrdinateTypeX = 64
```

Ordinate type. If set, ordinate is X-type; if not set, ordinate is Y-type.

### Radius

```text
static ACadSharp.Entities.DimensionType Radius = 4
```

Radius.

### TextUserDefinedLocation

```text
static ACadSharp.Entities.DimensionType TextUserDefinedLocation = 128
```

Indicates if the dimension text has been positioned at a user-defined location rather than at the default location.
