# ACadSharp.Objects.Evaluations.BlockAction

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockAction`

No upstream type summary is available.

Base type: `ACadSharp.Objects.Evaluations.BlockElement`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockAction')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Entities

```text
System.Collections.Generic.List[ACadSharp.Entities.Entity] Entities { get; }
```

Gets the list of ACadSharp.Entities.Entity objects affected by this ACadSharp.Objects.Evaluations.BlockAction.

### LabelPosition

```text
CSMath.XYZ LabelPosition { get; set; }
```

Gets or sets the position of the action label.

### ParametersIds

```text
System.Collections.Generic.List[System.Int32] ParametersIds { get; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
