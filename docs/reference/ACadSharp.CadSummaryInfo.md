# ACadSharp.CadSummaryInfo

`class` · `ACadSharp` · CLR name: `ACadSharp.CadSummaryInfo`

Holds general info and metadata about a CAD document. Like title, author, and timestamps.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.CadSummaryInfo')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.CadSummaryInfo()
```

### Author

```text
System.String Author { get; set; }
```

Name of the person or organization that created the document.

### Comments

```text
System.String Comments { get; set; }
```

Any notes or comments about the document.

### CreatedDate

```text
System.DateTime CreatedDate { get; set; }
```

When the document was first created.

### HyperlinkBase

```text
System.String HyperlinkBase { get; set; }
```

Base URL for hyperlinks in the document.

### Keywords

```text
System.String Keywords { get; set; }
```

Keywords to help categorize or search for the document.

### LastSavedBy

```text
System.String LastSavedBy { get; set; }
```

Name of the last person who saved the document.

### ModifiedDate

```text
System.DateTime ModifiedDate { get; set; }
```

When the document was last modified.

### Properties

```text
System.Collections.Generic.Dictionary[System.String, System.String] Properties { get; set; }
```

Custom properties defined by the user or application.

### RevisionNumber

```text
System.String RevisionNumber { get; set; }
```

Revision number, useful for tracking changes or versions.

### Subject

```text
System.String Subject { get; set; }
```

A short description or subject for for the document.

### Title

```text
System.String Title { get; set; }
```

Title of the document.
