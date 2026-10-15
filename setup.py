"""Setuptools hooks keep source builds reproducible without an SDK downloader."""

from pathlib import Path
import runpy

from setuptools import setup
from setuptools.command.build_py import build_py
from setuptools.command.sdist import sdist

ROOT = Path(__file__).resolve().parent


class BuildManaged(build_py):
    def run(self):
        runpy.run_path(str(ROOT / "scripts" / "build_managed.py"))["build"]()
        super().run()


class SourceDistribution(sdist):
    def run(self):
        required = ROOT / "external/ACadSharp/src/CSUtilities/CSMath/CSMath.projitems"
        if not required.is_file():
            raise RuntimeError("Initialize recursive submodules before building an sdist")
        super().run()


setup(cmdclass={"build_py": BuildManaged, "sdist": SourceDistribution})
