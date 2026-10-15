# ACadSharp.Objects.Evaluations.BlockActionBasePt

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Evaluations.BlockActionBasePt`

No upstream type summary is available.

Base type: `ACadSharp.Objects.Evaluations.BlockAction`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Evaluations.BlockActionBasePt')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### BasePoint

```text
CSMath.XYZ BasePoint { get; set; }
```

Gets or sets the base point of the action.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### UpdateBaseXConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection UpdateBaseXConnection { get; set; }
```

### UpdateBaseYConnection

```text
ACadSharp.Objects.Evaluations.EvalConnection UpdateBaseYConnection { get; set; }
```

### Value1012

```text
CSMath.XYZ Value1012 { get; set; }
```

### Value280

```text
System.Boolean Value280 { get; set; }
```
