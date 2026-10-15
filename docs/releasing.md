# Releasing and maintaining packages

The repository publishes two distributions at the same version:

| Distribution | Contents | Runtime requirements |
| --- | --- | --- |
| `acadsharp` | Python interface, API catalog, managed assembly and interop adapter, XML reference, licenses | Python 3.11+; install `[managed]` and .NET 10 for Python.NET |
| `acadsharp-native` | Platform-specific NativeAOT shared library and licenses | Python 3.11+ and supported native platform; no .NET installation |

The universal managed wheel is built from the source distribution, which includes
the recursive ACadSharp and CSUtilities source trees. Neither source builds nor
package installation download a .NET SDK. Source builds require an already
installed .NET 10 SDK. CI explicitly provisions its build toolchain.

## Local verification

```sh
git submodule update --init --recursive
python -m pip install -e '.[dev,docs]'
python scripts/build_managed.py
python scripts/generate_api.py --assembly src/acadsharp/_managed/ACadSharp.dll --check
python -m pytest tests --ignore=tests/test_native.py
python -m ruff check src tests scripts setup.py packaging
python -m mkdocs build --strict
python -m build
python -m twine check --strict dist/*
python scripts/check_dist.py dist
```

`python -m build` creates the source archive first, extracts it into an isolated
temporary directory, and builds the wheel there. This verifies the source
distribution is sufficient without the original Git checkout or its submodules.
`check_dist.py` checks the assembly, XML docs, runtime configuration, type catalog,
upstream source inputs and licenses, and rejects generated build directories or
Git metadata in the source archive.

To build the native companion locally, select your runtime identifier:
`linux-x64`, `linux-arm64`, `osx-x64`, `osx-arm64`, or `win-x64`.

```sh
python scripts/build_native.py --rid osx-arm64
ACADSHARP_NATIVE_DIR="$PWD/artifacts/native/osx-arm64" \
  python -m build --wheel --outdir dist-native packaging/native
```

In PowerShell, set `$env:ACADSHARP_NATIVE_DIR` to the absolute artifact directory
before running the wheel command. NativeAOT requires the platform C/C++ toolchain:
Xcode Command Line Tools on macOS, Visual Studio C++ tools on Windows, or Clang and
zlib development headers on Linux. Native wheels have a `py3-none-<platform>` tag;
they use a C ABI through `ctypes` and do not depend on a CPython extension ABI.
The companion has no separate source archive; build it from the main project's
complete source archive or recursive checkout.

## Continuous integration

`ci.yml` invokes reusable `build.yml` for branches and pull requests. It:

- Builds and audits the managed wheel and source archive.
- Installs the built wheel on Ubuntu, Windows, and macOS under Python 3.11–3.14.
- Builds native wheels for Linux x64/Arm64, macOS x64/Arm64, and Windows x64.
- Builds Linux binaries inside the official `manylinux_2_28` images and runs
  `auditwheel repair` to inspect and package their ELF dependencies.
- Tests each installed native wheel without Python.NET installed.
- Checks lint, generated API reference consistency, and documentation links.

Native builds run on the corresponding CPU architecture. The Linux wheel's
manylinux tag declares its actual glibc compatibility; Linux musl/Alpine and
Windows Arm64 wheels are not currently published. macOS wheel tags are derived
from the shared library's Mach-O deployment target; the filename declares that
requirement independently of the Python interpreter used to build the wheel.

## One-time service configuration

An owner must configure external services before the first public release:

1. Create the four GitHub environments listed below. Add the repository's
   chosen release protection rules to both production environments.
2. On each package index, create a pending Trusted Publisher for each project
   with owner `wieslawsoltes`, repository `ACadSharp.Python`, workflow
   `release.yml`, and the project's exact environment from this table. For
   existing projects, add the publisher in the project's publishing settings.
   Package names must be available or owned by the publishing account.
3. In GitHub Settings → Pages, select **GitHub Actions** as the build source.
   The `docs.yml` workflow deploys the rendered site through the `github-pages`
   environment on main, version tags, or manual dispatch.

| Project | PyPI environment | TestPyPI environment | Downloaded release artifacts |
| --- | --- | --- | --- |
| `acadsharp` | `pypi` | `testpypi` | `distributions-managed` (wheel and source archive) |
| `acadsharp-native` | `pypi-native` | `testpypi-native` | `distributions-native-*` (native wheels) |

PyPI rejects a second **pending** publisher with an identical owner, repository,
workflow and environment for a different project name. The separate environments
make each pending publishing identity unique while allowing both packages to use
`release.yml`. Registering `acadsharp-native` with `pypi` instead of `pypi-native`
will collide with the pending `acadsharp` publisher. Apply the same separation
when configuring TestPyPI.

The publish job runs once per project. Each run downloads only that project's
artifact group and checks its distribution filename prefix before upload. The
GitHub release waits for both publishing runs to succeed and attaches all built
distributions.

On 2026-10-15, both production PyPI pending publishers were verified with the
project/environment mapping above. All four GitHub publishing environments and
the GitHub Pages workflow source are configured. These registrations authorize
the matching workflow identities; package publication still requires a successful
release run.

TestPyPI publisher registration has not been verified. Before a rehearsal,
configure both TestPyPI projects with their respective `testpypi` and
`testpypi-native` environments. GitHub environment creation alone does not grant
permission to publish on either package index.

Trusted Publishing exchanges GitHub's short-lived OIDC identity for an upload
credential. No PyPI API token belongs in the repository or its secrets. See
[PyPI's Trusted Publishing guide](https://docs.pypi.org/trusted-publishers/using-a-publisher/)
and [adding a publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).

## Cut a release

Before the first manual workflow run, merge the reviewed implementation branch
into the repository's default branch. GitHub only enables `workflow_dispatch`
for workflows that exist on the default branch; after that initial merge, a
manual run can select a release branch or tag. This applies to both `release.yml`
and `docs.yml`. Keeping the implementation on its feature branch does not
publish a package or deploy documentation.
See GitHub's [manual workflow prerequisites](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow).

1. Update the version in `pyproject.toml`,
   `packaging/native/pyproject.toml`, both Python `__version__` values, and the
   exact native/base dependency pins, and the `Version` in
   `managed/ACadSharp.Python/ACadSharp.Python.csproj`. Add the release's changes to
   the changelog.
2. If updating ACadSharp, commit both recursive submodule revisions, update
   `upstream-versions.json`, rebuild, and regenerate the API reference. Review the
   upstream version's supported CAD formats and any changed public types.
3. Complete local checks and CI, then create the exact `v<version>` tag on the
   reviewed release commit. `check_release.py` rejects a mismatching tag or pin.
4. To rehearse without publishing to PyPI, manually dispatch `release.yml` from
   the release branch with `index=testpypi`. TestPyPI accepts a branch build;
   production requires the matching version tag. Use a fresh version if that
   filename already exists on TestPyPI.
5. Pushing a version tag triggers a fresh complete build and test run. After the
   `pypi` and `pypi-native` environments permit their respective publishing runs,
   each run uploads its package with attestations. Once both succeed, the workflow
   creates a GitHub release containing all exact distributions.

Be aware that **pushing any `v*` tag automatically requests a production release**;
manual `testpypi` dispatch does not cancel that trigger. Rehearse from a branch
before pushing the version tag.
Package indexes do not permit replacing a published filename; fix a bad release
with a new version. A failed partial upload can be recovered by uploading only
the missing, already verified artifacts after inspecting the index contents.

## Provenance and licenses

The managed assembly's `build-info.json` records its target framework, content
hash of source inputs, and ACadSharp/CSUtilities revisions. The release source
archive retains those revisions in `upstream-versions.json`. Upstream sources
remain pinned Git submodules in the repository. Dependency update pull requests
must regenerate the reference and pass the same test suite as a release.

Both distributions carry the upstream MIT license texts. The native companion
also carries the .NET runtime license and third-party notices because NativeAOT
embeds runtime components. These files are required by the native wheel builder.
