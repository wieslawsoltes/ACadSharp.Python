# ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair

`struct` · `ACadSharp` · CLR name: `ACadSharp.Objects.MultiLeaderObjectContextData+StartEndPointPair`

Start/end point pairs 3BD 11 Start Point 3BD 12 End point

Base type: `System.ValueType`. Inherited members are documented on their declaring type.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.MultiLeaderObjectContextData+StartEndPointPair')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair(CSMath.XYZ startPoint, CSMath.XYZ endPoint)
```

Initializes a new instance of the ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair struct with the specified start and end points.

- `startPoint`: The start point of the pair.
- `endPoint`: The end point of the pair.

### Clone

```text
ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair Clone()
```

Creates a copy of the current ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair instance.

**Returns:** A new ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair instance with the same start and end points.

### EndPoint

```text
CSMath.XYZ EndPoint { get; }
```

Break end point

### StartPoint

```text
CSMath.XYZ StartPoint { get; }
```

Break start point
