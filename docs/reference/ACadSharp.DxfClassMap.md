# ACadSharp.DxfClassMap

`class` · `ACadSharp` · CLR name: `ACadSharp.DxfClassMap`

Represents the mapping information for a DXF class, including metadata and property mappings used for serialization and deserialization of CAD objects.

Instances of this class are typically created and managed via the static Create methods, which provide caching to improve performance when mapping types multiple times. Use the ClearCache method to clear all cached mappings if the underlying type information changes or to force remapping.

Base type: `ACadSharp.DxfMapBase`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.DxfClassMap')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.DxfClassMap()
```

### .ctor

```text
ACadSharp.DxfClassMap(ACadSharp.DxfClassMap map)
```

### .ctor

```text
ACadSharp.DxfClassMap(System.String name)
```

### ClearCache

```text
System.Void ClearCache()
```

Clears the map cache.

### Create

```text
static ACadSharp.DxfClassMap Create[T]()
```

Creates a DXF map of the passed type.

**Remarks:** Will return a cached instance if it exists. if not, it will be created on call. Use the ACadSharp.DxfClassMap.ClearCache method to clear the cache and force a new mapping to be created.

**Returns:** Mapped class

### Create

```text
static ACadSharp.DxfClassMap Create[T](T obj)
```

Creates a new instance of the DxfClassMap for the specified CAD object type and instance.

**Returns:** A DxfClassMap instance representing the mapping for the specified CAD object type and instance.

- `obj`: The CAD object instance to associate with the created class map.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.
