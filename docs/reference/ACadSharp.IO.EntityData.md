# ACadSharp.IO.EntityData

`struct` · `ACadSharp` · CLR name: `ACadSharp.IO.EntityData`

Represents the common graphical properties associated with a CAD entity.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.EntityData')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.EntityData(ACadSharp.IO.ReferenceData bookColor, ACadSharp.Color color, System.Boolean isInvisible, ACadSharp.IO.ReferenceData layer, ACadSharp.IO.ReferenceData lineType, System.Double lineTypeScale, ACadSharp.LineWeightType lineWeight)
```

Initializes a new instance of the ACadSharp.IO.EntityData struct.

- `bookColor`: The reference data for the book color.
- `color`: The color of the entity.
- `isInvisible`: A value indicating whether the entity is invisible.
- `layer`: The reference data for the layer.
- `lineType`: The reference data for the line type.
- `lineTypeScale`: The line type scale.
- `lineWeight`: The line weight.

### BookColor

```text
ACadSharp.IO.ReferenceData BookColor { get; }
```

Gets the reference data for the book color of the entity.

### Color

```text
ACadSharp.Color Color { get; }
```

Gets the color of the entity.

### IsInvisible

```text
System.Boolean IsInvisible { get; }
```

Gets a value indicating whether the entity is invisible.

### Layer

```text
ACadSharp.IO.ReferenceData Layer { get; }
```

Gets the reference data for the layer the entity belongs to.

### LineType

```text
ACadSharp.IO.ReferenceData LineType { get; }
```

Gets the reference data for the line type of the entity.

### LineTypeScale

```text
System.Double LineTypeScale { get; }
```

Gets the line type scale applied to the entity.

### LineWeight

```text
ACadSharp.LineWeightType LineWeight { get; }
```

Gets the line weight of the entity.
