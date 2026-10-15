# ACadSharp.Objects.UnderlayDefinition

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.UnderlayDefinition`

Common base class for all underlay definitions, like ACadSharp.Objects.PdfUnderlayDefinition.

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.UnderlayDefinition')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### File

```text
System.String File { get; set; }
```

Gets or sets the underlay file.

**Remarks:** The file extension must match the underlay type.

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
