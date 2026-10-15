# Troubleshooting

## Missing Python.NET

Install the managed extra in the interpreter running your application:

```sh
python -m pip install 'acadsharp[managed]'
```

The base package can be imported without Python.NET for native-only applications. Managed type access requires the extra.

## CoreCLR cannot be found or started

Run `dotnet --list-runtimes` and verify `Microsoft.NETCore.App 10.*` is installed. Check that Python and .NET share an architecture. Set `DOTNET_ROOT` if .NET is installed in a custom directory. Restart Python after changing runtime settings; a previously initialized runtime cannot be replaced within the process.

Load `acadsharp` before importing `clr` or `ACadSharp`. Importing `clr` first can select Python.NET's platform default runtime rather than CoreCLR. If another library owns runtime initialization, configure it to use CoreCLR.

## Managed assembly is missing in a source checkout

Initialize all recursive submodules and build the assembly:

```sh
git submodule update --init --recursive
python scripts/build_managed.py
```

Installed release wheels already bundle the assembly. Building from a source distribution requires the .NET 10 SDK.

## A method does not accept a Python value

Read the live method's `__doc__`, the generated [reference](reference/index.md), and [interoperability guide](interop.md). Use explicit CLR types for ambiguous numeric arguments, CLR collections/arrays where required, and .NET streams instead of Python file objects. Properties and methods retain upstream capitalization.

## Coordinate edits appear to disappear

`XYZ` and other .NET structs use value semantics. Assign the modified value back to its containing property or collection:

```python
point = entity.StartPoint
point.X = 20
entity.StartPoint = point
```

## CAD content is missing after a round trip

Collect reader and writer notifications. Compare the pinned ACadSharp version's feature and format support with the input drawing. Check the specific entities, references and properties required by your application after re-reading output. The binding cannot add upstream format support by exposing a type.

## Native library load failures

See the [native guide](native.md). Check OS, CPU architecture, wheel availability and the shared library search configuration. Managed assembly files (`.dll`) and Native AOT shared libraries serve different backends and are not interchangeable.

## Reporting an issue

Include Python version, OS/architecture, package version, `dotnet --info` for managed issues, backend, a minimal reproducer, the exception and captured notifications. Attach the smallest shareable CAD file that reproduces a parsing issue. Record the ACadSharp submodule revision for source builds.
