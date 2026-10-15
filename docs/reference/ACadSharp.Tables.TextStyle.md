# ACadSharp.Tables.TextStyle

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.TextStyle`

Represents a ACadSharp.Tables.TextStyle entry.

Object name F:ACadSharp.DxfFileToken.TableStyle Dxf class name F:ACadSharp.DxfSubclassMarker.TextStyle

Base type: `ACadSharp.Tables.TableEntry`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.TextStyle')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.TextStyle(System.String name)
```

Documentation inherited from: `base member`.

### DefaultName

```text
static System.String DefaultName = Standard
```

### BigFontFilename

```text
System.String BigFontFilename { get; set; }
```

Big-font file name, blank if none.

### Default

```text
static ACadSharp.Tables.TextStyle Default { get; }
```

Default text style.

### Filename

```text
System.String Filename { get; set; }
```

Primary font file name.

### Flags

```text
ACadSharp.Tables.StyleFlags Flags { get; set; }
```

Style state flags.

### Height

```text
System.Double Height { get; set; }
```

Fixed text height; 0 if not fixed

### IsShapeFile

```text
System.Boolean IsShapeFile { get; }
```

Flag that indicates weather this ACadSharp.Tables.TextStyle is linked to a Shape file

### LastHeight

```text
System.Double LastHeight { get; set; }
```

Last height used

### MirrorFlag

```text
ACadSharp.Entities.TextMirrorFlag MirrorFlag { get; set; }
```

Mirror flags.

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

### ObliqueAngle

```text
System.Double ObliqueAngle { get; set; }
```

Specifies the oblique angle of the object.

**Value:** The angle in radians within the range of -85 to +85 degrees. A positive angle denotes a lean to the right; a negative value will have 2*PI added to it to convert it to its positive equivalent.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### TrueType

```text
ACadSharp.Tables.FontFlags TrueType { get; set; }
```

A long value which contains a true-type font’s pitch and family, character set, and italic and bold flags

### Width

```text
System.Double Width { get; set; }
```

Width factor
