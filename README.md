# ACadSharp.Python

Python access to the complete public object model of [ACadSharp](https://github.com/wieslawsoltes/ACadSharp), with DXF/DWG readers and writers, entities, tables, blocks, objects, geometry, collections, enums and events. The managed backend uses Python.NET to expose the actual .NET types and preserve their behavior. ACadSharp is pinned as a recursive Git submodule.

```sh
python -m pip install 'acadsharp[managed]'
```

Install the [.NET 10 runtime](https://dotnet.microsoft.com/download/dotnet/10.0) for your Python architecture first. Python 3.11 or newer is required. The wheel includes ACadSharp itself; a .NET SDK is needed only to build from source.

```python
from acadsharp import CadDocument, XYZ
from acadsharp.entities import Line, Circle
from acadsharp.io import DxfWriter, DxfReader

cad = CadDocument()
line = Line(XYZ(0, 0, 0), XYZ(100, 50, 0))
cad.Entities.Add(line)

circle = Circle()
circle.Center = XYZ(50, 25, 0)
circle.Radius = 10
cad.Entities.Add(circle)

DxfWriter.Write("drawing.dxf", cad)
restored = DxfReader.Read("drawing.dxf")
for entity in restored.Entities:
    print(entity.ObjectName, entity.Handle)
```

The public .NET spelling remains intact: `StartPoint`, `Layers`, `Add`, and `Read` work as in ACadSharp. Original `ACadSharp`, `CSMath`, and `CSUtilities` namespaces are available after `acadsharp.load()`. Nested types and generics are available too; the generated reference inventories every exported type and its declared public members. Three span-returning color operations use [compiled Python adapters](docs/interop.md#stack-only-color-return-values), preserving their original behavior as Python bytes.

An optional Native AOT backend runs through `ctypes` without Python.NET or an installed .NET runtime. It provides its own documented operation set; it does **not** expose the entire managed object model. See the [native backend guide](docs/native.md) for supported operations, builds, platforms and limitations.

- [Installation and runtime setup](docs/installation.md)
- [Quickstart and executable examples](docs/quickstart.md)
- [Working with the object model](docs/object-model.md)
- [DXF/DWG I/O and notifications](docs/io.md)
- [Python and .NET interoperability](docs/interop.md)
- [Python helpers and configuration](docs/python-api.md)
- [Complete generated API reference](docs/reference/index.md)
- [Native AOT](docs/native.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Building, testing and contributing](CONTRIBUTING.md)
- [Package publishing and releases](docs/releasing.md)

## Development

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

See [CONTRIBUTING.md](CONTRIBUTING.md) for the native build and upstream update workflow. Format compatibility and unimplemented CAD features follow the pinned upstream library; full access to its public API does not imply support for every DWG/DXF feature.

## License

MIT. Bundled ACadSharp, CSMath, and CSUtilities retain their upstream notices; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
