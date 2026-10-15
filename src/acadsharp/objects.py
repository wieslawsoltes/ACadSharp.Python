"""Lazy alias for the complete ``ACadSharp.Objects`` CLR namespace."""

from ._namespace import names, resolve


def __getattr__(name):
    return resolve("ACadSharp.Objects", name)


def __dir__():
    return names("ACadSharp.Objects")
