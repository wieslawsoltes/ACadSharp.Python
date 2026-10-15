# ACadSharp.Tables.UCS

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.UCS`

Represents a ACadSharp.Tables.UCS entry.

Object name F:ACadSharp.DxfFileToken.TableUcs Dxf class name F:ACadSharp.DxfSubclassMarker.Ucs

Base type: `ACadSharp.Tables.TableEntry`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.UCS')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.UCS(System.String name)
```

Documentation inherited from: `base member`.

### Elevation

```text
System.Double Elevation { get; set; }
```

Elevation.

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

### Origin

```text
CSMath.XYZ Origin { get; set; }
```

Origin (in WCS).

### OrthographicType

```text
ACadSharp.OrthographicType OrthographicType { get; set; }
```

Orthographic type.

### OrthographicViewType

```text
ACadSharp.OrthographicType OrthographicViewType { get; set; }
```

Always 0.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### XAxis

```text
CSMath.XYZ XAxis { get; set; }
```

X-axis direction (in WCS).

### YAxis

```text
CSMath.XYZ YAxis { get; set; }
```

Y-axis direction(in WCS).
