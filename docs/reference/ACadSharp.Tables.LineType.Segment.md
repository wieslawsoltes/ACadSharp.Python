# ACadSharp.Tables.LineType.Segment

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.LineType+Segment`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.LineType+Segment')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.LineType.Segment()
```

### Clone

```text
ACadSharp.Tables.LineType.Segment Clone()
```

Clone the current segment.

### Flags

```text
ACadSharp.Tables.LineTypeShapeFlags Flags { get; set; }
```

Complex line type element type.

### IsLine

```text
System.Boolean IsLine { get; }
```

Get whether this segment is a line (dash).

### IsPoint

```text
System.Boolean IsPoint { get; }
```

Get whether this segment is a point (dot).

### IsShape

```text
System.Boolean IsShape { get; set; }
```

Get or set whether this segment is a shape.

### IsSpace

```text
System.Boolean IsSpace { get; }
```

Get whether this segment is a space.

### IsText

```text
System.Boolean IsText { get; set; }
```

Get or set whether this segment is a text.

### Length

```text
System.Double Length { get; set; }
```

Dash, dot or space length.

**Remarks:** Negative lengths represents a space, zero a dot and a positive value a line segment.

### Offset

```text
CSMath.XY Offset { get; set; }
```

Offset.

### Owner

```text
ACadSharp.Tables.LineType Owner { get; }
```

Line type where this segment belongs.

### Rotation

```text
System.Double Rotation { get; set; }
```

Rotation value in radians of embedded shape or text.

### Scale

```text
System.Double Scale { get; set; }
```

Scale value.

### ShapeNumber

```text
System.Int16 ShapeNumber { get; set; }
```

Shape number.

### Style

```text
ACadSharp.Tables.TextStyle Style { get; set; }
```

Pointer to STYLE object (one per element if code 74 > 0)

### Text

```text
System.String Text { get; set; }
```

Text string.

**Remarks:** Only present if F:ACadSharp.Tables.LineTypeShapeFlags.Text is present.
