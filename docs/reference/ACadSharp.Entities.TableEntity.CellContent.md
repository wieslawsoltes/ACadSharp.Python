# ACadSharp.Entities.TableEntity.CellContent

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.TableEntity+CellContent`

Represents the content of a table cell, including its type, format, and associated CAD value.

Use this class to encapsulate the data and metadata for a single cell in a table, such as in a CAD drawing or spreadsheet context. The properties provide access to the cell's content type, formatting information, and the underlying CAD value.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.TableEntity+CellContent')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.TableEntity.CellContent()
```

### CadValue

```text
ACadSharp.CadValue CadValue { get; }
```

Gets the value associated with the CAD entity or property.

### ContentType

```text
ACadSharp.Entities.TableEntity.TableCellContentType ContentType { get; set; }
```

Gets or sets the type of content contained in the table cell.

### Format

```text
ACadSharp.Objects.TableStyle.ContentFormat Format { get; }
```

Gets the format used to interpret or serialize the content.
