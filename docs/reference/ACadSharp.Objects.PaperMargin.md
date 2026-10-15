# ACadSharp.Objects.PaperMargin

`struct` · `ACadSharp` · CLR name: `ACadSharp.Objects.PaperMargin`

Represents the unprintable margins of a paper.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.PaperMargin')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.PaperMargin(System.Double left, System.Double bottom, System.Double right, System.Double top)
```

Initializes a new instance of ACadSharp.Objects.PaperMargin.

- `left`: Margin on left side of paper.
- `bottom`: Margin on bottom side of paper.
- `right`: Margin on right side of paper.
- `top`: Margin on top side of paper.

### Bottom

```text
System.Double Bottom { get; set; }
```

Gets or set the size, in millimeters, of unprintable margin on bottom side of paper.

### BottomLeftCorner

```text
CSMath.XY BottomLeftCorner { get; }
```

Gets the bottom left corner of the margin.

### Left

```text
System.Double Left { get; set; }
```

Gets or set the size, in millimeters, of unprintable margin on left side of paper.

### Right

```text
System.Double Right { get; set; }
```

Gets or set the size, in millimeters, of unprintable margin on right side of paper.

### Top

```text
System.Double Top { get; set; }
```

Gets or set the size, in millimeters, of unprintable margin on top side of paper.

### TopCorner

```text
CSMath.XY TopCorner { get; }
```

Gets the top right corer of the margin.
