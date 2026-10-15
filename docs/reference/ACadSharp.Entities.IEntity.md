# ACadSharp.Entities.IEntity

`interface` · `ACadSharp` · CLR name: `ACadSharp.Entities.IEntity`

Defines the contract for a CAD entity, providing common properties and methods for graphical objects within a CAD document.

The ACadSharp.Entities.IEntity interface exposes standard attributes such as color, layer, linetype, line weight, material, and transparency, as well as methods to resolve effective property values and to match properties with another entity. Implementations are expected to represent geometric or drawable objects in a CAD environment. This interface extends IHandledCadObject and IGeometricEntity, ensuring that all entities have unique handles and geometric characteristics. Thread safety and mutability depend on the specific implementation.

Interfaces: `ACadSharp.Entities.IGeometricEntity`, `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Entities.IEntity')
```

This type cannot be instantiated directly.

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### GetActiveColor

```text
ACadSharp.Color GetActiveColor()
```

Get the active color for the entity, process the colors like ACadSharp.Color.ByBlock and ACadSharp.Color.ByLayer.

### GetActiveLineType

```text
ACadSharp.Tables.LineType GetActiveLineType()
```

Get the active line type for the entity, process the line types like ACadSharp.Tables.LineType.ByBlock and ACadSharp.Tables.LineType.ByLayer.

### GetActiveLineWeightType

```text
ACadSharp.LineWeightType GetActiveLineWeightType()
```

Get the active line weight for the entity, process the line weights like F:ACadSharp.LineWeightType.ByBlock and F:ACadSharp.LineWeightType.ByLayer.

### MatchProperties

```text
System.Void MatchProperties(ACadSharp.Entities.IEntity entity)
```

Copies matching property values from the specified entity to the current object.

**Remarks:** Only properties with matching names and compatible types are considered for copying. Properties that do not exist or are not compatible in either object are ignored.

- `entity`: The source entity whose property values will be matched and copied. Cannot be null.

### Color

```text
ACadSharp.Color Color { get; set; }
```

The True Color object of the object.

**Remarks:** This property is used to change an object's color. Colors are identified by an AcCmColor object. This object can hold an RGB value, an ACI number (an integer from 1 to 255), or a named color. Using an RGB value, you can choose from millions of colors.

### Document

```text
ACadSharp.CadDocument Document { get; }
```

Document where this element belongs.

### IsInvisible

```text
System.Boolean IsInvisible { get; set; }
```

Specifies the visibility of an object or the application.

**Remarks:** If you specify an object to be invisible, it will be invisible regardless of the application visible setting. Other factors can also cause an object to be invisible; for example, an object will not be displayed if its layer is off or frozen.

### Layer

```text
ACadSharp.Tables.Layer Layer { get; set; }
```

Specifies the layer for an object.

### LineType

```text
ACadSharp.Tables.LineType LineType { get; set; }
```

Linetype name (present if not BYLAYER). The special name BYBLOCK indicates a floating linetype (optional)

### LineTypeScale

```text
System.Double LineTypeScale { get; set; }
```

Linetype scale for this entity.

**Remarks:** This must be a positive, non-negative number.

### LineWeight

```text
ACadSharp.LineWeightType LineWeight { get; set; }
```

Specifies the line weight of an individual object or the default line weight for the drawing.

### Material

```text
ACadSharp.Objects.Material Material { get; set; }
```

Material object (present if not BYLAYER)

### Transparency

```text
ACadSharp.Transparency Transparency { get; set; }
```

Transparency value.
