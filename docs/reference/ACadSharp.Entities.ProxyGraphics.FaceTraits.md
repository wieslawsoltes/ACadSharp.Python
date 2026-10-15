# ACadSharp.Entities.ProxyGraphics.FaceTraits

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.ProxyGraphics.FaceTraits`

Represents the traits of a face in proxy graphics, including its normals.

Base type: `ACadSharp.Entities.ProxyGraphics.PrimitiveTraits`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.ProxyGraphics.FaceTraits')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.ProxyGraphics.FaceTraits()
```

### Normals

```text
System.Collections.Generic.List[CSMath.XYZ] Normals { get; }
```

Gets the list of normals associated with the face.
