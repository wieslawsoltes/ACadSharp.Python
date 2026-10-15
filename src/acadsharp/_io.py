"""Path and bytes conveniences that return the original managed document."""

from __future__ import annotations

import os
from contextlib import suppress

from ._runtime import load, namespace


def _format(path, format):
    value = format.lower().lstrip(".") if isinstance(format, str) else None
    if format is not None and value is None:
        raise TypeError("format must be 'dxf' or 'dwg'")
    if value is None and path is not None:
        value = os.path.splitext(os.fsdecode(path))[1].lower().lstrip(".")
    if value not in {"dxf", "dwg"}:
        raise ValueError("Specify format='dxf' or format='dwg', or use a .dxf/.dwg path")
    return value


def _reader(source, format, configuration, notification):
    io = namespace("ACadSharp.IO")
    factory = io.DxfReader if format == "dxf" else io.DwgReader
    _configuration(io, format, "Reader", configuration)
    callback = io.NotificationEventHandler(notification) if notification is not None else None
    reader = factory(source, callback)
    try:
        if configuration is not None:
            reader.Configuration = configuration
        result = reader.Read()
    except BaseException:
        with suppress(Exception):
            reader.Dispose()
        raise
    else:
        reader.Dispose()
        return result


def _configuration(io, format, kind, value):
    expected = getattr(io, f"{format.title()}{kind}Configuration")
    if value is not None and not isinstance(value, expected):
        raise TypeError(f"configuration must be {expected.__name__}")


def _writer(document, target, format, binary, configuration, notification):
    if binary and format != "dxf":
        raise ValueError("binary is a DXF option; omit it for DWG")
    io = namespace("ACadSharp.IO")
    _configuration(io, format, "Writer", configuration)
    if not isinstance(document, namespace("ACadSharp").CadDocument):
        raise TypeError("document must be an ACadSharp.CadDocument")
    callback = io.NotificationEventHandler(notification) if notification is not None else None
    from System.IO import File

    # Own file streams ourselves: upstream DXF Dispose can fail before Write
    # initializes its writer, and DWG construction can reject a version.
    owned = isinstance(target, str)
    stream = File.Create(target) if owned else target
    try:
        writer = io.DxfWriter(stream, document, binary) if format == "dxf" else io.DwgWriter(stream, document)
        try:
            if configuration is not None:
                writer.Configuration = configuration
            if callback is not None:
                writer.OnNotification += callback
            writer.Write()
        except BaseException:
            with suppress(Exception):
                writer.Dispose()
            raise
        else:
            writer.Dispose()
    finally:
        if owned:
            stream.Dispose()


def read(path, *, format=None, configuration=None, notification=None):
    """Read a DXF/DWG path into a fully editable ``ACadSharp.CadDocument``."""
    return _reader(os.fsdecode(path), _format(path, format), configuration, notification)


def write(document, path, *, format=None, binary=False, configuration=None, notification=None):
    """Write a managed document to DXF/DWG; accept strings and pathlib paths."""
    _writer(document, os.fsdecode(path), _format(path, format), binary, configuration, notification)


def loads(data, *, format, configuration=None, notification=None):
    """Read DXF/DWG bytes into a managed document (``format`` is required)."""
    kind = _format(None, format)
    if not isinstance(data, (bytes, bytearray, memoryview)):
        raise TypeError("data must be bytes, bytearray, or memoryview")
    load()
    from System import Array, Byte
    from System.IO import MemoryStream

    stream = MemoryStream(Array[Byte](bytes(data)))
    try:
        return _reader(stream, kind, configuration, notification)
    finally:
        stream.Dispose()


def dumps(document, *, format="dxf", binary=False, configuration=None, notification=None):
    """Serialize a managed document as DXF/DWG bytes."""
    kind = _format(None, format)
    load()
    from System.IO import MemoryStream

    stream = MemoryStream()
    try:
        _writer(document, stream, kind, binary, configuration, notification)
        # MemoryStream.ToArray remains available after the writer closes it.
        return bytes(stream.ToArray())
    finally:
        stream.Dispose()
