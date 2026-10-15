#!/usr/bin/env python3
"""Publish the optional NativeAOT C ABI library (requires .NET 10 + native linker)."""
from __future__ import annotations

import argparse
import platform
import json
import shutil
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def host_rid() -> str:
    system = {"Darwin": "osx", "Linux": "linux", "Windows": "win"}[platform.system()]
    arch = {"aarch64": "arm64", "arm64": "arm64", "x86_64": "x64", "AMD64": "x64"}[platform.machine()]
    return f"{system}-{arch}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rid", default=host_rid())
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = (args.output or ROOT / "artifacts" / "native" / args.rid).resolve()
    subprocess.run([
        "dotnet", "publish", str(ROOT / "native" / "ACadSharp.Native" / "ACadSharp.Native.csproj"),
        "--configuration", "Release", "--runtime", args.rid, "--output", str(output),
        "-p:GeneratePackageOnBuild=false",
    ], check=True, cwd=ROOT)
    suffix = ".dll" if args.rid.startswith("win-") else ".dylib" if args.rid.startswith("osx-") else ".so"
    library = output / ("acadsharp_native" + suffix)
    if not library.is_file():
        raise RuntimeError(f"NativeAOT publish did not produce {library}")
    licenses = output / "licenses"
    licenses.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "external/ACadSharp/LICENSE", licenses / "ACadSharp-LICENSE.txt")
    shutil.copy2(ROOT / "external/ACadSharp/src/CSUtilities/LICENSE", licenses / "CSUtilities-LICENSE.txt")
    assets = json.loads((ROOT / "native/ACadSharp.Native/obj/project.assets.json").read_text())
    package_roots = [Path(folder) for folder in assets["packageFolders"]]
    runtime_package = next((p for p in assets["libraries"] if p.lower().startswith("microsoft.netcore.app.runtime." + args.rid + "/")), None)
    # NativeAOT resolves the runtime pack as a download dependency rather than a
    # normal library in some SDK releases; use the restored dependency version.
    if runtime_package is None:
        downloads = assets["project"]["frameworks"]["net10.0"].get("downloadDependencies", [])
        runtime = next(p for p in downloads if p["name"].lower() == "microsoft.netcore.app.runtime." + args.rid)
        runtime_version = runtime["version"].strip("[]").split(",")[0].strip()
        runtime_package = runtime["name"] + "/" + runtime_version
    pack = next(root / runtime_package.lower() for root in package_roots if (root / runtime_package.lower()).is_dir())
    for source, destination in (("LICENSE.TXT", "dotnet-LICENSE.txt"), ("THIRD-PARTY-NOTICES.TXT", "dotnet-THIRD-PARTY-NOTICES.txt")):
        shutil.copy2(pack / source, licenses / destination)
    recorded = ROOT / "upstream-versions.json"
    if (ROOT / "external/ACadSharp/.git").exists():
        revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT / "external/ACadSharp", text=True).strip()
    elif recorded.is_file():
        revision = json.loads(recorded.read_text())["acadsharp_revision"]
    else:
        raise RuntimeError("Source archive is missing upstream-versions.json")
    (output / "build-info.json").write_text(json.dumps({"rid": args.rid, "abi": 1, "acadsharp_commit": revision, "dotnet_runtime": runtime_package.split("/")[1]}, indent=2) + "\n")
    print(library)


if __name__ == "__main__":
    main()
