# ACadSharp.Entities.CadWipeoutBase

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.CadWipeoutBase`

Common base class for ACadSharp.Entities.RasterImage and ACadSharp.Entities.Wipeout.

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.CadWipeoutBase')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

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

### IsValid

```text
System.Boolean IsValid(ACadSharp.IO.CadFileFormat format, ACadSharp.ACadVersion version, out System.Collections.Generic.IList[System.String] errors)
```

Documentation inherited from: `base member`.

### Brightness

```text
System.Byte Brightness { get; set; }
```

Brightness

**Remarks:** 0-100; default = 50

### ClassVersion

```text
System.Int32 ClassVersion { get; set; }
```

Class version

### ClipBoundaryVertices

```text
System.Collections.Generic.List[CSMath.XY] ClipBoundaryVertices { get; set; }
```

Clip boundary vertices.

**Remarks:** For rectangular clip boundary type, two opposite corners must be specified.Default is (-0.5,-0.5), (size.x-0.5, size.y-0.5). 2) For polygonal clip boundary type, three or more vertices must be specified.Polygonal vertices must be listed sequentially

### ClipMode

```text
ACadSharp.Entities.ClipMode ClipMode { get; set; }
```

Clipping state.

### ClipType

```text
ACadSharp.Entities.ClipType ClipType { get; }
```

Clipping boundary type.

### ClippingState

```text
System.Boolean ClippingState { get; set; }
```

Clipping state.

### Contrast

```text
System.Byte Contrast { get; set; }
```

Contrast

**Remarks:** 0-100; default = 50

### Definition

```text
ACadSharp.Objects.ImageDefinition Definition { get; set; }
```

Image definition.

### Fade

```text
System.Byte Fade { get; set; }
```

Fade

**Remarks:** 0-100; default = 0

### Flags

```text
ACadSharp.Entities.ImageDisplayFlags Flags { get; set; }
```

Image display properties.

### InsertPoint

```text
CSMath.XYZ InsertPoint { get; set; }
```

Insertion point(in WCS)

### ShowImage

```text
System.Boolean ShowImage { get; set; }
```

Add the ShowImage flag to the display flags property.

### Size

```text
CSMath.XY Size { get; set; }
```

Image size in pixels.

**Remarks:** 2D point(U and V values).

### UVector

```text
CSMath.XYZ UVector { get; set; }
```

U-vector of a single pixel(points along the visual bottom of the image, starting at the insertion point) (in WCS)

### VVector

```text
CSMath.XYZ VVector { get; set; }
```

V-vector of a single pixel(points along the visual left side of the image, starting at the insertion point) (in WCS)
