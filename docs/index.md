# ACadSharp.Python

Create, inspect, edit and exchange CAD drawings from Python using the public ACadSharp .NET object model. The managed backend keeps upstream types, method overloads, enum values, inheritance, collections and events available through Python.NET.

Start with [installation](installation.md), then run the [quickstart](quickstart.md). The [object model guide](object-model.md) explains documents, tables, blocks and entities; [interoperability](interop.md) covers the Python/.NET boundary. The [Python helper reference](python-api.md) describes loading, dynamic type access, metadata and file/bytes convenience functions. Every exported public type is listed in the [generated API reference](reference/index.md).

The [Native AOT backend](native.md) is a separate option for applications that need to run without Python.NET or an installed .NET runtime. Its implemented operations and limitations are documented explicitly.

The [release guide](releasing.md) describes reproducible builds, CI, package contents, native artifacts and Trusted Publishing. Upstream source is pinned in `external/ACadSharp`, including its recursive submodules.
