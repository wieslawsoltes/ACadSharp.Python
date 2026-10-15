# ACadSharp.Objects.BookColor

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.BookColor`

Represents a ACadSharp.Objects.BookColor object.

Object name F:ACadSharp.DxfFileToken.ObjectDBColor Dxf class name F:ACadSharp.DxfSubclassMarker.DbColor

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.BookColor')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.BookColor()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Objects.BookColor(System.String name)
```

Initialize a ACadSharp.Objects.BookColor with an specific name.

- `name`: 

### .ctor

```text
ACadSharp.Objects.BookColor(System.String name, System.String bookName)
```

Initialize a ACadSharp.Objects.BookColor with an specific book and color name.

- `name`: 
- `bookName`: 

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### BookName

```text
System.String BookName { get; set; }
```

Book name where the color is stored.

### Color

```text
ACadSharp.Color Color { get; set; }
```

### ColorName

```text
System.String ColorName { get; set; }
```

Color name.

### Name

```text
System.String Name { get; set; }
```

Returns the full name of the color, following the structure BookName$ColorName, if when set doesn't follow this structure only the name will be changed.

Documentation inherited from: `base member`.

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
