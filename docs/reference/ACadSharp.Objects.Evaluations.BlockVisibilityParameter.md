# ACadSharp.Objects.Evaluations.BlockVisibilityParameter

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockVisibilityParameter`

Represents a BLOCKVISIBILITYPARAMETER object, in AutoCAD used to control the visibility state of entities in a dynamic block.

Object name F:ACadSharp.DxfFileToken.ObjectBlockVisibilityParameter Dxf class name F:ACadSharp.DxfSubclassMarker.BlockVisibilityParameter

Base type: `ACadSharp.Objects.Evaluations.Block1PtParameter`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockVisibilityParameter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Evaluations.BlockVisibilityParameter()
```

### AddState

```text
System.Void AddState(ACadSharp.Objects.Evaluations.BlockVisibilityParameter.State state)
```

Adds a state to the collection using the state's name as the key.

- `state`: The state to add to the collection. Cannot be null. The state's name must be unique within the collection.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### Description

```text
System.String Description { get; set; }
```

Visibility parameter description.

### Entities

```text
System.Collections.Generic.List[ACadSharp.Entities.Entity] Entities { get; }
```

Gets the list of all ACadSharp.Entities.Entity objects of the dynamic block this ACadSharp.Objects.Evaluations.BlockVisibilityParameter is associated with.

### Label

```text
System.String Label { get; set; }
```

Visibility parameter label.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### States

```text
System.Collections.Generic.IReadOnlyDictionary[System.String, ACadSharp.Objects.Evaluations.BlockVisibilityParameter.State] States { get; }
```

Gets the list of states each containing a 2 subsets of ACadSharp.Entities.Entity Objects must belong to the dynamic ACadSharp.Objects.Evaluations.BlockVisibilityParameter associated with.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Value281

```text
System.Boolean Value281 { get; set; }
```

### Value91

```text
System.Boolean Value91 { get; set; }
```
