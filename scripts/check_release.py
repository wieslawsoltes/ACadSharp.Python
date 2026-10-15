#!/usr/bin/env python3
"""Reject releases whose tag, package versions, or companion pins disagree."""

import ast
import json
import os
from pathlib import Path
import subprocess
import tomllib
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
base = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]
native = tomllib.loads((ROOT / "packaging/native/pyproject.toml").read_text())["project"]
version = base["version"]
assert native["version"] == version, "Native and managed versions differ"
adapter = ET.parse(ROOT / "managed/ACadSharp.Python/ACadSharp.Python.csproj")
assert adapter.findtext(".//Version") == version, "Managed adapter version differs"
assert f"acadsharp-native=={version}" in base["optional-dependencies"]["native"]
assert f"acadsharp=={version}" in native["dependencies"]
for source in ("src/acadsharp/__init__.py", "packaging/native/src/acadsharp_native/__init__.py"):
    module = ast.parse((ROOT / source).read_text())
    versions = [ast.literal_eval(node.value) for node in module.body
                if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == "__version__"
                        for target in node.targets)]
    assert versions == [version], f"Version differs in {source}"
provenance = json.loads((ROOT / "upstream-versions.json").read_text())
for path, key in (
    ("external/ACadSharp", "acadsharp_revision"),
    ("external/ACadSharp/src/CSUtilities", "csutilities_revision"),
):
    if (ROOT / path / ".git").exists():
        actual = subprocess.check_output(["git", "-C", str(ROOT / path), "rev-parse", "HEAD"], text=True).strip()
        assert actual == provenance[key], f"Update upstream-versions.json for {path}"
if os.environ.get("RELEASE_INDEX", "pypi") != "testpypi":
    assert os.environ.get("GITHUB_REF") == f"refs/tags/v{version}", (
        f"Run production releases from the exact version tag v{version}"
    )
print(f"Release metadata matches {version}")
