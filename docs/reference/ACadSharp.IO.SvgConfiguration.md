# ACadSharp.IO.SvgConfiguration

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.SvgConfiguration`

Configuration for writing SVG files.

Base type: `ACadSharp.IO.CadWriterConfiguration`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.SvgConfiguration')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.SvgConfiguration()
```

### GetLineWeightValue

```text
System.Double GetLineWeightValue(ACadSharp.LineWeightType lineWeight, ACadSharp.Types.Units.UnitsType units)
```

Get the value of the stroke-width in mm.

- `lineWeight`: 
- `units`: 

### ArcPoints

```text
System.Int32 ArcPoints { get; set; }
```

### DefaultLineWeight

```text
System.Double DefaultLineWeight { get; set; }
```

Weight value for the F:ACadSharp.LineWeightType.Default.

**Value:** Value must be in mm.

### LineWeightRatio

```text
System.Double LineWeightRatio { get; set; }
```

The ACadSharp.LineWeightType will be divided by this value to process the stroke-width in the svg when the units are F:ACadSharp.Types.Units.UnitsType.Unitless.

**Remarks:** The default value is 100, which matches with the line weight real value in mm.

### PointRadius

```text
System.Double PointRadius { get; set; }
```

Radius applied for the points.

**Remarks:** In svg the points will be drawn as circles.
