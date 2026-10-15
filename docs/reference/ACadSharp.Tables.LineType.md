# ACadSharp.Tables.LineType

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.LineType`

Represents a ACadSharp.Tables.LineType entry.

Object name F:ACadSharp.DxfFileToken.TableLinetype Dxf class name F:ACadSharp.DxfSubclassMarker.Linetype

Base type: `ACadSharp.Tables.TableEntry`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.LineType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.LineType(System.String name)
```

Documentation inherited from: `base member`.

### ByBlockName

```text
static System.String ByBlockName = ByBlock
```

### ByLayerName

```text
static System.String ByLayerName = ByLayer
```

### ContinuousName

```text
static System.String ContinuousName = Continuous
```

### AddSegment

```text
System.Void AddSegment(ACadSharp.Tables.LineType.Segment segment)
```

Add a segment to this line type.

- `segment`: 

- Raises `System.ArgumentException`: 

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### CreateLineTypeShape

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.Polyline3D] CreateLineTypeShape(ACadSharp.Entities.IPolyline polyline, System.Nullable[System.Double] pointSize = null)
```

Converts a ACadSharp.Entities.IPolyline to a series of ACadSharp.Entities.Polyline3D in line type shape.

- `polyline`: 
- `pointSize`: 

### CreateLineTypeShape

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.Polyline3D] CreateLineTypeShape[T](System.Collections.Generic.IEnumerable[T] points)
```

Converts a collection of CSMath.IVector to a series of ACadSharp.Entities.Polyline3D in the line type shape.

- `points`: 

### CreateLineTypeShape

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.Polyline3D] CreateLineTypeShape[T](System.Nullable[System.Double] pointSize, System.Collections.Generic.IEnumerable[T] points)
```

Converts a collection of CSMath.IVector to a series of ACadSharp.Entities.Polyline3D in the line type shape.

- `pointSize`: 
- `points`: 

### Alignment

```text
System.Char Alignment { get; }
```

Alignment code.

**Value:** value is always 65, the ASCII code for A.

### ByBlock

```text
static ACadSharp.Tables.LineType ByBlock { get; }
```

### ByLayer

```text
static ACadSharp.Tables.LineType ByLayer { get; }
```

### Continuous

```text
static ACadSharp.Tables.LineType Continuous { get; }
```

### Description

```text
System.String Description { get; set; }
```

Descriptive text for line type.

### HasShapes

```text
System.Boolean HasShapes { get; }
```

Gets if this line type has any segment defined by a shape.

### IsComplex

```text
System.Boolean IsComplex { get; }
```

Gets if this line type is complex (has segments).

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

### PatternLength

```text
System.Double PatternLength { get; }
```

Total pattern length.

### Segments

```text
System.Collections.Generic.IEnumerable[ACadSharp.Tables.LineType.Segment] Segments { get; }
```

LineType Segments

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
