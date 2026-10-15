# ACadSharp.Python

[![CI](https://github.com/wieslawsoltes/ACadSharp.Python/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/wieslawsoltes/ACadSharp.Python/actions/workflows/ci.yml)
[![Documentation](https://github.com/wieslawsoltes/ACadSharp.Python/actions/workflows/docs.yml/badge.svg?branch=main)](https://wieslawsoltes.github.io/ACadSharp.Python/)
[![Python versions](https://img.shields.io/pypi/pyversions/acadsharp.svg)](https://pypi.org/project/acadsharp/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/wieslawsoltes/ACadSharp.Python/blob/main/LICENSE)

Create, inspect, edit and exchange CAD drawings from Python with [ACadSharp](https://github.com/wieslawsoltes/ACadSharp). Read and write DXF/DWG files, work with entities, layers, blocks and geometry, and use the complete public .NET object model through Python.NET. An optional NativeAOT backend supports CAD operations through `ctypes` without Python.NET or a separately installed .NET runtime.

**[Documentation](https://wieslawsoltes.github.io/ACadSharp.Python/)** · **[Quickstart](https://wieslawsoltes.github.io/ACadSharp.Python/quickstart/)** · **[API reference](https://wieslawsoltes.github.io/ACadSharp.Python/reference/)** · **[Releases](https://github.com/wieslawsoltes/ACadSharp.Python/releases)**

## Highlights

- **CAD files:** read and write DWG, ASCII DXF and binary DXF, with reader/writer configuration and notification handling.
- **Object model:** documents, entities, tables, layers, blocks, dictionaries, extended data, geometry, collections and enums.
- **Managed interoperability:** original CLR types, overloads, nested types, generics and events retain their upstream behavior.
- **Python helpers:** load files using strings or `pathlib` paths, serialize drawings to bytes, and inspect the API without starting .NET.
- **Native deployment:** platform wheels bundle a compiled NativeAOT library for supported operations.
- **Reference documentation:** the pinned assembly exposes **607 public types and 5,790 declared public members**, with generated signatures and upstream XML documentation.

Format compatibility and unsupported CAD features follow the pinned upstream ACadSharp library. Access to its complete public API does not imply support for every DWG/DXF feature.

## Packages

Both distributions are published on PyPI and require Python 3.11 or newer.

| Package | Latest version | Contents | Recommended installation |
| --- | --- | --- | --- |
| [`acadsharp`](https://pypi.org/project/acadsharp/) | [![acadsharp on PyPI](https://img.shields.io/pypi/v/acadsharp.svg)](https://pypi.org/project/acadsharp/) | Python interface, managed assemblies, API catalog and native bridge client | `python -m pip install 'acadsharp[managed]'` |
| [`acadsharp-native`](https://pypi.org/project/acadsharp-native/) | [![acadsharp-native on PyPI](https://img.shields.io/pypi/v/acadsharp-native.svg)](https://pypi.org/project/acadsharp-native/) | Optional platform-specific NativeAOT shared library | `python -m pip install 'acadsharp[native]'` |

The extras select the dependencies for your backend: `[managed]` installs Python.NET, while `[native]` installs the matching `acadsharp-native` version. Installing the base `acadsharp` package alone does not install either backend dependency or start .NET.

## Choose a backend

| | Managed / Python.NET | Native / NativeAOT |
| --- | --- | --- |
| API access | Complete public managed object model using the original CLR types | Object construction, editing, inspection, collections and file I/O through native proxies |
| Runtime requirements | Python.NET and a matching-architecture .NET 10 runtime | Matching native wheel; Linux also requires system ICU |
| Generics and callbacks | CLR generics, delegates and event subscriptions | Existing compiled collections work; runtime generic construction and Python callbacks require the managed backend |
| Best fit | Full API access and .NET interoperability | Supported CAD operations without a separate .NET installation |

The native backend has its own documented operation set. See [supported operations and restrictions](https://wieslawsoltes.github.io/ACadSharp.Python/native/#nativeaot-restrictions) before choosing it for an application that needs dynamic CLR behavior.

## Installation

### Managed backend

Install the [.NET 10 runtime](https://dotnet.microsoft.com/download/dotnet/10.0) for the same architecture as Python, then:

```sh
python -m pip install 'acadsharp[managed]'
dotnet --list-runtimes
```

The runtime list should include `Microsoft.NETCore.App 10.*`. The wheel bundles ACadSharp and its interop adapter; no AutoCAD or separate NuGet installation is required. The .NET SDK is needed only when building from source. See [runtime setup](https://wieslawsoltes.github.io/ACadSharp.Python/installation/#custom-runtime-configuration) for custom .NET locations and environment configuration.

### Native backend

```sh
python -m pip install 'acadsharp[native]'
```

Native use requires neither Python.NET nor a separately installed .NET runtime. Prebuilt native wheels for **0.1.0** cover:

| Platform | Architectures | Notes |
| --- | --- | --- |
| Linux | x64, Arm64 | manylinux wheels for glibc systems; system ICU libraries are required |
| macOS | Arm64 / Apple Silicon | macOS 12 or newer, as declared by the wheel tag |
| Windows | x64 | Native Windows wheel |

Intel macOS is omitted from hosted CI and has no prebuilt native wheel in 0.1.0. Intel Mac users can use the managed backend or [build locally](https://wieslawsoltes.github.io/ACadSharp.Python/native/#building-from-source) with `--rid osx-x64`. Linux musl/Alpine and Windows Arm64 wheels are not currently published.

## Quickstart

### Create and round-trip a drawing

This example uses the managed backend:

```python
import acadsharp
from acadsharp import CadDocument, XYZ
from acadsharp.entities import Circle, Line
from acadsharp.tables import Layer

document = CadDocument()
layer = Layer("Geometry")
document.Layers.Add(layer)

line = Line(XYZ(0, 0, 0), XYZ(100, 50, 0))
line.Layer = layer
document.Entities.Add(line)

circle = Circle()
circle.Center = XYZ(50, 25, 0)
circle.Radius = 10
circle.Layer = layer
document.Entities.Add(circle)

acadsharp.write(document, "drawing.dxf")
acadsharp.write(document, "drawing.dwg")
restored = acadsharp.read("drawing.dwg")

assert restored.Entities.Count == 2
for entity in restored.Entities:
    print(entity.ObjectName, entity.Handle, entity.Layer.Name)
```

`CadDocument()` creates the default tables, model space and paper space. Adding entities through `document.Entities` assigns their document ownership and handles through ACadSharp.

### Work with bytes

Continue with the managed document above to exchange a drawing in memory:

```python
payload = acadsharp.dumps(document, format="dxf", binary=True)
restored = acadsharp.loads(payload, format="dxf")
assert restored.Entities.Count == 2
```

The same helpers support `format="dwg"`. Original `DxfReader`, `DxfWriter`, `DwgReader` and `DwgWriter` types remain available through `acadsharp.io`; see [I/O and notifications](https://wieslawsoltes.github.io/ACadSharp.Python/io/) and the [Python helper reference](https://wieslawsoltes.github.io/ACadSharp.Python/python-api/).

### Use the native backend

The native API has an explicit session lifetime and uses its own type proxies:

```python
from acadsharp import native

with native.load() as cad:
    document = cad.ACadSharp.CadDocument()
    line = cad.ACadSharp.Entities.Line()
    line.StartPoint = cad.CSMath.XYZ(0, 0, 0)
    line.EndPoint = cad.CSMath.XYZ(100, 50, 0)
    document.Entities.Add(line)

    cad.write(document, "native.dwg")
    restored = cad.read("native.dwg")
    assert len(restored.Entities) == 1
```

Leaving the `with` block releases the session's native object handles. See the [native guide](https://wieslawsoltes.github.io/ACadSharp.Python/native/) for collections, overloads, ref/out parameters, ownership and errors.

## Using the full object model

The managed backend preserves public .NET spelling: `StartPoint`, `Layers`, `Add` and `Read` work as in ACadSharp. Original `ACadSharp`, `CSMath` and `CSUtilities` namespaces are available after `acadsharp.load()`; `acadsharp.get_type(fullname)` also resolves nested types and generic definitions.

Use convenience modules such as `acadsharp.entities`, `acadsharp.tables`, `acadsharp.objects` and `acadsharp.geometry`, or import the original namespaces directly. Three span-returning color operations use [compiled Python adapters](https://wieslawsoltes.github.io/ACadSharp.Python/interop/#stack-only-color-return-values) that preserve their upstream behavior as Python bytes.

The [object model guide](https://wieslawsoltes.github.io/ACadSharp.Python/object-model/) covers editing drawings, and the [interoperability guide](https://wieslawsoltes.github.io/ACadSharp.Python/interop/) explains conversions, generics, events and CLR value types.

## Documentation and examples

| Resource | What it covers |
| --- | --- |
| [Installation](https://wieslawsoltes.github.io/ACadSharp.Python/installation/) | Runtime setup, source installs and custom configuration |
| [Quickstart](https://wieslawsoltes.github.io/ACadSharp.Python/quickstart/) | Creating, reading and inspecting drawings |
| [Object model](https://wieslawsoltes.github.io/ACadSharp.Python/object-model/) | Entities, tables, blocks, collections and ownership |
| [Python helpers](https://wieslawsoltes.github.io/ACadSharp.Python/python-api/) | File/bytes I/O, runtime loading and type discovery |
| [DXF/DWG I/O](https://wieslawsoltes.github.io/ACadSharp.Python/io/) | Configurations, notifications and upstream format behavior |
| [Python/.NET interop](https://wieslawsoltes.github.io/ACadSharp.Python/interop/) | Generics, delegates, events and conversion rules |
| [Generated API reference](https://wieslawsoltes.github.io/ACadSharp.Python/reference/) | All exported public types and declared public members |
| [NativeAOT](https://wieslawsoltes.github.io/ACadSharp.Python/native/) | Native operations, platforms, builds and restrictions |
| [Troubleshooting](https://wieslawsoltes.github.io/ACadSharp.Python/troubleshooting/) | Diagnosing installation and runtime issues |
| [Release guide](https://wieslawsoltes.github.io/ACadSharp.Python/releasing/) | Package builds, CI and Trusted Publishing |

Runnable [examples](https://github.com/wieslawsoltes/ACadSharp.Python/tree/main/examples) are included in a source checkout:

```sh
python examples/create_drawing.py drawing.dxf
python examples/inspect_drawing.py drawing.dxf
python examples/blocks.py blocks.dxf
python examples/interop.py
```

`create_drawing.py` also accepts a `.dwg` output path.

## Development

ACadSharp is pinned as a recursive Git submodule. Use Python 3.11 or newer and the .NET 10 SDK:

```sh
git clone --recurse-submodules https://github.com/wieslawsoltes/ACadSharp.Python.git
cd ACadSharp.Python
python -m venv .venv
# POSIX: source .venv/bin/activate
# PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e '.[dev,docs]'
python scripts/build_managed.py
python scripts/generate_api.py
python -m pytest
python -m mkdocs build --strict
python -m build
```

CI checks installed managed wheels on Linux, Windows and macOS with Python 3.11–3.14, builds and tests the four native wheel targets, validates distribution contents, and checks generated API documentation. Native tests run without Python.NET installed.

See [CONTRIBUTING.md](https://github.com/wieslawsoltes/ACadSharp.Python/blob/main/CONTRIBUTING.md) for native builds and upstream updates. Report bugs with a minimal reproducer, package/backend versions, operating system and architecture in [GitHub Issues](https://github.com/wieslawsoltes/ACadSharp.Python/issues).

## License

MIT. Bundled ACadSharp, CSMath and CSUtilities retain their upstream notices; see [THIRD_PARTY_NOTICES.md](https://github.com/wieslawsoltes/ACadSharp.Python/blob/main/THIRD_PARTY_NOTICES.md). Native wheels also include the .NET runtime license and third-party notices.
