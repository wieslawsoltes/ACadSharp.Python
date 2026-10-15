# ACadSharp.Header.DimensionAssociation

`enum` · `ACadSharp` · CLR name: `ACadSharp.Header.DimensionAssociation`

Controls the associativity of dimension objects.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Header.DimensionAssociation')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### CreateAssociativeDimensions

```text
static ACadSharp.Header.DimensionAssociation CreateAssociativeDimensions = 2
```

Creates associative dimension objects; the elements of the dimension are formed into a single object and one or more definition points of the dimension are coupled with association points on geometric objects

### CreateExplodedDimensions

```text
static ACadSharp.Header.DimensionAssociation CreateExplodedDimensions = 0
```

Creates exploded dimensions; there is no association between elements of the dimension, and the lines, arcs, arrowheads, and text of a dimension are drawn as separate objects

### CreateNonAssociativeDimensions

```text
static ACadSharp.Header.DimensionAssociation CreateNonAssociativeDimensions = 1
```

Creates non-associative dimension objects; the elements of the dimension are formed into a single object, and if the definition point on the object moves, then the dimension value is updated
