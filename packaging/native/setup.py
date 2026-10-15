"""Package an explicitly built NativeAOT artifact without guessing its target."""

from pathlib import Path
import os
import shutil
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
        licenses = source / "licenses"
        if not licenses.is_dir() or not list(licenses.glob("*")):
            raise RuntimeError("Native artifacts must include their licenses directory")
        shutil.copytree(licenses, destination / "licenses", dirs_exist_ok=True)
        for name in ("build-info.json",):
            if (source / name).is_file():
                shutil.copy2(source / name, destination / name)
        shutil.copy2(ROOT / "LICENSE", destination / "licenses" / "ACadSharp.Python.txt")
        shutil.copy2(ROOT / "THIRD_PARTY_NOTICES.md", destination / "licenses")


class NativeWheel(bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        self.root_is_pure = False

    def get_tag(self):
        _, _, platform_tag = super().get_tag()
        return "py3", "none", platform_tag


setup(distclass=NativeDistribution, cmdclass={"build_py": BuildNative, "bdist_wheel": NativeWheel})
