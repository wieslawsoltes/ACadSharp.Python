# Installation

## Managed backend

Use CPython 3.11 or newer with the .NET 10 runtime. Python and .NET must use the same architecture: for example, both ARM64 on an Apple Silicon Mac, or both x64 on x64 Windows/Linux.

```sh
python -m pip install 'acadsharp[managed]'
dotnet --list-runtimes
```

The runtime list must include `Microsoft.NETCore.App 10.*`. Download the runtime from [Microsoft](https://dotnet.microsoft.com/download/dotnet/10.0); the larger SDK also includes it. Installing the package does not install .NET. The wheel bundles ACadSharp's managed assembly and its XML documentation. You do not need a separate NuGet install or an AutoCAD installation.

```python
import acadsharp
acadsharp.load()
from ACadSharp import CadDocument
print(CadDocument().Header.Version)
```

The base `acadsharp` distribution keeps managed initialization lazy. The `[managed]` extra installs Python.NET; use that extra when working with the full object model. Importing `acadsharp` alone does not start .NET. A managed type import or `acadsharp.load()` starts CoreCLR for the process.

## Native backend

See [Native AOT](native.md) for the `acadsharp[native]` extra, available wheel platforms and how to build a native shared library. Native use does not require Python.NET or an installed .NET runtime. A native wheel has to match your operating system and architecture.

Prebuilt native wheels for 0.1.0 target Linux x64/Arm64, macOS Arm64 (Apple Silicon), and Windows x64. On Intel macOS, use the [managed backend](#managed-backend) or [build the native library locally](native.md#building-from-source) with `--rid osx-x64`; an Intel macOS native wheel is not included in this release.

## From a Git checkout

Install the .NET 10 SDK, then:

```sh
git clone --recurse-submodules https://github.com/wieslawsoltes/ACadSharp.Python.git
cd ACadSharp.Python
python -m venv .venv
# Activate the environment using the command appropriate for your shell.
python -m pip install -e '.[dev,docs]'
python scripts/build_managed.py
```

For an existing checkout, initialize source dependencies first:

```sh
git submodule update --init --recursive
```

Build a redistributable wheel with `python -m build`. The source distribution includes the pinned upstream source needed for rebuilding; the .NET SDK is still required for a source build. See [releasing](releasing.md) for artifact validation.

## Custom runtime configuration

The package loads CoreCLR. If your host application initializes Python.NET itself, initialize it with CoreCLR before importing managed types. A process can host only one selected Python.NET runtime; switching between Mono, .NET Framework and CoreCLR after initialization is not supported.

For an SDK/runtime installed outside standard locations, set `DOTNET_ROOT` to that installation's root before starting Python. Keep process architecture consistent when using Rosetta, conda, virtual environments or container images.
