# ACadSharp.Entities.ProxyGraphics.PrimitiveTraits

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.PrimitiveTraits`

Represents the base class for traits associated with graphics primitives in proxy graphics. Contains collections for colors, layer handles, marker identifiers, and visibility indicators.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.PrimitiveTraits')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Colors

```text
System.Collections.Generic.List[System.Int32] Colors { get; }
```

Gets the collection of color values for the graphics primitives.

### LayerHandles

```text
System.Collections.Generic.List[System.UInt64] LayerHandles { get; }
```

Gets the collection of layer handles referenced by the graphics primitives.

### MakerIds

```text
System.Collections.Generic.List[System.Int32] MakerIds { get; }
```

Gets the collection of marker identifiers associated with the graphics primitives.

### VisibilityIndicators

```text
System.Collections.Generic.List[System.Int32] VisibilityIndicators { get; }
```

Gets the collection of visibility indicators for the graphics primitives.
