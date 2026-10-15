# ACadSharp.Objects.DictionaryVariable

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.DictionaryVariable`

Represents a ACadSharp.Objects.DictionaryVariable object.

Object name F:ACadSharp.DxfFileToken.ObjectDictionaryVar Dxf class name F:ACadSharp.DxfSubclassMarker.DictionaryVariables

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.DictionaryVariable')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.DictionaryVariable()
```

Documentation inherited from: `base member`.

### .ctor

```text
ACadSharp.Objects.DictionaryVariable(System.String name, System.String value)
```

Initializes a new instance of the ACadSharp.Objects.DictionaryVariable class with the specified name and value.

**Remarks:** The name parameter is used to uniquely identify the dictionary variable, while the value parameter represents the associated data.

- `name`: The name of the dictionary variable.
- `value`: The value associated with the dictionary variable.

### CurrentAnnotationScale

```text
static System.String CurrentAnnotationScale = CANNOSCALE
```

Represents the name of the system variable that specifies the current ACadSharp.Objects.Scale.

**Remarks:** This constant is used to identify the current ACadSharp.Objects.Scale in the application.

### CurrentMultiLeaderStyle

```text
static System.String CurrentMultiLeaderStyle = CMLEADERSTYLE
```

Represents the name of the current ACadSharp.Objects.MultiLeaderStyle.

**Remarks:** This constant is used to identify the current ACadSharp.Objects.MultiLeaderStyle in the application.

### CurrentTableStyle

```text
static System.String CurrentTableStyle = CTABLESTYLE
```

Represents the name of the current ACadSharp.Objects.TableStyle.

**Remarks:** This constant is used to identify the current ACadSharp.Objects.TableStyle in the application.

### WipeoutFrame

```text
static System.String WipeoutFrame = WIPEOUTFRAME
```

The name of the system variable that controls the display of frames for wipeout objects.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### ObjectSchemaNumber

```text
System.Int32 ObjectSchemaNumber { get; }
```

Object schema number (currently set to 0)

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

### Value

```text
System.String Value { get; set; }
```

Value of variable
