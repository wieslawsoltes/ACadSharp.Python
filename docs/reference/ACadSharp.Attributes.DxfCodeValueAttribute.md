# ACadSharp.Attributes.DxfCodeValueAttribute

`class` · `ACadSharp` · CLR name: `ACadSharp.Attributes.DxfCodeValueAttribute`

No upstream type summary is available.

Base type: `System.Attribute`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Attributes.ICodeValueAttribute`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Attributes.DxfCodeValueAttribute')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Attributes.DxfCodeValueAttribute(ACadSharp.DxfReferenceType referenceType, System.Int32[] codes)
```

### .ctor

```text
ACadSharp.Attributes.DxfCodeValueAttribute(System.Int32[] codes)
```

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
