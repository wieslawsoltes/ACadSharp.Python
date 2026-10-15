"""Lazy alias for the complete ``ACadSharp.Types`` CLR namespace."""

from ._namespace import names, resolve


def __getattr__(name):
    return resolve("ACadSharp.Types", name)


def __dir__():
    return names("ACadSharp.Types")
