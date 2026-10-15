# ACadSharp.Objects.Evaluations.EvaluationGraph

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.EvaluationGraph`

Represents an evaluation graph containing a list of ACadSharp.Objects.Evaluations.EvaluationGraph.Node. objects.

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.EvaluationGraph')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.EvaluationGraph()
```

Initializes a new instance of the EvaluationGraph class.

### DictionaryEntryName

```text
static System.String DictionaryEntryName = ACAD_ENHANCEDBLOCK
```

Dictionary entry name for the object ACadSharp.Objects.Evaluations.EvaluationGraph

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### CreateNode

```text
ACadSharp.Objects.Evaluations.EvaluationGraph.Node CreateNode()
```

Creates a new ACadSharp.Objects.Evaluations.EvaluationGraph.Node object and adds it to the list of nodes.

**Returns:** The newly created ACadSharp.Objects.Evaluations.EvaluationGraph.Node object.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### RemoveNode

```text
System.Boolean RemoveNode(System.Int32 id)
```

Removes a ACadSharp.Objects.Evaluations.EvaluationGraph.Node object from the list of nodes by its ID.

**Returns:** True if the node was found and removed; otherwise, false.

- `id`: The ID of the ACadSharp.Objects.Evaluations.EvaluationGraph.Node to remove.

### Edges

```text
System.Collections.Generic.IList[ACadSharp.Objects.Evaluations.EvaluationGraph.Edge] Edges { get; }
```

Gets a list of ACadSharp.Objects.Evaluations.EvaluationGraph.Edge objects.

### Nodes

```text
System.Collections.Generic.IEnumerable[ACadSharp.Objects.Evaluations.EvaluationGraph.Node] Nodes { get; }
```

Gets a list of ACadSharp.Objects.Evaluations.EvaluationGraph.Node objects.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

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

### Value96

```text
System.Int32 Value96 { get; set; }
```

### Value97

```text
System.Int32 Value97 { get; set; }
```
