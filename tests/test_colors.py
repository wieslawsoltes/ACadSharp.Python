"""Exercise compiled adapters for the complete upstream stack-only API surface."""

import importlib

import pytest

import acadsharp
from acadsharp.colors import ADAPTERS, index_rgb, rgb, true_color_rgb


def test_every_stack_only_signature_has_a_python_adapter():
    assembly = acadsharp.load()
    from System.Reflection import BindingFlags

    flags = BindingFlags.Public | BindingFlags.Static | BindingFlags.Instance | BindingFlags.DeclaredOnly
    def requires_adapter(clr_type):
        if clr_type.IsByRefLike or clr_type.IsPointer:
            return True
        return bool(clr_type.HasElementType and requires_adapter(clr_type.GetElementType()))

    unsupported = set()
    for clr_type in assembly.GetExportedTypes():
        assert not clr_type.IsByRefLike, f"New stack-only public type needs an adapter: {clr_type}"
        for method in clr_type.GetMethods(flags):
            types = [method.ReturnType, *(p.ParameterType for p in method.GetParameters())]
            if not any(requires_adapter(t) for t in types):
                continue
            identity = f"M:{clr_type.FullName}.{method.Name}"
            parameters = method.GetParameters()
            if len(parameters):
                identity += "(" + ",".join(str(p.ParameterType.FullName) for p in parameters) + ")"
            unsupported.add(identity)
        for constructor in clr_type.GetConstructors(flags):
            assert not any(requires_adapter(p.ParameterType)
                           for p in constructor.GetParameters()), str(constructor)
    assert unsupported == set(ADAPTERS), "Update compatibility adapters when the upstream surface changes"
    for target in ADAPTERS.values():
        module, name = target.rsplit(".", 1)
        assert callable(getattr(importlib.import_module(module), name))


def test_all_palette_indices_match_original_color_properties():
    from System import Int16

    for index in range(256):
        color = acadsharp.Color(Int16(index))
        expected = bytes((color.R, color.G, color.B))
        assert rgb(color) == expected
        assert index_rgb(index) == expected


@pytest.mark.parametrize("components", [(0, 0, 0), (255, 255, 255), (23, 101, 245), (0, 0, 1)])
def test_true_colors_preserve_rgb_bytes(components):
    color = acadsharp.Color(*components)
    assert color.IsTrueColor
    assert rgb(color) == bytes(components)
    assert true_color_rgb(color) == bytes(components)


def test_true_color_operation_preserves_upstream_indexed_semantics():
    # Upstream returns default(ReadOnlySpan<byte>) for indexed colors.
    assert true_color_rgb(acadsharp.Color.Red) == b""
    assert rgb(acadsharp.Color.Red) == b"\xff\x00\x00"


@pytest.mark.parametrize("index", [-1, 256, 1.5, "red"])
def test_invalid_palette_argument_is_rejected(index):
    with pytest.raises((TypeError, OverflowError)):
        index_rgb(index)


def test_color_adapter_does_not_replace_original_types():
    import ACadSharp

    assert acadsharp.Color is ACadSharp.Color
    assert rgb(ACadSharp.Color.Green) == b"\x00\xff\x00"
    with pytest.raises(TypeError):
        rgb("red")


def test_generated_inventory_marks_stack_only_adapters():
    inventory = acadsharp.api()
    actual = {
        member["xml_id"]: member["python_adapter"]
        for entry in inventory["types"] for member in entry["members"]
        if "python_adapter" in member
    }
    assert actual == ADAPTERS


def test_sentinel_colors_follow_upstream_palette_casts():
    assert rgb(acadsharp.Color.ByBlock) == index_rgb(0)
    assert rgb(acadsharp.Color.ByLayer) == index_rgb(0)
    assert rgb(acadsharp.Color.ByEntity) == index_rgb(1)
    assert true_color_rgb(acadsharp.Color.ByLayer) == b""
