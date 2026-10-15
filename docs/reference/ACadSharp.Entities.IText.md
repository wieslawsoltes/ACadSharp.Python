# ACadSharp.Entities.IText

`interface` · `ACadSharp` · CLR name: `ACadSharp.Entities.IText`

Common interface for all text entities in the drawing.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.IText')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### AlignmentPoint

```text
CSMath.XYZ AlignmentPoint { get; set; }
```

X-axis direction vector(in WCS).

**Remarks:** A group code 50 (rotation angle in radians) passed as DXF input is converted to the equivalent direction vector (if both a code 50 and codes 11, 21, 31 are passed, the last one wins). This is provided as a convenience for conversions from text objects

### Height

```text
System.Double Height { get; set; }
```

Changes the height of the object.

### InsertPoint

```text
CSMath.XYZ InsertPoint { get; set; }
```

First alignment point(in OCS).

### Rotation

```text
System.Double Rotation { get; }
```

Specifies the rotation angle for the object.

**Value:** The rotation angle in radians.

### Style

```text
ACadSharp.Tables.TextStyle Style { get; set; }
```

Style of this text entity.

### Value

```text
System.String Value { get; set; }
```

Specifies the text string for the entity.
