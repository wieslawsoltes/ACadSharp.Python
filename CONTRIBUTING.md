# Contributing

## Prepare a checkout

Use Python 3.11 or newer, Git and the .NET 10 SDK. Native builds additionally require the platform's Native AOT compiler/linker prerequisites; see [native development](docs/native.md).

```sh
git clone --recurse-submodules https://github.com/wieslawsoltes/ACadSharp.Python.git
cd ACadSharp.Python
python -m venv .venv
# Activate .venv for your shell.
python -m pip install -e '.[dev,docs]'
python scripts/build_managed.py
python scripts/generate_api.py
python -m pytest
python -m mkdocs build --strict
python -m build
```

Use the commands from [releasing](docs/releasing.md) to inspect and validate wheel/sdist artifacts. Editable installs use the built files in `src/acadsharp/_managed`.

## Architecture

- `src/acadsharp`: lazy managed loader, namespace access, helpers, native Python interface and generated API inventory.
- `external/ACadSharp`: pinned upstream Git submodule, including recursive dependencies.
- `managed/ACadSharp.Python`: compiled adapters for public stack-only signatures Python.NET cannot marshal.
- `native`: Native AOT bridge implementation.
- `scripts`: reproducible managed/native builds, reference generation and packaging verification.
- `tests`: Python tests, including exhaustive exported-type inventory/resolution and functional CAD round trips.
- `docs/reference`: generated public API reference; edit its generator rather than individual pages.
- `examples`: executable documentation examples.

The full public managed object model is exposed through Python.NET. Keep this automatic when adding conveniences; do not replace the original objects with partial Python projections. Native additions must state their supported operation set and validate lifetime/error handling.

## Update upstream deliberately

Advance the `external/ACadSharp` gitlink to a reviewed revision and initialize its recursive submodules. Rebuild the managed assembly, regenerate the API inventory/reference, review the change in exported types and members, and run the complete test suite. Commit the submodule revision and generated artifacts together. Do not edit vendored sources to conceal binding errors.

```sh
git submodule update --init --recursive
python scripts/build_managed.py
python scripts/generate_api.py
python scripts/generate_api.py --check
python -m pytest
```

The generator reflects the compiled assembly and joins compiler XML documentation. It includes public nested types and generic definitions; tests compare the inventory against the assembly rather than trusting a hand-maintained count.

## Documentation

```sh
python -m mkdocs serve
python -m mkdocs build --strict
```

Document Python/.NET conversion pitfalls with tested examples. Be precise about the difference between complete managed API exposure and native operation coverage. New CAD operations should include meaningful assertions against actual serialized content or a round trip.

## Releases

Follow the [release guide](docs/releasing.md). CI builds and validates packages; publishing requires the repository's configured release environment and PyPI Trusted Publisher. Never put credentials in configuration files or commit generated binaries outside the designated packaging workflow.
