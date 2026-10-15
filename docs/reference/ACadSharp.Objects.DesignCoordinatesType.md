# ACadSharp.Objects.DesignCoordinatesType

`enum` · `ACadSharp` · CLR name: `ACadSharp.Objects.DesignCoordinatesType`

No upstream type summary is available.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.DesignCoordinatesType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Geographic

```text
static ACadSharp.Objects.DesignCoordinatesType Geographic = 3
```

Geographic (latitude/longitude).

### LocalGrid

```text
static ACadSharp.Objects.DesignCoordinatesType LocalGrid = 1
```

Local grid.

### ProjectedGrid

```text
static ACadSharp.Objects.DesignCoordinatesType ProjectedGrid = 2
```

Projected grid.

### Unknown

```text
static ACadSharp.Objects.DesignCoordinatesType Unknown = 0
```

Unknown.
