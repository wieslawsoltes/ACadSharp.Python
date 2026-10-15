# ACadSharp.Objects.Evaluations.StretchActionBase

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.StretchActionBase`

No upstream type summary is available.

Base type: `ACadSharp.Objects.Evaluations.BlockAction`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.StretchActionBase')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### AngleOffset

```text
System.Double AngleOffset { get; set; }
```

Gets or sets the angle offset for the stretch action.

### Boundary

```text
System.Collections.Generic.List[CSMath.XY] Boundary { get; }
```

### DistanceMultiplier

```text
System.Double DistanceMultiplier { get; set; }
```

Gets or sets the distance multiplier for the stretch action.

### StretchBindings

```text
System.Collections.Generic.List[ACadSharp.Objects.Evaluations.StretchEntityBind] StretchBindings { get; }
```

### StretchNodes

```text
System.Collections.Generic.List[ACadSharp.Objects.Evaluations.StretchNode] StretchNodes { get; }
```
