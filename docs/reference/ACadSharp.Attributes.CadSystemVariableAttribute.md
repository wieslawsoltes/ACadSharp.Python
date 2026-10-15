# ACadSharp.Attributes.CadSystemVariableAttribute

`class` · `ACadSharp` · CLR name: `ACadSharp.Attributes.CadSystemVariableAttribute`

No upstream type summary is available.

Base type: `System.Attribute`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Attributes.ICodeValueAttribute`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Attributes.CadSystemVariableAttribute')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Attributes.CadSystemVariableAttribute(ACadSharp.DxfReferenceType referenceType, System.String variable, System.Int32[] codes)
```

### .ctor

```text
ACadSharp.Attributes.CadSystemVariableAttribute(System.String variable, ACadSharp.DxfCode[] codes)
```

### .ctor

```text
ACadSharp.Attributes.CadSystemVariableAttribute(System.String variable, System.Boolean isName, System.Int32[] codes)
```

### .ctor

```text
ACadSharp.Attributes.CadSystemVariableAttribute(System.String variable, System.Int32[] codes)
```

### IsName

```text
System.Boolean IsName { get; }
```

### Name

```text
System.String Name { get; }
```

System variable name

### ReferenceType

```text
ACadSharp.DxfReferenceType ReferenceType { get; }
```

Documentation inherited from: `base member`.

### ValueCodes

```text
ACadSharp.DxfCode[] ValueCodes { get; }
```

Documentation inherited from: `base member`.
