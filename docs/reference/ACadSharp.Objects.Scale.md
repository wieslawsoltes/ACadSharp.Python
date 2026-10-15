# ACadSharp.Objects.Scale

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Scale`

Represents a ACadSharp.Objects.Scale object

Object name F:ACadSharp.DxfFileToken.ObjectScale Dxf class name F:ACadSharp.DxfSubclassMarker.Scale

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Scale')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Scale()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Objects.Scale(System.String name)
```

Documentation inherited from: `base member`.

### DefaultName

```text
static System.String DefaultName = 1:1
```

### ApplyTo

```text
System.Double ApplyTo(System.Double value)
```

### ApplyTo

```text
T ApplyTo[T](T value)
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### Default

```text
static ACadSharp.Objects.Scale Default { get; }
```

### DrawingUnits

```text
System.Double DrawingUnits { get; set; }
```

Group description.

### IsUnitScale

```text
System.Boolean IsUnitScale { get; set; }
```

Group description.

### Name

```text
System.String Name { get; set; }
```

Name

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

### PaperUnits

```text
System.Double PaperUnits { get; set; }
```

Group description.

### ScaleFactor

```text
System.Double ScaleFactor { get; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
