# ACadSharp.Objects.Evaluations.BlockArrayAction

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockArrayAction`

Represents a BLOCKARRAYACTION object, used in AutoCAD to control a array action in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockArrayAction Dxf class name F:ACadSharp.DxfSubclassMarker.BlockArrayAction

Base type: `ACadSharp.Objects.Evaluations.BlockAction`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockArrayAction')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockArrayAction()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### BaseConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection BaseConnection { get; set; }
```

### ColumnOffset

```text
System.Double ColumnOffset { get; set; }
```

### EndConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection EndConnection { get; set; }
```

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### RowOffset

```text
System.Double RowOffset { get; set; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### UpdatedBaseConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection UpdatedBaseConnection { get; set; }
```

### UpdatedEndConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection UpdatedEndConnection { get; set; }
```
