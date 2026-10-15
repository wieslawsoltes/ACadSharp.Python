# ACadSharp.Tables.View

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.View`

Represents a ACadSharp.Tables.View entry.

Object name F:ACadSharp.DxfFileToken.TableView Dxf class name F:ACadSharp.DxfSubclassMarker.View

Base type: `ACadSharp.Tables.TableEntry`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.View')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.View(System.String name)
```

### Clone

```text
ACadSharp.CadObject Clone()
```

### Angle

```text
System.Double Angle { get; set; }
```

Twist angle.

### BackClipping

```text
System.Double BackClipping { get; set; }
```

Back clipping plane (offset from target point).

### Center

```text
CSMath.XY Center { get; set; }
```

View center point (in DCS)

### Direction

```text
CSMath.XYZ Direction { get; set; }
```

View direction from target (in WCS)

### FrontClipping

```text
System.Double FrontClipping { get; set; }
```

Front clipping plane (offset from target point).

### Height

```text
System.Double Height { get; set; }
```

View height (in DCS).

### IsPlottable

```text
System.Boolean IsPlottable { get; set; }
```

1 if the camera is plottable.

### IsUcsAssociated

```text
System.Boolean IsUcsAssociated { get; set; }
```

1 if there is a UCS associated to this view; 0 otherwise.

### LensLength

```text
System.Double LensLength { get; set; }
```

View width (in DCS).

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

### RenderMode

```text
ACadSharp.RenderMode RenderMode { get; set; }
```

View mode (see VIEWMODE system variable)

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Target

```text
CSMath.XYZ Target { get; set; }
```

Target point (in WCS)

### UcsElevation

```text
System.Double UcsElevation { get; set; }
```

UCS elevation

### UcsOrigin

```text
CSMath.XYZ UcsOrigin { get; set; }
```

UCS origin

### UcsOrthographicType

```text
ACadSharp.OrthographicType UcsOrthographicType { get; set; }
```

Orthographic type of UCS

### UcsXAxis

```text
CSMath.XYZ UcsXAxis { get; set; }
```

UCS X-axis

### UcsYAxis

```text
CSMath.XYZ UcsYAxis { get; set; }
```

UCS Y-axis

### ViewMode

```text
ACadSharp.Tables.ViewModeType ViewMode { get; set; }
```

View mode (see VIEWMODE system variable).

### VisualStyle

```text
ACadSharp.Objects.VisualStyle VisualStyle { get; set; }
```

Visual style object (optional)

### Width

```text
System.Double Width { get; set; }
```

View width (in DCS).
