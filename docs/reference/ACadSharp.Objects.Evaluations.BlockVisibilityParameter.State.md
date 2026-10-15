# ACadSharp.Objects.Evaluations.BlockVisibilityParameter.State

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockVisibilityParameter+State`

Represents a named state containing ACadSharp.Entities.Entity objects. The state controls the visibility of the entities assigned to it.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `System.ICloneable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockVisibilityParameter+State')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockVisibilityParameter.State()
```

### Clone

```text
System.Object Clone()
```

Documentation inherited from: `base member`.

### Entities

```text
System.Collections.Generic.List[ACadSharp.Entities.Entity] Entities { get; }
```

Get the list of ACadSharp.Entities.Entity objects in this state.

### Expressions

```text
System.Collections.Generic.List[ACadSharp.Objects.Evaluations.EvaluationExpression] Expressions { get; }
```

Get the list of ACadSharp.Objects.Evaluations.EvaluationExpression objects.

### Name

```text
System.String Name { get; set; }
```

Gets the name of the state.
