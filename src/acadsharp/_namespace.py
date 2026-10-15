"""Shared implementation for convenient lowercase namespace aliases."""

from functools import lru_cache

from ._runtime import load, namespace


def resolve(namespace_name, name):
    if name == "__all__":
        return [value for value in names(namespace_name) if not value.startswith("_")]
    if name.startswith("_"):
        raise AttributeError(name)
    return getattr(namespace(namespace_name), name)


@lru_cache(maxsize=None)
def names(namespace_name):
    # CLR module dir() contains only names already materialized by Python.NET.
    # Enumerate metadata so discovery and star imports also work in a fresh
    # process and include child namespaces such as ACadSharp.Types.Units.
    result = set()
    for item in load().GetExportedTypes():
        containing = str(item.Namespace)
        if containing == namespace_name and not item.IsNested:
            result.add(str(item.Name).split("`")[0])
        elif containing.startswith(namespace_name + "."):
            result.add(containing[len(namespace_name) + 1:].split(".")[0])
    return sorted(result)
