# ACadSharp.Objects.LinkedData

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.LinkedData`

Represents a ACadSharp.Objects.LinkedData object.

Dxf class name F:ACadSharp.DxfSubclassMarker.LinkedData

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.LinkedData')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Description

```text
System.String Description { get; set; }
```

Gets or sets the description associated with the object.

### Name

```text
System.String Name { get; set; }
```

Gets or sets the name of the object.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
