"""Lazy alias for the complete ``ACadSharp.Classes`` CLR namespace."""

from ._namespace import names, resolve


def __getattr__(name):
    return resolve("ACadSharp.Classes", name)


def __dir__():
    return names("ACadSharp.Classes")
