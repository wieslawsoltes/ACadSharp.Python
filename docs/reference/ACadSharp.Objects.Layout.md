# ACadSharp.Objects.Layout

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Layout`

Represents a ACadSharp.Objects.Layout object.

Object name F:ACadSharp.DxfFileToken.ObjectLayout. Dxf class name F:ACadSharp.DxfSubclassMarker.Layout.

Base type: `ACadSharp.Objects.PlotSettings`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Layout')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Layout(System.String name)
```

Initializes a new instance of the Layout class using the specified name for both the layout's name and display name.

- `name`: The name to assign to the layout. This value is used for both the internal name and the display name.

### .ctor

```text
ACadSharp.Objects.Layout(System.String name, System.String blockName)
```

Initializes a new instance of the Layout class with the specified layout name and associated block record name.

- `name`: The name to assign to the layout. Cannot be null or empty.
- `blockName`: The name of the block record associated with the layout. Cannot be null or empty.

### ModelLayoutName

```text
static System.String ModelLayoutName = Model
```

Represents the name of the model layout used in view rendering.

### PaperLayoutName

```text
static System.String PaperLayoutName = Layout1
```

Specifies the default name for the paper layout used in document generation.

### AddViewport

```text
System.Void AddViewport(ACadSharp.Entities.Viewport viewport)
```

Adds the specified viewport to the collection of entities associated with this block.

- `viewport`: The viewport to add to the associated block's entities. Cannot be null.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### UpdatePaperViewport

```text
System.Void UpdatePaperViewport()
```

Ensures that the paper ACadSharp.Entities.Viewport exists and updates its dimensions to match the current paper size.

**Remarks:** If no ACadSharp.Entities.Viewport is associated with the paper space, a new ACadSharp.Entities.Viewport is created and added. This method has no effect if the object is not a paper space.

### AssociatedBlock

```text
ACadSharp.Tables.BlockRecord AssociatedBlock { get; }
```

The associated paper space block table record.

### BaseUCS

```text
ACadSharp.Tables.UCS BaseUCS { get; set; }
```

UCSTableRecord of base UCS if UCS is orthographic (ACadSharp.Objects.Layout.UcsOrthographicType is non-zero).

**Remarks:** If not present and ACadSharp.Objects.Layout.UcsOrthographicType is non-zero, then base UCS is taken to be WORLD.

### Elevation

```text
System.Double Elevation { get; set; }
```

Layout elevation.

### InsertionBasePoint

```text
CSMath.XYZ InsertionBasePoint { get; set; }
```

Insertion base point for this layout(defined by INSBASE while this layout is current).

### IsPaperSpace

```text
System.Boolean IsPaperSpace { get; }
```

If true, the layout is a paper space.

### LastActiveViewport

```text
ACadSharp.Entities.Viewport LastActiveViewport { get; }
```

Viewport that was last active in this layout when the layout was current.

### LayoutFlags

```text
ACadSharp.Objects.LayoutFlags LayoutFlags { get; set; }
```

Layout flags.

### MaxExtents

```text
CSMath.XYZ MaxExtents { get; set; }
```

Maximum extents for this layout(defined by EXTMAX while this layout is current).

### MaxLimits

```text
CSMath.XY MaxLimits { get; set; }
```

Maximum limits for this layout(defined by LIMMAX while this layout is current).

### MinExtents

```text
CSMath.XYZ MinExtents { get; set; }
```

Minimum extents for this layout(defined by EXTMIN while this layout is current).

### MinLimits

```text
CSMath.XY MinLimits { get; set; }
```

Minimum limits for this layout (defined by LIMMIN while this layout is current).

### Name

```text
System.String Name { get; set; }
```

Layout name.

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

### Origin

```text
CSMath.XYZ Origin { get; set; }
```

UCS origin.

### PaperViewport

```text
ACadSharp.Entities.Viewport PaperViewport { get; }
```

Gets the paper viewport associated with this layout. If there are multiple viewports, this property returns the first one found. If no viewports are associated with the layout, this property returns null.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### TabOrder

```text
System.Int32 TabOrder { get; set; }
```

Tab order. This number is an ordinal indicating this layout's ordering in the tab control that is attached to the drawing window. Note that the “Model” tab always appears as the first tab regardless of its tab order.

### UCS

```text
ACadSharp.Tables.UCS UCS { get; set; }
```

UCS Table Record if UCS is a named UCS.

**Remarks:** If not present, then UCS is unnamed.

### UcsOrthographicType

```text
ACadSharp.OrthographicType UcsOrthographicType { get; set; }
```

Orthographic type of UCS.

### Viewports

```text
System.Collections.Generic.IEnumerable[ACadSharp.Entities.Viewport] Viewports { get; }
```

Gets the collection of viewports associated with this instance.

### XAxis

```text
CSMath.XYZ XAxis { get; set; }
```

UCS X-axis.

### YAxis

```text
CSMath.XYZ YAxis { get; set; }
```

UCS Y-axis.
