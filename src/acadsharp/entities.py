"""Lazy alias for the complete ``ACadSharp.Entities`` CLR namespace."""

from ._namespace import names, resolve


def __getattr__(name):
    return resolve("ACadSharp.Entities", name)


def __dir__():
    return names("ACadSharp.Entities")
