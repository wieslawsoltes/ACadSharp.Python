# ACadSharp.DwgReferenceType

`enum` · `ACadSharp` · CLR name: `ACadSharp.DwgReferenceType`

No upstream type summary is available.

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.DwgReferenceType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### HardOwnership

```text
static ACadSharp.DwgReferenceType HardOwnership = 3
```

Hard ownership reference: the owner needs the owned object. The owned object cannot exist by itself.

### HardPointer

```text
static ACadSharp.DwgReferenceType HardPointer = 5
```

Hard pointer reference: the referencing object needs the referenced object, but both are owned by another object.

### SoftOwnership

```text
static ACadSharp.DwgReferenceType SoftOwnership = 2
```

Soft ownership reference: the owner does not need the owned object. The owned object cannot exist by itself.

### SoftPointer

```text
static ACadSharp.DwgReferenceType SoftPointer = 4
```

Soft pointer reference: the referencing object does not need the referenced object and vice versa.

### Undefined

```text
static ACadSharp.DwgReferenceType Undefined = 0
```
