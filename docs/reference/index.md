# Complete managed API reference

Generated from the shipped assembly: **607 exported public types** across **29 namespaces**. Every public class, interface, struct, enum, delegate, nested type and open generic definition returned by .NET reflection is included.

Each page lists the type's declared public constructors, properties, fields, events, methods and operators, including overload signatures and upstream XML documentation when present. Inherited members remain available through Python.NET and are documented on their declaring type. A missing upstream summary is reported explicitly; this generator does not invent documentation.

Use `acadsharp.get_type(clr_name)` for exact type resolution, including CLR nested names (`+`) and generic arity suffixes (backticks). Original namespaces such as `ACadSharp.Entities` can be imported after `acadsharp.load()`. The machine-readable equivalent is bundled as `acadsharp/api.json`.

This reference describes the managed backend. See [Native AOT](../native.md) for the separate native backend's implemented operations.

## ACadSharp

- [ACadSharp.ACadVersion](ACadSharp.ACadVersion.md) — enum
- [ACadSharp.CadDocument](ACadSharp.CadDocument.md) — class
- [ACadSharp.CadObject](ACadSharp.CadObject.md) — class
- [ACadSharp.CadObjectCollection](ACadSharp.CadObjectCollection-1.md) — class
- [ACadSharp.CadSummaryInfo](ACadSharp.CadSummaryInfo.md) — class
- [ACadSharp.CadSystemVariable](ACadSharp.CadSystemVariable.md) — class
- [ACadSharp.CadValue](ACadSharp.CadValue.md) — class
- [ACadSharp.CadValueType](ACadSharp.CadValueType.md) — enum
- [ACadSharp.CadValueUnitType](ACadSharp.CadValueUnitType.md) — enum
- [ACadSharp.CollectionChangedEventArgs](ACadSharp.CollectionChangedEventArgs.md) — class
- [ACadSharp.Color](ACadSharp.Color.md) — struct
- [ACadSharp.DwgPreview](ACadSharp.DwgPreview.md) — class
- [ACadSharp.DwgPreview.PreviewType](ACadSharp.DwgPreview.PreviewType.md) — enum
- [ACadSharp.DwgReferenceType](ACadSharp.DwgReferenceType.md) — enum
- [ACadSharp.DxfClassMap](ACadSharp.DxfClassMap.md) — class
- [ACadSharp.DxfCode](ACadSharp.DxfCode.md) — enum
- [ACadSharp.DxfFileToken](ACadSharp.DxfFileToken.md) — class
- [ACadSharp.DxfMap](ACadSharp.DxfMap.md) — class
- [ACadSharp.DxfMapBase](ACadSharp.DxfMapBase.md) — class
- [ACadSharp.DxfProperty](ACadSharp.DxfProperty.md) — class
- [ACadSharp.DxfPropertyBase](ACadSharp.DxfPropertyBase-1.md) — class
- [ACadSharp.DxfReferenceType](ACadSharp.DxfReferenceType.md) — enum
- [ACadSharp.DxfSubclassMarker](ACadSharp.DxfSubclassMarker.md) — class
- [ACadSharp.FlowDirectionType](ACadSharp.FlowDirectionType.md) — enum
- [ACadSharp.GroupCodeValue](ACadSharp.GroupCodeValue.md) — class
- [ACadSharp.GroupCodeValueType](ACadSharp.GroupCodeValueType.md) — enum
- [ACadSharp.ICadCollection](ACadSharp.ICadCollection-1.md) — interface
- [ACadSharp.IHandledCadObject](ACadSharp.IHandledCadObject.md) — interface
- [ACadSharp.INamedCadObject](ACadSharp.INamedCadObject.md) — interface
- [ACadSharp.IObservableCadCollection](ACadSharp.IObservableCadCollection-1.md) — interface
- [ACadSharp.IOrientable](ACadSharp.IOrientable.md) — interface
- [ACadSharp.IProxy](ACadSharp.IProxy.md) — interface
- [ACadSharp.ISeqendCollection](ACadSharp.ISeqendCollection.md) — interface
- [ACadSharp.LineSpacingStyle](ACadSharp.LineSpacingStyle.md) — enum
- [ACadSharp.LineWeightType](ACadSharp.LineWeightType.md) — enum
- [ACadSharp.MultiLeaderPathType](ACadSharp.MultiLeaderPathType.md) — enum
- [ACadSharp.ObjectType](ACadSharp.ObjectType.md) — enum
- [ACadSharp.OnNameChangedArgs](ACadSharp.OnNameChangedArgs.md) — class
- [ACadSharp.OrthographicType](ACadSharp.OrthographicType.md) — enum
- [ACadSharp.RenderMode](ACadSharp.RenderMode.md) — enum
- [ACadSharp.SeqendCollection](ACadSharp.SeqendCollection-1.md) — class
- [ACadSharp.TextAlignmentType](ACadSharp.TextAlignmentType.md) — enum
- [ACadSharp.TextAngleType](ACadSharp.TextAngleType.md) — enum
- [ACadSharp.TextAttachmentDirectionType](ACadSharp.TextAttachmentDirectionType.md) — enum
- [ACadSharp.TextAttachmentPointType](ACadSharp.TextAttachmentPointType.md) — enum
- [ACadSharp.TextAttachmentType](ACadSharp.TextAttachmentType.md) — enum
- [ACadSharp.Transparency](ACadSharp.Transparency.md) — struct

## ACadSharp.Attributes

- [ACadSharp.Attributes.CadSystemVariableAttribute](ACadSharp.Attributes.CadSystemVariableAttribute.md) — class
- [ACadSharp.Attributes.DxfCodeValueAttribute](ACadSharp.Attributes.DxfCodeValueAttribute.md) — class
- [ACadSharp.Attributes.DxfCollectionCodeValueAttribute](ACadSharp.Attributes.DxfCollectionCodeValueAttribute.md) — class
- [ACadSharp.Attributes.DxfNameAttribute](ACadSharp.Attributes.DxfNameAttribute.md) — class
- [ACadSharp.Attributes.DxfSubClassAttribute](ACadSharp.Attributes.DxfSubClassAttribute.md) — class
- [ACadSharp.Attributes.ICodeValueAttribute](ACadSharp.Attributes.ICodeValueAttribute.md) — interface

## ACadSharp.Blocks

- [ACadSharp.Blocks.Block](ACadSharp.Blocks.Block.md) — class
- [ACadSharp.Blocks.BlockEnd](ACadSharp.Blocks.BlockEnd.md) — class
- [ACadSharp.Blocks.BlockTypeFlags](ACadSharp.Blocks.BlockTypeFlags.md) — enum
- [ACadSharp.Blocks.DimensionArrowhead](ACadSharp.Blocks.DimensionArrowhead.md) — class

## ACadSharp.Classes

- [ACadSharp.Classes.DxfClass](ACadSharp.Classes.DxfClass.md) — class
- [ACadSharp.Classes.DxfClassCollection](ACadSharp.Classes.DxfClassCollection.md) — class
- [ACadSharp.Classes.IDxfClassDefined](ACadSharp.Classes.IDxfClassDefined.md) — interface
- [ACadSharp.Classes.ProxyFlags](ACadSharp.Classes.ProxyFlags.md) — enum

## ACadSharp.DataStorage

- [ACadSharp.DataStorage.SchemaRecordFlags](ACadSharp.DataStorage.SchemaRecordFlags.md) — enum

## ACadSharp.Entities

- [ACadSharp.Entities.Arc](ACadSharp.Entities.Arc.md) — class
- [ACadSharp.Entities.AttachmentPointType](ACadSharp.Entities.AttachmentPointType.md) — enum
- [ACadSharp.Entities.AttributeBase](ACadSharp.Entities.AttributeBase.md) — class
- [ACadSharp.Entities.AttributeDefinition](ACadSharp.Entities.AttributeDefinition.md) — class
- [ACadSharp.Entities.AttributeEntity](ACadSharp.Entities.AttributeEntity.md) — class
- [ACadSharp.Entities.AttributeFlags](ACadSharp.Entities.AttributeFlags.md) — enum
- [ACadSharp.Entities.AttributeType](ACadSharp.Entities.AttributeType.md) — enum
- [ACadSharp.Entities.BackgroundFillFlags](ACadSharp.Entities.BackgroundFillFlags.md) — enum
- [ACadSharp.Entities.BlockContentConnectionType](ACadSharp.Entities.BlockContentConnectionType.md) — enum
- [ACadSharp.Entities.BoundaryPathFlags](ACadSharp.Entities.BoundaryPathFlags.md) — enum
- [ACadSharp.Entities.CadBody](ACadSharp.Entities.CadBody.md) — class
- [ACadSharp.Entities.CadWipeoutBase](ACadSharp.Entities.CadWipeoutBase.md) — class
- [ACadSharp.Entities.Circle](ACadSharp.Entities.Circle.md) — class
- [ACadSharp.Entities.ClipMode](ACadSharp.Entities.ClipMode.md) — enum
- [ACadSharp.Entities.ClipType](ACadSharp.Entities.ClipType.md) — enum
- [ACadSharp.Entities.ColumnType](ACadSharp.Entities.ColumnType.md) — enum
- [ACadSharp.Entities.Dimension](ACadSharp.Entities.Dimension.md) — class
- [ACadSharp.Entities.DimensionAligned](ACadSharp.Entities.DimensionAligned.md) — class
- [ACadSharp.Entities.DimensionAngular2Line](ACadSharp.Entities.DimensionAngular2Line.md) — class
- [ACadSharp.Entities.DimensionAngular3Pt](ACadSharp.Entities.DimensionAngular3Pt.md) — class
- [ACadSharp.Entities.DimensionArc](ACadSharp.Entities.DimensionArc.md) — class
- [ACadSharp.Entities.DimensionDiameter](ACadSharp.Entities.DimensionDiameter.md) — class
- [ACadSharp.Entities.DimensionLinear](ACadSharp.Entities.DimensionLinear.md) — class
- [ACadSharp.Entities.DimensionOrdinate](ACadSharp.Entities.DimensionOrdinate.md) — class
- [ACadSharp.Entities.DimensionRadius](ACadSharp.Entities.DimensionRadius.md) — class
- [ACadSharp.Entities.DimensionType](ACadSharp.Entities.DimensionType.md) — enum
- [ACadSharp.Entities.DrawingDirectionType](ACadSharp.Entities.DrawingDirectionType.md) — enum
- [ACadSharp.Entities.Ellipse](ACadSharp.Entities.Ellipse.md) — class
- [ACadSharp.Entities.Entity](ACadSharp.Entities.Entity.md) — class
- [ACadSharp.Entities.ExtrudedSurface](ACadSharp.Entities.ExtrudedSurface.md) — class
- [ACadSharp.Entities.Face3D](ACadSharp.Entities.Face3D.md) — class
- [ACadSharp.Entities.GradientColor](ACadSharp.Entities.GradientColor.md) — class
- [ACadSharp.Entities.Hatch](ACadSharp.Entities.Hatch.md) — class
- [ACadSharp.Entities.Hatch.BoundaryPath](ACadSharp.Entities.Hatch.BoundaryPath.md) — class
- [ACadSharp.Entities.Hatch.BoundaryPath.Arc](ACadSharp.Entities.Hatch.BoundaryPath.Arc.md) — class
- [ACadSharp.Entities.Hatch.BoundaryPath.Edge](ACadSharp.Entities.Hatch.BoundaryPath.Edge.md) — class
- [ACadSharp.Entities.Hatch.BoundaryPath.EdgeType](ACadSharp.Entities.Hatch.BoundaryPath.EdgeType.md) — enum
- [ACadSharp.Entities.Hatch.BoundaryPath.Ellipse](ACadSharp.Entities.Hatch.BoundaryPath.Ellipse.md) — class
- [ACadSharp.Entities.Hatch.BoundaryPath.Line](ACadSharp.Entities.Hatch.BoundaryPath.Line.md) — class
- [ACadSharp.Entities.Hatch.BoundaryPath.Polyline](ACadSharp.Entities.Hatch.BoundaryPath.Polyline.md) — class
- [ACadSharp.Entities.Hatch.BoundaryPath.Spline](ACadSharp.Entities.Hatch.BoundaryPath.Spline.md) — class
- [ACadSharp.Entities.HatchGradientPattern](ACadSharp.Entities.HatchGradientPattern.md) — class
- [ACadSharp.Entities.HatchPattern](ACadSharp.Entities.HatchPattern.md) — class
- [ACadSharp.Entities.HatchPattern.Line](ACadSharp.Entities.HatchPattern.Line.md) — class
- [ACadSharp.Entities.HatchPatternType](ACadSharp.Entities.HatchPatternType.md) — enum
- [ACadSharp.Entities.HatchStyleType](ACadSharp.Entities.HatchStyleType.md) — enum
- [ACadSharp.Entities.HookLineDirection](ACadSharp.Entities.HookLineDirection.md) — enum
- [ACadSharp.Entities.IEntity](ACadSharp.Entities.IEntity.md) — interface
- [ACadSharp.Entities.IGeometricEntity](ACadSharp.Entities.IGeometricEntity.md) — interface
- [ACadSharp.Entities.IPolyline](ACadSharp.Entities.IPolyline.md) — interface
- [ACadSharp.Entities.IText](ACadSharp.Entities.IText.md) — interface
- [ACadSharp.Entities.IVertex](ACadSharp.Entities.IVertex.md) — interface
- [ACadSharp.Entities.ImageDisplayFlags](ACadSharp.Entities.ImageDisplayFlags.md) — enum
- [ACadSharp.Entities.Insert](ACadSharp.Entities.Insert.md) — class
- [ACadSharp.Entities.InvisibleEdgeFlags](ACadSharp.Entities.InvisibleEdgeFlags.md) — enum
- [ACadSharp.Entities.KnotParametrization](ACadSharp.Entities.KnotParametrization.md) — enum
- [ACadSharp.Entities.Leader](ACadSharp.Entities.Leader.md) — class
- [ACadSharp.Entities.LeaderCreationType](ACadSharp.Entities.LeaderCreationType.md) — enum
- [ACadSharp.Entities.LeaderPathType](ACadSharp.Entities.LeaderPathType.md) — enum
- [ACadSharp.Entities.LightingType](ACadSharp.Entities.LightingType.md) — enum
- [ACadSharp.Entities.Line](ACadSharp.Entities.Line.md) — class
- [ACadSharp.Entities.LineSpacingStyleType](ACadSharp.Entities.LineSpacingStyleType.md) — enum
- [ACadSharp.Entities.LoftedSurface](ACadSharp.Entities.LoftedSurface.md) — class
- [ACadSharp.Entities.LwPolyline](ACadSharp.Entities.LwPolyline.md) — class
- [ACadSharp.Entities.LwPolyline.Vertex](ACadSharp.Entities.LwPolyline.Vertex.md) — class
- [ACadSharp.Entities.LwPolylineFlags](ACadSharp.Entities.LwPolylineFlags.md) — enum
- [ACadSharp.Entities.MLine](ACadSharp.Entities.MLine.md) — class
- [ACadSharp.Entities.MLine.Vertex](ACadSharp.Entities.MLine.Vertex.md) — class
- [ACadSharp.Entities.MLine.Vertex.Segment](ACadSharp.Entities.MLine.Vertex.Segment.md) — class
- [ACadSharp.Entities.MLineFlags](ACadSharp.Entities.MLineFlags.md) — enum
- [ACadSharp.Entities.MLineJustification](ACadSharp.Entities.MLineJustification.md) — enum
- [ACadSharp.Entities.MText](ACadSharp.Entities.MText.md) — class
- [ACadSharp.Entities.MText.TextColumnData](ACadSharp.Entities.MText.TextColumnData.md) — class
- [ACadSharp.Entities.Mesh](ACadSharp.Entities.Mesh.md) — class
- [ACadSharp.Entities.Mesh.Edge](ACadSharp.Entities.Mesh.Edge.md) — struct
- [ACadSharp.Entities.ModelerGeometry](ACadSharp.Entities.ModelerGeometry.md) — class
- [ACadSharp.Entities.ModelerGeometry.Silhouette](ACadSharp.Entities.ModelerGeometry.Silhouette.md) — class
- [ACadSharp.Entities.ModelerGeometry.Wire](ACadSharp.Entities.ModelerGeometry.Wire.md) — class
- [ACadSharp.Entities.MultiLeader](ACadSharp.Entities.MultiLeader.md) — class
- [ACadSharp.Entities.MultiLeader.BlockAttribute](ACadSharp.Entities.MultiLeader.BlockAttribute.md) — class
- [ACadSharp.Entities.MultiLeaderPropertyOverrideFlags](ACadSharp.Entities.MultiLeaderPropertyOverrideFlags.md) — enum
- [ACadSharp.Entities.NurbSurface](ACadSharp.Entities.NurbSurface.md) — class
- [ACadSharp.Entities.Ole2Frame](ACadSharp.Entities.Ole2Frame.md) — class
- [ACadSharp.Entities.OleObjectType](ACadSharp.Entities.OleObjectType.md) — enum
- [ACadSharp.Entities.PdfUnderlay](ACadSharp.Entities.PdfUnderlay.md) — class
- [ACadSharp.Entities.PlaneSurface](ACadSharp.Entities.PlaneSurface.md) — class
- [ACadSharp.Entities.Point](ACadSharp.Entities.Point.md) — class
- [ACadSharp.Entities.PolyfaceMesh](ACadSharp.Entities.PolyfaceMesh.md) — class
- [ACadSharp.Entities.PolygonMesh](ACadSharp.Entities.PolygonMesh.md) — class
- [ACadSharp.Entities.PolygonMeshVertex](ACadSharp.Entities.PolygonMeshVertex.md) — class
- [ACadSharp.Entities.Polyline2D](ACadSharp.Entities.Polyline2D.md) — class
- [ACadSharp.Entities.Polyline3D](ACadSharp.Entities.Polyline3D.md) — class
- [ACadSharp.Entities.PolylineFlags](ACadSharp.Entities.PolylineFlags.md) — enum
- [ACadSharp.Entities.Polyline](ACadSharp.Entities.Polyline-1.md) — class
- [ACadSharp.Entities.ProxyEntity](ACadSharp.Entities.ProxyEntity.md) — class
- [ACadSharp.Entities.RasterImage](ACadSharp.Entities.RasterImage.md) — class
- [ACadSharp.Entities.Ray](ACadSharp.Entities.Ray.md) — class
- [ACadSharp.Entities.Region](ACadSharp.Entities.Region.md) — class
- [ACadSharp.Entities.RevolvedSurface](ACadSharp.Entities.RevolvedSurface.md) — class
- [ACadSharp.Entities.Seqend](ACadSharp.Entities.Seqend.md) — class
- [ACadSharp.Entities.ShadowMode](ACadSharp.Entities.ShadowMode.md) — enum
- [ACadSharp.Entities.Shape](ACadSharp.Entities.Shape.md) — class
- [ACadSharp.Entities.SmoothSurfaceType](ACadSharp.Entities.SmoothSurfaceType.md) — enum
- [ACadSharp.Entities.Solid](ACadSharp.Entities.Solid.md) — class
- [ACadSharp.Entities.Solid3D](ACadSharp.Entities.Solid3D.md) — class
- [ACadSharp.Entities.Spline](ACadSharp.Entities.Spline.md) — class
- [ACadSharp.Entities.SplineFlags](ACadSharp.Entities.SplineFlags.md) — enum
- [ACadSharp.Entities.SplineFlags1](ACadSharp.Entities.SplineFlags1.md) — enum
- [ACadSharp.Entities.Surface](ACadSharp.Entities.Surface.md) — class
- [ACadSharp.Entities.SweptSurface](ACadSharp.Entities.SweptSurface.md) — class
- [ACadSharp.Entities.TableEntity](ACadSharp.Entities.TableEntity.md) — class
- [ACadSharp.Entities.TableEntity.BreakFlowDirection](ACadSharp.Entities.TableEntity.BreakFlowDirection.md) — enum
- [ACadSharp.Entities.TableEntity.BreakOptionFlags](ACadSharp.Entities.TableEntity.BreakOptionFlags.md) — enum
- [ACadSharp.Entities.TableEntity.Cell](ACadSharp.Entities.TableEntity.Cell.md) — class
- [ACadSharp.Entities.TableEntity.CellContent](ACadSharp.Entities.TableEntity.CellContent.md) — class
- [ACadSharp.Entities.TableEntity.CellContentGeometry](ACadSharp.Entities.TableEntity.CellContentGeometry.md) — class
- [ACadSharp.Entities.TableEntity.CellRange](ACadSharp.Entities.TableEntity.CellRange.md) — class
- [ACadSharp.Entities.TableEntity.CellType](ACadSharp.Entities.TableEntity.CellType.md) — enum
- [ACadSharp.Entities.TableEntity.Column](ACadSharp.Entities.TableEntity.Column.md) — class
- [ACadSharp.Entities.TableEntity.CustomDataEntry](ACadSharp.Entities.TableEntity.CustomDataEntry.md) — class
- [ACadSharp.Entities.TableEntity.ITableComponent](ACadSharp.Entities.TableEntity.ITableComponent.md) — interface
- [ACadSharp.Entities.TableEntity.Row](ACadSharp.Entities.TableEntity.Row.md) — class
- [ACadSharp.Entities.TableEntity.TableAttribute](ACadSharp.Entities.TableEntity.TableAttribute.md) — class
- [ACadSharp.Entities.TableEntity.TableBreakData](ACadSharp.Entities.TableEntity.TableBreakData.md) — class
- [ACadSharp.Entities.TableEntity.TableBreakData.BreakHeight](ACadSharp.Entities.TableEntity.TableBreakData.BreakHeight.md) — struct
- [ACadSharp.Entities.TableEntity.TableCellContentType](ACadSharp.Entities.TableEntity.TableCellContentType.md) — enum
- [ACadSharp.Entities.TableEntity.TableCellStateFlags](ACadSharp.Entities.TableEntity.TableCellStateFlags.md) — enum
- [ACadSharp.Entities.TableEntity.ValueUnitType](ACadSharp.Entities.TableEntity.ValueUnitType.md) — enum
- [ACadSharp.Entities.TextEntity](ACadSharp.Entities.TextEntity.md) — class
- [ACadSharp.Entities.TextHorizontalAlignment](ACadSharp.Entities.TextHorizontalAlignment.md) — enum
- [ACadSharp.Entities.TextMirrorFlag](ACadSharp.Entities.TextMirrorFlag.md) — enum
- [ACadSharp.Entities.TextVerticalAlignmentType](ACadSharp.Entities.TextVerticalAlignmentType.md) — enum
- [ACadSharp.Entities.Tolerance](ACadSharp.Entities.Tolerance.md) — class
- [ACadSharp.Entities.UnderlayDisplayFlags](ACadSharp.Entities.UnderlayDisplayFlags.md) — enum
- [ACadSharp.Entities.UnderlayEntity](ACadSharp.Entities.UnderlayEntity-1.md) — class
- [ACadSharp.Entities.UnknownEntity](ACadSharp.Entities.UnknownEntity.md) — class
- [ACadSharp.Entities.Vertex](ACadSharp.Entities.Vertex.md) — class
- [ACadSharp.Entities.Vertex2D](ACadSharp.Entities.Vertex2D.md) — class
- [ACadSharp.Entities.Vertex3D](ACadSharp.Entities.Vertex3D.md) — class
- [ACadSharp.Entities.VertexFaceMesh](ACadSharp.Entities.VertexFaceMesh.md) — class
- [ACadSharp.Entities.VertexFaceRecord](ACadSharp.Entities.VertexFaceRecord.md) — class
- [ACadSharp.Entities.VertexFlags](ACadSharp.Entities.VertexFlags.md) — enum
- [ACadSharp.Entities.VerticalAlignmentType](ACadSharp.Entities.VerticalAlignmentType.md) — enum
- [ACadSharp.Entities.Viewport](ACadSharp.Entities.Viewport.md) — class
- [ACadSharp.Entities.ViewportStatusFlags](ACadSharp.Entities.ViewportStatusFlags.md) — enum
- [ACadSharp.Entities.Wipeout](ACadSharp.Entities.Wipeout.md) — class
- [ACadSharp.Entities.XLine](ACadSharp.Entities.XLine.md) — class

## ACadSharp.Entities.AecEntities

- [ACadSharp.Entities.AecEntities.AecEntity](ACadSharp.Entities.AecEntities.AecEntity.md) — class
- [ACadSharp.Entities.AecEntities.Wall](ACadSharp.Entities.AecEntities.Wall.md) — class
- [ACadSharp.Entities.AecEntities.WallJustification](ACadSharp.Entities.AecEntities.WallJustification.md) — enum

## ACadSharp.Entities.Mechanical

- [ACadSharp.Entities.Mechanical.AcmBalloon](ACadSharp.Entities.Mechanical.AcmBalloon.md) — class
- [ACadSharp.Entities.Mechanical.AcmPartList](ACadSharp.Entities.Mechanical.AcmPartList.md) — class
- [ACadSharp.Entities.Mechanical.AcmPartRef](ACadSharp.Entities.Mechanical.AcmPartRef.md) — class
- [ACadSharp.Entities.Mechanical.MechanicalEntity](ACadSharp.Entities.Mechanical.MechanicalEntity.md) — class

## ACadSharp.Entities.ProxyGraphics

- [ACadSharp.Entities.ProxyGraphics.EdgeTraits](ACadSharp.Entities.ProxyGraphics.EdgeTraits.md) — class
- [ACadSharp.Entities.ProxyGraphics.FaceTraits](ACadSharp.Entities.ProxyGraphics.FaceTraits.md) — class
- [ACadSharp.Entities.ProxyGraphics.GraphicsType](ACadSharp.Entities.ProxyGraphics.GraphicsType.md) — enum
- [ACadSharp.Entities.ProxyGraphics.IProxyGeometry](ACadSharp.Entities.ProxyGraphics.IProxyGeometry.md) — interface
- [ACadSharp.Entities.ProxyGraphics.PrimitiveFlags](ACadSharp.Entities.ProxyGraphics.PrimitiveFlags.md) — enum
- [ACadSharp.Entities.ProxyGraphics.PrimitiveTraits](ACadSharp.Entities.ProxyGraphics.PrimitiveTraits.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyCircle](ACadSharp.Entities.ProxyGraphics.ProxyCircle.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyCirclePt3](ACadSharp.Entities.ProxyGraphics.ProxyCirclePt3.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyCircularArc](ACadSharp.Entities.ProxyGraphics.ProxyCircularArc.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyCircularArc3Pt](ACadSharp.Entities.ProxyGraphics.ProxyCircularArc3Pt.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyColorMethod](ACadSharp.Entities.ProxyGraphics.ProxyColorMethod.md) — enum
- [ACadSharp.Entities.ProxyGraphics.ProxyExtents](ACadSharp.Entities.ProxyGraphics.ProxyExtents.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyGeometryReader](ACadSharp.Entities.ProxyGraphics.ProxyGeometryReader.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyLwPolyine](ACadSharp.Entities.ProxyGraphics.ProxyLwPolyine.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyMesh](ACadSharp.Entities.ProxyGraphics.ProxyMesh.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyMeshBase](ACadSharp.Entities.ProxyGraphics.ProxyMeshBase.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyPlotStyleType](ACadSharp.Entities.ProxyGraphics.ProxyPlotStyleType.md) — enum
- [ACadSharp.Entities.ProxyGraphics.ProxyPolygon](ACadSharp.Entities.ProxyGraphics.ProxyPolygon.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyPolyline](ACadSharp.Entities.ProxyGraphics.ProxyPolyline.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyPolylineWithNormal](ACadSharp.Entities.ProxyGraphics.ProxyPolylineWithNormal.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyPopClip](ACadSharp.Entities.ProxyGraphics.ProxyPopClip.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyPopModelTransform](ACadSharp.Entities.ProxyGraphics.ProxyPopModelTransform.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyPushClip](ACadSharp.Entities.ProxyGraphics.ProxyPushClip.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyPushModelTransform](ACadSharp.Entities.ProxyGraphics.ProxyPushModelTransform.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyPushModelTransform2](ACadSharp.Entities.ProxyGraphics.ProxyPushModelTransform2.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyRay](ACadSharp.Entities.ProxyGraphics.ProxyRay.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyShell](ACadSharp.Entities.ProxyGraphics.ProxyShell.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubEntityMapper](ACadSharp.Entities.ProxyGraphics.ProxySubEntityMapper.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubEntityMaterial](ACadSharp.Entities.ProxyGraphics.ProxySubEntityMaterial.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubentColor](ACadSharp.Entities.ProxyGraphics.ProxySubentColor.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubentFillon](ACadSharp.Entities.ProxyGraphics.ProxySubentFillon.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubentLayer](ACadSharp.Entities.ProxyGraphics.ProxySubentLayer.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubentLineType](ACadSharp.Entities.ProxyGraphics.ProxySubentLineType.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubentLineTypeScale](ACadSharp.Entities.ProxyGraphics.ProxySubentLineTypeScale.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubentLineWeight](ACadSharp.Entities.ProxyGraphics.ProxySubentLineWeight.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubentMarker](ACadSharp.Entities.ProxyGraphics.ProxySubentMarker.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubentPlotStyleName](ACadSharp.Entities.ProxyGraphics.ProxySubentPlotStyleName.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubentThickness](ACadSharp.Entities.ProxyGraphics.ProxySubentThickness.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxySubentTrueColor](ACadSharp.Entities.ProxyGraphics.ProxySubentTrueColor.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyText](ACadSharp.Entities.ProxyGraphics.ProxyText.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyText2](ACadSharp.Entities.ProxyGraphics.ProxyText2.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText](ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText2](ACadSharp.Entities.ProxyGraphics.ProxyUnicodeText2.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyUnknown37](ACadSharp.Entities.ProxyGraphics.ProxyUnknown37.md) — class
- [ACadSharp.Entities.ProxyGraphics.ProxyXLine](ACadSharp.Entities.ProxyGraphics.ProxyXLine.md) — class
- [ACadSharp.Entities.ProxyGraphics.TrueTypeFontDescriptor](ACadSharp.Entities.ProxyGraphics.TrueTypeFontDescriptor.md) — class
- [ACadSharp.Entities.ProxyGraphics.VertexTraits](ACadSharp.Entities.ProxyGraphics.VertexTraits.md) — class

## ACadSharp.Exceptions

- [ACadSharp.Exceptions.CadNotSupportedException](ACadSharp.Exceptions.CadNotSupportedException.md) — class
- [ACadSharp.Exceptions.DwgException](ACadSharp.Exceptions.DwgException.md) — class
- [ACadSharp.Exceptions.DxfException](ACadSharp.Exceptions.DxfException.md) — class

## ACadSharp.Extensions

- [ACadSharp.Extensions.CadObjectExtensions](ACadSharp.Extensions.CadObjectExtensions.md) — class
- [ACadSharp.Extensions.INamedCadObjectExtensions](ACadSharp.Extensions.INamedCadObjectExtensions.md) — class
- [ACadSharp.Extensions.LineWeightTypeExtensions](ACadSharp.Extensions.LineWeightTypeExtensions.md) — class
- [ACadSharp.Extensions.PolylineExtensions](ACadSharp.Extensions.PolylineExtensions.md) — class
- [ACadSharp.Extensions.UnitExtensions](ACadSharp.Extensions.UnitExtensions.md) — class

## ACadSharp.Header

- [ACadSharp.Header.AttributeVisibilityMode](ACadSharp.Header.AttributeVisibilityMode.md) — enum
- [ACadSharp.Header.CadHeader](ACadSharp.Header.CadHeader.md) — class
- [ACadSharp.Header.DimensionAssociation](ACadSharp.Header.DimensionAssociation.md) — enum
- [ACadSharp.Header.EntityPlotStyleType](ACadSharp.Header.EntityPlotStyleType.md) — enum
- [ACadSharp.Header.IndexCreationFlags](ACadSharp.Header.IndexCreationFlags.md) — enum
- [ACadSharp.Header.MeasurementUnits](ACadSharp.Header.MeasurementUnits.md) — enum
- [ACadSharp.Header.ObjectSnapMode](ACadSharp.Header.ObjectSnapMode.md) — enum
- [ACadSharp.Header.ObjectSortingFlags](ACadSharp.Header.ObjectSortingFlags.md) — enum
- [ACadSharp.Header.ShadeEdgeType](ACadSharp.Header.ShadeEdgeType.md) — enum
- [ACadSharp.Header.ShadowMode](ACadSharp.Header.ShadowMode.md) — enum
- [ACadSharp.Header.SpaceLineTypeScaling](ACadSharp.Header.SpaceLineTypeScaling.md) — enum
- [ACadSharp.Header.SplineType](ACadSharp.Header.SplineType.md) — enum
- [ACadSharp.Header.XClipFrameType](ACadSharp.Header.XClipFrameType.md) — enum

## ACadSharp.IO

- [ACadSharp.IO.CadFileFormat](ACadSharp.IO.CadFileFormat.md) — enum
- [ACadSharp.IO.CadObjectData](ACadSharp.IO.CadObjectData.md) — struct
- [ACadSharp.IO.CadReaderBase](ACadSharp.IO.CadReaderBase-1.md) — class
- [ACadSharp.IO.CadReaderConfiguration](ACadSharp.IO.CadReaderConfiguration.md) — class
- [ACadSharp.IO.CadReaderFactory](ACadSharp.IO.CadReaderFactory.md) — class
- [ACadSharp.IO.CadWriterBase](ACadSharp.IO.CadWriterBase-1.md) — class
- [ACadSharp.IO.CadWriterConfiguration](ACadSharp.IO.CadWriterConfiguration.md) — class
- [ACadSharp.IO.DwgReader](ACadSharp.IO.DwgReader.md) — class
- [ACadSharp.IO.DwgReaderConfiguration](ACadSharp.IO.DwgReaderConfiguration.md) — class
- [ACadSharp.IO.DwgWriter](ACadSharp.IO.DwgWriter.md) — class
- [ACadSharp.IO.DwgWriterConfiguration](ACadSharp.IO.DwgWriterConfiguration.md) — class
- [ACadSharp.IO.DxfReader](ACadSharp.IO.DxfReader.md) — class
- [ACadSharp.IO.DxfReaderConfiguration](ACadSharp.IO.DxfReaderConfiguration.md) — class
- [ACadSharp.IO.DxfWriter](ACadSharp.IO.DxfWriter.md) — class
- [ACadSharp.IO.DxfWriterConfiguration](ACadSharp.IO.DxfWriterConfiguration.md) — class
- [ACadSharp.IO.EntityData](ACadSharp.IO.EntityData.md) — struct
- [ACadSharp.IO.ICadReader](ACadSharp.IO.ICadReader.md) — interface
- [ACadSharp.IO.ICadWriter](ACadSharp.IO.ICadWriter.md) — interface
- [ACadSharp.IO.NotificationEventArgs](ACadSharp.IO.NotificationEventArgs.md) — class
- [ACadSharp.IO.NotificationEventHandler](ACadSharp.IO.NotificationEventHandler.md) — delegate
- [ACadSharp.IO.NotificationType](ACadSharp.IO.NotificationType.md) — enum
- [ACadSharp.IO.ProgressEventArgs](ACadSharp.IO.ProgressEventArgs.md) — class
- [ACadSharp.IO.ProgressEventHandler](ACadSharp.IO.ProgressEventHandler.md) — delegate
- [ACadSharp.IO.ReadStage](ACadSharp.IO.ReadStage.md) — enum
- [ACadSharp.IO.ReferenceData](ACadSharp.IO.ReferenceData.md) — struct
- [ACadSharp.IO.SvgConfiguration](ACadSharp.IO.SvgConfiguration.md) — class
- [ACadSharp.IO.SvgWriter](ACadSharp.IO.SvgWriter.md) — class

## ACadSharp.Objects

- [ACadSharp.Objects.AcdbPlaceHolder](ACadSharp.Objects.AcdbPlaceHolder.md) — class
- [ACadSharp.Objects.AecCleanupGroup](ACadSharp.Objects.AecCleanupGroup.md) — class
- [ACadSharp.Objects.AecWallStyle](ACadSharp.Objects.AecWallStyle.md) — class
- [ACadSharp.Objects.AnnotScaleObjectContextData](ACadSharp.Objects.AnnotScaleObjectContextData.md) — class
- [ACadSharp.Objects.AssociativityFlags](ACadSharp.Objects.AssociativityFlags.md) — enum
- [ACadSharp.Objects.AutoTransformMethodFlags](ACadSharp.Objects.AutoTransformMethodFlags.md) — enum
- [ACadSharp.Objects.BlockReferenceObjectContextData](ACadSharp.Objects.BlockReferenceObjectContextData.md) — class
- [ACadSharp.Objects.BlockRepresentationData](ACadSharp.Objects.BlockRepresentationData.md) — class
- [ACadSharp.Objects.BookColor](ACadSharp.Objects.BookColor.md) — class
- [ACadSharp.Objects.CadDictionary](ACadSharp.Objects.CadDictionary.md) — class
- [ACadSharp.Objects.CadDictionaryWithDefault](ACadSharp.Objects.CadDictionaryWithDefault.md) — class
- [ACadSharp.Objects.ColorMethod](ACadSharp.Objects.ColorMethod.md) — enum
- [ACadSharp.Objects.DesignCoordinatesType](ACadSharp.Objects.DesignCoordinatesType.md) — enum
- [ACadSharp.Objects.DictionaryCloningFlags](ACadSharp.Objects.DictionaryCloningFlags.md) — enum
- [ACadSharp.Objects.DictionaryVariable](ACadSharp.Objects.DictionaryVariable.md) — class
- [ACadSharp.Objects.DimensionAssociation](ACadSharp.Objects.DimensionAssociation.md) — class
- [ACadSharp.Objects.DimensionAssociation.OsnapPointRef](ACadSharp.Objects.DimensionAssociation.OsnapPointRef.md) — class
- [ACadSharp.Objects.DynamicBlockPurgePreventer](ACadSharp.Objects.DynamicBlockPurgePreventer.md) — class
- [ACadSharp.Objects.EdgeStyleModel](ACadSharp.Objects.EdgeStyleModel.md) — enum
- [ACadSharp.Objects.EvaluationOptionFlags](ACadSharp.Objects.EvaluationOptionFlags.md) — enum
- [ACadSharp.Objects.EvaluationStatusFlags](ACadSharp.Objects.EvaluationStatusFlags.md) — enum
- [ACadSharp.Objects.FaceColorMode](ACadSharp.Objects.FaceColorMode.md) — enum
- [ACadSharp.Objects.FaceLightingModelType](ACadSharp.Objects.FaceLightingModelType.md) — enum
- [ACadSharp.Objects.FaceLightingQualityType](ACadSharp.Objects.FaceLightingQualityType.md) — enum
- [ACadSharp.Objects.FaceModifierType](ACadSharp.Objects.FaceModifierType.md) — enum
- [ACadSharp.Objects.Field](ACadSharp.Objects.Field.md) — class
- [ACadSharp.Objects.FieldList](ACadSharp.Objects.FieldList.md) — class
- [ACadSharp.Objects.FieldStateFlags](ACadSharp.Objects.FieldStateFlags.md) — enum
- [ACadSharp.Objects.FilingOptionFlags](ACadSharp.Objects.FilingOptionFlags.md) — enum
- [ACadSharp.Objects.Filter](ACadSharp.Objects.Filter.md) — class
- [ACadSharp.Objects.FormattedTableData](ACadSharp.Objects.FormattedTableData.md) — class
- [ACadSharp.Objects.GeoData](ACadSharp.Objects.GeoData.md) — class
- [ACadSharp.Objects.GeoData.GeoMeshFace](ACadSharp.Objects.GeoData.GeoMeshFace.md) — class
- [ACadSharp.Objects.GeoData.GeoMeshPoint](ACadSharp.Objects.GeoData.GeoMeshPoint.md) — class
- [ACadSharp.Objects.GeoDataVersion](ACadSharp.Objects.GeoDataVersion.md) — enum
- [ACadSharp.Objects.Group](ACadSharp.Objects.Group.md) — class
- [ACadSharp.Objects.ImageDefinition](ACadSharp.Objects.ImageDefinition.md) — class
- [ACadSharp.Objects.ImageDefinitionReactor](ACadSharp.Objects.ImageDefinitionReactor.md) — class
- [ACadSharp.Objects.ImageDisplayQuality](ACadSharp.Objects.ImageDisplayQuality.md) — enum
- [ACadSharp.Objects.Layout](ACadSharp.Objects.Layout.md) — class
- [ACadSharp.Objects.LayoutFlags](ACadSharp.Objects.LayoutFlags.md) — enum
- [ACadSharp.Objects.LeaderContentType](ACadSharp.Objects.LeaderContentType.md) — enum
- [ACadSharp.Objects.LeaderDrawOrderType](ACadSharp.Objects.LeaderDrawOrderType.md) — enum
- [ACadSharp.Objects.LeaderLinePropertOverrideFlags](ACadSharp.Objects.LeaderLinePropertOverrideFlags.md) — enum
- [ACadSharp.Objects.LinkedData](ACadSharp.Objects.LinkedData.md) — class
- [ACadSharp.Objects.LinkedTableData](ACadSharp.Objects.LinkedTableData.md) — class
- [ACadSharp.Objects.MLineStyle](ACadSharp.Objects.MLineStyle.md) — class
- [ACadSharp.Objects.MLineStyle.Element](ACadSharp.Objects.MLineStyle.Element.md) — class
- [ACadSharp.Objects.MLineStyleFlags](ACadSharp.Objects.MLineStyleFlags.md) — enum
- [ACadSharp.Objects.MTextAttributeObjectContextData](ACadSharp.Objects.MTextAttributeObjectContextData.md) — class
- [ACadSharp.Objects.MapSource](ACadSharp.Objects.MapSource.md) — enum
- [ACadSharp.Objects.Material](ACadSharp.Objects.Material.md) — class
- [ACadSharp.Objects.MaterialChannelFlags](ACadSharp.Objects.MaterialChannelFlags.md) — enum
- [ACadSharp.Objects.MaterialIlluminationModel](ACadSharp.Objects.MaterialIlluminationModel.md) — enum
- [ACadSharp.Objects.MaterialMode](ACadSharp.Objects.MaterialMode.md) — enum
- [ACadSharp.Objects.MultiLeaderDrawOrderType](ACadSharp.Objects.MultiLeaderDrawOrderType.md) — enum
- [ACadSharp.Objects.MultiLeaderObjectContextData](ACadSharp.Objects.MultiLeaderObjectContextData.md) — class
- [ACadSharp.Objects.MultiLeaderObjectContextData.BreakInfo](ACadSharp.Objects.MultiLeaderObjectContextData.BreakInfo.md) — class
- [ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine](ACadSharp.Objects.MultiLeaderObjectContextData.LeaderLine.md) — class
- [ACadSharp.Objects.MultiLeaderObjectContextData.LeaderRoot](ACadSharp.Objects.MultiLeaderObjectContextData.LeaderRoot.md) — class
- [ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair](ACadSharp.Objects.MultiLeaderObjectContextData.StartEndPointPair.md) — struct
- [ACadSharp.Objects.MultiLeaderStyle](ACadSharp.Objects.MultiLeaderStyle.md) — class
- [ACadSharp.Objects.NonGraphicalObject](ACadSharp.Objects.NonGraphicalObject.md) — class
- [ACadSharp.Objects.ObjectContextData](ACadSharp.Objects.ObjectContextData.md) — class
- [ACadSharp.Objects.ObjectOsnapType](ACadSharp.Objects.ObjectOsnapType.md) — enum
- [ACadSharp.Objects.PaperMargin](ACadSharp.Objects.PaperMargin.md) — struct
- [ACadSharp.Objects.PdfUnderlayDefinition](ACadSharp.Objects.PdfUnderlayDefinition.md) — class
- [ACadSharp.Objects.PlotFlags](ACadSharp.Objects.PlotFlags.md) — enum
- [ACadSharp.Objects.PlotPaperUnits](ACadSharp.Objects.PlotPaperUnits.md) — enum
- [ACadSharp.Objects.PlotRotation](ACadSharp.Objects.PlotRotation.md) — enum
- [ACadSharp.Objects.PlotSettings](ACadSharp.Objects.PlotSettings.md) — class
- [ACadSharp.Objects.PlotType](ACadSharp.Objects.PlotType.md) — enum
- [ACadSharp.Objects.ProjectionMethod](ACadSharp.Objects.ProjectionMethod.md) — enum
- [ACadSharp.Objects.ProxyObject](ACadSharp.Objects.ProxyObject.md) — class
- [ACadSharp.Objects.RasterVariables](ACadSharp.Objects.RasterVariables.md) — class
- [ACadSharp.Objects.ResolutionUnit](ACadSharp.Objects.ResolutionUnit.md) — enum
- [ACadSharp.Objects.RotatedDimensionType](ACadSharp.Objects.RotatedDimensionType.md) — enum
- [ACadSharp.Objects.Scale](ACadSharp.Objects.Scale.md) — class
- [ACadSharp.Objects.ScaleEstimationType](ACadSharp.Objects.ScaleEstimationType.md) — enum
- [ACadSharp.Objects.ScaledType](ACadSharp.Objects.ScaledType.md) — enum
- [ACadSharp.Objects.ShadePlotMode](ACadSharp.Objects.ShadePlotMode.md) — enum
- [ACadSharp.Objects.ShadePlotResolutionMode](ACadSharp.Objects.ShadePlotResolutionMode.md) — enum
- [ACadSharp.Objects.SortEntitiesTable](ACadSharp.Objects.SortEntitiesTable.md) — class
- [ACadSharp.Objects.SortEntitiesTable.Sorter](ACadSharp.Objects.SortEntitiesTable.Sorter.md) — class
- [ACadSharp.Objects.SpatialFilter](ACadSharp.Objects.SpatialFilter.md) — class
- [ACadSharp.Objects.SubentType](ACadSharp.Objects.SubentType.md) — enum
- [ACadSharp.Objects.TableContent](ACadSharp.Objects.TableContent.md) — class
- [ACadSharp.Objects.TableFlowDirectionType](ACadSharp.Objects.TableFlowDirectionType.md) — enum
- [ACadSharp.Objects.TableStyle](ACadSharp.Objects.TableStyle.md) — class
- [ACadSharp.Objects.TableStyle.BorderPropertyFlags](ACadSharp.Objects.TableStyle.BorderPropertyFlags.md) — enum
- [ACadSharp.Objects.TableStyle.BorderType](ACadSharp.Objects.TableStyle.BorderType.md) — enum
- [ACadSharp.Objects.TableStyle.CellAlignmentType](ACadSharp.Objects.TableStyle.CellAlignmentType.md) — enum
- [ACadSharp.Objects.TableStyle.CellBorder](ACadSharp.Objects.TableStyle.CellBorder.md) — class
- [ACadSharp.Objects.TableStyle.CellContentLayoutFlags](ACadSharp.Objects.TableStyle.CellContentLayoutFlags.md) — enum
- [ACadSharp.Objects.TableStyle.CellEdgeFlags](ACadSharp.Objects.TableStyle.CellEdgeFlags.md) — enum
- [ACadSharp.Objects.TableStyle.CellStyle](ACadSharp.Objects.TableStyle.CellStyle.md) — class
- [ACadSharp.Objects.TableStyle.CellStyleClass](ACadSharp.Objects.TableStyle.CellStyleClass.md) — enum
- [ACadSharp.Objects.TableStyle.CellStylePropertyFlags](ACadSharp.Objects.TableStyle.CellStylePropertyFlags.md) — enum
- [ACadSharp.Objects.TableStyle.CellStyleType](ACadSharp.Objects.TableStyle.CellStyleType.md) — enum
- [ACadSharp.Objects.TableStyle.ContentFormat](ACadSharp.Objects.TableStyle.ContentFormat.md) — class
- [ACadSharp.Objects.TableStyle.MarginFlags](ACadSharp.Objects.TableStyle.MarginFlags.md) — enum
- [ACadSharp.Objects.TilingMethod](ACadSharp.Objects.TilingMethod.md) — enum
- [ACadSharp.Objects.UnderlayDefinition](ACadSharp.Objects.UnderlayDefinition.md) — class
- [ACadSharp.Objects.UnknownNonGraphicalObject](ACadSharp.Objects.UnknownNonGraphicalObject.md) — class
- [ACadSharp.Objects.VisualStyle](ACadSharp.Objects.VisualStyle.md) — class
- [ACadSharp.Objects.WipeoutFrameType](ACadSharp.Objects.WipeoutFrameType.md) — enum
- [ACadSharp.Objects.WipeoutVariables](ACadSharp.Objects.WipeoutVariables.md) — class
- [ACadSharp.Objects.XRecord](ACadSharp.Objects.XRecord.md) — class
- [ACadSharp.Objects.XRecord.Entry](ACadSharp.Objects.XRecord.Entry.md) — class

## ACadSharp.Objects.AEC

- [ACadSharp.Objects.AEC.AecBinRecord](ACadSharp.Objects.AEC.AecBinRecord.md) — class

## ACadSharp.Objects.Collections

- [ACadSharp.Objects.Collections.ColorCollection](ACadSharp.Objects.Collections.ColorCollection.md) — class
- [ACadSharp.Objects.Collections.DictionaryVariableCollection](ACadSharp.Objects.Collections.DictionaryVariableCollection.md) — class
- [ACadSharp.Objects.Collections.GroupCollection](ACadSharp.Objects.Collections.GroupCollection.md) — class
- [ACadSharp.Objects.Collections.ImageDefinitionCollection](ACadSharp.Objects.Collections.ImageDefinitionCollection.md) — class
- [ACadSharp.Objects.Collections.LayoutCollection](ACadSharp.Objects.Collections.LayoutCollection.md) — class
- [ACadSharp.Objects.Collections.MLeaderStyleCollection](ACadSharp.Objects.Collections.MLeaderStyleCollection.md) — class
- [ACadSharp.Objects.Collections.MLineStyleCollection](ACadSharp.Objects.Collections.MLineStyleCollection.md) — class
- [ACadSharp.Objects.Collections.MaterialCollection](ACadSharp.Objects.Collections.MaterialCollection.md) — class
- [ACadSharp.Objects.Collections.ObjectDictionaryCollection](ACadSharp.Objects.Collections.ObjectDictionaryCollection-1.md) — class
- [ACadSharp.Objects.Collections.PdfDefinitionCollection](ACadSharp.Objects.Collections.PdfDefinitionCollection.md) — class
- [ACadSharp.Objects.Collections.ScaleCollection](ACadSharp.Objects.Collections.ScaleCollection.md) — class
- [ACadSharp.Objects.Collections.TableStyleCollection](ACadSharp.Objects.Collections.TableStyleCollection.md) — class

## ACadSharp.Objects.Evaluations

- [ACadSharp.Objects.Evaluations.Block1PtParameter](ACadSharp.Objects.Evaluations.Block1PtParameter.md) — class
- [ACadSharp.Objects.Evaluations.Block2PtParameter](ACadSharp.Objects.Evaluations.Block2PtParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockAction](ACadSharp.Objects.Evaluations.BlockAction.md) — class
- [ACadSharp.Objects.Evaluations.BlockActionBasePt](ACadSharp.Objects.Evaluations.BlockActionBasePt.md) — class
- [ACadSharp.Objects.Evaluations.BlockAlignmentGrip](ACadSharp.Objects.Evaluations.BlockAlignmentGrip.md) — class
- [ACadSharp.Objects.Evaluations.BlockAlignmentParameter](ACadSharp.Objects.Evaluations.BlockAlignmentParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockArrayAction](ACadSharp.Objects.Evaluations.BlockArrayAction.md) — class
- [ACadSharp.Objects.Evaluations.BlockBasePointParameter](ACadSharp.Objects.Evaluations.BlockBasePointParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockElement](ACadSharp.Objects.Evaluations.BlockElement.md) — class
- [ACadSharp.Objects.Evaluations.BlockFlipAction](ACadSharp.Objects.Evaluations.BlockFlipAction.md) — class
- [ACadSharp.Objects.Evaluations.BlockFlipGrip](ACadSharp.Objects.Evaluations.BlockFlipGrip.md) — class
- [ACadSharp.Objects.Evaluations.BlockFlipParameter](ACadSharp.Objects.Evaluations.BlockFlipParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockGrip](ACadSharp.Objects.Evaluations.BlockGrip.md) — class
- [ACadSharp.Objects.Evaluations.BlockGripLocationComponent](ACadSharp.Objects.Evaluations.BlockGripLocationComponent.md) — class
- [ACadSharp.Objects.Evaluations.BlockLinearGrip](ACadSharp.Objects.Evaluations.BlockLinearGrip.md) — class
- [ACadSharp.Objects.Evaluations.BlockLinearParameter](ACadSharp.Objects.Evaluations.BlockLinearParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockLookupAction](ACadSharp.Objects.Evaluations.BlockLookupAction.md) — class
- [ACadSharp.Objects.Evaluations.BlockLookupAction.ColumnData](ACadSharp.Objects.Evaluations.BlockLookupAction.ColumnData.md) — class
- [ACadSharp.Objects.Evaluations.BlockLookupGrip](ACadSharp.Objects.Evaluations.BlockLookupGrip.md) — class
- [ACadSharp.Objects.Evaluations.BlockLookupParameter](ACadSharp.Objects.Evaluations.BlockLookupParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockMoveAction](ACadSharp.Objects.Evaluations.BlockMoveAction.md) — class
- [ACadSharp.Objects.Evaluations.BlockParameter](ACadSharp.Objects.Evaluations.BlockParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockPointParameter](ACadSharp.Objects.Evaluations.BlockPointParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockPolarGrip](ACadSharp.Objects.Evaluations.BlockPolarGrip.md) — class
- [ACadSharp.Objects.Evaluations.BlockPolarParameter](ACadSharp.Objects.Evaluations.BlockPolarParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockPolarStretchAction](ACadSharp.Objects.Evaluations.BlockPolarStretchAction.md) — class
- [ACadSharp.Objects.Evaluations.BlockRotationAction](ACadSharp.Objects.Evaluations.BlockRotationAction.md) — class
- [ACadSharp.Objects.Evaluations.BlockRotationGrip](ACadSharp.Objects.Evaluations.BlockRotationGrip.md) — class
- [ACadSharp.Objects.Evaluations.BlockRotationParameter](ACadSharp.Objects.Evaluations.BlockRotationParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockScaleAction](ACadSharp.Objects.Evaluations.BlockScaleAction.md) — class
- [ACadSharp.Objects.Evaluations.BlockStretchAction](ACadSharp.Objects.Evaluations.BlockStretchAction.md) — class
- [ACadSharp.Objects.Evaluations.BlockVisibilityGrip](ACadSharp.Objects.Evaluations.BlockVisibilityGrip.md) — class
- [ACadSharp.Objects.Evaluations.BlockVisibilityParameter](ACadSharp.Objects.Evaluations.BlockVisibilityParameter.md) — class
- [ACadSharp.Objects.Evaluations.BlockVisibilityParameter.State](ACadSharp.Objects.Evaluations.BlockVisibilityParameter.State.md) — class
- [ACadSharp.Objects.Evaluations.BlockXYGrip](ACadSharp.Objects.Evaluations.BlockXYGrip.md) — class
- [ACadSharp.Objects.Evaluations.BlockXYParameter](ACadSharp.Objects.Evaluations.BlockXYParameter.md) — class
- [ACadSharp.Objects.Evaluations.DxfValuePair](ACadSharp.Objects.Evaluations.DxfValuePair.md) — class
- [ACadSharp.Objects.Evaluations.EvalConnection](ACadSharp.Objects.Evaluations.EvalConnection.md) — class
- [ACadSharp.Objects.Evaluations.EvalParameterProperty](ACadSharp.Objects.Evaluations.EvalParameterProperty.md) — class
- [ACadSharp.Objects.Evaluations.EvaluationExpression](ACadSharp.Objects.Evaluations.EvaluationExpression.md) — class
- [ACadSharp.Objects.Evaluations.EvaluationGraph](ACadSharp.Objects.Evaluations.EvaluationGraph.md) — class
- [ACadSharp.Objects.Evaluations.EvaluationGraph.Edge](ACadSharp.Objects.Evaluations.EvaluationGraph.Edge.md) — class
- [ACadSharp.Objects.Evaluations.EvaluationGraph.Node](ACadSharp.Objects.Evaluations.EvaluationGraph.Node.md) — class
- [ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags](ACadSharp.Objects.Evaluations.EvaluationGraph.NodeFlags.md) — enum
- [ACadSharp.Objects.Evaluations.LinearParameterBaseLocation](ACadSharp.Objects.Evaluations.LinearParameterBaseLocation.md) — enum
- [ACadSharp.Objects.Evaluations.ParameterValueSet](ACadSharp.Objects.Evaluations.ParameterValueSet.md) — class
- [ACadSharp.Objects.Evaluations.ParameterValueSetType](ACadSharp.Objects.Evaluations.ParameterValueSetType.md) — enum
- [ACadSharp.Objects.Evaluations.StretchActionBase](ACadSharp.Objects.Evaluations.StretchActionBase.md) — class
- [ACadSharp.Objects.Evaluations.StretchEntityBind](ACadSharp.Objects.Evaluations.StretchEntityBind.md) — struct
- [ACadSharp.Objects.Evaluations.StretchNode](ACadSharp.Objects.Evaluations.StretchNode.md) — struct

## ACadSharp.Prototype1b

- [ACadSharp.Prototype1b.DataBlobReference](ACadSharp.Prototype1b.DataBlobReference.md) — class
- [ACadSharp.Prototype1b.DataEntry](ACadSharp.Prototype1b.DataEntry.md) — class
- [ACadSharp.Prototype1b.DataHeader](ACadSharp.Prototype1b.DataHeader.md) — class
- [ACadSharp.Prototype1b.DataIndex](ACadSharp.Prototype1b.DataIndex.md) — class
- [ACadSharp.Prototype1b.DataIndexEntry](ACadSharp.Prototype1b.DataIndexEntry.md) — class
- [ACadSharp.Prototype1b.DataIndexEntryPointer](ACadSharp.Prototype1b.DataIndexEntryPointer.md) — class
- [ACadSharp.Prototype1b.DataStorage](ACadSharp.Prototype1b.DataStorage.md) — class
- [ACadSharp.Prototype1b.DataStoragePointers](ACadSharp.Prototype1b.DataStoragePointers.md) — class
- [ACadSharp.Prototype1b.DataValue](ACadSharp.Prototype1b.DataValue.md) — class
- [ACadSharp.Prototype1b.FileHeader](ACadSharp.Prototype1b.FileHeader.md) — class
- [ACadSharp.Prototype1b.FreeSpaceArea](ACadSharp.Prototype1b.FreeSpaceArea.md) — class
- [ACadSharp.Prototype1b.PreviousSave](ACadSharp.Prototype1b.PreviousSave.md) — class
- [ACadSharp.Prototype1b.Schema](ACadSharp.Prototype1b.Schema.md) — class
- [ACadSharp.Prototype1b.SchemaIndex](ACadSharp.Prototype1b.SchemaIndex.md) — class
- [ACadSharp.Prototype1b.SchemaProperty](ACadSharp.Prototype1b.SchemaProperty.md) — class
- [ACadSharp.Prototype1b.SchemaPropertyPointer](ACadSharp.Prototype1b.SchemaPropertyPointer.md) — class
- [ACadSharp.Prototype1b.SchemaSearch](ACadSharp.Prototype1b.SchemaSearch.md) — class
- [ACadSharp.Prototype1b.SchemaSearchEntry](ACadSharp.Prototype1b.SchemaSearchEntry.md) — class
- [ACadSharp.Prototype1b.SchemaUnknownProperty](ACadSharp.Prototype1b.SchemaUnknownProperty.md) — class
- [ACadSharp.Prototype1b.SearchEntryObject](ACadSharp.Prototype1b.SearchEntryObject.md) — class
- [ACadSharp.Prototype1b.SegmentHeader](ACadSharp.Prototype1b.SegmentHeader.md) — class
- [ACadSharp.Prototype1b.SegmentIndexEntry](ACadSharp.Prototype1b.SegmentIndexEntry.md) — class

## ACadSharp.Prototype1b.Segments

- [ACadSharp.Prototype1b.Segments.Blob01](ACadSharp.Prototype1b.Segments.Blob01.md) — class
- [ACadSharp.Prototype1b.Segments.DataField](ACadSharp.Prototype1b.Segments.DataField.md) — class
- [ACadSharp.Prototype1b.Segments.FreeSpace](ACadSharp.Prototype1b.Segments.FreeSpace.md) — class
- [ACadSharp.Prototype1b.Segments.IPrototype1bSegment](ACadSharp.Prototype1b.Segments.IPrototype1bSegment.md) — interface
- [ACadSharp.Prototype1b.Segments.SchemaData](ACadSharp.Prototype1b.Segments.SchemaData.md) — class
- [ACadSharp.Prototype1b.Segments.SegmentIndex](ACadSharp.Prototype1b.Segments.SegmentIndex.md) — class

## ACadSharp.Tables

- [ACadSharp.Tables.AngularZeroHandling](ACadSharp.Tables.AngularZeroHandling.md) — enum
- [ACadSharp.Tables.AppId](ACadSharp.Tables.AppId.md) — class
- [ACadSharp.Tables.ArcLengthSymbolPosition](ACadSharp.Tables.ArcLengthSymbolPosition.md) — enum
- [ACadSharp.Tables.BlockRecord](ACadSharp.Tables.BlockRecord.md) — class
- [ACadSharp.Tables.DefaultLightingType](ACadSharp.Tables.DefaultLightingType.md) — enum
- [ACadSharp.Tables.DimensionStyle](ACadSharp.Tables.DimensionStyle.md) — class
- [ACadSharp.Tables.DimensionTextBackgroundFillMode](ACadSharp.Tables.DimensionTextBackgroundFillMode.md) — enum
- [ACadSharp.Tables.DimensionTextHorizontalAlignment](ACadSharp.Tables.DimensionTextHorizontalAlignment.md) — enum
- [ACadSharp.Tables.DimensionTextVerticalAlignment](ACadSharp.Tables.DimensionTextVerticalAlignment.md) — enum
- [ACadSharp.Tables.EntryFlags](ACadSharp.Tables.EntryFlags.md) — enum
- [ACadSharp.Tables.FontFlags](ACadSharp.Tables.FontFlags.md) — enum
- [ACadSharp.Tables.FractionFormat](ACadSharp.Tables.FractionFormat.md) — enum
- [ACadSharp.Tables.GridFlags](ACadSharp.Tables.GridFlags.md) — enum
- [ACadSharp.Tables.Layer](ACadSharp.Tables.Layer.md) — class
- [ACadSharp.Tables.LayerFlags](ACadSharp.Tables.LayerFlags.md) — enum
- [ACadSharp.Tables.LineType](ACadSharp.Tables.LineType.md) — class
- [ACadSharp.Tables.LineType.Segment](ACadSharp.Tables.LineType.Segment.md) — class
- [ACadSharp.Tables.LineTypeShapeFlags](ACadSharp.Tables.LineTypeShapeFlags.md) — enum
- [ACadSharp.Tables.StandardFlags](ACadSharp.Tables.StandardFlags.md) — enum
- [ACadSharp.Tables.StyleFlags](ACadSharp.Tables.StyleFlags.md) — enum
- [ACadSharp.Tables.TableEntry](ACadSharp.Tables.TableEntry.md) — class
- [ACadSharp.Tables.TextArrowFitType](ACadSharp.Tables.TextArrowFitType.md) — enum
- [ACadSharp.Tables.TextDirection](ACadSharp.Tables.TextDirection.md) — enum
- [ACadSharp.Tables.TextMovement](ACadSharp.Tables.TextMovement.md) — enum
- [ACadSharp.Tables.TextStyle](ACadSharp.Tables.TextStyle.md) — class
- [ACadSharp.Tables.ToleranceAlignment](ACadSharp.Tables.ToleranceAlignment.md) — enum
- [ACadSharp.Tables.UCS](ACadSharp.Tables.UCS.md) — class
- [ACadSharp.Tables.UscIconType](ACadSharp.Tables.UscIconType.md) — enum
- [ACadSharp.Tables.VPort](ACadSharp.Tables.VPort.md) — class
- [ACadSharp.Tables.View](ACadSharp.Tables.View.md) — class
- [ACadSharp.Tables.ViewModeType](ACadSharp.Tables.ViewModeType.md) — enum
- [ACadSharp.Tables.ZeroHandling](ACadSharp.Tables.ZeroHandling.md) — enum

## ACadSharp.Tables.Collections

- [ACadSharp.Tables.Collections.AppIdsTable](ACadSharp.Tables.Collections.AppIdsTable.md) — class
- [ACadSharp.Tables.Collections.BlockRecordsTable](ACadSharp.Tables.Collections.BlockRecordsTable.md) — class
- [ACadSharp.Tables.Collections.DimensionStylesTable](ACadSharp.Tables.Collections.DimensionStylesTable.md) — class
- [ACadSharp.Tables.Collections.ITable](ACadSharp.Tables.Collections.ITable.md) — interface
- [ACadSharp.Tables.Collections.LayersTable](ACadSharp.Tables.Collections.LayersTable.md) — class
- [ACadSharp.Tables.Collections.LineTypesTable](ACadSharp.Tables.Collections.LineTypesTable.md) — class
- [ACadSharp.Tables.Collections.Table](ACadSharp.Tables.Collections.Table-1.md) — class
- [ACadSharp.Tables.Collections.TextStylesTable](ACadSharp.Tables.Collections.TextStylesTable.md) — class
- [ACadSharp.Tables.Collections.UCSTable](ACadSharp.Tables.Collections.UCSTable.md) — class
- [ACadSharp.Tables.Collections.VPortsTable](ACadSharp.Tables.Collections.VPortsTable.md) — class
- [ACadSharp.Tables.Collections.ViewsTable](ACadSharp.Tables.Collections.ViewsTable.md) — class

## ACadSharp.Text

- [ACadSharp.Text.TextProcessor](ACadSharp.Text.TextProcessor.md) — class

## ACadSharp.Types.Units

- [ACadSharp.Types.Units.AngularDirection](ACadSharp.Types.Units.AngularDirection.md) — enum
- [ACadSharp.Types.Units.AngularUnitFormat](ACadSharp.Types.Units.AngularUnitFormat.md) — enum
- [ACadSharp.Types.Units.ImageUnits](ACadSharp.Types.Units.ImageUnits.md) — enum
- [ACadSharp.Types.Units.LinearUnitFormat](ACadSharp.Types.Units.LinearUnitFormat.md) — enum
- [ACadSharp.Types.Units.UnitStyleFormat](ACadSharp.Types.Units.UnitStyleFormat.md) — class
- [ACadSharp.Types.Units.UnitsType](ACadSharp.Types.Units.UnitsType.md) — enum

## ACadSharp.XData

- [ACadSharp.XData.ExtendedData](ACadSharp.XData.ExtendedData.md) — class
- [ACadSharp.XData.ExtendedDataBinaryChunk](ACadSharp.XData.ExtendedDataBinaryChunk.md) — class
- [ACadSharp.XData.ExtendedDataControlString](ACadSharp.XData.ExtendedDataControlString.md) — class
- [ACadSharp.XData.ExtendedDataCoordinate](ACadSharp.XData.ExtendedDataCoordinate.md) — class
- [ACadSharp.XData.ExtendedDataDictionary](ACadSharp.XData.ExtendedDataDictionary.md) — class
- [ACadSharp.XData.ExtendedDataDirection](ACadSharp.XData.ExtendedDataDirection.md) — class
- [ACadSharp.XData.ExtendedDataDisplacement](ACadSharp.XData.ExtendedDataDisplacement.md) — class
- [ACadSharp.XData.ExtendedDataDistance](ACadSharp.XData.ExtendedDataDistance.md) — class
- [ACadSharp.XData.ExtendedDataHandle](ACadSharp.XData.ExtendedDataHandle.md) — class
- [ACadSharp.XData.ExtendedDataInteger16](ACadSharp.XData.ExtendedDataInteger16.md) — class
- [ACadSharp.XData.ExtendedDataInteger32](ACadSharp.XData.ExtendedDataInteger32.md) — class
- [ACadSharp.XData.ExtendedDataLayer](ACadSharp.XData.ExtendedDataLayer.md) — class
- [ACadSharp.XData.ExtendedDataReal](ACadSharp.XData.ExtendedDataReal.md) — class
- [ACadSharp.XData.ExtendedDataRecord](ACadSharp.XData.ExtendedDataRecord.md) — class
- [ACadSharp.XData.ExtendedDataRecord](ACadSharp.XData.ExtendedDataRecord-1.md) — class
- [ACadSharp.XData.ExtendedDataReference](ACadSharp.XData.ExtendedDataReference-1.md) — class
- [ACadSharp.XData.ExtendedDataScale](ACadSharp.XData.ExtendedDataScale.md) — class
- [ACadSharp.XData.ExtendedDataString](ACadSharp.XData.ExtendedDataString.md) — class
- [ACadSharp.XData.ExtendedDataWorldCoordinate](ACadSharp.XData.ExtendedDataWorldCoordinate.md) — class
- [ACadSharp.XData.IExtendedDataHandleReference](ACadSharp.XData.IExtendedDataHandleReference.md) — interface

## CSMath

- [CSMath.BoundingBox](CSMath.BoundingBox.md) — struct
- [CSMath.BoundingBoxExtent](CSMath.BoundingBoxExtent.md) — enum
- [CSMath.IVector](CSMath.IVector.md) — interface
- [CSMath.MathHelper](CSMath.MathHelper.md) — class
- [CSMath.Matrix3](CSMath.Matrix3.md) — struct
- [CSMath.Matrix4](CSMath.Matrix4.md) — struct
- [CSMath.Quaternion](CSMath.Quaternion.md) — struct
- [CSMath.Transform](CSMath.Transform.md) — class
- [CSMath.XY](CSMath.XY.md) — struct
- [CSMath.XYZ](CSMath.XYZ.md) — struct
- [CSMath.XYZM](CSMath.XYZM.md) — struct

## CSMath.Extensions

- [CSMath.Extensions.DoubleExtensions](CSMath.Extensions.DoubleExtensions.md) — class
- [CSMath.Extensions.IntExtensions](CSMath.Extensions.IntExtensions.md) — class
- [CSMath.Extensions.VectorExtensions](CSMath.Extensions.VectorExtensions.md) — class

## CSMath.Geometry

- [CSMath.Geometry.Arc2D](CSMath.Geometry.Arc2D.md) — struct
- [CSMath.Geometry.Circle2D](CSMath.Geometry.Circle2D.md) — struct
- [CSMath.Geometry.CurveExtensions](CSMath.Geometry.CurveExtensions.md) — class
- [CSMath.Geometry.ICurve](CSMath.Geometry.ICurve.md) — interface
- [CSMath.Geometry.ILine](CSMath.Geometry.ILine-1.md) — interface
- [CSMath.Geometry.Line2D](CSMath.Geometry.Line2D.md) — struct
- [CSMath.Geometry.Line3D](CSMath.Geometry.Line3D.md) — struct
- [CSMath.Geometry.LineExtensions](CSMath.Geometry.LineExtensions.md) — class
- [CSMath.Geometry.Segment2D](CSMath.Geometry.Segment2D.md) — struct
- [CSMath.Geometry.Segment3D](CSMath.Geometry.Segment3D.md) — struct

## CSUtilities.Attributes

- [CSUtilities.Attributes.StringValueAttribute](CSUtilities.Attributes.StringValueAttribute.md) — class

## CSUtilities.Extensions

- [CSUtilities.Extensions.IDictionaryExtension](CSUtilities.Extensions.IDictionaryExtension.md) — class
