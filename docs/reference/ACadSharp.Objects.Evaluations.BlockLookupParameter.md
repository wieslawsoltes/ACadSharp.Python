# ACadSharp.Objects.Evaluations.BlockLookupParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockLookupParameter`

Represents a BLOCKLOOKUPPARAMETER object, used in AutoCAD to drive block geometry from a lookup table in the Block Properties Table (the "Lookup" rows of the Customize tab of a dynamic block).

Object name F:ACadSharp.DxfFileToken.ObjectBlockLookupParameter Dxf class name F:ACadSharp.DxfSubclassMarker.BlockLookupParameter Minimal implementation: only the common block-element prefix (which carries ACadSharp.Objects.Evaluations.EvaluationExpression.Id, code 90 — the key found in ACAD_ENHANCEDBLOCKDATA) and the display name are decoded. The lookup table itself is not decoded.

Base type: `ACadSharp.Objects.Evaluations.Block1PtParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockLookupParameter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockLookupParameter()
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### ActionId

```text
System.Int32 ActionId { get; set; }
```

Gets or sets the action ID associated with the block lookup parameter. This ID is used to link the parameter to a specific action in the dynamic block's evaluation graph.

### Description

```text
System.String Description { get; set; }
```

Gets or sets the description of the block lookup parameter. This description is used to provide additional information about the parameter in the Block Properties Table and in the Customize tab of a dynamic block.

### Label

```text
System.String Label { get; set; }
```

Gets or sets the label of the block lookup parameter. This label is used to identify the parameter in the Block Properties Table and in the Customize tab of a dynamic block.

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
