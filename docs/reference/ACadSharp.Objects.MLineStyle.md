# ACadSharp.Objects.MLineStyle

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.MLineStyle`

Represents a ACadSharp.Objects.MLineStyle object

Object name F:ACadSharp.DxfFileToken.ObjectMLineStyle Dxf class name F:ACadSharp.DxfSubclassMarker.MLineStyle

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MLineStyle')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.MLineStyle(System.String name)
```

### DefaultName

```text
static System.String DefaultName = Standard
```

Default multiline style name

### AddElement

```text
System.Void AddElement(ACadSharp.Objects.MLineStyle.Element element)
```

Adds a segment to the current line style.

**Remarks:** The method associates the specified element with the current line style and updates its line type using the document's line type collection, if available.

- `element`: The element to add as a segment. The element must not already belong to another line style.

- Raises `System.ArgumentException`: Thrown if the element is already assigned to another line style.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### Default

```text
static ACadSharp.Objects.MLineStyle Default { get; }
```

Gets the default multiline style with predefined settings.

**Remarks:** This property provides a preconfigured instance of ACadSharp.Objects.MLineStyle that can be used as a baseline for creating multiline styles. The default configuration includes two elements with offsets of 0.5 and -0.5, respectively.

### Description

```text
System.String Description { get; set; }
```

Style description

**Value:** 255 characters maximum

### Elements

```text
System.Collections.Generic.IEnumerable[ACadSharp.Objects.MLineStyle.Element] Elements { get; }
```

Elements in the style

### EndAngle

```text
System.Double EndAngle { get; set; }
```

End angle

### FillColor

```text
ACadSharp.Color FillColor { get; set; }
```

Fill color

### Flags

```text
ACadSharp.Objects.MLineStyleFlags Flags { get; set; }
```

Multi line style flags

### Name

```text
System.String Name { get; set; }
```

Mline style name

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

### StartAngle

```text
System.Double StartAngle { get; set; }
```

Start angle

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
