# ACadSharp.Objects.BlockReferenceObjectContextData

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.BlockReferenceObjectContextData`

Represents object context data for a block reference entity, including insertion point, rotation, and scale factors in world coordinates.

This type provides context-specific information for block references, such as position and transformation parameters, which are used when applying annotation scaling or other context-dependent behaviors. It is typically used in scenarios where block references must adapt to different annotation scales or contexts within a drawing. All scale factor properties must be non-zero; setting a scale factor to zero will result in an exception.

Base type: `ACadSharp.Objects.AnnotScaleObjectContextData`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.BlockReferenceObjectContextData')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.BlockReferenceObjectContextData()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### InsertionPoint

```text
CSMath.XYZ InsertionPoint { get; set; }
```

Gets or sets the insertion point of the entity in world coordinates.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### Rotation

```text
System.Double Rotation { get; set; }
```

Gets or sets the rotation angle of the entity, in degrees.

### XScale

```text
System.Double XScale { get; set; }
```

X scale factor.

### YScale

```text
System.Double YScale { get; set; }
```

Y scale factor.

### ZScale

```text
System.Double ZScale { get; set; }
```

Z scale factor.
