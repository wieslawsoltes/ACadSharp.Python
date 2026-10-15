# ACadSharp.Entities.MText

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.MText`

Represents a ACadSharp.Entities.MText entity.

Object name F:ACadSharp.DxfFileToken.EntityMText Dxf class name F:ACadSharp.DxfSubclassMarker.MText

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.Entities.IText`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.MText')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.MText()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Entities.MText(System.String value)
```

Initializes a new instance of the ACadSharp.Entities.MText class with the specified text value.

- `value`: The text value to initialize the instance with. Cannot be null.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### GetPlainTextLines

```text
System.String[] GetPlainTextLines()
```

Splits the plain text into an array of lines based on common line break sequences.

**Remarks:** The method splits the text using the following line break sequences: carriage return and line feed ("\r\n"), carriage return ("\r"), line feed ("\n"), and the Unicode paragraph separator ("\P"). The resulting array includes all lines, including empty ones.

**Returns:** An array of strings, where each string represents a line of text. The array may contain empty strings if the plain text includes consecutive line break sequences.

### GetTextLines

```text
System.String[] GetTextLines()
```

Splits the text into an array of lines based on common line break sequences.

**Remarks:** The method splits the text using the following line break sequences: carriage return and line feed ("\r\n"), carriage return ("\r"), line feed ("\n"), and the Unicode paragraph separator ("\P"). The resulting array includes all lines, including empty ones.

**Returns:** An array of strings, where each string represents a line of text. The array may contain empty strings if the text includes consecutive line break sequences.

### AlignmentPoint

```text
CSMath.XYZ AlignmentPoint { get; set; }
```

Documentation inherited from: `base member`.

### AttachmentPoint

```text
ACadSharp.Entities.AttachmentPointType AttachmentPoint { get; set; }
```

Attachment point

### BackgroundColor

```text
ACadSharp.Color BackgroundColor { get; set; }
```

Background fill color

**Remarks:** Color to use for background fill when group code 90 is 1.

### BackgroundFillFlags

```text
ACadSharp.Entities.BackgroundFillFlags BackgroundFillFlags { get; set; }
```

Background fill setting

### BackgroundScale

```text
System.Double BackgroundScale { get; set; }
```

Determines how much border there is around the text.

### BackgroundTransparency

```text
ACadSharp.Transparency BackgroundTransparency { get; set; }
```

Transparency of background fill color

### ColumnData

```text
ACadSharp.Entities.MText.TextColumnData ColumnData { get; }
```

Gets or sets the text column data associated with this instance.

### DrawingDirection

```text
ACadSharp.Entities.DrawingDirectionType DrawingDirection { get; set; }
```

Drawing direction

### HasColumns

```text
System.Boolean HasColumns { get; }
```

Gets a value indicating whether the current object contains any columns.

### Height

```text
System.Double Height { get; set; }
```

Documentation inherited from: `base member`.

### HorizontalWidth

```text
System.Double HorizontalWidth { get; set; }
```

Horizontal width of the characters that make up the mtext entity. This value will always be equal to or less than the value of group code 41

**Remarks:** read-only, ignored if supplied

### InsertPoint

```text
CSMath.XYZ InsertPoint { get; set; }
```

A 3D WCS coordinate representing the insertion or origin point.

### IsAnnotative

```text
System.Boolean IsAnnotative { get; set; }
```

### LineSpacing

```text
System.Double LineSpacing { get; set; }
```

Mtext line spacing factor.

**Remarks:** Percentage of default (3-on-5) line spacing to be applied.Valid values range from 0.25 to 4.00

### LineSpacingStyle

```text
ACadSharp.Entities.LineSpacingStyleType LineSpacingStyle { get; set; }
```

Mtext line spacing style.

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Documentation inherited from: `base member`.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.

### PlainText

```text
System.String PlainText { get; }
```

Gets the plain text representation of the processed value.

**Remarks:** This property processes the underlying value and returns its plain text equivalent. The parsing operation may involve removing formatting or extracting meaningful content.

### RectangleHeight

```text
System.Double RectangleHeight { get; set; }
```

Reference rectangle height.

### RectangleWidth

```text
System.Double RectangleWidth { get; set; }
```

Reference rectangle width.

### Rotation

```text
System.Double Rotation { get; }
```

Documentation inherited from: `base member`.

**Remarks:** The rotation is only valid if the ACadSharp.Entities.MText.Normal is set to the Z axis.

### Style

```text
ACadSharp.Tables.TextStyle Style { get; set; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Value

```text
System.String Value { get; set; }
```

Documentation inherited from: `base member`.

### VerticalHeight

```text
System.Double VerticalHeight { get; set; }
```

Vertical height of the mtext entity

**Remarks:** read-only, ignored if supplied
