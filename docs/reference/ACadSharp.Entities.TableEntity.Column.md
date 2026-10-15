# ACadSharp.Entities.TableEntity.Column

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.TableEntity+Column`

Represents a table column with a name, width, custom data, and style information.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.TableEntity.ITableComponent`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.TableEntity+Column')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.TableEntity.Column()
```

### CellStyle

```text
ACadSharp.Objects.TableStyle.CellStyle CellStyle { get; set; }
```

Documentation inherited from: `base member`.

### CellStyleOverride

```text
ACadSharp.Objects.TableStyle.CellStyle CellStyleOverride { get; set; }
```

Documentation inherited from: `base member`.

### CustomData

```text
System.Int32 CustomData { get; set; }
```

Documentation inherited from: `base member`.

### CustomDataCollection

```text
System.Collections.Generic.List[ACadSharp.Entities.TableEntity.CustomDataEntry] CustomDataCollection { get; }
```

Documentation inherited from: `base member`.

### Name

```text
System.String Name { get; set; }
```

Gets or sets the name associated with this instance.

### Width

```text
System.Double Width { get; set; }
```

Column width.
