# Python and .NET interoperability

The package exposes actual CLR types through Python.NET. This guide uses the pinned assembly and executable example `examples/interop.py`. The [Python.NET interoperability reference](https://pythonnet.github.io/pythonnet/python.html) explains the underlying conversion rules.

## Imports, nested types and generics

```python
import acadsharp
acadsharp.load()
from ACadSharp.Entities import Line, LwPolyline
from CSMath import XYZ
from System.Collections.Generic import List

lines = List[Line]()
lines.Add(Line(XYZ.Zero, XYZ(1, 2, 0)))
vertex = LwPolyline.Vertex()
```

Use `acadsharp.get_type()` with a reference entry's exact CLR name when discovering types dynamically. Open generic definitions retain their backtick arity in the inventory, for example ``ACadSharp.CadObjectCollection`1`` if present in your assembly. Bind generic definitions with CLR type arguments before constructing them. Generic methods likewise support `method[Type](...)`.

## Properties, collections and enums

Property names match C#. CLR collections generally support iteration; a collection's `Count` property is the portable way to obtain its item count. Collection-specific indexers are accessible using brackets. Prefer explicit enum members and `System.Int32`, `UInt64`, `Double` or other CLR primitives when overload selection is ambiguous.

```python
from acadsharp import ACadVersion, CadDocument

cad = CadDocument(ACadVersion.AC1032)
for layer in cad.Layers:
    print(layer.Name)
```

A concrete overload pitfall is `Color`: `Color(System.Int16(1))` selects indexed color 1 (red), while `Color(1)` selects the integer true-color constructor. Use named colors such as `Color.Red`, or explicit `System.Int16` values for ACI palette indices.

## Overloads and out parameters

Inspect `Type.Method.__doc__` or `help(Type)` to see the live method signatures. When automatic overload resolution is ambiguous, `Method.__overloads__[ParameterType, ...](...)` chooses an exact parameter list. Constructors also have `__overloads__`.

.NET `out` and `ref` parameters appear in a Python return value or tuple. For a method that returns a Boolean and one output object, unpack `(success, value)`. Use the live method signature to provide any required placeholders or explicit types.

```python
from acadsharp.entities import Line

line = Line()
cad.Entities.Add(line)
found, result = cad.TryGetCadObject[Line](line.Handle)
assert found and result == line
```

## Structs and arrays

Read a struct-valued property, modify it, then assign it back. For example, `point = line.StartPoint; point.X = 10; line.StartPoint = point`. Assigning `line.StartPoint.X` alone can change a boxed copy.

Construct explicit CLR arrays for APIs expecting arrays:

```python
from System import Array, Byte
from System.IO import MemoryStream

payload = Array[Byte](b"example bytes")
stream = MemoryStream(payload)
try:
    assert stream.Length == 13
finally:
    stream.Dispose()
```

## Delegates, events and lifetime

A Python callable can back a .NET delegate. Retain the callable/delegate until the managed operation ends, and unsubscribe event handlers when their subscription is no longer needed. Use `source.Event += handler` and `source.Event -= handler` with the actual event from the reference.

Dispose instances implementing `IDisposable` using `try/finally` and `Dispose()`. Do not rely on Python garbage collection to release file handles promptly. The package does not add thread safety to ACadSharp's mutable documents; coordinate access in your application.

## Stack-only color return values

Three upstream color methods return `ReadOnlySpan<byte>`, a stack-only .NET type that Python.NET cannot return to Python. Use the compiled adapters, which invoke the original methods and return copied Python `bytes`:

| Upstream operation | Python adapter |
| --- | --- |
| `color.GetRgb()` | `acadsharp.colors.rgb(color)` |
| `color.GetTrueColorRgb()` | `acadsharp.colors.true_color_rgb(color)` |
| `Color.GetIndexRGB(index)` | `acadsharp.colors.index_rgb(index)` |

```python
from acadsharp import Color
from acadsharp.colors import rgb, true_color_rgb, index_rgb

assert rgb(Color.Red) == bytes((255, 0, 0))
assert true_color_rgb(Color(12, 34, 56)) == bytes((12, 34, 56))
assert true_color_rgb(Color.Red) == b""  # Original indexed-color behavior.
assert index_rgb(5) == bytes((0, 0, 255))
```

The original `Color` type and its identity are preserved. Calling these three span-returning methods directly raises a .NET `NotSupportedException` through Python.NET. `Color.R`, `Color.G`, and `Color.B` work directly. The adapter copies the actual upstream result, including its indexed-color and sentinel behavior. A reflection test checks every public method for stack-only/pointer signatures and fails if upstream adds an operation without an adapter.

## Type hints

The Python wrapper contains type information for its own helpers. Managed classes are created dynamically by Python.NET; static type checkers cannot infer their entire reflected surface from Python source. `api.json` and the generated reference provide the complete upstream signatures. At runtime, use `help()`, `__doc__`, `dir()` and reflection for discovery.
