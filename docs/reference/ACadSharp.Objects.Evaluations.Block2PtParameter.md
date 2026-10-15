# ACadSharp.Objects.Evaluations.Block2PtParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.Block2PtParameter`

Represents the dynamic block 2 point parameter.

Base type: `ACadSharp.Objects.Evaluations.BlockParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.Block2PtParameter')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### BaseLocation

```text
ACadSharp.Objects.Evaluations.LinearParameterBaseLocation BaseLocation { get; set; }
```

Base point the distance is measured from (start point or middle point).

### FirstPoint

```text
CSMath.XYZ FirstPoint { get; set; }
```

Gets or sets the first point.

### FirstPointDisplacementX

```text
ACadSharp.Objects.Evaluations.EvalParameterProperty FirstPointDisplacementX { get; set; }
```

Gets or sets the first point displacement in X direction.

### FirstPointDisplacementY

```text
ACadSharp.Objects.Evaluations.EvalParameterProperty FirstPointDisplacementY { get; set; }
```

Gets or sets the first point displacement in Y direction.

### GripIds

```text
System.Collections.Generic.List[System.Int64] GripIds { get; }
```

Gets or sets the grip ids.

**Remarks:** Size 4 array of grip ids.

### SecondPoint

```text
CSMath.XYZ SecondPoint { get; set; }
```

Gets or sets the second point.

### SecondPointDisplacementX

```text
ACadSharp.Objects.Evaluations.EvalParameterProperty SecondPointDisplacementX { get; set; }
```

Gets or sets the second point displacement in X direction.

### SecondPointDisplacementY

```text
ACadSharp.Objects.Evaluations.EvalParameterProperty SecondPointDisplacementY { get; set; }
```

Gets or sets the second point displacement in Y direction.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
