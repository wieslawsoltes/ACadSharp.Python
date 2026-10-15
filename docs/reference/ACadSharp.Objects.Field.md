# ACadSharp.Objects.Field

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Field`

Represents a ACadSharp.Objects.Field object.

Object name F:ACadSharp.DxfFileToken.ObjectField Dxf class name F:ACadSharp.DxfSubclassMarker.Field

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Field')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Field()
```

Documentation inherited from: `base member`.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### CadObjects

```text
System.Collections.Generic.List[ACadSharp.CadObject] CadObjects { get; set; }
```

Gets or sets the collection of CAD objects associated with this entity.

### Children

```text
ACadSharp.CadObjectCollection[ACadSharp.Objects.Field] Children { get; }
```

Gets the collection of child fields associated with this object.

### EvaluationErrorCode

```text
System.Int32 EvaluationErrorCode { get; set; }
```

Gets or sets the error code resulting from the evaluation process.

### EvaluationErrorMessage

```text
System.String EvaluationErrorMessage { get; set; }
```

Gets or sets the error message generated during evaluation.

### EvaluationOptionFlags

```text
ACadSharp.Objects.EvaluationOptionFlags EvaluationOptionFlags { get; set; }
```

Gets or sets the evaluation option flags that control how the associated expression is evaluated.

### EvaluationStatusFlags

```text
ACadSharp.Objects.EvaluationStatusFlags EvaluationStatusFlags { get; set; }
```

Gets or sets the evaluation status flags that indicate the current state of the object evaluation process.

**Remarks:** These flags provide information about the outcome or progress of the evaluation, such as whether the evaluation succeeded, failed, or is in progress. The specific meaning of each flag is defined by the EvaluationStatusFlags enumeration.

### EvaluatorId

```text
System.String EvaluatorId { get; set; }
```

Gets or sets the identifier of the evaluator associated with this entity.

### FieldCode

```text
System.String FieldCode { get; set; }
```

Gets or sets the code string representing the field definition in the DXF file.

**Remarks:** The field code typically contains the raw expression or formula used in the field. This value may be used for parsing or evaluating the field within DXF processing workflows.

### FieldStateFlags

```text
ACadSharp.Objects.FieldStateFlags FieldStateFlags { get; set; }
```

Gets or sets the flags that indicate the current state of the field.

### FilingOptionFlags

```text
ACadSharp.Objects.FilingOptionFlags FilingOptionFlags { get; set; }
```

Gets or sets the set of flags that specify filing options for the associated entity.

**Remarks:** The filing option flags determine how the entity is processed or stored during serialization. The specific meaning of each flag depends on the context in which the entity is used. Refer to the documentation for the FilingOptionFlags enumeration for details on available options.

### FormatString

```text
System.String FormatString { get; set; }
```

Gets or sets the format string used to control how values are displayed or serialized.

**Remarks:** The format string determines the representation of values when output or stored. The expected format depends on the context in which this property is used. If the format string is invalid or unsupported, the output may not be formatted as intended.

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

### Value

```text
ACadSharp.CadValue Value { get; set; }
```

### Values

```text
System.Collections.Generic.Dictionary[System.String, ACadSharp.CadValue] Values { get; }
```

Gets or sets the collection of CAD values associated with the field.
