# ACadSharp.Objects.Evaluations.Block1PtParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.Block1PtParameter`

Represents a dynamic block parameter that is defined by a single point in 3D space.

Base type: `ACadSharp.Objects.Evaluations.BlockParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.Block1PtParameter')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### DisplacementX

```text
ACadSharp.Objects.Evaluations.EvalParameterProperty DisplacementX { get; set; }
```

Gets or sets the displacement in the X direction for the parameter.

### DisplacementY

```text
ACadSharp.Objects.Evaluations.EvalParameterProperty DisplacementY { get; set; }
```

Gets or sets the displacement in the Y direction for the parameter.

### GripId

```text
System.Int64 GripId { get; set; }
```

Gets or sets the grip id.

### Location

```text
CSMath.XYZ Location { get; set; }
```

Location for parameter to be placed in the block.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
