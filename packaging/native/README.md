# acadsharp-native

This platform wheel contains the NativeAOT shared library used by
`acadsharp.native`. Install `acadsharp[native]` to obtain both packages.
No .NET runtime or Python.NET installation is required for native operations.

Prebuilt wheels for 0.1.0 target Linux x64/Arm64, macOS Arm64 (Apple Silicon),
and Windows x64. Intel macOS has no prebuilt native wheel in this release;
install `acadsharp[managed]` or build locally with `--rid osx-x64` on an Intel Mac.

Build from the complete ACadSharp.Python source checkout:

```sh
python scripts/build_native.py --rid osx-arm64
ACADSHARP_NATIVE_DIR="$PWD/artifacts/native/osx-arm64" python -m build --wheel packaging/native
```

Use the runtime identifier matching the current operating system and CPU.
NativeAOT requires a .NET 10 SDK and the platform's native C/C++ toolchain.
The full object model and native limitations are documented in the main
[project documentation](https://wieslawsoltes.github.io/ACadSharp.Python/).
Native wheels are built from the main project's source distribution; this
binary companion does not publish a separate source distribution.
