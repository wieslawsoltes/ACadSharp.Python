# ACadSharp.Objects.Material

`class` · `ACadSharp` · CLR name: `ACadSharp.Objects.Material`

Represents a ACadSharp.Objects.Material object

Object name F:ACadSharp.DxfFileToken.ObjectMaterial Dxf class name F:ACadSharp.DxfSubclassMarker.Material

Base type: `ACadSharp.Objects.NonGraphicalObject`. Inherited members are documented on their declaring type.

Interfaces: `ACadSharp.Classes.IDxfClassDefined`, `ACadSharp.IHandledCadObject`, `ACadSharp.INamedCadObject`.

```python
import acadsharp
Type = acadsharp.get_type('ACadSharp.Objects.Material')
```

## Declared public members

Signatures retain CLR types and names. Python.NET resolves overloads and converts compatible Python values at call time. Property setters are shown only when public. Operators retain their CLR names; Python.NET also maps supported operators to Python syntax.

### .ctor

```text
ACadSharp.Objects.Material(System.String name)
```

Initializes a new instance of the ACadSharp.Objects.Material class with the specified name.

- `name`: The name of the material. This value cannot be null or empty.

### ByBlockName

```text
static System.String ByBlockName = ByBlock
```

### ByLayerName

```text
static System.String ByLayerName = ByLayer
```

### GlobalName

```text
static System.String GlobalName = Global
```

### GetDxfClass

```text
ACadSharp.Classes.DxfClass GetDxfClass()
```

Documentation inherited from: `base member`.

### AmbientColor

```text
ACadSharp.Color AmbientColor { get; set; }
```

Ambient color value.

### AmbientColorFactor

```text
System.Double AmbientColorFactor { get; set; }
```

Ambient color factor.

**Value:** valid range is 0.0 to 1.0)

### AmbientColorMethod

```text
ACadSharp.Objects.ColorMethod AmbientColorMethod { get; set; }
```

Ambient color method.

### BumpAutoTransform

```text
ACadSharp.Objects.AutoTransformMethodFlags BumpAutoTransform { get; set; }
```

Auto transform method of bump map mapper.

### BumpMapBlendFactor

```text
System.Double BumpMapBlendFactor { get; set; }
```

Bump map blend factor.

**Value:** default = 1.0

### BumpMapFileName

```text
System.String BumpMapFileName { get; set; }
```

Bump map file name.

**Remarks:** null file name specifies no map.

### BumpMapSource

```text
ACadSharp.Objects.MapSource BumpMapSource { get; set; }
```

Bump map source.

### BumpMatrix

```text
CSMath.Matrix4 BumpMatrix { get; set; }
```

Transform matrix of bump map mapper.

### BumpProjectionMethod

```text
ACadSharp.Objects.ProjectionMethod BumpProjectionMethod { get; set; }
```

Bump method of specular map mapper.

### BumpTilingMethod

```text
ACadSharp.Objects.TilingMethod BumpTilingMethod { get; set; }
```

Tiling method of bump map mapper.

### ChannelFlags

```text
ACadSharp.Objects.MaterialChannelFlags ChannelFlags { get; set; }
```

Channel Flags.

### Description

```text
System.String Description { get; set; }
```

Material description.

### DiffuseAutoTransform

```text
ACadSharp.Objects.AutoTransformMethodFlags DiffuseAutoTransform { get; set; }
```

Auto transform method of diffuse map mapper.

### DiffuseColor

```text
ACadSharp.Color DiffuseColor { get; set; }
```

Diffuse color value.

### DiffuseColorFactor

```text
System.Double DiffuseColorFactor { get; set; }
```

Diffuse color factor.

**Value:** valid range is 0.0 to 1.0)

### DiffuseColorMethod

```text
ACadSharp.Objects.ColorMethod DiffuseColorMethod { get; set; }
```

Diffuse color method.

### DiffuseMapBlendFactor

```text
System.Double DiffuseMapBlendFactor { get; set; }
```

Diffuse map blend factor.

### DiffuseMapFileName

```text
System.String DiffuseMapFileName { get; set; }
```

Diffuse map file name.

**Remarks:** null file name specifies no map.

### DiffuseMapSource

```text
ACadSharp.Objects.MapSource DiffuseMapSource { get; set; }
```

Diffuse map source.

### DiffuseMatrix

```text
CSMath.Matrix4 DiffuseMatrix { get; set; }
```

Transform matrix of diffuse map mapper.

### DiffuseProjectionMethod

```text
ACadSharp.Objects.ProjectionMethod DiffuseProjectionMethod { get; set; }
```

Projection method of diffuse map mapper.

### DiffuseTilingMethod

```text
ACadSharp.Objects.TilingMethod DiffuseTilingMethod { get; set; }
```

Tiling method of diffuse map mapper.

### IlluminationModel

```text
ACadSharp.Objects.MaterialIlluminationModel IlluminationModel { get; set; }
```

Shader chosen to evaluate the Material's illumination. Defaults to F:ACadSharp.Objects.MaterialIlluminationModel.BlinnShader, the ODA SDK default for OdGiMaterialTraits.

### Mode

```text
ACadSharp.Objects.MaterialMode Mode { get; set; }
```

Render-pipeline mode hint. Defaults to F:ACadSharp.Objects.MaterialMode.Realistic, the ODA SDK default.

### Name

```text
System.String Name { get; set; }
```

Material name.

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

### Opacity

```text
System.Double Opacity { get; set; }
```

Opacity percent.

### OpacityAutoTransform

```text
ACadSharp.Objects.AutoTransformMethodFlags OpacityAutoTransform { get; set; }
```

Auto transform method of opacity map mapper.

### OpacityMapBlendFactor

```text
System.Double OpacityMapBlendFactor { get; set; }
```

Opacity map blend factor.

**Value:** default = 1.0

### OpacityMapFileName

```text
System.String OpacityMapFileName { get; set; }
```

Opacity map file name.

**Remarks:** null file name specifies no map.

### OpacityMapSource

```text
ACadSharp.Objects.MapSource OpacityMapSource { get; set; }
```

Opacity map source.

### OpacityMatrix

```text
CSMath.Matrix4 OpacityMatrix { get; set; }
```

Transform matrix of opacity map mapper.

### OpacityProjectionMethod

```text
ACadSharp.Objects.ProjectionMethod OpacityProjectionMethod { get; set; }
```

Opacity method of specular map mapper.

### OpacityTilingMethod

```text
ACadSharp.Objects.TilingMethod OpacityTilingMethod { get; set; }
```

Tiling method of opacity map mapper.

### ReflectionAutoTransform

```text
ACadSharp.Objects.AutoTransformMethodFlags ReflectionAutoTransform { get; set; }
```

Auto transform method of reflection map mapper.

### ReflectionMapBlendFactor

```text
System.Double ReflectionMapBlendFactor { get; set; }
```

Blend factor of reflection map.

### ReflectionMapFileName

```text
System.String ReflectionMapFileName { get; set; }
```

Reflection map file name.

**Remarks:** null file name specifies no map.

### ReflectionMapSource

```text
ACadSharp.Objects.MapSource ReflectionMapSource { get; set; }
```

Reflection map source.

### ReflectionMatrix

```text
CSMath.Matrix4 ReflectionMatrix { get; set; }
```

Transform matrix of reflection map mapper.

### ReflectionProjectionMethod

```text
ACadSharp.Objects.ProjectionMethod ReflectionProjectionMethod { get; set; }
```

Projection method of specular map mapper.

### ReflectionTilingMethod

```text
ACadSharp.Objects.TilingMethod ReflectionTilingMethod { get; set; }
```

Tiling method of reflection map mapper.

### Reflectivity

```text
System.Double Reflectivity { get; set; }
```

### RefractionAutoTransform

```text
ACadSharp.Objects.AutoTransformMethodFlags RefractionAutoTransform { get; set; }
```

Auto transform method of refraction map mapper.

### RefractionIndex

```text
System.Double RefractionIndex { get; set; }
```

Refraction index.

### RefractionMapBlendFactor

```text
System.Double RefractionMapBlendFactor { get; set; }
```

Bump map refraction factor.

**Value:** default = 1.0

### RefractionMapFileName

```text
System.String RefractionMapFileName { get; set; }
```

Refraction map file name.

**Remarks:** null file name specifies no map.

### RefractionMapSource

```text
ACadSharp.Objects.MapSource RefractionMapSource { get; set; }
```

Refraction map source.

### RefractionMatrix

```text
CSMath.Matrix4 RefractionMatrix { get; set; }
```

Transform matrix of refraction map mapper.

### RefractionProjectionMethod

```text
ACadSharp.Objects.ProjectionMethod RefractionProjectionMethod { get; set; }
```

Projection method of refraction map mapper.

### RefractionTilingMethod

```text
ACadSharp.Objects.TilingMethod RefractionTilingMethod { get; set; }
```

Tiling method of refraction map mapper.

### SelfIllumination

```text
System.Double SelfIllumination { get; set; }
```

Self-illumination factor.

### SpecularAutoTransform

```text
ACadSharp.Objects.AutoTransformMethodFlags SpecularAutoTransform { get; set; }
```

Auto transform method of specular map mapper.

### SpecularColor

```text
ACadSharp.Color SpecularColor { get; set; }
```

Specular color.

### SpecularColorFactor

```text
System.Double SpecularColorFactor { get; set; }
```

Specular color factor.

**Value:** valid range is 0.0 to 1.0)

### SpecularColorMethod

```text
ACadSharp.Objects.ColorMethod SpecularColorMethod { get; set; }
```

Specular color method.

### SpecularGlossFactor

```text
System.Double SpecularGlossFactor { get; set; }
```

Specular gloss factor.

**Value:** default = 0.5

### SpecularMapBlendFactor

```text
System.Double SpecularMapBlendFactor { get; set; }
```

Specular map blend factor.

**Value:** default = 1.0

### SpecularMapFileName

```text
System.String SpecularMapFileName { get; set; }
```

Specular map file name.

**Remarks:** null file name specifies no map.

### SpecularMapSource

```text
ACadSharp.Objects.MapSource SpecularMapSource { get; set; }
```

Specular map source.

### SpecularMatrix

```text
CSMath.Matrix4 SpecularMatrix { get; set; }
```

Transform matrix of specular map mapper.

### SpecularProjectionMethod

```text
ACadSharp.Objects.ProjectionMethod SpecularProjectionMethod { get; set; }
```

Projection method of specular map mapper.

### SpecularTilingMethod

```text
ACadSharp.Objects.TilingMethod SpecularTilingMethod { get; set; }
```

Tiling method of specular map mapper.

### SubclassMarker

```text
System.String SubclassMarker { get; }
```

Documentation inherited from: `base member`.

### Translucence

```text
System.Double Translucence { get; set; }
```

Translucence factor.
