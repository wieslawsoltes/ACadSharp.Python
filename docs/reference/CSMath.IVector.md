# CSMath.IVector

`interface` · `ACadSharp` · CLR name: `CSMath.IVector`

No upstream type summary is available.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.IVector')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Dimension

```text
System.UInt32 Dimension { get; }
```

Get the dimension of the CSMath.IVector.

### Item

```text
System.Double Item[System.Int32 index] { get; set; }
```

Value of the coordinate at the specified index.

**Returns:** The value of the coordinate at the specified index.

- `index`: The index.
