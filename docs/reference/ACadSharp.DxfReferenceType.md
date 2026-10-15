# ACadSharp.DxfReferenceType

`enum` · `ACadSharp` · CLR name: `ACadSharp.DxfReferenceType`

Type of dxf reference

Base type: `System.Enum`. Inherited members are documented on their declaring type.

Interfaces: `System.IComparable`, `System.IConvertible`, `System.IFormattable`, `System.ISpanFormattable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.DxfReferenceType')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Count

```text
static ACadSharp.DxfReferenceType Count = 4
```

Counter reference, the value is a list with multiple elements referenced to it

### Handle

```text
static ACadSharp.DxfReferenceType Handle = 1
```

Handle reference, the value is a handle pointing to an object

### Ignored

```text
static ACadSharp.DxfReferenceType Ignored = 16
```

Value will be ignored by the reader and writer

### IsAngle

```text
static ACadSharp.DxfReferenceType IsAngle = 32
```

Value is an angle and must be converted when convinient

### Name

```text
static ACadSharp.DxfReferenceType Name = 2
```

Name reference, the value is a name pointing to an object

### None

```text
static ACadSharp.DxfReferenceType None = 0
```

No reference, the value is a primitive

### Optional

```text
static ACadSharp.DxfReferenceType Optional = 8
```

Optional value

### Unprocess

```text
static ACadSharp.DxfReferenceType Unprocess = 64
```
