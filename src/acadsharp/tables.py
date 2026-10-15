"""Lazy alias for the complete ``ACadSharp.Tables`` CLR namespace."""

from ._namespace import names, resolve


def __getattr__(name):
    return resolve("ACadSharp.Tables", name)


def __dir__():
    return names("ACadSharp.Tables")
