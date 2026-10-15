# NativeAOT backend

The optional `acadsharp-native` package runs ACadSharp from CPython through
`ctypes`. It contains a .NET 10 NativeAOT shared library, including its runtime,
so neither pythonnet nor a separately installed .NET runtime is needed. The
managed backend provides the complete CLR interop surface; this native backend
provides object construction, editing, inspection and file I/O subject to the
NativeAOT restrictions below.

```sh
pip install acadsharp-native
```

```python
from acadsharp import native

with native.load() as cad:
    document = cad.ACadSharp.CadDocument()
    line = cad.ACadSharp.Entities.Line()
    line.StartPoint = cad.CSMath.XYZ(1, 2, 3)
    line.EndPoint = cad.CSMath.XYZ(10, 20, 30)
    document.Entities.Add(line)

    layer = cad.ACadSharp.Tables.Layer("Geometry")
    document.Layers.Add(layer)
    line.Layer = layer

    cad.write(document, "drawing.dwg")
    cad.write(document, "drawing.dxf")
    loaded = cad.read("drawing.dwg")
    for entity in loaded.Entities:
        print(entity.type_name, entity.Handle, entity.Layer.Name)
```

`read` and `write` infer `dxf` or `dwg` from the file extension. Pass `format=`
for another extension and `binary=True` for binary DXF. These operations use the
same upstream ACadSharp readers and writers as the managed package. Upstream
format/version support and limitations apply unchanged.

## Object model

All 607 public types in the pinned ACadSharp assembly are discoverable through
`cad.types`, including the `CSMath` and `CSUtilities` namespaces compiled into
ACadSharp. Namespaces and nested types support attribute access, such as
`cad.ACadSharp.Entities.LwPolyline.Vertex(2, 3)`. Use `cad.type(full_name)` for
names that cannot be written as Python identifiers, and `cad.describe(full_name)`
for constructors, properties, fields, method signatures, events and nested types.
`instance.describe()` also works for returned closed generic collection types.

Ordinary public constructors, methods, properties and fields are reflected at
runtime. Static members are accessed on the type proxy. CLR enums are integer
values carrying `type_name` and `name`. Python lists and tuples convert to arrays
when a method accepts a compatible array or sequence interface. Collection
proxies support `len`, iteration, integer/name indexing and writable indexers.
Their upstream methods, such as `Add`, `Remove`, and `Clear`, remain available.
`Color.GetRgb()`, `Color.GetTrueColorRgb()`, and `Color.GetIndexRGB(index)`
return byte-array proxies, which can be converted with `list(...)` or `bytes(...)`.
These three upstream methods return unboxable `ReadOnlySpan<byte>` values;
the native bridge uses compiled adapters while preserving their method names.

```python
with native.load() as cad:
    doc = cad.ACadSharp.CadDocument(cad.ACadSharp.ACadVersion.AC1032)
    doc.Layers.Add(cad.ACadSharp.Tables.Layer("Objects"))
    success, layer = doc.Layers.TryGetValue("Objects", None)
    assert success and layer.Name == "Objects"
    point = cad.CSMath.XYZ.construct(5, signature=["System.Double"])
    print(point.X, point.Y, point.Z)
```

For an overloaded constructor, use `construct(*args, signature=[...])` or pass
`signature=` to the type call. Methods accept the same keyword through their
attribute callable or `object.call("MethodName", *args, signature=[...])`.
Signatures use fully qualified CLR parameter type names, including `&` for
by-reference parameters. Ref/out arguments occupy their parameter positions;
pass `None` for an `out` argument. The result is a tuple containing the return
value followed by each ref/out value in declaration order. Ambiguous overloads
raise an error asking for an explicit signature rather than selecting arbitrarily.

CLR value types are boxed copies. For example, editing `line.StartPoint.X`
changes a temporary vector, so assign the whole value back:

```python
point = line.StartPoint
point.X = 42
line.StartPoint = point
```

`get(name)`, `set(name, value)` and `call(name, ...)` provide explicit member
access if a CLR name conflicts with a Python proxy helper. Compare underlying
objects using their CLR `Equals` method; separate Python proxies can refer to
the same CLR object.

## Ownership and errors

Use `with native.load() as cad` or call `cad.close()` to release every outstanding
handle in that session. An individual proxy's `close()` releases its reference;
other proxies to the same object remain valid. Garbage collection also releases
proxy handles. Closed handles fail predictably when used again. Objects cannot
be passed between `NativeRuntime` sessions.

Releasing a handle does **not** invoke the CLR object's `Dispose` method because
other handles or the document can still refer to it. Invoke `obj.Dispose()` for
an explicitly created disposable reader/writer/stream. Iteration disposes its
internal enumerator automatically when exhausted or closed. The shared library
stays loaded for the lifetime of the Python process.

The C ABI catches managed exceptions and returns their type and message.
Python raises `NativeError` with a `managed_type` attribute. Missing attribute
lookups become `AttributeError`; index and key failures become `IndexError` and
`KeyError`. Calls are serialized within the native library, including calls from
separate sessions. This provides bridge safety, not parallel execution of CAD
operations.

## NativeAOT restrictions

The native package is an optional backend, not a replacement for every feature
of pythonnet. These features require the managed backend:

- Constructing arbitrary closed generic CLR types or calling open generic methods
  with runtime type arguments. Existing compiled generic collections returned by
  ACadSharp remain usable.
- Python callbacks, CLR delegate/event subscriptions, Python subclasses of CLR
  classes, and Python implementations of CLR interfaces.
- Loading additional managed assemblies or JIT-compiling code at runtime.
- Automatic conversions for arbitrary Python objects, dictionaries, file-like
  objects, NumPy arrays, or CLR types from unrelated assemblies.

The bridge preserves the complete ACadSharp assembly and reflection metadata
using `TrimmerRootAssembly` and `rd.xml`. NativeAOT still emits trimming and
dynamic-code analysis warnings for reflection and generic operations. These are
not hidden: the test suite covers complete public-type discovery, every default
constructible entity, metadata, model edits, collections, overloads, ref/out,
ownership, all 256 indexed colors, and actual ASCII DXF, binary DXF and DWG
round trips. Twenty-one upstream reference drawings also exercise R12–2018 file
versions with complex drawings. This is evidence
for those operations, not a guarantee that every conceivable reflected call is
AOT compatible. Use the managed backend if an operation requires unavailable
runtime code or reflection metadata.

## Building from source

Install the .NET 10 SDK and the host platform's native toolchain. On macOS use
Xcode command line tools; on Linux install clang and zlib development headers;
on Windows install Visual Studio C++ build tools and the Windows SDK. Linux
binaries retain .NET globalization support and require the system ICU libraries
at runtime (for example, the distribution's `libicu` package).

```sh
git submodule update --init --recursive
python scripts/build_native.py
```

The script publishes to `artifacts/native/<RID>/`, alongside build provenance
and the upstream/.NET license notices. It accepts `--rid` and `--output`.
NativeAOT builds should run on the target operating system; the supported release
matrix is maintained in the CI workflows. Set the library explicitly for a
source checkout:

```sh
export ACADSHARP_NATIVE_LIBRARY="$PWD/artifacts/native/osx-arm64/acadsharp_native.dylib"
python -m pytest tests/test_native.py
```

The other library names are `acadsharp_native.so` on Linux and
`acadsharp_native.dll` on Windows. You can also pass the absolute library path
to `native.load(path)`. A built wheel finds its library through the
`acadsharp_native` provider package. See [releasing](releasing.md) for packaging.

## C ABI

[`acadsharp_native.h`](https://github.com/wieslawsoltes/ACadSharp.Python/blob/v0.1.0/native/ACadSharp.Native/acadsharp_native.h) declares the
three exports: `acadsharp_abi_version`, `acadsharp_call` and `acadsharp_free`.
ABI version 1 accepts null-terminated UTF-8 JSON requests. Every allocated
response, including an error, must be freed exactly once with `acadsharp_free`.
The Python wrapper handles this in a `finally` block. Never use the C library's
`free` on an allocation returned by this library.

Requests name an `op`: `info`, `types`, `describe`, `create`, `get`, `set`,
`invoke`, `getitem`, `setitem`, `length`, `iterate`, `next`, `dispose_iterator`,
`read`, `write`, `string`, or `release`. Object operations identify a numeric
`handle`; static/constructor operations identify a fully qualified `type`.
Successful responses have `{"ok": true, "result": ...}` and errors have
`{"ok": false, "error": "CLR.Exception.Type", "message": "..."}`. Object results
carry `$ref` and `$type`; references passed as arguments carry `$ref`. Enum
values carry `$enum`, `value` and `name`. Nonfinite floating-point numbers carry
`$number`. The wrapper source is the reference for the request schemas.
