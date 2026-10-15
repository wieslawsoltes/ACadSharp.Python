# ACadSharp.Objects.TableStyle.CellBorder

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.TableStyle+CellBorder`

Represents the border settings for a cell, including appearance, visibility, and style options.

Use this class to configure the visual and printing characteristics of cell borders in a drawing or table. The properties allow customization of color, line weight, border type, and visibility. Changes to these settings affect how borders are displayed in the editor and when plotted or printed.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.TableStyle+CellBorder')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.TableStyle.CellBorder(ACadSharp.Objects.TableStyle.CellEdgeFlags edgeFlags)
```

Initializes a new instance of the CellBorder class with the specified edge flags.

- `edgeFlags`: The set of edge flags that define which borders are applied to the cell.

### ApplyBorder

```text
System.Boolean ApplyBorder { get; set; }
```

Gets or sets a value indicating whether a border is applied.

### Color

```text
ACadSharp.Color Color { get; set; }
```

Gets or sets the color associated with the entity.

### DoubleLineSpacing

```text
System.Double DoubleLineSpacing { get; set; }
```

Gets or sets the spacing distance between parallel lines in a double-line entity.

**Remarks:** The value determines the distance between the two lines when rendering double-line geometry. Adjust this property to control the visual separation of the lines. The unit of measurement is typically consistent with the drawing's coordinate system.

### EdgeFlags

```text
ACadSharp.Objects.TableStyle.CellEdgeFlags EdgeFlags { get; }
```

Gets the set of flags that describe the characteristics of the cell's edges.

**Remarks:** Use these flags to determine which edges of the cell have specific properties, such as visibility or formatting. The meaning of each flag is defined by the CellEdgeFlags enumeration.

### IsInvisible

```text
System.Boolean IsInvisible { get; set; }
```

Gets or sets a value indicating whether the border is invisible. Invisible borders are not plotted and do not print, but they are still visible in the drawing editor.

### LineWeight

```text
ACadSharp.LineWeightType LineWeight { get; set; }
```

Gets or sets the line weight to use when rendering the entity.

### PropertyOverrideFlags

```text
ACadSharp.Objects.TableStyle.BorderPropertyFlags PropertyOverrideFlags { get; set; }
```

Gets or sets the set of flags that specify which border properties are overridden.

### Type

```text
ACadSharp.Objects.TableStyle.BorderType Type { get; set; }
```

Gets or sets the border style type to be applied.
