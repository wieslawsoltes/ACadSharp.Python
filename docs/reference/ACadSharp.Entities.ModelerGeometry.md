# ACadSharp.Entities.ModelerGeometry

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ModelerGeometry`

Represents a ACadSharp.Entities.ModelerGeometry entity.

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ModelerGeometry')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### GetAcisText

```text
System.String GetAcisText()
```

Gets the SAT text carried by ACadSharp.Entities.ModelerGeometry.AcisData.

**Returns:** The SAT content as a string, or null when the payload is empty or binary SAB.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

### AcisData

```text
System.Byte[] AcisData { get; set; }
```

Raw ACIS payload that describes the geometry of this entity.

**Remarks:** The payload is binary SAB when it starts with the "ACIS BinaryFile" signature (check ACadSharp.Entities.ModelerGeometry.IsBinaryAcisData), plain SAT text bytes otherwise. In R2013+ files the modeler geometry is stored apart from the entity (ACDSDATA section in DXF, AcDs data section in DWG) and this property is the only carrier of the geometry; older versions embed it in the entity itself.

### IsBinaryAcisData

```text
System.Boolean IsBinaryAcisData { get; }
```

Flag that indicates if ACadSharp.Entities.ModelerGeometry.AcisData contains a binary SAB payload instead of SAT text.

### ModelerFormatVersion

```text
System.Int16 ModelerFormatVersion { get; set; }
```

Gets or sets the modeler format version used in the drawing.

### Point

```text
CSMath.XYZ Point { get; set; }
```

### ProprietaryData

```text
System.Text.StringBuilder ProprietaryData { get; }
```

### Silhouettes

```text
System.Collections.Generic.List[ACadSharp.Entities.ModelerGeometry.Silhouette] Silhouettes { get; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Wires

```text
System.Collections.Generic.List[ACadSharp.Entities.ModelerGeometry.Wire] Wires { get; }
```
