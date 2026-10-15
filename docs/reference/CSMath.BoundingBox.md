# CSMath.BoundingBox

`struct` · `ACadSharp` · CLR name: `CSMath.BoundingBox`

Bounding box representation aligned to XYZ axis.

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('CSMath.BoundingBox')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
CSMath.BoundingBox(CSMath.XYZ min, CSMath.XYZ max)
```

Initializes a new instance of the BoundingBox class that represents the axis-aligned box defined by the specified minimum and maximum coordinates.

**Remarks:** If the specified minimum and maximum points are equal, the bounding box represents a single point. The constructor automatically assigns the smaller of each coordinate to Min and the larger to Max, regardless of the order of the input parameters.

- `min`: The point representing the minimum X, Y, and Z coordinates of the bounding box.
- `max`: The point representing the maximum X, Y, and Z coordinates of the bounding box.

### .ctor

```text
CSMath.BoundingBox(CSMath.XYZ point)
```

Initializes a new instance of the BoundingBox class that represents a single point.

- `point`: The point to use as both the minimum and maximum bounds of the bounding box.

### .ctor

```text
CSMath.BoundingBox(System.Double minX, System.Double minY, System.Double minZ, System.Double maxX, System.Double maxY, System.Double maxZ)
```

Initializes a new instance of the BoundingBox structure using the specified minimum and maximum X, Y, and Z coordinates.

- `minX`: The minimum X coordinate of the bounding box.
- `minY`: The minimum Y coordinate of the bounding box.
- `minZ`: The minimum Z coordinate of the bounding box.
- `maxX`: The maximum X coordinate of the bounding box.
- `maxY`: The maximum Y coordinate of the bounding box.
- `maxZ`: The maximum Z coordinate of the bounding box.

### Infinite

```text
static CSMath.BoundingBox Infinite
```

Instance of an infinite bounding box.

### Null

```text
static CSMath.BoundingBox Null
```

Instance of a null bounding box.

### FromPoints

```text
static CSMath.BoundingBox FromPoints(System.Collections.Generic.IEnumerable[CSMath.XYZ] points)
```

Create a bounding box from a collection of points.

- `points`: 

### IsIn

```text
System.Boolean IsIn(CSMath.BoundingBox box)
```

Checks if the given box is in the bounds of this box.

- `box`: 

### IsIn

```text
System.Boolean IsIn(CSMath.BoundingBox box, out System.Boolean partialIn)
```

Checks if the given box is in the bounds of this box.

- `box`: 
- `partialIn`: Flag to notify that on part of the box is inside but not completely.

### IsIn

```text
System.Boolean IsIn(CSMath.XYZ point)
```

Checks if the point is in the bounds of the box.

- `point`: 

### Merge

```text
CSMath.BoundingBox Merge(CSMath.BoundingBox box)
```

Merge 2 boxes into the common one.

**Returns:** The merged box.

- `box`: 

### Merge

```text
static CSMath.BoundingBox Merge(System.Collections.Generic.IEnumerable[CSMath.BoundingBox] boxes)
```

Merge Multiple boxes into the common one.

**Returns:** The merged box.

- `boxes`: 

### Move

```text
CSMath.BoundingBox Move(CSMath.XYZ xyz)
```

Returns a new bounding box translated by the specified vector.

**Returns:** A new BoundingBox instance that is the result of translating the current bounding box by the specified vector.

- `xyz`: The vector by which to translate the bounding box. Each component is added to the corresponding coordinates of the bounding box's minimum and maximum points.

### Center

```text
CSMath.XYZ Center { get; }
```

Center of the box.

### Extent

```text
CSMath.BoundingBoxExtent Extent { get; }
```

Gets the extent of the bounding box, indicating whether it is finite, infinite, or null.

### LengthX

```text
System.Double LengthX { get; }
```

Gets the length of the bounding box along the X-axis.

### LengthY

```text
System.Double LengthY { get; }
```

Gets the length of the bounding box along the Y-axis.

### LengthZ

```text
System.Double LengthZ { get; }
```

Gets the length of the bounding box along the Z-axis.

### Max

```text
CSMath.XYZ Max { get; set; }
```

Get the max corner of the bounding box.

### Min

```text
CSMath.XYZ Min { get; set; }
```

Get the min corner of the bounding box.
