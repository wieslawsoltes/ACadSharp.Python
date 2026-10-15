# ACadSharp.Objects.GeoData

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.GeoData`

Represents a ACadSharp.Objects.GeoData object

Object name F:ACadSharp.DxfFileToken.ObjectGeoData Dxf class name F:ACadSharp.DxfSubclassMarker.GeoData

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.GeoData')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.GeoData()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### CoordinateProjectionRadius

```text
System.Double CoordinateProjectionRadius { get; set; }
```

Coordinate projection radius.

### CoordinateSystemDefinition

```text
System.String CoordinateSystemDefinition { get; set; }
```

Coordinate system definition string.

### CoordinatesType

```text
ACadSharp.Objects.DesignCoordinatesType CoordinatesType { get; set; }
```

Type of design coordinates.

### DesignPoint

```text
CSMath.XYZ DesignPoint { get; set; }
```

Design point, reference point in WCS coordinates.

### EnableSeaLevelCorrection

```text
System.Boolean EnableSeaLevelCorrection { get; set; }
```

Bool flag specifying whether to do sea level correction.

### Faces

```text
System.Collections.Generic.List[ACadSharp.Objects.GeoData.GeoMeshFace] Faces { get; }
```

Faces.

### GeoRssTag

```text
System.String GeoRssTag { get; set; }
```

GeoRSS tag.

### HorizontalUnitScale

```text
System.Double HorizontalUnitScale { get; set; }
```

Horizontal unit scale, factor which converts horizontal design coordinates to meters by multiplication.

### HorizontalUnits

```text
ACadSharp.Types.Units.UnitsType HorizontalUnits { get; set; }
```

Horizontal units.

### HostBlock

```text
ACadSharp.Tables.BlockRecord HostBlock { get; set; }
```

Host block table record.

### NorthDirection

```text
CSMath.XY NorthDirection { get; set; }
```

North direction vector.

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

### ObservationCoverageTag

```text
System.String ObservationCoverageTag { get; set; }
```

Observation coverage tag.

### ObservationFromTag

```text
System.String ObservationFromTag { get; set; }
```

Observation from tag.

### ObservationToTag

```text
System.String ObservationToTag { get; set; }
```

Observation to tag.

### Points

```text
System.Collections.Generic.List[ACadSharp.Objects.GeoData.GeoMeshPoint] Points { get; }
```

Geo-Mesh points.

### ReferencePoint

```text
CSMath.XYZ ReferencePoint { get; set; }
```

Reference point in coordinate system coordinates, valid only when coordinate type is Local Grid.

### ScaleEstimationMethod

```text
ACadSharp.Objects.ScaleEstimationType ScaleEstimationMethod { get; set; }
```

Scale estimation method.

### SeaLevelElevation

```text
System.Double SeaLevelElevation { get; set; }
```

Sea level elevation.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### UpDirection

```text
CSMath.XYZ UpDirection { get; set; }
```

Up direction.

### UserSpecifiedScaleFactor

```text
System.Double UserSpecifiedScaleFactor { get; set; }
```

User specified scale factor.

### Version

```text
ACadSharp.Objects.GeoDataVersion Version { get; set; }
```

AcDbGeoData Object version.

**Remarks:** 1 - 2009 2 - 2010 3 - 2013

### VerticalUnitScale

```text
System.Double VerticalUnitScale { get; set; }
```

Vertical unit scale, factor which converts vertical design coordinates to meters by multiplication.

### VerticalUnits

```text
ACadSharp.Types.Units.UnitsType VerticalUnits { get; set; }
```

Vertical units.
