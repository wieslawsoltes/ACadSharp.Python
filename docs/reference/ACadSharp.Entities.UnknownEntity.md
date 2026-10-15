# ACadSharp.Entities.UnknownEntity

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.UnknownEntity`

Class that holds the basic information for an unknown ACadSharp.Entities.Entity.

Unknown entities may appear in the ACadSharp.CadDocument if the cad file contains proxies or entities not yet supported by ACadSharp.

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.UnknownEntity')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### ApplyTransform

```text
System.Void ApplyTransform(CSMath.Transform transform)
```

Documentation inherited from: `base member`.

### GetBoundingBox

```text
CSMath.BoundingBox GetBoundingBox()
```

Documentation inherited from: `base member`.

**Remarks:** An Unknown Entity does not have any geometric shape, therfore it's bounding box will be always 0

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
