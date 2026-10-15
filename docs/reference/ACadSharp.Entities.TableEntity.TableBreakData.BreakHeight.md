# ACadSharp.Entities.TableEntity.TableBreakData.BreakHeight

`struct` · `ACadSharp` · CLR name: `ACadSharp.Entities.TableEntity+TableBreakData+BreakHeight`

Represents the height and insertion position of a table break segment.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.TableEntity+TableBreakData+BreakHeight')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Height

```text
System.Double Height { get; set; }
```

Gets or sets the height of the break segment.

### Position

```text
CSMath.XYZ Position { get; set; }
```

Gets or sets the position of the break segment.
