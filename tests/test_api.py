"""Validate the complete shipped API against authoritative assembly reflection."""

import json
from pathlib import Path
import subprocess
import sys

import pytest

import acadsharp

INVENTORY = acadsharp.api()


@pytest.fixture(scope="module")
def assembly():
    return acadsharp.load()


def test_inventory_covers_every_exported_type(assembly):
    actual = {str(t.FullName) for t in assembly.GetExportedTypes()}
    declared = [entry["fullname"] for entry in INVENTORY["types"]]
    assert len(declared) == len(set(declared)), "Duplicate exported types in inventory"
    assert set(declared) == actual
    assert INVENTORY["assemblies"] == [
        {"name": str(assembly.GetName().Name), "version": str(assembly.GetName().Version)}
    ]
    # The upstream assembly embeds these namespaces from its recursive sources.
    roots = {entry["namespace"].split(".")[0] for entry in INVENTORY["types"]}
    assert {"ACadSharp", "CSMath", "CSUtilities"} <= roots


@pytest.mark.parametrize("entry", INVENTORY["types"], ids=lambda entry: entry["fullname"])
def test_every_exported_type_resolves_exactly(entry, assembly):
    import clr

    resolved = acadsharp.get_type(entry["fullname"])
    actual = clr.GetClrType(resolved)
    expected = assembly.GetType(entry["fullname"], True)
    assert actual == expected
    assert bool(actual.IsNested) == entry["is_nested"]
    assert (len(actual.GetGenericArguments()) if actual.IsGenericType else 0) == entry["generic_arity"]


@pytest.mark.parametrize("entry", INVENTORY["types"], ids=lambda entry: entry["fullname"])
def test_inventory_covers_declared_public_members(entry, assembly):
    from System.Reflection import BindingFlags

    reflected = assembly.GetType(entry["fullname"], True)
    members = reflected.GetMembers(
        BindingFlags.DeclaredOnly | BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
    )
    # Properties/events represent their accessors. Nested types have independent
    # records, and the enum backing field is an implementation detail.
    expected = {}
    python_type = acadsharp.get_type(entry["fullname"])
    python_names = dir(python_type)
    for member in members:
        kind, name = str(member.MemberType).lower(), str(member.Name)
        if kind == "nestedtype" or (kind == "field" and name == "value__"):
            continue
        if kind == "method" and member.IsSpecialName and not name.startswith("op_"):
            continue
        expected[(kind, name)] = expected.get((kind, name), 0) + 1
        # Verify the public binding exists too; metadata alone cannot prove exposure.
        if kind == "constructor":
            continue
        if kind == "field" and not member.IsStatic:
            assert name in python_names  # Instance fields reject class-level reads.
        elif kind == "property" and len(member.GetIndexParameters()):
            if member.GetGetMethod() is not None:
                assert hasattr(python_type, "__getitem__")
            if member.GetSetMethod() is not None:
                assert hasattr(python_type, "__setitem__")
        else:
            getattr(python_type, name)
    actual = {}
    for member in entry["members"]:
        key = (member["kind"], member["name"])
        actual[key] = actual.get(key, 0) + 1
        assert member["signature"]
        assert member["declaring_type"] == entry["fullname"]
        assert member["xml_id"]
    assert actual == expected


def test_inventory_is_available_without_starting_pythonnet():
    process = subprocess.run(
        [sys.executable, "-c", "import sys, acadsharp; data = acadsharp.api(); "
         "assert data['types']; assert 'clr' not in sys.modules; "
         "assert 'pythonnet' not in sys.modules"],
        check=True, capture_output=True, text=True,
    )
    assert process.returncode == 0


def test_generated_docs_and_inventory_agree():
    root = Path(__file__).resolve().parents[1]
    reference = root / "docs/reference"
    if not reference.is_dir():
        pytest.skip("Reference source is not installed in a wheel")
    for entry in INVENTORY["types"]:
        name = entry["fullname"].replace("`", "-").replace("+", ".") + ".md"
        content = (reference / name).read_text(encoding="utf-8")
        assert entry["fullname"] in content
        for member in entry["members"]:
            assert member["signature"] in content
    on_disk = json.loads((root / "src/acadsharp/api.json").read_text(encoding="utf-8"))
    assert on_disk == INVENTORY


@pytest.mark.parametrize(
    ("script", "argument"),
    [("create_drawing.py", "example.dxf"), ("create_drawing.py", "example.dwg"),
     ("blocks.py", "blocks.dxf"), ("interop.py", None)],
)
def test_documented_examples_run(script, argument, tmp_path):
    import os

    root = Path(__file__).resolve().parents[1]
    path = root / "examples" / script
    if not path.exists():
        pytest.skip("Example source is not installed in a wheel")
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(Path(acadsharp.__file__).resolve().parent.parent)
    command = [sys.executable, str(path)]
    if argument:
        command.append(argument)
    subprocess.run(command, cwd=tmp_path, env=environment, check=True, capture_output=True, text=True)
    if argument:
        subprocess.run(
            [sys.executable, str(root / "examples/inspect_drawing.py"), argument],
            cwd=tmp_path, env=environment, check=True, capture_output=True, text=True,
        )
