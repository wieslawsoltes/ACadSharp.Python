# ACadSharp.Objects.UnknownNonGraphicalObject

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.UnknownNonGraphicalObject`

Class that holds the basic information for an unknown ACadSharp.Objects.NonGraphicalObject.

Unknown entities may appear in the ACadSharp.CadDocument if the cad file contains proxies or objects not yet supported by ACadSharp.

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.UnknownNonGraphicalObject')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### DxfClass

```text
ACadSharp.Classes.DxfClass DxfClass { get; }
```

Dxf class linked to this entity.

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
