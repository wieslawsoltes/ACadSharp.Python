using System.Collections;
using System.Globalization;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Text.Json;
using System.Text.Json.Nodes;
using ACadSharp;
using ACadSharp.IO;

namespace ACadSharp.Native;

/// <summary>A versioned C ABI. Every response allocation must be freed by its caller.</summary>
public static unsafe class Exports
{
    private static readonly object Gate = new();
    private static readonly Dictionary<long, object> Objects = new();
    private static readonly Dictionary<string, Type> Types = typeof(CadDocument).Assembly
        .GetExportedTypes().ToDictionary(t => t.FullName!, StringComparer.Ordinal);
    private static long _nextHandle;
    private const BindingFlags Public = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static | BindingFlags.FlattenHierarchy;

    [UnmanagedCallersOnly(EntryPoint = "acadsharp_abi_version")]
    public static int AbiVersion() => 1;

    [UnmanagedCallersOnly(EntryPoint = "acadsharp_call")]
    public static nint Call(byte* request)
    {
        // Do not permit a managed exception to escape an unmanaged entry point.
        JsonObject response;
        try
        {
            string text = Marshal.PtrToStringUTF8((nint)request) ?? throw new ArgumentNullException(nameof(request));
            using JsonDocument document = JsonDocument.Parse(text);
            lock (Gate)
                response = new JsonObject { ["ok"] = true, ["result"] = Execute(document.RootElement) };
        }
        catch (Exception error)
        {
            while (error is TargetInvocationException && error.InnerException is not null) error = error.InnerException;
            response = new JsonObject { ["ok"] = false, ["error"] = error.GetType().FullName, ["message"] = error.Message };
        }
        return Marshal.StringToCoTaskMemUTF8(response.ToJsonString());
    }

    [UnmanagedCallersOnly(EntryPoint = "acadsharp_free")]
    public static void Free(nint response) => Marshal.FreeCoTaskMem(response);

    private static JsonNode? Execute(JsonElement request)
    {
        string op = request.GetProperty("op").GetString()!;
        switch (op)
        {
            case "info":
                return new JsonObject { ["abi"] = 1, ["acadsharp"] = typeof(CadDocument).Assembly.GetName().Version?.ToString(),
                    ["type_count"] = Types.Count, ["handle_count"] = Objects.Count };
            case "types": return new JsonArray(Types.Keys.Order().Select(s => (JsonNode?)JsonValue.Create(s)).ToArray());
            case "describe": return Describe(request.TryGetProperty("handle", out var described) ? Object(described.GetInt64()).GetType() : FindType(request.GetProperty("type").GetString()!));
            case "release":
                Objects.Remove(request.GetProperty("handle").GetInt64());
                return null;
            case "create":
            {
                Type type = FindType(request.GetProperty("type").GetString()!);
                JsonElement[] args = Arguments(request);
                if (type.IsEnum)
                    return Encode(args.Length == 0 ? Enum.ToObject(type, 0) : ConvertValue(args[0], type, out _));
                if (type.IsValueType && args.Length == 0) return Encode(Activator.CreateInstance(type));
                var match = Bind(type.GetConstructors(), args, Signature(request));
                return Encode(((ConstructorInfo)match.Method).Invoke(match.Arguments));
            }
            case "read":
            {
                string path = request.GetProperty("path").GetString()!;
                string format = request.GetProperty("format").GetString()!;
                return Encode(format == "dwg" ? DwgReader.Read(path) : format == "dxf" ? DxfReader.Read(path)
                    : throw new ArgumentException("Format must be dxf or dwg."));
            }
            case "write":
            {
                CadDocument document = (CadDocument)Object(request.GetProperty("handle").GetInt64());
                string path = request.GetProperty("path").GetString()!;
                string format = request.GetProperty("format").GetString()!;
                if (format == "dwg") DwgWriter.Write(path, document);
                else if (format == "dxf") DxfWriter.Write(path, document, request.TryGetProperty("binary", out var binary) && binary.GetBoolean());
                else throw new ArgumentException("Format must be dxf or dwg.");
                return null;
            }
        }
        object? target = request.TryGetProperty("handle", out var handle) ? Object(handle.GetInt64()) : null;
        Type targetType = target?.GetType() ?? FindType(request.GetProperty("type").GetString()!);
        BindingFlags flags = Public & ~(target is null ? BindingFlags.Instance : BindingFlags.Static);
        string name = request.TryGetProperty("name", out var nameValue) ? nameValue.GetString()! : "";
        switch (op)
        {
            case "get":
            {
                PropertyInfo? property = targetType.GetProperties(flags).FirstOrDefault(p => p.Name == name && p.GetIndexParameters().Length == 0 && p.GetMethod?.IsPublic == true);
                if (property is not null) return Encode(property.GetValue(target));
                FieldInfo? field = targetType.GetField(name, flags);
                if (field is not null) return Encode(field.GetValue(target));
                Type? nested = targetType.GetNestedType(name, BindingFlags.Public);
                if (nested is not null) return new JsonObject { ["$type_ref"] = nested.FullName };
                if (targetType.GetMethods(flags).Any(m => m.Name == name)) return new JsonObject { ["$method"] = name };
                throw new MissingMemberException(targetType.FullName, name);
            }
            case "set":
            {
                JsonElement value = request.GetProperty("value");
                PropertyInfo? property = targetType.GetProperties(flags).FirstOrDefault(p => p.Name == name && p.GetIndexParameters().Length == 0);
                if (property?.SetMethod?.IsPublic == true) property.SetValue(target, ConvertValue(value, property.PropertyType, out _));
                else if (targetType.GetField(name, flags) is FieldInfo field && !field.IsInitOnly && !field.IsLiteral)
                    field.SetValue(target, ConvertValue(value, field.FieldType, out _));
                else throw new MissingMemberException($"Public writable member {targetType.FullName}.{name} was not found.");
                return null;
            }
            case "invoke":
            {
                var match = Bind(targetType.GetMethods(flags).Where(m => m.Name == name && !m.ContainsGenericParameters), Arguments(request), Signature(request));
                object? result = ((MethodInfo)match.Method).Invoke(target, match.Arguments);
                var byrefs = match.Method.GetParameters().Select((p, i) => (p, i)).Where(pair => pair.p.ParameterType.IsByRef).ToArray();
                if (byrefs.Length == 0) return Encode(result);
                return new JsonObject { ["$return"] = Encode(result), ["$out"] = new JsonArray(byrefs.Select(pair => Encode(match.Arguments[pair.i])).ToArray()) };
            }
            case "getitem":
            {
                JsonElement index = request.GetProperty("index");
                if (target is Array array) return Encode(array.GetValue(index.GetInt32()));
                foreach (PropertyInfo property in targetType.GetProperties(flags).Where(p => p.GetMethod?.IsPublic == true && p.GetIndexParameters().Length == 1))
                {
                    object? converted;
                    try { converted = ConvertValue(index, property.GetIndexParameters()[0].ParameterType, out _); }
                    catch (ArgumentException) { continue; }
                    return Encode(property.GetValue(target, new[] { converted }));
                }
                if (target is IEnumerable enumerable && index.ValueKind == JsonValueKind.Number)
                {
                    int selected = index.GetInt32();
                    if (selected < 0) throw new IndexOutOfRangeException();
                    foreach (object? item in enumerable) if (selected-- == 0) return Encode(item);
                    throw new IndexOutOfRangeException();
                }
                throw new MissingMemberException($"No compatible indexer on {targetType.FullName}.");
            }
            case "setitem":
            {
                JsonElement index = request.GetProperty("index"), value = request.GetProperty("value");
                if (target is Array array) { array.SetValue(ConvertValue(value, targetType.GetElementType()!, out _), index.GetInt32()); return null; }
                foreach (PropertyInfo property in targetType.GetProperties(flags).Where(p => p.SetMethod?.IsPublic == true && p.GetIndexParameters().Length == 1))
                {
                    object? convertedIndex, convertedValue;
                    try
                    {
                        convertedIndex = ConvertValue(index, property.GetIndexParameters()[0].ParameterType, out _);
                        convertedValue = ConvertValue(value, property.PropertyType, out _);
                    }
                    catch (ArgumentException) { continue; }
                    property.SetValue(target, convertedValue, new[] { convertedIndex });
                    return null;
                }
                throw new MissingMemberException($"No compatible writable indexer on {targetType.FullName}.");
            }
            case "length":
                if (target is ICollection collection) return JsonValue.Create(collection.Count);
                PropertyInfo? count = targetType.GetProperty("Count");
                if (count is not null) return Encode(count.GetValue(target));
                if (target is IEnumerable values) { int length = 0; foreach (object? ignored in values) length++; return JsonValue.Create(length); }
                throw new ArgumentException("Object is not a collection.");
            case "iterate":
                if (target is IEnumerable items) return Encode(items.GetEnumerator());
                throw new ArgumentException("Object is not iterable.");
            case "next":
                if (target is IEnumerator iterator)
                    return iterator.MoveNext() ? new JsonObject { ["done"] = false, ["value"] = Encode(iterator.Current) } : new JsonObject { ["done"] = true };
                throw new ArgumentException("Object is not an iterator.");
            case "dispose_iterator":
                if (target is IEnumerator && target is IDisposable disposable) disposable.Dispose();
                return null;
            case "string": return JsonValue.Create(target?.ToString() ?? targetType.ToString());
            default: throw new ArgumentException($"Unknown operation '{op}'.");
        }
    }

    private static Type FindType(string name) => Types.TryGetValue(name, out Type? type) ? type : throw new TypeLoadException($"Public ACadSharp type '{name}' was not found.");
    private static object Object(long handle) => Objects.TryGetValue(handle, out object? value) ? value : throw new ObjectDisposedException($"Native handle {handle}");
    private static JsonElement[] Arguments(JsonElement request) => request.TryGetProperty("args", out var args) ? args.EnumerateArray().ToArray() : Array.Empty<JsonElement>();
    private static string[]? Signature(JsonElement request) => request.TryGetProperty("signature", out var signature) ? signature.EnumerateArray().Select(p => p.GetString()!).ToArray() : null;

    private static (MethodBase Method, object?[] Arguments) Bind(IEnumerable<MethodBase> methods, JsonElement[] arguments, string[]? signature)
    {
        var candidates = new List<(MethodBase Method, object?[] Arguments, int Score)>();
        foreach (MethodBase method in methods)
        {
            ParameterInfo[] parameters = method.GetParameters();
            if (signature is not null && !parameters.Select(p => p.ParameterType.FullName).SequenceEqual(signature)) continue;
            bool variadic = parameters.LastOrDefault()?.GetCustomAttribute<ParamArrayAttribute>() is not null;
            if ((!variadic && arguments.Length > parameters.Length) || parameters.Take(Math.Min(arguments.Length, parameters.Length)).Any(p => p.ParameterType.IsPointer)) continue;
            object?[] converted = new object?[parameters.Length];
            int score = 0;
            bool compatible = true;
            for (int i = 0; i < parameters.Length; i++)
            {
                ParameterInfo parameter = parameters[i];
                try
                {
                    if (variadic && i == parameters.Length - 1 && (i >= arguments.Length || arguments.Length != parameters.Length || arguments[i].ValueKind != JsonValueKind.Array))
                    {
                        Type elementType = parameter.ParameterType.GetElementType()!;
                        Array values = Array.CreateInstance(elementType, Math.Max(0, arguments.Length - i));
                        for (int j = i; j < arguments.Length; j++) values.SetValue(ConvertValue(arguments[j], elementType, out _), j - i);
                        converted[i] = values;
                        score += 5;
                    }
                    else if (i < arguments.Length)
                    {
                        if (parameter.IsOut) converted[i] = null;
                        else { converted[i] = ConvertValue(arguments[i], parameter.ParameterType, out int conversionScore); score += conversionScore; }
                    }
                    else if (parameter.IsOptional) { converted[i] = parameter.DefaultValue; score += 10; }
                    else { compatible = false; break; }
                }
                catch (Exception error) when (error is ArgumentException or InvalidCastException or OverflowException or FormatException or NotSupportedException)
                { compatible = false; break; }
            }
            if (compatible) candidates.Add((method, converted, score));
        }
        if (candidates.Count == 0) throw new MissingMethodException("No supported overload accepts these arguments. Use describe() for signatures; callbacks and open generic methods are unavailable in NativeAOT.");
        candidates.Sort((a, b) => a.Score.CompareTo(b.Score));
        if (candidates.Count > 1 && candidates[0].Score == candidates[1].Score)
            throw new AmbiguousMatchException("Several overloads match. Pass an explicit signature of fully qualified parameter type names to call() or construct().");
        return (candidates[0].Method, candidates[0].Arguments);
    }

    private static object? ConvertValue(JsonElement value, Type type, out int score)
    {
        score = 0;
        if (type.IsByRef) type = type.GetElementType()!;
        Type? nullable = Nullable.GetUnderlyingType(type);
        if (value.ValueKind == JsonValueKind.Null)
        {
            if (!type.IsValueType || nullable is not null) { score = 1; return null; }
            throw new ArgumentException($"null cannot be converted to {type}.");
        }
        type = nullable ?? type;
        if (value.ValueKind == JsonValueKind.Object && value.TryGetProperty("$ref", out var reference))
        {
            object instance = Object(reference.GetInt64());
            if (!type.IsInstanceOfType(instance)) throw new ArgumentException($"{instance.GetType()} is not assignable to {type}.");
            score = type == instance.GetType() ? 0 : type == typeof(object) ? 10 : 1;
            return instance;
        }
        if (value.ValueKind == JsonValueKind.Object && value.TryGetProperty("$enum", out var enumType))
        {
            Type actual = FindType(enumType.GetString()!);
            if (!actual.IsEnum || (actual != type && type != typeof(object))) throw new ArgumentException("Incompatible enum type.");
            return Enum.ToObject(actual, value.GetProperty("value").GetInt64());
        }
        if (value.ValueKind == JsonValueKind.Object && value.TryGetProperty("$number", out var special))
        {
            double number = special.GetString() switch { "NaN" => double.NaN, "Infinity" => double.PositiveInfinity, "-Infinity" => double.NegativeInfinity, _ => throw new ArgumentException("Invalid floating-point number.") };
            if (type == typeof(double) || type == typeof(object)) return number;
            if (type == typeof(float)) return (float)number;
            throw new ArgumentException("Floating-point value requires a floating-point target.");
        }
        if (type.IsEnum)
        {
            score = 3;
            return value.ValueKind == JsonValueKind.String ? Enum.Parse(type, value.GetString()!) : Enum.ToObject(type, value.GetInt64());
        }
        if (value.ValueKind == JsonValueKind.Array)
        {
            Type? element = type.IsArray ? type.GetElementType() : type.IsGenericType && type.GetGenericArguments().Length == 1 ? type.GetGenericArguments()[0] : null;
            if (element is null) throw new ArgumentException($"Cannot convert a sequence to {type}.");
            Array array = Array.CreateInstance(element, value.GetArrayLength());
            int i = 0;
            foreach (JsonElement item in value.EnumerateArray()) array.SetValue(ConvertValue(item, element, out _), i++);
            if (!type.IsInstanceOfType(array)) throw new ArgumentException($"An array is not assignable to {type}; construct the target collection explicitly.");
            score = type.IsArray ? 0 : 1;
            return array;
        }
        if (type == typeof(object))
        {
            score = 20;
            return value.ValueKind switch
            {
                JsonValueKind.String => value.GetString(),
                JsonValueKind.True => true,
                JsonValueKind.False => false,
                JsonValueKind.Number => value.TryGetInt64(out long integer) ? (object)integer : value.GetDouble(),
                _ => throw new ArgumentException("Unsupported object value.")
            };
        }
        if (type == typeof(string) && value.ValueKind == JsonValueKind.String) return value.GetString();
        if (type == typeof(char) && value.ValueKind == JsonValueKind.String && value.GetString()!.Length == 1) { score = 1; return value.GetString()![0]; }
        if (type == typeof(bool) && value.ValueKind is JsonValueKind.True or JsonValueKind.False) return value.GetBoolean();
        if (value.ValueKind == JsonValueKind.Number && (type.IsPrimitive || type == typeof(decimal)) && type != typeof(bool) && type != typeof(char))
        {
            if (value.TryGetInt64(out long number))
            {
                score = type == typeof(int) && number >= int.MinValue && number <= int.MaxValue ? 0 : type == typeof(long) ? 1 : type == typeof(double) ? 3 : 2;
                return Convert.ChangeType(number, type, CultureInfo.InvariantCulture);
            }
            if (value.TryGetUInt64(out ulong unsigned))
            {
                score = type == typeof(ulong) ? 0 : 3;
                return Convert.ChangeType(unsigned, type, CultureInfo.InvariantCulture);
            }
            if (type != typeof(double) && type != typeof(float) && type != typeof(decimal)) throw new ArgumentException("A fractional number requires a floating-point target.");
            score = type == typeof(double) ? 0 : 1;
            return Convert.ChangeType(value.GetDouble(), type, CultureInfo.InvariantCulture);
        }
        throw new ArgumentException($"Cannot convert JSON {value.ValueKind} to {type}.");
    }

    private static JsonNode? Encode(object? value)
    {
        if (value is null) return null;
        Type type = value.GetType();
        if (type.IsEnum) return new JsonObject { ["$enum"] = type.FullName, ["value"] = Convert.ToInt64(value, CultureInfo.InvariantCulture), ["name"] = value.ToString() };
        switch (value)
        {
            case string text: return JsonValue.Create(text);
            case char c: return JsonValue.Create(c.ToString());
            case bool b: return JsonValue.Create(b);
            case byte n: return JsonValue.Create(n);
            case sbyte n: return JsonValue.Create(n);
            case short n: return JsonValue.Create(n);
            case ushort n: return JsonValue.Create(n);
            case int n: return JsonValue.Create(n);
            case uint n: return JsonValue.Create(n);
            case long n: return JsonValue.Create(n);
            case ulong n: return JsonValue.Create(n);
            case float n: return Number(n);
            case double n: return Number(n);
            case decimal n: return JsonValue.Create(n);
        }
        long handle = ++_nextHandle;
        Objects.Add(handle, value);
        return new JsonObject { ["$ref"] = handle, ["$type"] = type.FullName };
    }

    private static JsonNode Number(double value) => double.IsFinite(value) ? JsonValue.Create(value)! : new JsonObject { ["$number"] = value.ToString(CultureInfo.InvariantCulture) };

    private static JsonObject Describe(Type type)
    {
        static JsonObject Parameter(ParameterInfo p) => new() { ["name"] = p.Name, ["type"] = p.ParameterType.FullName ?? p.ParameterType.ToString(), ["optional"] = p.IsOptional, ["out"] = p.IsOut };
        static JsonObject Method(MethodBase m) => new() { ["name"] = m.Name, ["static"] = m.IsStatic, ["generic"] = m.ContainsGenericParameters,
            ["parameters"] = new JsonArray(m.GetParameters().Select(p => (JsonNode?)Parameter(p)).ToArray()),
            ["returns"] = m is MethodInfo mi ? mi.ReturnType.FullName ?? mi.ReturnType.ToString() : null };
        return new JsonObject
        {
            ["name"] = type.FullName, ["base"] = type.BaseType?.FullName, ["enum"] = type.IsEnum,
            ["value_type"] = type.IsValueType, ["abstract"] = type.IsAbstract, ["generic"] = type.ContainsGenericParameters,
            ["constructors"] = new JsonArray(type.GetConstructors().Select(c => (JsonNode?)Method(c)).ToArray()),
            ["properties"] = new JsonArray(type.GetProperties(Public).Select(p => (JsonNode?)new JsonObject { ["name"] = p.Name, ["type"] = p.PropertyType.FullName ?? p.PropertyType.ToString(),
                ["readable"] = p.GetMethod?.IsPublic == true, ["writable"] = p.SetMethod?.IsPublic == true, ["static"] = p.GetMethod?.IsStatic ?? p.SetMethod?.IsStatic ?? false,
                ["parameters"] = new JsonArray(p.GetIndexParameters().Select(x => (JsonNode?)Parameter(x)).ToArray()) }).ToArray()),
            ["fields"] = new JsonArray(type.GetFields(Public).Select(f => (JsonNode?)new JsonObject { ["name"] = f.Name, ["type"] = f.FieldType.FullName ?? f.FieldType.ToString(), ["static"] = f.IsStatic, ["writable"] = !f.IsInitOnly && !f.IsLiteral }).ToArray()),
            ["methods"] = new JsonArray(type.GetMethods(Public).Where(m => !m.IsSpecialName).Select(m => (JsonNode?)Method(m)).ToArray()),
            ["events"] = new JsonArray(type.GetEvents(Public).Select(e => (JsonNode?)JsonValue.Create(e.Name)).ToArray()),
            ["nested_types"] = new JsonArray(type.GetNestedTypes(BindingFlags.Public).Select(t => (JsonNode?)JsonValue.Create(t.FullName)).ToArray()),
        };
    }
}
