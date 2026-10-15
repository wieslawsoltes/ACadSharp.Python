# ACadSharp.Color

`struct` · `ACadSharp` · CLR name: `ACadSharp.Color`

Represents an ACI color that also supports true color.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

Interfaces: `System.IEquatable[ACadSharp.Color]`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Color')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Color(System.Byte r, System.Byte g, System.Byte b)
```

Creates a color out of RGB true color bytes.

- `r`: Red
- `g`: Green
- `b`: Blue

### .ctor

```text
ACadSharp.Color(System.Byte[] rgb)
```

Creates a color out of a RGB true color byte array.

- `rgb`: Red Green Blue

### .ctor

```text
ACadSharp.Color(System.Int16 index)
```

Creates a new color out of an indexed color.

- `index`: Index color with a value between 0 to 257

### ApproxIndex

```text
static System.Byte ApproxIndex(System.Byte r, System.Byte g, System.Byte b)
```

Approximates color from a true color RGB.

**Returns:** Approximate RGB color.

- `r`: Red
- `g`: Green
- `b`: Blue

### Equals

```text
System.Boolean Equals(ACadSharp.Color other)
```

Documentation inherited from: `base member`.

### Equals

```text
System.Boolean Equals(System.Object obj)
```

Documentation inherited from: `base member`.

### FromTrueColor

```text
static ACadSharp.Color FromTrueColor(System.UInt32 color)
```

Creates a color out of a true color int32.

- `color`: True color int 32.

### GetApproxIndex

```text
System.Int16 GetApproxIndex()
```

Approximates color from a true color RGB.

**Returns:** Approximate RGB color.

### GetHashCode

```text
System.Int32 GetHashCode()
```

Documentation inherited from: `base member`.

### GetIndexRGB

```text
static System.ReadOnlySpan[System.Byte] GetIndexRGB(System.Byte index)
```

Returns the RGB color code which matches the passed indexed color.

**Returns:** Approximate RGB color from indexed color.

### GetRgb

```text
System.ReadOnlySpan[System.Byte] GetRgb()
```

Returns the RGB color code

### GetTrueColorRgb

```text
System.ReadOnlySpan[System.Byte] GetTrueColorRgb()
```

Returns the RGB color code using the true color value.

**Remarks:** If the color is not ACadSharp.Color.IsTrueColor it will return the default values for RGB

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### B

```text
System.Byte B { get; }
```

Blue component of the color

### Black

```text
static ACadSharp.Color Black { get; }
```

Defines a default black color.

### Blue

```text
static ACadSharp.Color Blue { get; }
```

Defines a default blue color.

### ByBlock

```text
static ACadSharp.Color ByBlock { get; }
```

Gets the ByBlock color.

### ByEntity

```text
static ACadSharp.Color ByEntity { get; }
```

This is found in some header variables but is not valid for Entities or Objects

### ByLayer

```text
static ACadSharp.Color ByLayer { get; }
```

Gets the ByLayer color.

### Cyan

```text
static ACadSharp.Color Cyan { get; }
```

Defines a default cyan color.

### DarkGray

```text
static ACadSharp.Color DarkGray { get; }
```

Defines a default dark gray color.

### Default

```text
static ACadSharp.Color Default { get; }
```

Defines a default white/black color.

### G

```text
System.Byte G { get; }
```

Green component of the color

### Green

```text
static ACadSharp.Color Green { get; }
```

Defines a default green color.

### Index

```text
System.Int16 Index { get; }
```

Indexed color. If the color is stored as a true color, returns -1;

### IsByBlock

```text
System.Boolean IsByBlock { get; }
```

Defines if the color is defined by block.

### IsByLayer

```text
System.Boolean IsByLayer { get; }
```

Defines if the color is defined by layer.

### IsTrueColor

```text
System.Boolean IsTrueColor { get; }
```

True if the stored color is a true color. False if the color is an indexed color.

### LightGray

```text
static ACadSharp.Color LightGray { get; }
```

Defines a default light gray color.

### Magenta

```text
static ACadSharp.Color Magenta { get; }
```

Defines a default magenta color.

### R

```text
System.Byte R { get; }
```

Red component of the color

### Red

```text
static ACadSharp.Color Red { get; }
```

Defines a default red color.

### TrueColor

```text
System.Int32 TrueColor { get; }
```

True color. If the color is stored as an indexed color, returns -1;

### Yellow

```text
static ACadSharp.Color Yellow { get; }
```

Defines a default yellow color.
