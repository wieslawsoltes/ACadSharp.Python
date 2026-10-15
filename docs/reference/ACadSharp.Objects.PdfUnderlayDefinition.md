# ACadSharp.Objects.PdfUnderlayDefinition

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.PdfUnderlayDefinition`

Represents a ACadSharp.Objects.PdfUnderlayDefinition object.

Object name F:ACadSharp.DxfFileToken.ObjectPdfDefinition Dxf class name F:ACadSharp.DxfSubclassMarker.UnderlayDefinition

Base type: `ACadSharp.Objects.UnderlayDefinition`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.PdfUnderlayDefinition')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.PdfUnderlayDefinition()
```

Documentation inherited from: `base member`.

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

### Page

```text
System.String Page { get; set; }
```

Gets or sets the PDF page to show.
