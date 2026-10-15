#!/usr/bin/env python3
"""Audit publishable distributions for binaries, licenses and complete sources."""

from pathlib import Path, PurePosixPath
import sys
import tarfile
import zipfile


def check(directory: Path) -> None:
    wheels = list(directory.glob("acadsharp-*-py3-none-any.whl"))
    archives = list(directory.glob("acadsharp-*.tar.gz"))
    assert len(wheels) == 1 and len(archives) == 1, "Expected one wheel and one sdist"
    with zipfile.ZipFile(wheels[0]) as wheel:
        names = set(wheel.namelist())
        for path in (
            "acadsharp/__init__.py", "acadsharp/py.typed", "acadsharp/api.json",
            "acadsharp/_managed/ACadSharp.dll", "acadsharp/_managed/ACadSharp.xml",
            "acadsharp/_managed/ACadSharp.runtimeconfig.json",
            "acadsharp/_managed/build-info.json",
            "acadsharp/_managed/licenses/ACadSharp.txt",
            "acadsharp/_managed/licenses/CSUtilities.txt",
        ):
            assert path in names, f"Missing wheel artifact: {path}"
        assert any(name.endswith(".dist-info/licenses/LICENSE") for name in names)
    with tarfile.open(archives[0]) as archive:
        names = {str(PurePosixPath(name).relative_to(PurePosixPath(name).parts[0]))
                 for name in archive.getnames()}
        for path in (
            "scripts/build_managed.py", "upstream-versions.json",
            "external/ACadSharp/src/ACadSharp/ACadSharp.csproj",
            "external/ACadSharp/src/ACadSharp/CadDocument.cs",
            "external/ACadSharp/src/ACadSharp.snk",
            "external/ACadSharp/src/Directory.Build.props",
            "external/ACadSharp/src/CSUtilities/CSMath/CSMath.projitems",
            "external/ACadSharp/src/CSUtilities/CSUtilities/CSUtilities.projitems",
            "external/ACadSharp/LICENSE", "external/ACadSharp/src/CSUtilities/LICENSE",
        ):
            assert path in names, f"Missing source artifact: {path}"
        for name in names:
            assert not {".git", "bin", "obj", "__pycache__"}.intersection(
                PurePosixPath(name).parts
            ), f"Unexpected build or repository metadata: {name}"
    print(f"Verified {wheels[0].name} and {archives[0].name}")


if __name__ == "__main__":
    check(Path(sys.argv[1] if len(sys.argv) > 1 else "dist"))
