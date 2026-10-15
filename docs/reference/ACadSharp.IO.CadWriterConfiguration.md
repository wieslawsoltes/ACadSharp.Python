# ACadSharp.IO.CadWriterConfiguration

`class` · `ACadSharp` · CLR name: `ACadSharp.IO.CadWriterConfiguration`

Configuration for the ACadSharp.IO.CadWriterBase`1 class.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IO.CadWriterConfiguration')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.IO.CadWriterConfiguration()
```

### CloseStream

```text
System.Boolean CloseStream { get; set; }
```

The writer will close the stream once the operation is completed.

**Value:** default: true

### ResetDxfClasses

```text
System.Boolean ResetDxfClasses { get; set; }
```

Resets the ACadSharp.Classes.DxfClass collection in the ACadSharp.CadDocument before writing it.

**Remarks:** Sometimes the files are corrupted by badly formed dxf classes, is recommended to keep this flag set.

**Value:** default: false

### UpdateDimensionsInBlocks

```text
System.Boolean UpdateDimensionsInBlocks { get; set; }
```

Update the blocks that visualize the dimensions in the model space.

**Remarks:** When creating or modifying a dimension in a block, it needs to be updated in order to appear in the drawing.

**Value:** default: false

### UpdateDimensionsInModel

```text
System.Boolean UpdateDimensionsInModel { get; set; }
```

Update the blocks that visualize the dimensions in the blocks.

**Remarks:** The dimensions in the model space are automatically updated by the drawing software, is not recommended to update them if is not needed.

**Value:** default: false

### WriteDynamicBlockData

```text
System.Boolean WriteDynamicBlockData { get; set; }
```

The writer will not ignore the ACadSharp.Objects.Evaluations.EvaluationGraph objects in the document.

**Remarks:** Evaluation graphs can cause corruption for some documents due the complexity of their data.

**Value:** default: false

### WriteShapes

```text
System.Boolean WriteShapes { get; set; }
```

The writer will not ignore the ACadSharp.Entities.Shape entities in the document.

**Remarks:** Shapes can cause corruption for some documents due the lack of support for shx files in this library which cannot validate the correct shape format.

**Value:** default: false

### WriteXData

```text
System.Boolean WriteXData { get; set; }
```

The writer will not ignore the ACadSharp.XData.ExtendedData collection in the ACadSharp.CadObject.

**Value:** default: true

### WriteXRecords

```text
System.Boolean WriteXRecords { get; set; }
```

The writer will not ignore the ACadSharp.Objects.XRecord objects in the document.

**Remarks:** Due the complexity of XRecords, if this flag is set to true, it may cause a corruption of the file.

**Value:** default: true
