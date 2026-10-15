# ACadSharp.Tables.Layer

`class` · `ACadSharp` · CLR name: `ACadSharp.Tables.Layer`

Represents a ACadSharp.Tables.Layer entry

Object name F:ACadSharp.DxfFileToken.TableLayer Dxf class name F:ACadSharp.DxfSubclassMarker.Layer

Base type: `ACadSharp.Tables.TableEntry`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Tables.Layer')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Tables.Layer(System.String name)
```

### DefaultName

```text
static System.String DefaultName = 0
```

Default layer 0, it will always exist in a file

### DefpointsName

```text
static System.String DefpointsName = defpoints
```

DefPoints layer name.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### Color

```text
ACadSharp.Color Color { get; set; }
```

Color

**Remarks:** if the index is negative, layer is off

### Default

```text
static ACadSharp.Tables.Layer Default { get; }
```

Default layer in all cad formats, it will always exist in a file

### Defpoints

```text
static ACadSharp.Tables.Layer Defpoints { get; }
```

Defpoints layer, this layer usually stores definition points that will not be plot.

### Flags

```text
ACadSharp.Tables.LayerFlags Flags { get; set; }
```

Layer state flags.

### IsOn

```text
System.Boolean IsOn { get; set; }
```

Indicates if the Layer is visible in the model

### LineType

```text
ACadSharp.Tables.LineType LineType { get; set; }
```

The line type of an object. The default line type is the line type of the layer (ByLayer).

### LineWeight

```text
ACadSharp.LineWeightType LineWeight { get; set; }
```

Specifies the line weight of an individual object or the default line weight for the drawing.

### Material

```text
ACadSharp.Objects.Material Material { get; set; }
```

Hard-pointer ID/handle to Material object

### ObjectName

```text
System.String ObjectName { get; }
```

Documentation inherited from: `base member`.

### ObjectType

```text
ACadSharp.ObjectType ObjectType { get; }
```

Documentation inherited from: `base member`.

### PlotFlag

```text
System.Boolean PlotFlag { get; set; }
```

Specifies if the layer is plottable.

### PlotStyleName

```text
System.UInt64 PlotStyleName { get; }
```

PlotStyleName object

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
