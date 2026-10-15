# ACadSharp.DxfMap

`class` · `ACadSharp` · CLR name: `ACadSharp.DxfMap`

No upstream type summary is available.

Base type: `ACadSharp.DxfMapBase`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.DxfMap')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.DxfMap()
```

### ClearCache

```text
static System.Void ClearCache()
```

Clears the map cache.

### Create

```text
static ACadSharp.DxfMap Create[T]()
```

Creates a dxf map for an ACadSharp.Entities.Entity or a ACadSharp.Tables.TableEntry

**Remarks:** This method does not work with the entities ACadSharp.Entities.AttributeEntity and ACadSharp.Entities.AttributeDefinition

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### SubClasses

```text
System.Collections.Generic.Dictionary[System.String, ACadSharp.DxfClassMap] SubClasses { get; }
```
