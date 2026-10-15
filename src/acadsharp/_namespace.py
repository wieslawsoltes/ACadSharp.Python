"""Shared implementation for convenient lowercase namespace aliases."""

from ._runtime import namespace


def resolve(namespace_name, name):
    if name == "__all__":
        return [value for value in names(namespace_name) if not value.startswith("_")]
    if name.startswith("_"):
        raise AttributeError(name)
    return getattr(namespace(namespace_name), name)


def names(namespace_name):
    return dir(namespace(namespace_name))
