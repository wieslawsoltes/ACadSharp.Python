# ACadSharp.Objects.FieldList

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.FieldList`

Represents a ACadSharp.Objects.FieldList object.

Object name F:ACadSharp.DxfFileToken.ObjectFieldList Dxf class name F:ACadSharp.DxfSubclassMarker.FieldList

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.FieldList')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.FieldList()
```

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

### Fields

```text
System.Collections.Generic.List[ACadSharp.Objects.Field] Fields { get; }
```

Gets the collection of fields associated with this instance.

**Remarks:** The returned collection is read-only from outside the class. To modify the fields, use the provided methods of the containing class, if available.

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
