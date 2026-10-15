# ACadSharp.Entities.Mesh.Edge

`struct` · `ACadSharp` · CLR name: `ACadSharp.Entities.Mesh+Edge`

No upstream type summary is available.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Mesh+Edge')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.Mesh.Edge(System.Int32 start, System.Int32 end)
```

Edge constructor with the start and end of the edge.

- `start`: 
- `end`: 

### ToString

```text
System.String ToString()
```

### Crease

```text
System.Nullable[System.Double] Crease { get; set; }
```

Edge crease value, null if not set

### End

```text
System.Int32 End { get; set; }
```

Index from the vertices where this edge ends

### Start

```text
System.Int32 Start { get; set; }
```

Index from the vertices where this edge starts
