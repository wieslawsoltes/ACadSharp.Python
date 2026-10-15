# ACadSharp.DwgPreview

`class` · `ACadSharp` · CLR name: `ACadSharp.DwgPreview`

Stores the thumbnail information to generate the preview for a CadDocument.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.DwgPreview')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.DwgPreview()
```

Default constructor with an unknown media type.

### .ctor

```text
ACadSharp.DwgPreview(ACadSharp.DwgPreview.PreviewType code, System.Byte[] rawHeader, System.Byte[] rawImage)
```

Constructor to define a preview instance.

- `code`: 
- `rawHeader`: 
- `rawImage`: 

### Save

```text
System.Void Save(System.String path)
```

Save the image into a file.

- `path`: Path where the image has to be stored.

- Raises `System.NotSupportedException`: 

### Code

```text
ACadSharp.DwgPreview.PreviewType Code { get; }
```

Code that specifies the type of media stored in the preview.

### RawHeader

```text
System.Byte[] RawHeader { get; }
```

Header for the preview section.

**Remarks:** Usually is formed by an empty array of 80 zeros.

### RawImage

```text
System.Byte[] RawImage { get; }
```

Bytes conforming the thumbnail.
