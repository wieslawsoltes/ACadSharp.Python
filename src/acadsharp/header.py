"""Lazy alias for the complete ``ACadSharp.Header`` CLR namespace."""

from ._namespace import names, resolve


def __getattr__(name):
    return resolve("ACadSharp.Header", name)


def __dir__():
    return names("ACadSharp.Header")
