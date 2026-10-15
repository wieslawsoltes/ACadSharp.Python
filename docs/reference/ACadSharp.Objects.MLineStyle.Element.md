# ACadSharp.Objects.MLineStyle.Element

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.MLineStyle+Element`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MLineStyle+Element')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.MLineStyle.Element()
```

### Clone

```text
ACadSharp.Objects.MLineStyle.Element Clone()
```

Clone the current segment.

### Color

```text
ACadSharp.Color Color { get; set; }
```

Element color.

### LineType

```text
ACadSharp.Tables.LineType LineType { get; set; }
```

Element linetype.

### Offset

```text
System.Double Offset { get; set; }
```

Element offset.

### Owner

```text
ACadSharp.Objects.MLineStyle Owner { get; }
```

Line type where this segment belongs.
