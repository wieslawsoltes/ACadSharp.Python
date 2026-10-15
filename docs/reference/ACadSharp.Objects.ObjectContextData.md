# ACadSharp.Objects.ObjectContextData

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.ObjectContextData`

No upstream type summary is available.

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.ObjectContextData')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Default

```text
System.Boolean Default { get; set; }
```

Gets or sets a value indicating whether this instance uses the default setting.

### HasFileToExtensionDictionary

```text
System.Boolean HasFileToExtensionDictionary { get; set; }
```

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Version

```text
System.Int16 Version { get; set; }
```

Gets or sets the version number of the entity definition.
