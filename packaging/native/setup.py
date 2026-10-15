"""Package an explicitly built NativeAOT artifact without guessing its target."""

from pathlib import Path
import json
import os
import platform
import re
import shutil
import subprocess
import sys

from setuptools import Distribution, setup
from setuptools.command.build_py import build_py
from wheel.bdist_wheel import bdist_wheel

ROOT = Path(__file__).resolve().parents[2]


class NativeDistribution(Distribution):
    def has_ext_modules(self):
        return True


class BuildNative(build_py):
    def run(self):
        super().run()
        directory = os.environ.get("ACADSHARP_NATIVE_DIR")
        if not directory:
            raise RuntimeError(
                "Set ACADSHARP_NATIVE_DIR to the output of scripts/build_native.py"
            )
        source = Path(directory).resolve()
        suffix = {"win32": ".dll", "darwin": ".dylib"}.get(sys.platform, ".so")
        library = source / ("acadsharp_native" + suffix)
        if not library.is_file():
            raise RuntimeError(f"Native library for the current platform is missing: {library}")
        destination = Path(self.build_lib) / "acadsharp_native"
        shutil.copy2(library, destination / library.name)
        info_file = source / "build-info.json"
        info = json.loads(info_file.read_text())
        architecture = {"arm64": "arm64", "aarch64": "arm64",
                        "x86_64": "x64", "amd64": "x64"}[platform.machine().lower()]
        host_rid = {"win32": "win", "darwin": "osx"}.get(sys.platform, "linux")
        host_rid += "-" + architecture
        if info.get("rid") != host_rid:
            raise RuntimeError(f"Build this {info.get('rid')} wheel on a matching host, not {host_rid}")
        licenses = source / "licenses"
        for name in ("ACadSharp-LICENSE.txt", "CSUtilities-LICENSE.txt",
                     "dotnet-LICENSE.txt", "dotnet-THIRD-PARTY-NOTICES.txt"):
            if not (licenses / name).is_file():
                raise RuntimeError(f"Required native artifact license is missing: {name}")
        shutil.copytree(licenses, destination / "licenses", dirs_exist_ok=True)
        shutil.copy2(info_file, destination / info_file.name)
        shutil.copy2(ROOT / "LICENSE", destination / "licenses" / "ACadSharp.Python.txt")
        shutil.copy2(ROOT / "THIRD_PARTY_NOTICES.md", destination / "licenses")


class NativeWheel(bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        self.root_is_pure = False

    def get_tag(self):
        _, _, platform_tag = super().get_tag()
        if sys.platform == "darwin":
            # A builder's Python may require a newer macOS than the library.
            # Read the actual Mach-O deployment target rather than borrowing it.
            library = Path(os.environ["ACADSHARP_NATIVE_DIR"]) / "acadsharp_native.dylib"
            headers = subprocess.check_output(["otool", "-l", str(library)], text=True)
            targets = re.findall(r"\bminos\s+(\d+)\.(\d+)", headers)
            targets += re.findall(r"LC_VERSION_MIN_MACOSX\s+cmdsize\s+\d+\s+version\s+(\d+)\.(\d+)", headers)
            if not targets:
                raise RuntimeError("Cannot determine the native library's macOS deployment target")
            major, minor = max((int(major), int(minor)) for major, minor in targets)
            architecture = "arm64" if platform.machine().lower() == "arm64" else "x86_64"
            platform_tag = f"macosx_{major}_{minor}_{architecture}"
        return "py3", "none", platform_tag


setup(distclass=NativeDistribution, cmdclass={"build_py": BuildNative, "bdist_wheel": NativeWheel})
