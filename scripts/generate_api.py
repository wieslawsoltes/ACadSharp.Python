#!/usr/bin/env python3
"""Reflect the shipped assembly into a deterministic Python API inventory/reference.

Requires Python.NET and the same .NET runtime used by the package. No source regex
or hand-maintained type allowlist is used: GetExportedTypes is authoritative.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

# Python-only metadata import does not initialize the managed runtime.
sys.path.insert(0, str(ROOT / "src"))
from acadsharp.colors import ADAPTERS  # noqa: E402


def typename(t):
    """Readable CLR signature including generic arguments, arrays and references."""
    if t.IsByRef:
        return typename(t.GetElementType()) + "&"
    if t.IsPointer:
        return typename(t.GetElementType()) + "*"
    if t.IsArray:
        return typename(t.GetElementType()) + "[" + "," * (t.GetArrayRank() - 1) + "]"
    if t.IsGenericParameter:
        return str(t.Name)
    name = str(t.FullName or t.Name).replace("+", ".")
    if t.IsGenericType:
        definition = t.GetGenericTypeDefinition()
        name = re.sub(r"`\d+", "", str(definition.FullName).replace("+", "."))
        return name + "[" + ", ".join(typename(a) for a in t.GetGenericArguments()) + "]"
    return name


def xml_typename(t):
    """Encode a parameter's type using compiler XML documentation ID syntax."""
    if t.IsByRef:
        return xml_typename(t.GetElementType()) + "@"
    if t.IsPointer:
        return xml_typename(t.GetElementType()) + "*"
    if t.IsArray:
        rank = t.GetArrayRank()
        return xml_typename(t.GetElementType()) + ("[]" if rank == 1 else "[" + ",".join(["0:"] * rank) + "]")
    if t.IsGenericParameter:
        return ("``" if t.DeclaringMethod is not None else "`") + str(t.GenericParameterPosition)
    if t.IsGenericType:
        name = str(t.GetGenericTypeDefinition().FullName).replace("+", ".")
        args = iter(t.GetGenericArguments())
        return re.sub(r"`(\d+)", lambda m: "{" + ",".join(xml_typename(next(args)) for _ in range(int(m[1]))) + "}", name)
    return str(t.FullName or t.Name).replace("+", ".")


def xml_member_id(member):
    kind = str(member.MemberType)
    if kind in {"TypeInfo", "NestedType"}:
        return "T:" + str(member.FullName).replace("+", ".")
    prefix = {"Constructor": "M", "Method": "M", "Property": "P", "Event": "E", "Field": "F"}[kind]
    owner = str(member.DeclaringType.FullName).replace("+", ".")
    name = str(member.Name).replace(".", "#")
    if kind == "Method" and member.IsGenericMethod:
        name += "``" + str(len(member.GetGenericArguments()))
    result = prefix + ":" + owner + "." + name
    params = member.GetIndexParameters() if kind == "Property" else member.GetParameters() if kind in {"Method", "Constructor"} else []
    if len(params):
        result += "(" + ",".join(xml_typename(p.ParameterType) for p in params) + ")"
    if kind == "Method" and str(member.Name) in {"op_Implicit", "op_Explicit"}:
        result += "~" + xml_typename(member.ReturnType)
    return result


def xml_text(element):
    if element is None:
        return ""
    parts = [element.text or ""]
    for child in element:
        if child.tag in {"see", "seealso"}:
            parts.append(child.get("cref", child.get("href", child.get("langword", ""))).removeprefix("T:").removeprefix("P:").removeprefix("M:"))
        elif child.tag in {"paramref", "typeparamref"}:
            parts.append(child.get("name", ""))
        else:
            parts.append(xml_text(child))
        parts.append(child.tail or "")
    return " ".join("".join(parts).split())


def documentation(element):
    if element is None:
        return {"summary": ""}
    result = {"summary": xml_text(element.find("summary"))}
    for key in ("remarks", "returns", "value", "example"):
        value = xml_text(element.find(key))
        if value:
            result[key] = value
    params = {p.get("name"): xml_text(p) for p in element.findall("param")}
    if params:
        result["parameters"] = params
    exceptions = [{"type": p.get("cref", "").removeprefix("T:"), "description": xml_text(p)} for p in element.findall("exception")]
    if exceptions:
        result["exceptions"] = exceptions
    inherited = element.find("inheritdoc")
    if inherited is not None:
        result["inheritdoc"] = inherited.get("cref", "base member")
    return result


def parameter(p):
    prefix = "out " if p.IsOut else "ref " if p.ParameterType.IsByRef else ""
    result = prefix + typename(p.ParameterType).removesuffix("&") + " " + str(p.Name)
    if p.IsOptional:
        default = p.DefaultValue
        result += " = " + ("null" if default is None else str(default))
    return result


def member_record(member, xml):
    kind = str(member.MemberType)
    name = str(member.Name)
    if kind in {"NestedType", "TypeInfo"}:
        return None  # Nested types have their own complete records.
    if kind == "Method" and member.IsSpecialName and not name.startswith("op_"):
        return None  # Accessors are represented by the property/event.
    if kind == "Field" and name == "value__":
        return None  # CLR enum implementation detail.
    prefix = "static " if getattr(member, "IsStatic", False) else ""
    if kind in {"Constructor", "Method"}:
        args = ", ".join(parameter(p) for p in member.GetParameters())
        if kind == "Method":
            if member.IsGenericMethod:
                name += "[" + ", ".join(str(t.Name) for t in member.GetGenericArguments()) + "]"
            signature = prefix + typename(member.ReturnType) + " " + name + "(" + args + ")"
        else:
            signature = typename(member.DeclaringType) + "(" + args + ")"
    elif kind == "Property":
        accessors = []
        get = member.GetGetMethod()
        setter = member.GetSetMethod()
        accessor = get or setter
        prefix = "static " if accessor is not None and accessor.IsStatic else ""
        if get is not None:
            accessors.append("get;")
        if setter is not None:
            accessors.append("set;")
        parameters = member.GetIndexParameters()
        suffix = "[" + ", ".join(parameter(p) for p in parameters) + "]" if len(parameters) else ""
        signature = prefix + typename(member.PropertyType) + " " + name + suffix + " { " + " ".join(accessors) + " }"
    elif kind == "Field":
        signature = prefix + typename(member.FieldType) + " " + name
        if member.IsLiteral:
            signature += " = " + str(member.GetRawConstantValue())
    elif kind == "Event":
        signature = "event " + typename(member.EventHandlerType) + " " + name
    else:
        raise ValueError(f"Unhandled reflection member kind: {kind}")
    identity = xml_member_id(member)
    return {"kind": kind.lower(), "name": str(member.Name), "signature": signature, "declaring_type": str(member.DeclaringType.FullName), "xml_id": identity, **({"python_adapter": ADAPTERS[identity]} if identity in ADAPTERS else {}), **documentation(xml.get(identity))}


def inventory(assembly_path):
    from pythonnet import load

    runtimeconfig = assembly_path.with_suffix(".runtimeconfig.json")
    load("coreclr", **({"runtime_config": str(runtimeconfig)} if runtimeconfig.exists() else {}))
    import clr
    from System.Reflection import BindingFlags

    assembly = clr.AddReference(str(assembly_path))
    xml_path = assembly_path.with_suffix(".xml")
    if not xml_path.exists():
        raise SystemExit(f"Missing XML documentation beside assembly: {xml_path}")
    xml = {element.get("name"): element for element in ET.parse(xml_path).findall("./members/member")}
    flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly
    types = []
    for t in sorted(assembly.GetExportedTypes(), key=lambda t: str(t.FullName)):
        base = t.BaseType
        kind = "enum" if t.IsEnum else "interface" if t.IsInterface else "struct" if t.IsValueType else "delegate" if base is not None and str(base.FullName) == "System.MulticastDelegate" else "class"
        members = [record for m in t.GetMembers(flags) if (record := member_record(m, xml)) is not None]
        identity = "T:" + str(t.FullName).replace("+", ".")
        types.append({
            "fullname": str(t.FullName),
            "python_name": re.sub(r"`\d+", "", str(t.FullName).replace("+", ".")),
            "namespace": str(t.Namespace or ""),
            "assembly": str(assembly.GetName().Name),
            "kind": kind,
            "generic_arity": len(t.GetGenericArguments()) if t.IsGenericType else 0,
            "is_nested": bool(t.IsNested),
            "is_abstract": bool(t.IsAbstract),
            "declaring_type": str(t.DeclaringType.FullName) if t.IsNested else None,
            "base_type": typename(base) if base is not None else None,
            "interfaces": sorted(typename(i) for i in t.GetInterfaces()),
            **documentation(xml.get(identity)),
            "members": sorted(members, key=lambda m: (m["kind"], m["name"], m["signature"])),
        })
    return {"schema_version": 1, "assemblies": [{"name": str(assembly.GetName().Name), "version": str(assembly.GetName().Version)}], "types": types}


def filename(fullname):
    return fullname.replace("`", "-").replace("+", ".") + ".md"


def inline_code(value):
    delimiter = "``" if "`" in value else "`"
    return delimiter + value + delimiter


def markdown(data):
    """One page per exported type, plus a namespace index with complete coverage."""
    namespace_types = defaultdict(list)
    pages = {}
    for t in data["types"]:
        namespace_types[t["namespace"]].append(t)
        lines = [f"# {t['python_name']}", "", f"`{t['kind']}` · `{t['assembly']}` · CLR name: {inline_code(t['fullname'])}", "", t["summary"] or "No upstream type summary is available.", ""]
        if t.get("remarks"):
            lines += [t["remarks"], ""]
        if t["base_type"]:
            lines += [f"Base type: `{t['base_type']}`. Inherited members are documented on their declaring type.", ""]
        if t["interfaces"]:
            lines += ["Interfaces: " + ", ".join(f"`{i}`" for i in t["interfaces"]) + ".", ""]
        lines += ["```python", "import acadsharp", f"Type = acadsharp.get_type({t['fullname']!r})", "```", ""]
        if t["generic_arity"]:
            lines += [f"This is an open generic type with {t['generic_arity']} parameter(s). Bind concrete CLR types using `Type[...]` before instantiation.", ""]
        if t["is_abstract"] or t["kind"] == "interface":
            lines += ["This type cannot be instantiated directly.", ""]
        lines += ["## Declared public members", "", "Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.", ""]
        if not t["members"]:
            lines += ["No declared public members.", ""]
        for member in t["members"]:
            lines += [f"### {member['name']}", "", "```text", member["signature"], "```", ""]
            if member.get("python_adapter"):
                lines += [f"**Python adapter:** `{member['python_adapter']}` returns Python `bytes`. The upstream method returns a stack-only span that Python.NET cannot invoke directly; the compiled adapter calls that exact operation and copies its result.", ""]
            if member["summary"]:
                lines += [member["summary"], ""]
            if member.get("inheritdoc"):
                lines += ["Documentation inherited from: " + inline_code(member["inheritdoc"]) + ".", ""]
            for key in ("remarks", "returns", "value", "example"):
                if member.get(key):
                    lines += [f"**{key.title()}:** {member[key]}", ""]
            for name, description in member.get("parameters", {}).items():
                lines += [f"- `{name}`: {description}"]
            if member.get("parameters"):
                lines.append("")
            for error in member.get("exceptions", []):
                lines += [f"- Raises `{error['type']}`: {error['description']}"]
            if member.get("exceptions"):
                lines.append("")
        pages[filename(t["fullname"])] = "\n".join(lines)
    lines = ["# Complete managed API reference", "", f"Generated from the shipped assembly: **{len(data['types'])} exported public types** across **{len(namespace_types)} namespaces**. Every public class, interface, struct, enum, delegate, nested type and open generic definition returned by .NET reflection is included.", "", "Each page lists the type's declared public constructors, properties, fields, events, methods and operators, including overload signatures and upstream XML documentation when present. Inherited members remain available through Python.NET and are documented on their declaring type. A missing upstream summary is reported explicitly; this generator does not invent documentation.", "", "Use `acadsharp.get_type(clr_name)` for exact type resolution, including CLR nested names (`+`) and generic arity suffixes (backticks). Original namespaces such as `ACadSharp.Entities` can be imported after `acadsharp.load()`. The machine-readable equivalent is bundled as `acadsharp/api.json`.", "", "This reference describes the managed backend. See [Native AOT](../native.md) for the separate native backend's implemented operations.", ""]
    for namespace, items in sorted(namespace_types.items()):
        lines += [f"## {namespace}", ""]
        lines += [f"- [{t['python_name']}]({filename(t['fullname'])}) — {t['kind']}" for t in items]
        lines.append("")
    pages["index.md"] = "\n".join(lines)
    return pages


def emit(path, content, check):
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return True
    if check:
        print(f"Out of date: {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}", file=sys.stderr)
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assembly", type=Path, default=ROOT / "src/acadsharp/_managed/ACadSharp.dll")
    parser.add_argument("--output", type=Path, default=ROOT / "src/acadsharp/api.json")
    parser.add_argument("--docs", type=Path, default=ROOT / "docs/reference")
    parser.add_argument("--check", action="store_true", help="Fail if generated inventory/reference differ from checked-in files")
    args = parser.parse_args()
    data = inventory(args.assembly.resolve())
    okay = emit(args.output, json.dumps(data, indent=2, ensure_ascii=False) + "\n", args.check)
    pages = markdown(data)
    for name, content in pages.items():
        okay = emit(args.docs / name, content, args.check) and okay
    for stale in sorted(args.docs.glob("*.md")):
        if stale.name not in pages:
            if args.check:
                print(f"Stale generated page: {stale}", file=sys.stderr)
                okay = False
            else:
                stale.unlink()
    print(f"{'Verified' if args.check else 'Generated'} {len(data['types'])} public types and {sum(len(t['members']) for t in data['types'])} declared public members")
    return 0 if okay else 1


if __name__ == "__main__":
    raise SystemExit(main())
