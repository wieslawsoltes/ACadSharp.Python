# Changelog

## 0.1.0 (2026-10-15)

Initial Python distribution of the pinned ACadSharp public object model.

- Lazy Python.NET/CoreCLR loading and original CLR namespace/type access, including nested and generic types.
- Complete generated inventory and reference for 607 exported types and 5,790 declared public members.
- DXF/DWG files and bytes helpers, including ASCII and binary DXF.
- Compiled adapters for upstream color operations returning stack-only spans.
- Optional Native AOT package for the operation set documented in the native guide.
- Native wheels for Linux x64/Arm64, macOS Arm64, and Windows x64. Intel macOS users can use the managed backend or a local `osx-x64` native build; this release omits hosted Intel macOS CI and its native wheel.
- Reproducible managed/native packaging, CI, release workflows and documentation.
