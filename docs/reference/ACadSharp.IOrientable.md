# ACadSharp.IOrientable

`interface` · `ACadSharp` · CLR name: `ACadSharp.IOrientable`

Represents an object that has a three-dimensional orientation.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.IOrientable')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Normal

```text
CSMath.XYZ Normal { get; set; }
```

Specifies the three-dimensional normal unit vector for the object.
