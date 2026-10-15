# Third-party notices

ACadSharp.Python is licensed under the MIT license in `LICENSE`.

The managed and native distributions contain ACadSharp and the CSMath and
CSUtilities source components compiled into it. These projects are MIT licensed:

- ACadSharp: Copyright (c) 2021 Albert Domenech,
  <https://github.com/wieslawsoltes/ACadSharp>.
- CSUtilities: Copyright (c) 2020 Albert Domenech,
  <https://github.com/DomCR/CSUtilities>.

The exact upstream revisions are recorded in `upstream-versions.json` in source
distributions and in `acadsharp/_managed/build-info.json` in the managed wheel.
Complete upstream license texts accompany the binaries in their `licenses`
directory. Source distributions include the original `LICENSE` files.

The optional NativeAOT wheel also includes portions of the .NET runtime,
licensed under MIT. Its license and third-party notices are included alongside
the shared library. Python.NET is a separately installed MIT-licensed dependency
of the `managed` extra and is not bundled in these distributions.
