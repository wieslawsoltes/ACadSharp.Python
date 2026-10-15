# ACadSharp.Transparency

`struct` · `ACadSharp` · CLR name: `ACadSharp.Transparency`

Represents the transparency for the graphical objects.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Transparency')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Transparency(System.Int16 value)
```

Initializes a new instance of the Transparency struct.

**Remarks:** Transparency values must be in range from 0 (opaque) to 90 (transparent), the reserved values -1 and 100 represents ByLayer and ByBlock.

- `value`: Alpha value range from 0 to 90.

### FromAlphaValue

```text
static ACadSharp.Transparency FromAlphaValue(System.Int32 value)
```

Gets the transparency from a transparency value

**Returns:** A ACadSharp.Transparency

- `value`: A transparency value

### ToAlphaValue

```text
static System.Int32 ToAlphaValue(ACadSharp.Transparency transparency)
```

Gets the alpha value of a transperency.

- `transparency`: 

### ByBlock

```text
static ACadSharp.Transparency ByBlock { get; }
```

Gets the ByBlock transparency.

### ByLayer

```text
static ACadSharp.Transparency ByLayer { get; }
```

Gets the ByLayer transparency.

### IsByBlock

```text
System.Boolean IsByBlock { get; }
```

Defines if the transparency is defined by block.

### IsByLayer

```text
System.Boolean IsByLayer { get; }
```

Defines if the transparency is defined by layer.

### Opaque

```text
static ACadSharp.Transparency Opaque { get; }
```

Gets the Opaque transparency.

### Value

```text
System.Int16 Value { get; set; }
```

Gets or sets the transparency value.

**Remarks:** Transparency values must be in range from 0 (opaque) to 90 (transparent), the reserved values -1 and 100 represents ByLayer and ByBlock.
