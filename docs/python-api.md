# Python helpers

These helpers supplement the original managed API. They preserve the original `CadDocument` and entity objects, so a document returned by `read()` can be passed to any upstream method.

## Runtime and type access

### `load(*, assembly_dir=None, runtime_config=None, dotnet_root=None)`

Load CoreCLR and the ACadSharp assembly, returning its CLR `Assembly` instance. Repeated calls reuse the loaded assembly. Call before importing original namespaces such as `ACadSharp.Entities` or importing `clr` yourself.

`assembly_dir` overrides the directory containing `ACadSharp.dll`; `ACADSHARP_ASSEMBLY_DIR` supplies the same override through the environment. `runtime_config` selects a Python.NET/CoreCLR runtime configuration file. `dotnet_root` selects a .NET installation root. Omitting these arguments uses the package's bundled assembly and runtime configuration.

An assembly cannot be switched after it has loaded. Run a new Python process to use a different assembly or runtime. The bundled inventory describes the bundled assembly; after overriding it, regenerate the inventory when auditing a different version.

### `namespace(name)`

Import a namespace under `ACadSharp`, `CSMath` or `CSUtilities`, initializing the managed backend if needed. The return value is the Python.NET namespace module.

```python
import acadsharp
entities = acadsharp.namespace("ACadSharp.Entities")
line = entities.Line()
```

### `get_type(fullname)`

Resolve one exported public CLR type by exact full name. Nested names use `+`; generic definitions use a backtick followed by their arity. The returned object is the actual Python.NET type. Unknown or non-public types raise `LookupError`.

```python
Line = acadsharp.get_type("ACadSharp.Entities.Line")
Vertex = acadsharp.get_type("ACadSharp.Entities.LwPolyline+Vertex")
Collection = acadsharp.get_type("ACadSharp.CadObjectCollection`1")
block = acadsharp.tables.BlockRecord("temporary")
lines = Collection[Line](block)
```

A generic type might have constructor constraints or require parameters; consult its generated reference before instantiation.

### `runtime_info()`

Return a dictionary describing the active backend, Python version, CPU architecture, .NET version, Python.NET runtime kind, assembly identity and assembly path. This initializes the managed runtime if necessary. Include the result in bug reports.

### `api()`

Return the bundled machine-readable API inventory without loading .NET or Python.NET. The top-level fields are `schema_version`, `assemblies` and `types`. A type record includes its exact CLR full name, Python name, namespace, kind, generic arity, nesting, base class, interfaces, XML documentation and declared public members.

```python
for item in acadsharp.api()["types"]:
    if item["namespace"] == "ACadSharp.Entities":
        print(item["fullname"], item["kind"])
```

`api.json` is generated from the shipped assembly. Its schema version is independent of the package version. No executable CLR objects appear in this data.

## Files and bytes

### `read(path, *, format=None, configuration=None, notification=None)`

Read a DXF or DWG file and return its managed `CadDocument`. `path` accepts a string or path-like object. `format` is `"dxf"` or `"dwg"`; omit it to infer from the path suffix. `configuration` accepts the corresponding upstream reader configuration object. `notification` accepts a Python callback or an upstream notification delegate.

### `write(document, path, *, format=None, binary=False, configuration=None, notification=None)`

Write a managed document. Format inference and configuration/notification handling follow `read()`. `binary=True` selects binary DXF. DWG is inherently binary; the `binary` DXF option is not applicable to it.

### `loads(data, *, format, configuration=None, notification=None)`

Read a bytes-like value using an explicit `"dxf"` or `"dwg"` format. The helper creates and disposes the required .NET stream.

### `dumps(document, *, format="dxf", binary=False, configuration=None, notification=None)`

Serialize a document to Python `bytes`. The helper manages the .NET stream and supports ASCII DXF, binary DXF and DWG.

```python
from pathlib import Path
import acadsharp

cad = acadsharp.CadDocument()
cad.Entities.Add(acadsharp.entities.Line())
payload = acadsharp.dumps(cad, format="dwg")
copy = acadsharp.loads(payload, format="dwg")
acadsharp.write(copy, Path("copy.dxf"))
```

## Color span adapters

`acadsharp.colors.rgb(color)` returns the three RGB bytes from the upstream `Color.GetRgb()` operation. `acadsharp.colors.index_rgb(index)` returns the palette RGB bytes for an integer from 0 through 255. `acadsharp.colors.true_color_rgb(color)` returns three bytes for a true color and empty bytes for an indexed color, matching `Color.GetTrueColorRgb()`.

These functions call a bundled compiled adapter because Python.NET cannot invoke stack-only span return values. See [interop](interop.md#stack-only-color-return-values) for examples. The original `Color` class remains unchanged.

## Convenience imports

| Python module | Original managed namespace |
| --- | --- |
| `acadsharp.entities` | `ACadSharp.Entities` |
| `acadsharp.tables` | `ACadSharp.Tables` |
| `acadsharp.objects` | `ACadSharp.Objects` |
| `acadsharp.io` | `ACadSharp.IO` |
| `acadsharp.geometry` | `CSMath` |
| `acadsharp.header` | `ACadSharp.Header` |
| `acadsharp.classes` | `ACadSharp.Classes` |
| `acadsharp.types` | `ACadSharp.Types` |

Root-level managed names such as `acadsharp.CadDocument`, `acadsharp.ACadVersion`, `acadsharp.Color`, `acadsharp.XY` and `acadsharp.XYZ` are resolved lazily. Use `namespace()` or original imports to reach every other namespace and avoid name collisions.

The separate `acadsharp.native` module does not initialize Python.NET. Its API is documented in the [native guide](native.md).
