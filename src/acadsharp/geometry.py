"""Lazy alias for the complete ``CSMath`` CLR namespace."""

from ._namespace import names, resolve


def __getattr__(name):
    return resolve("CSMath", name)


def __dir__():
    return names("CSMath")
