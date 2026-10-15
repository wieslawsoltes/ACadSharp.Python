# ACadSharp.Entities.AecEntities.Wall

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.AecEntities.Wall`

Represents a wall entity in an AEC context.

AEC Wall entities can only be stored in DWG files, not in DXF files. DXF files may contain the class definition but not the actual entity instances.

Base type: `ACadSharp.Entities.AecEntities.AecEntity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`, `ACadSharp.IOrientable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.AecEntities.Wall')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.AecEntities.Wall()
```

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

### BaseHeight

```text
System.Double BaseHeight { get; set; }
```

Base height of the wall.

### BinRecord

```text
ACadSharp.Objects.AEC.AecBinRecord BinRecord { get; }
```

Reference to the BinRecord containing wall-specific data

### BinRecordHandle

```text
System.UInt64 BinRecordHandle { get; set; }
```

Handle reference to the AcAecBinRecord object containing the actual wall geometry data.

**Remarks:** This handle points to a separate object in the DWG file that stores the wall's properties in a proprietary binary format.

### CleanupGroup

```text
ACadSharp.Objects.AecCleanupGroup CleanupGroup { get; }
```

Reference to the cleanup group that manages wall intersections and cleanup operations.

### CleanupGroupHandle

```text
System.UInt64 CleanupGroupHandle { get; set; }
```

Handle reference to the cleanup group object.

### EndPoint

```text
CSMath.XYZ EndPoint { get; set; }
```

End position of the wall.

### Height

```text
System.Double Height { get; set; }
```

### Justification

```text
ACadSharp.Entities.AecEntities.WallJustification Justification { get; set; }
```

Wall justification (e.g., Baseline, Left, Center, Right).

### Length

```text
System.Double Length { get; set; }
```

Length of the wall.

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

### RawData

```text
System.Byte[] RawData { get; }
```

### StartPoint

```text
CSMath.XYZ StartPoint { get; set; }
```

Start position of the wall (insertion point).

### Style

```text
ACadSharp.Objects.AecWallStyle Style { get; }
```

Reference to the wall style that defines this wall's appearance and properties.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Version

```text
System.Int32 Version { get; set; }
```

AEC object version number (if available from DWG).

### Width

```text
System.Double Width { get; set; }
```

Wall width (thickness).
