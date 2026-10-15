#!/usr/bin/env python3
"""Build the pinned ACadSharp sources for the Python.NET distribution."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = ROOT / "external" / "ACadSharp"
PROJECT = UPSTREAM / "src" / "ACadSharp" / "ACadSharp.csproj"
DEFAULT_OUTPUT = ROOT / "src" / "acadsharp" / "_managed"
FRAMEWORK = "net10.0"


def source_digest() -> str:
    """Identify build inputs independently of checkout location and timestamps."""
    digest = hashlib.sha256()
    inputs = [Path(__file__).resolve(), ROOT / "upstream-versions.json",
              UPSTREAM / "LICENSE", UPSTREAM / "src/CSUtilities/LICENSE"]
    for path in (UPSTREAM / "src").rglob("*"):
        if path.is_file() and path.suffix in {
            ".cs", ".csproj", ".projitems", ".props", ".targets", ".snk"
        } and not {"bin", "obj", ".git"}.intersection(path.parts):
            inputs.append(path)
    for path in sorted(inputs):
        digest.update(path.relative_to(ROOT).as_posix().encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


def revision(path: Path) -> str | None:
    if not (path / ".git").exists():
        return None
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "HEAD"],
        text=True, capture_output=True, check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def build(output: Path = DEFAULT_OUTPUT, *, force: bool = False) -> Path:
    shared_sources = UPSTREAM / "src" / "CSUtilities" / "CSMath" / "CSMath.projitems"
    if not PROJECT.is_file() or not shared_sources.is_file():
        raise RuntimeError(
            "ACadSharp sources are missing. In a Git checkout run "
            "'git submodule update --init --recursive'; use the complete source "
            "distribution when building outside Git."
        )
    source_hash = source_digest()
    info_file = output / "build-info.json"
    required = [output / name for name in (
        "ACadSharp.dll", "ACadSharp.xml", "ACadSharp.runtimeconfig.json"
    )]
    if not force and info_file.is_file() and all(path.is_file() for path in required):
        if json.loads(info_file.read_text()).get("source_sha256") == source_hash:
            return output
    if not shutil.which("dotnet"):
        raise RuntimeError(
            "Building ACadSharp from source requires the .NET 10 SDK on PATH. "
            "Install a published wheel to avoid compiling during installation."
        )
    artifacts = ROOT / "artifacts" / "managed"
    artifacts.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "dotnet", "build", str(PROJECT), "--configuration", "Release",
        "--framework", FRAMEWORK, "--output", str(artifacts),
        "-p:TargetFrameworks=" + FRAMEWORK,
        "-p:GeneratePackageOnBuild=false", "-p:ContinuousIntegrationBuild=true",
        "-p:Deterministic=true", "--nologo",
    ], check=True)
    output.mkdir(parents=True, exist_ok=True)
    for name in ("ACadSharp.dll", "ACadSharp.xml"):
        shutil.copy2(artifacts / name, output / name)
    (output / "ACadSharp.runtimeconfig.json").write_text(json.dumps({
        "runtimeOptions": {
            "tfm": FRAMEWORK,
            "framework": {"name": "Microsoft.NETCore.App", "version": "10.0.0"},
            "rollForward": "LatestMinor",
        }
    }, indent=2) + "\n", encoding="utf-8")
    (output / "licenses").mkdir(exist_ok=True)
    for source, name in (
        (UPSTREAM / "LICENSE", "ACadSharp.txt"),
        (UPSTREAM / "src" / "CSUtilities" / "LICENSE", "CSUtilities.txt"),
    ):
        if not source.is_file():
            raise RuntimeError(f"Required upstream license is missing: {source}")
        shutil.copy2(source, output / "licenses" / name)
    info = {
        "framework": FRAMEWORK,
        "source_sha256": source_hash,
        "acadsharp_revision": revision(UPSTREAM),
        "csutilities_revision": revision(UPSTREAM / "src" / "CSUtilities"),
    }
    # Preserve provenance when building from an sdist without Git metadata.
    provenance = ROOT / "upstream-versions.json"
    if provenance.is_file():
        for key, value in json.loads(provenance.read_text()).items():
            if key in info and info[key] is None:
                info[key] = value
    info_file.write_text(json.dumps(info, indent=2) + "\n", encoding="utf-8")
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    print(build(args.output.resolve(), force=args.force))
