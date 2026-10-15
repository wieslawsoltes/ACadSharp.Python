"""Lazy alias for the complete ``ACadSharp.IO`` CLR namespace."""

from ._namespace import names, resolve


def __getattr__(name):
    return resolve("ACadSharp.IO", name)


def __dir__():
    return names("ACadSharp.IO")
