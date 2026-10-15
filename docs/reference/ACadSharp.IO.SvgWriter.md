# ACadSharp.IO.SvgWriter

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.SvgWriter`

Writer to support the creation of SVG from ACadSharp.Tables.BlockRecord and ACadSharp.Objects.Layout.

Base type: `ACadSharp.IO.CadWriterBase[ACadSharp.IO.SvgConfiguration]`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IO.ICadWriter`, `System.IDisposable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.SvgWriter')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.SvgWriter(System.IO.Stream stream)
```

Initialize an instance of ACadSharp.IO.SvgWriter with a default document as a reference.

- `stream`: 

### .ctor

```text
ACadSharp.IO.SvgWriter(System.IO.Stream stream, ACadSharp.CadDocument document)
```

### .ctor

```text
ACadSharp.IO.SvgWriter(System.String filename)
```

Initialize an instance of ACadSharp.IO.SvgWriter with a default document as a reference.

- `filename`: 

### .ctor

```text
ACadSharp.IO.SvgWriter(System.String filename, ACadSharp.CadDocument document)
```

- `filename`: 
- `document`: Document to export from.

### Dispose

```text
System.Void Dispose()
```

Documentation inherited from: `base member`.

### Write

```text
System.Void Write()
```

Documentation inherited from: `base member`.

**Remarks:** ACadSharp.IO.SvgWriter will draw all the content in the model space. The writer must be initialized with a none null ACadSharp.CadDocument.

### Write

```text
System.Void Write(ACadSharp.Objects.Layout layout)
```

Write the selected layout into a SVG.

- `layout`: 

### Write

```text
System.Void Write(ACadSharp.Tables.BlockRecord record)
```
