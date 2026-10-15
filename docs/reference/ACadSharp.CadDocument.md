# ACadSharp.CadDocument

`class` · `ACadSharp` · CLR name: `ACadSharp.CadDocument`

Represents a CAD drawing document, providing access to all collections, tables, and configuration objects within the drawing. Supports management of entities, layers, styles, dictionaries, and other core CAD structures.

The CadDocument class serves as the root container for all objects and settings in a CAD drawing. It provides methods to retrieve, configure, and manage drawing content, including entities, tables, and dictionaries. Many collections are initialized automatically, but some may be null if the corresponding dictionary entry does not exist in the root dictionary.

Base type: `System.Object`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.IHandledCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.CadDocument')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.CadDocument()
```

Creates a document with the default objects

**Remarks:** Default version F:ACadSharp.ACadVersion.AC1032

### .ctor

```text
ACadSharp.CadDocument(ACadSharp.ACadVersion version)
```

Creates a document with the default objects and a specific version

- `version`: Version of the document

### CreateDefaults

```text
System.Void CreateDefaults()
```

Create the default entries and objects for the ACadSharp.CadDocument.

### GetCadObject

```text
ACadSharp.CadObject GetCadObject(System.UInt64 handle)
```

Gets an object in the document by it's handle

**Returns:** the cadObject or null if doesn't exists in the document

- `handle`: 

### GetCadObject

```text
T GetCadObject[T](System.UInt64 handle)
```

Gets an object in the document by it's handle

**Returns:** the cadObject or null if doesn't exists in the document

- `handle`: 

### GetCurrent

```text
T GetCurrent[T]()
```

Retrieves the current object of the specified type from the document's configuration.

**Returns:** The current object of the specified type, or throws an exception if the type is not supported.

- Raises `System.NotSupportedException`: Thrown if the specified type T is not a configurable type in the document.

### GetInstanceCount

```text
System.Int32 GetInstanceCount(System.String dxfName)
```

Gets the number of instances of a specific DXF object type in the document.

**Returns:** The number of instances of the specified DXF object type.

- `dxfName`: The name of the DXF object type.

### RestoreHandles

```text
System.Void RestoreHandles()
```

Reassign all the handles in the document to avoid the variable ACadSharp.Header.CadHeader.HandleSeed to grow past its limit.

### SetCurrent

```text
System.Void SetCurrent[T](T obj)
```

This method sets the current configurable object of the specified type in the document's configuration.

- `obj`: 

- Raises `System.NotSupportedException`: 

### ToString

```text
System.String ToString()
```

Documentation inherited from: `base member`.

### TryGetCadObject

```text
System.Boolean TryGetCadObject[T](System.UInt64 handle, out T cadObject)
```

Gets an object in the document by it's handle

- `handle`: 
- `cadObject`: 

### UpdateCollections

```text
System.Void UpdateCollections(System.Boolean createDictionaries, System.Boolean createDefaults)
```

Updates the collections in the document and link them to it's dictionary.

- `createDictionaries`: 

### UpdateDxfClasses

```text
System.Void UpdateDxfClasses(System.Boolean reset)
```

Updates the ACadSharp.Classes.DxfClass in the document and their instance count.

- `reset`: Resets the list and clears any unnecessary classes.

### UpdateImageReactors

```text
System.Void UpdateImageReactors()
```

Updates the image definition reactors for all raster images in the current collection.

**Remarks:** This method removes existing ACadSharp.Objects.ImageDefinitionReactor instances from the document and creates new reactors for each ACadSharp.Entities.RasterImage. The new reactors are associated with their corresponding image definitions and added to the document.

### AppIds

```text
ACadSharp.Tables.Collections.AppIdsTable AppIds { get; }
```

The collection of all registered applications in the drawing.

### BlockRecords

```text
ACadSharp.Tables.Collections.BlockRecordsTable BlockRecords { get; }
```

The collection of all block records in the drawing.

### Classes

```text
ACadSharp.Classes.DxfClassCollection Classes { get; }
```

Dxf classes defined in this document.

### Colors

```text
ACadSharp.Objects.Collections.ColorCollection Colors { get; }
```

The collection of all book colors in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.AcadColor doesn't exist in the root dictionary.

### DataStorage

```text
ACadSharp.Prototype1b.DataStorage DataStorage { get; set; }
```

The data stored in the Prototype1b header section. This primarily contains ACIS and thumbnail data

### DictionaryVariables

```text
ACadSharp.Objects.Collections.DictionaryVariableCollection DictionaryVariables { get; }
```

The collection of the system variables in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.VariableDictionary doesn't exist in the root dictionary.

### DimensionStyles

```text
ACadSharp.Tables.Collections.DimensionStylesTable DimensionStyles { get; }
```

The collection of all dimension styles in the drawing.

### Entities

```text
ACadSharp.CadObjectCollection[ACadSharp.Entities.Entity] Entities { get; }
```

Collection with all the entities in the drawing

### Groups

```text
ACadSharp.Objects.Collections.GroupCollection Groups { get; }
```

The collection of all groups in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.AcadGroup doesn't exist in the root dictionary.

### Handle

```text
System.UInt64 Handle { get; }
```

The document handle is always 0, this field makes sure that no object overrides this value.

### Header

```text
ACadSharp.Header.CadHeader Header { get; }
```

Contains all the header variables for this document.

### ImageDefinitions

```text
ACadSharp.Objects.Collections.ImageDefinitionCollection ImageDefinitions { get; }
```

The collection of all images in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.AcadImageDict doesn't exist in the root dictionary.

### Layers

```text
ACadSharp.Tables.Collections.LayersTable Layers { get; }
```

The collection of all layers in the drawing.

### Layouts

```text
ACadSharp.Objects.Collections.LayoutCollection Layouts { get; }
```

The collection of all layouts in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.AcadLayout doesn't exist in the root dictionary.

### LineTypes

```text
ACadSharp.Tables.Collections.LineTypesTable LineTypes { get; }
```

The collection of all line types in the drawing.

### MLeaderStyles

```text
ACadSharp.Objects.Collections.MLeaderStyleCollection MLeaderStyles { get; }
```

The collection of all Multi leader styles in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.AcadMLeaderStyle doesn't exist in the root dictionary.

### MLineStyles

```text
ACadSharp.Objects.Collections.MLineStyleCollection MLineStyles { get; }
```

The collection of all Multi line styles in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.AcadMLineStyle doesn't exist in the root dictionary.

### Materials

```text
ACadSharp.Objects.Collections.MaterialCollection Materials { get; }
```

The collection of all materials in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.AcadMaterial doesn't exist in the root dictionary.

### ModelSpace

```text
ACadSharp.Tables.BlockRecord ModelSpace { get; }
```

Model space block record containing the drawing

### PaperSpace

```text
ACadSharp.Tables.BlockRecord PaperSpace { get; }
```

Default paper space of the model

### PdfDefinitions

```text
ACadSharp.Objects.Collections.PdfDefinitionCollection PdfDefinitions { get; }
```

The collection of all images in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.AcadImageDict doesn't exist in the root dictionary.

### RootDictionary

```text
ACadSharp.Objects.CadDictionary RootDictionary { get; }
```

Root dictionary of the document.

### Scales

```text
ACadSharp.Objects.Collections.ScaleCollection Scales { get; }
```

The collection of all scales in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.AcadScaleList doesn't exist in the root dictionary.

### SummaryInfo

```text
ACadSharp.CadSummaryInfo SummaryInfo { get; set; }
```

Accesses drawing properties such as the Title, Subject, Author, and Keywords properties.

### TableStyles

```text
ACadSharp.Objects.Collections.TableStyleCollection TableStyles { get; }
```

The collection of all table styles in the drawing.

**Remarks:** The collection is null if the F:ACadSharp.Objects.CadDictionary.AcadTableStyle doesn't exist in the root dictionary.

### TextStyles

```text
ACadSharp.Tables.Collections.TextStylesTable TextStyles { get; }
```

The collection of all text styles in the drawing.

### UCSs

```text
ACadSharp.Tables.Collections.UCSTable UCSs { get; }
```

The collection of all user coordinate systems (UCSs) in the drawing.

### VPorts

```text
ACadSharp.Tables.Collections.VPortsTable VPorts { get; }
```

The collection of all vports in the drawing.

### Views

```text
ACadSharp.Tables.Collections.ViewsTable Views { get; }
```

The collection of all views in the drawing.
