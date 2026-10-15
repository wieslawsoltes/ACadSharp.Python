# ACadSharp.Objects.Evaluations.EvaluationGraph.Node

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.EvaluationGraph+Node`

Represents a graph node of a ACadSharp.Objects.Evaluations.EvaluationGraph.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.EvaluationGraph+Node')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.EvaluationGraph.Node(ACadSharp.Objects.Evaluations.EvaluationGraph evaluationGraph)
```

### Clone

```text
ACadSharp.Objects.Evaluations.EvaluationGraph.Node Clone()
```

Creates a deep copy of this ACadSharp.Objects.Evaluations.EvaluationGraph.Node.

**Returns:** A deep copy of this ACadSharp.Objects.Evaluations.EvaluationGraph.Node.

### Data1

```text
System.Int32 Data1 { get; }
```

Unknown

### Data2

```text
System.Int32 Data2 { get; }
```

Unknown

### Data3

```text
System.Int32 Data3 { get; }
```

Unknown

### Data4

```text
System.Int32 Data4 { get; }
```

Unknown

### Expression

```text
ACadSharp.Objects.Evaluations.EvaluationExpression Expression { get; set; }
```

Gets a ACadSharp.Objects.Evaluations.EvaluationExpression associated with this ACadSharp.Objects.Evaluations.EvaluationGraph.Node.

### Flags

```text
ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags Flags { get; set; }
```

Gets or sets the flags of this ACadSharp.Objects.Evaluations.EvaluationGraph.Node.

### Id

```text
System.Int32 Id { get; set; }
```

Gets or sets the index of the next ACadSharp.Objects.Evaluations.EvaluationGraph.Node in the list of graph nodes in the owning ACadSharp.Objects.Evaluations.EvaluationGraph.

### Index

```text
System.Int32 Index { get; set; }
```

Gets or sets the index of this ACadSharp.Objects.Evaluations.EvaluationGraph.Node in the list of graph nodes in the owning ACadSharp.Objects.Evaluations.EvaluationGraph.
