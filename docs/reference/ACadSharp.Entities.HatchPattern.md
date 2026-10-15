# ACadSharp.Entities.HatchPattern

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.HatchPattern`

No upstream type summary is available.

Base type: `System.Object`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.HatchPattern')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Entities.HatchPattern(System.String name)
```

Default constructor of a hatch pattern.

- `name`: 

### Clone

```text
ACadSharp.Entities.HatchPattern Clone()
```

Clones the current pattern.

### LoadFrom

```text
static System.Collections.Generic.IEnumerable[ACadSharp.Entities.HatchPattern] LoadFrom(System.String path)
```

Load a collection of patterns from a .pat file.

- `path`: 

### SavePatterns

```text
static System.Void SavePatterns(System.String filename, ACadSharp.Entities.HatchPattern[] patterns)
```

Write a pattern or a collection of patterns into a .pat file.

- `filename`: 
- `patterns`: 

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### Update

```text
System.Void Update(CSMath.XY translation, System.Double rotation, System.Double scale)
```

Update the pattern geometry with a translation, rotation and scale.

- `translation`: 
- `rotation`: 
- `scale`: 

### Description

```text
System.String Description { get; set; }
```

Description for this pattern.

**Remarks:** The description is not saved in dxf or dwg files, its only used in the .pat files.

### Lines

```text
System.Collections.Generic.List[ACadSharp.Entities.HatchPattern.Line] Lines { get; set; }
```

Gets or sets the collection of ACadSharp.Entities.HatchPattern.Line objects.

**Remarks:** This property allows adding, removing, or modifying the lines in the collection. Changes to this collection directly affect the associated context.

### Name

```text
System.String Name { get; set; }
```

Name for this pattern.

### Solid

```text
static ACadSharp.Entities.HatchPattern Solid { get; }
```
