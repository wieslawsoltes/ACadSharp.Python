# ACadSharp.Attributes.DxfSubClassAttribute

`class` · `ACadSharp` · CLR name: `ACadSharp.Attributes.DxfSubClassAttribute`

Mark the class as a dxf class equivalent

Base type: `System.Attribute`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Attributes.DxfSubClassAttribute')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Attributes.DxfSubClassAttribute(System.String className)
```

### .ctor

```text
ACadSharp.Attributes.DxfSubClassAttribute(System.String className, System.Boolean isEmpty)
```

### ClassName

```text
System.String ClassName { get; }
```

Dxf class name

### IsEmpty

```text
System.Boolean IsEmpty { get; }
```

Flag to mark the classes that don't contain any properties by itself, they are only a base for the subclasses
