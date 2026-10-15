# ACadSharp.Objects.DimensionAssociation

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.DimensionAssociation`

Represents a ACadSharp.Objects.DimensionAssociation object.

Object name F:ACadSharp.DxfFileToken.ObjectDimensionAssociation Dxf class name F:ACadSharp.DxfSubclassMarker.DimensionAssociation

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.DimensionAssociation')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.DimensionAssociation()
```

Documentation inherited from: `base member`.

### OsnapPointRefClassName

```text
static System.String OsnapPointRefClassName = AcDbOsnapPointRef
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### AssociativityFlags

```text
ACadSharp.Objects.AssociativityFlags AssociativityFlags { get; set; }
```

Gets or sets the associativity flags that define the reference points for an entity.

### Dimension

```text
ACadSharp.Entities.Dimension Dimension { get; set; }
```

Gets or sets the associated dimension object.

### FirstPointRef

```text
ACadSharp.Objects.DimensionAssociation.OsnapPointRef FirstPointRef { get; set; }
```

### FourthPointRef

```text
ACadSharp.Objects.DimensionAssociation.OsnapPointRef FourthPointRef { get; set; }
```

### IsTransSpace

```text
System.Boolean IsTransSpace { get; set; }
```

Gets or sets a value indicating whether the entity is in trans-space.

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

### RotatedDimensionType

```text
ACadSharp.Objects.RotatedDimensionType RotatedDimensionType { get; set; }
```

Gets or sets the type of the rotated dimension, indicating whether it is parallel or perpendicular.

### SecondPointRef

```text
ACadSharp.Objects.DimensionAssociation.OsnapPointRef SecondPointRef { get; set; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### ThirdPointRef

```text
ACadSharp.Objects.DimensionAssociation.OsnapPointRef ThirdPointRef { get; set; }
```
