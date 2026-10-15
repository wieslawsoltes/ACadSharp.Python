# ACadSharp.Objects.DictionaryCloningFlags

`enum` · `ACadSharp` · CLR name: `ACadSharp.Objects.DictionaryCloningFlags`

Duplicate record cloning flag (determines how to merge duplicate entries).

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.DictionaryCloningFlags')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### KeepExisting

```text
static ACadSharp.Objects.DictionaryCloningFlags KeepExisting = 1
```

Keep existing.

### Name

```text
static ACadSharp.Objects.DictionaryCloningFlags Name = 4
```

Name.

### NotApplicable

```text
static ACadSharp.Objects.DictionaryCloningFlags NotApplicable = 0
```

Not applicable.

### UnmangleName

```text
static ACadSharp.Objects.DictionaryCloningFlags UnmangleName = 5
```

Unmangle name.

### UseClone

```text
static ACadSharp.Objects.DictionaryCloningFlags UseClone = 2
```

Use clone.

### XrefName

```text
static ACadSharp.Objects.DictionaryCloningFlags XrefName = 3
```

External reference name.
