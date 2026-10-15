# ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.EvaluationGraph+NodeFlags`

No upstream type summary is available.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.EvaluationGraph+NodeFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### All

```text
static ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags All = 47
```

All flags are set.

### FirstLevel

```text
static ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags FirstLevel = 16
```

This bit is used to indicate that the node is a first-level node.

### InList

```text
static ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags InList = 8
```

This bit is used to indicate that the node is in a list.

### ListAll

```text
static ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags ListAll = 14
```

This bit is used to indicate that the node is in all lists.

### None

```text
static ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags None = 0
```

No flags are set.

### OutsideRefed

```text
static ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags OutsideRefed = 2
```

This bit is used internally by the xref detach code to keep track of xrefs that have multiple references, and can also be used for similar purposes by other callers.

### Selected

```text
static ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags Selected = 4
```

This bit is used to indicate that the node is selected.

### UnresTree

```text
static ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags UnresTree = 32
```

This bit is used to indicate that the node is an unreserved tree node.

### Visited

```text
static ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags Visited = 1
```

This bit is used internally by the xref detach code to keep track of xrefs that have been visited, and can also be used for similar purposes by other callers.
