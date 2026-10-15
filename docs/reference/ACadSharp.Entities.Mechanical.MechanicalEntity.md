# ACadSharp.Entities.Mechanical.MechanicalEntity

`class` · `ACadSharp` · CLR name: `ACadSharp.Entities.Mechanical.MechanicalEntity`

Represents a mechanical entity.

Base type: `ACadSharp.Entities.Entity`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Entities.IEntity`, `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.Mechanical.MechanicalEntity')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### Position

```text
CSMath.XYZ Position { get; set; }
```

Gets or sets the position of the entity.
