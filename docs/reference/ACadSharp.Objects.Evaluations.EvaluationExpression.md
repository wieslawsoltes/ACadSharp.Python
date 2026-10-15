# ACadSharp.Objects.Evaluations.EvaluationExpression

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.EvaluationExpression`

Represents an evaluation expression used in AutoCAD to define dynamic block parameters and constraints.

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.EvaluationExpression')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### EvaluatedValue

```text
ACadSharp.Objects.Evaluations.DxfValuePair EvaluatedValue { get; set; }
```

Gets or sets the evaluated value of the expression.

### Id

```text
System.Int32 Id { get; set; }
```

Gets or sets the unique identifier for the evaluation expression.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Value98

```text
System.Int32 Value98 { get; set; }
```

### Value99

```text
System.Int32 Value99 { get; set; }
```
