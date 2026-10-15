# ACadSharp.Objects.Evaluations.BlockLookupAction

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockLookupAction`

Represents a BLOCKLOOKUPACTION object, used in AutoCAD to control a lookup action in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockLookupAction Dxf class name F:ACadSharp.DxfSubclassMarker.BlockLookupAction

Base type: `ACadSharp.Objects.Evaluations.BlockAction`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockLookupAction')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockLookupAction()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### Columns

```text
System.Collections.Generic.List[ACadSharp.Objects.Evaluations.BlockLookupAction.ColumnData] Columns { get; set; }
```

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### UnknownFlag

```text
System.Boolean UnknownFlag { get; set; }
```
