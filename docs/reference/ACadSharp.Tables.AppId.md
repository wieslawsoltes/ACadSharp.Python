# ACadSharp.Tables.AppId

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.AppId`

Represents a ACadSharp.Tables.AppId entry

Object name F:ACadSharp.DxfFileToken.TableAppId Dxf class name F:ACadSharp.DxfSubclassMarker.ApplicationId

Base type: `ACadSharp.Tables.TableEntry`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.AppId')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.AppId(System.String name)
```

Documentation inherited from: `base member`.

### BlockRepBTag

```text
static System.String BlockRepBTag = AcDbBlockRepBTag
```

Application name for BlockRepETag.

### BlockRepETag

```text
static System.String BlockRepETag = AcDbBlockRepETag
```

Application name for AcDbBlockRepETag.

### DefaultName

```text
static System.String DefaultName = ACAD
```

Default application registry name.

### Default

```text
static ACadSharp.Tables.AppId Default { get; }
```

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
