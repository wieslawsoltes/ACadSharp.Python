# ACadSharp.IO.ProgressEventArgs

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.ProgressEventArgs`

Provides data for a progress update event during a CAD file read operation.

Base type: `System.EventArgs`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.ProgressEventArgs')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.ProgressEventArgs(ACadSharp.IO.ReadStage stage, ACadSharp.IO.CadObjectData current)
```

Initializes a new instance of the ACadSharp.IO.ProgressEventArgs class.

- `stage`: The current stage of the read operation.
- `current`: The current CAD object data being processed.

### Current

```text
ACadSharp.IO.CadObjectData Current { get; }
```

Gets the current CAD object data being processed.

### Stage

```text
ACadSharp.IO.ReadStage Stage { get; }
```

Gets the current stage of the read operation.
