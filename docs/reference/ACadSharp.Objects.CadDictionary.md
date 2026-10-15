# ACadSharp.Objects.CadDictionary

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.CadDictionary`

Represents a ACadSharp.Objects.CadDictionary object.

Object name F:ACadSharp.DxfFileToken.ObjectDictionary Dxf class name F:ACadSharp.DxfSubclassMarker.Dictionary

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`, `ACadSharp.IObservableCadCollection[ACadSharp.Objects.NonGraphicalObject]`, `System.Collections.Generic.IEnumerable[ACadSharp.Objects.NonGraphicalObject]`, `System.Collections.IEnumerable`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.CadDictionary')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.CadDictionary()
```

Default constructor.

### .ctor

```text
ACadSharp.Objects.CadDictionary(System.String name)
```

Constructor for a named dictionary.

- `name`: Dictionary name.

### OnAdd

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnAdd
```

### OnRemove

```text
event System.EventHandler[ACadSharp.CollectionChangedEventArgs] OnRemove
```

### AcadColor

```text
static System.String AcadColor = ACAD_COLOR
```

ACAD_COLOR dictionary entry.

### AcadFieldList

```text
static System.String AcadFieldList = ACAD_FIELDLIST
```

ACAD_FIELDLIST dictionary entry.

### AcadGroup

```text
static System.String AcadGroup = ACAD_GROUP
```

ACAD_GROUP dictionary entry.

### AcadImageDict

```text
static System.String AcadImageDict = ACAD_IMAGE_DICT
```

ACAD_IMAGE_DICT dictionary entry.

### AcadLayout

```text
static System.String AcadLayout = ACAD_LAYOUT
```

ACAD_LAYOUT dictionary entry.

### AcadMLeaderStyle

```text
static System.String AcadMLeaderStyle = ACAD_MLEADERSTYLE
```

ACAD_MLEADERSTYLE dictionary entry.

### AcadMLineStyle

```text
static System.String AcadMLineStyle = ACAD_MLINESTYLE
```

ACAD_MLINESTYLE dictionary entry.

### AcadMaterial

```text
static System.String AcadMaterial = ACAD_MATERIAL
```

ACAD_MATERIAL dictionary entry.

### AcadPdfDefinitions

```text
static System.String AcadPdfDefinitions = ACAD_PDFDEFINITIONS
```

ACAD_PDFDEFINITIONS dictionary entry.

### AcadPlotSettings

```text
static System.String AcadPlotSettings = ACAD_PLOTSETTINGS
```

ACAD_PLOTSETTINGS dictionary entry.

### AcadPlotStyleName

```text
static System.String AcadPlotStyleName = ACAD_PLOTSTYLENAME
```

ACAD_PLOTSTYLENAME dictionary entry.

### AcadScaleList

```text
static System.String AcadScaleList = ACAD_SCALELIST
```

scales dictionary

### AcadSortEnts

```text
static System.String AcadSortEnts = ACAD_SORTENTS
```

ACAD_SORTENTS dictionary entry.

### AcadTableStyle

```text
static System.String AcadTableStyle = ACAD_TABLESTYLE
```

ACAD_TABLESTYLE dictionary entry.

### AcadVisualStyle

```text
static System.String AcadVisualStyle = ACAD_VISUALSTYLE
```

ACAD_VISUALSTYLE dictionary entry.

### GeographicData

```text
static System.String GeographicData = ACAD_GEOGRAPHICDATA
```

ACAD_GEOGRAPHICDATA dictionary entry.

### Root

```text
static System.String Root = ROOT
```

ROOT dictionary, only used in the top level dictionary.

### VariableDictionary

```text
static System.String VariableDictionary = AcDbVariableDictionary
```

AcDbVariableDictionary dictionary entry.

### Add

```text
System.Void Add(ACadSharp.Objects.NonGraphicalObject value)
```

Add a ACadSharp.Objects.NonGraphicalObject to the collection, this method triggers E:ACadSharp.Objects.CadDictionary.OnAdd

- `value`: the name of the NonGraphicalObject will be used as a key for the dictionary

- Raises `System.ArgumentException`: 

### Add

```text
System.Void Add(System.String key, ACadSharp.Objects.NonGraphicalObject value)
```

Add a ACadSharp.Objects.NonGraphicalObject to the collection, this method triggers E:ACadSharp.Objects.CadDictionary.OnAdd

- `key`: key for the entry in the dictionary
- `value`: 

### Clear

```text
System.Void Clear()
```

Removes all keys and values from the ACadSharp.Objects.CadDictionary.

### Clone

```text
ACadSharp.CadObject Clone()
```

Documentation inherited from: `base member`.

### ContainsKey

```text
System.Boolean ContainsKey(System.String key)
```

Determines whether the ACadSharp.Objects.CadDictionary contains the specified key.

- `key`: The key to locate in the ACadSharp.Objects.CadDictionary

### CreateDefaultEntries

```text
static System.Void CreateDefaultEntries(ACadSharp.Objects.CadDictionary root)
```

Create the default entries for the root dictionary.

### CreateRoot

```text
static ACadSharp.Objects.CadDictionary CreateRoot()
```

Creates the root dictionary with the default entries.

### GetEntry

```text
T GetEntry[T](System.String name)
```

Gets the value associated with the specific key

**Returns:** The value with Type T or null if not found or different type

- `name`: 

### GetEnumerator

```text
System.Collections.Generic.IEnumerator[ACadSharp.Objects.NonGraphicalObject] GetEnumerator()
```

Documentation inherited from: `base member`.

### Remove

```text
System.Boolean Remove(System.String key)
```

Removes a ACadSharp.Objects.NonGraphicalObject from the collection, this method triggers E:ACadSharp.Objects.CadDictionary.OnRemove

**Returns:** true if the element is successfully removed; otherwise, false.

- `key`: 

### Remove

```text
System.Boolean Remove(System.String key, out ACadSharp.Objects.NonGraphicalObject item)
```

Removes a ACadSharp.Objects.NonGraphicalObject from the collection, this method triggers E:ACadSharp.Objects.CadDictionary.OnRemove

**Returns:** true if the element is successfully removed; otherwise, false.

- `key`: 
- `item`: 

### TryAdd

```text
System.Boolean TryAdd(ACadSharp.Objects.NonGraphicalObject value)
```

Tries to add the ACadSharp.Objects.NonGraphicalObject entry using the name as key.

**Returns:** true if the element is successfully added; otherwise, false.

- `value`: 

### TryGetEntry

```text
System.Boolean TryGetEntry[T](System.String name, out T value)
```

Gets the value associated with the specific key

**Returns:** true if the value is found or false if not found or different type

- `name`: 
- `value`: 

### ClonningFlags

```text
ACadSharp.Objects.DictionaryCloningFlags ClonningFlags { get; set; }
```

Duplicate record cloning flag (determines how to merge duplicate entries)

### EntryHandles

```text
System.UInt64[] EntryHandles { get; }
```

Soft-owner ID/handle to entry object

### EntryNames

```text
System.String[] EntryNames { get; }
```

Entry names

### HardOwnerFlag

```text
System.Boolean HardOwnerFlag { get; set; }
```

Indicates that elements of the dictionary are to be treated as hard-owned.

### Item

```text
ACadSharp.CadObject Item[System.String key] { get; }
```

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

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.
