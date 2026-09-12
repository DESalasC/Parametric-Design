# T_GH_IO_Serialization_GH_IReader

﻿ GH\_IReader Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Properties](../html/Properties_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Properties")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReader Interface |

Provides access to a subset of GH\_Chunk methods used for reading archives.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface GH_IReader : GH_IChunk, 
	GH_IBinarySupport, GH_IXmlSupport
```

```
Public Interface GH_IReader
	Inherits GH_IChunk, GH_IBinarySupport, GH_IXmlSupport
```

AddLanguageTabSet("ID0EBCA");

The GH\_IReader type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Archive](P_GH_IO_Serialization_GH_IChunk_Archive.htm) | Gets a pointer to the archive that owns the Root of the tree this chunk belongs to. (Inherited from [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).) |
| Public property | [ArchiveLocation](P_GH_IO_Serialization_GH_IChunk_ArchiveLocation.htm) | Gets a string representing the URI with which the archive is associated. The location may be a null string. (Inherited from [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).) |
| Public property | [ChunkCount](P_GH_IO_Serialization_GH_IChunk_ChunkCount.htm) | Gets the number of child chunks contained in this chunk. The set of all child chunks is referred to as a 'litter'. (Inherited from [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).) |
| Public property | [Chunks](P_GH_IO_Serialization_GH_IChunk_Chunks.htm) | Gets a pointer to the internal list of child chunks. Do not access this list unless you know what you are doing. (Inherited from [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).) |
| Public property | [Index](P_GH_IO_Serialization_GH_IChunk_Index.htm) | Gets the index of this chunk. The index is set by the owner of this chunk. Indices smaller than zero imply no index has been set. The combination of name+index is always unique among a set of chunks in the same litter. (Inherited from [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).) |
| Public property | [ItemCount](P_GH_IO_Serialization_GH_IChunk_ItemCount.htm) | Gets the number of items contained in this chunk. (Inherited from [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).) |
| Public property | [Items](P_GH_IO_Serialization_GH_IChunk_Items.htm) | Gets a pointer to the internal list of items. Do not access this list unless you know what you are doing. (Inherited from [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).) |
| Public property | [Name](P_GH_IO_Serialization_GH_IChunk_Name.htm) | Gets the name of this chunk. The name is set by the owner of this chunk. Names must be at least 1 character long. The combination of name+index is always unique among a set of chunks in a single litter. (Inherited from [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddMessage](M_GH_IO_Serialization_GH_IChunk_AddMessage.htm) | Log a new message with the top-level archive. Messages are collected during read/write operations, and can be displayed to the user upon completion using GH\_Archive.ShowMessageLog(). (Inherited from [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).) |
| Public method | [ChunkExists(String)](M_GH_IO_Serialization_GH_IReader_ChunkExists.htm) | Checks whether a chunk with the specified name exists in the litter. Only chunks without index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [ChunkExists(String, Int32)](M_GH_IO_Serialization_GH_IReader_ChunkExists_1.htm) | Checks whether a chunk with the specified name and index exists in the litter. Only chunks with index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [FindChunk(String)](M_GH_IO_Serialization_GH_IReader_FindChunk.htm) | Finds the first chunk in the litter that matches the given name. Only chunks without index qualifiers are considered. |
| Public method | [FindChunk(String, Int32)](M_GH_IO_Serialization_GH_IReader_FindChunk_1.htm) | Finds the first chunk in the list that matches the given name and index. Only chunks with index qualifiers are considered. |
| Public method | [FindItem(String)](M_GH_IO_Serialization_GH_IReader_FindItem.htm) | Finds the first item that matches the given name. Only items without index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [FindItem(String, Int32)](M_GH_IO_Serialization_GH_IReader_FindItem_1.htm) | Finds the first item that matches the given name and index. Only items with index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [GetBoolean(String)](M_GH_IO_Serialization_GH_IReader_GetBoolean.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetBoolean(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetBoolean_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetBoundingBox(String)](M_GH_IO_Serialization_GH_IReader_GetBoundingBox.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetBoundingBox(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetBoundingBox_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetByte(String)](M_GH_IO_Serialization_GH_IReader_GetByte.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetByte(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetByte_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetByteArray(String)](M_GH_IO_Serialization_GH_IReader_GetByteArray.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetByteArray(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetByteArray_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDate(String)](M_GH_IO_Serialization_GH_IReader_GetDate.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDate(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDate_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDecimal(String)](M_GH_IO_Serialization_GH_IReader_GetDecimal.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDecimal(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDecimal_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDouble(String)](M_GH_IO_Serialization_GH_IReader_GetDouble.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDouble(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDouble_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDoubleArray(String)](M_GH_IO_Serialization_GH_IReader_GetDoubleArray.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDoubleArray(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDoubleArray_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingBitmap(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingBitmap.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingBitmap(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingBitmap_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingColor(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingColor.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingColor(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingColor_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingPoint(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingPoint.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingPoint(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingPoint_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingPointF(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingPointF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingPointF(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingPointF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingRectangle(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingRectangle.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingRectangle(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingRectangle_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingRectangleF(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingRectangleF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingRectangleF(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingRectangleF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingSize(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingSize.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingSize(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingSize_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingSizeF(String)](M_GH_IO_Serialization_GH_IReader_GetDrawingSizeF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingSizeF(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingSizeF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetGuid(String)](M_GH_IO_Serialization_GH_IReader_GetGuid.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetGuid(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetGuid_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetInt32(String)](M_GH_IO_Serialization_GH_IReader_GetInt32.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetInt32(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetInt32_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetInt64(String)](M_GH_IO_Serialization_GH_IReader_GetInt64.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetInt64(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetInt64_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetInterval1D(String)](M_GH_IO_Serialization_GH_IReader_GetInterval1D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetInterval1D(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetInterval1D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetInterval2D(String)](M_GH_IO_Serialization_GH_IReader_GetInterval2D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetInterval2D(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetInterval2D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetLine(String)](M_GH_IO_Serialization_GH_IReader_GetLine.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetLine(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetLine_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetPath(String, String)](M_GH_IO_Serialization_GH_IReader_GetPath_1.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetPath(String, Int32, String)](M_GH_IO_Serialization_GH_IReader_GetPath.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetPlane(String)](M_GH_IO_Serialization_GH_IReader_GetPlane.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetPlane(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetPlane_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetPoint2D(String)](M_GH_IO_Serialization_GH_IReader_GetPoint2D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetPoint2D(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetPoint2D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetPoint3D(String)](M_GH_IO_Serialization_GH_IReader_GetPoint3D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetPoint3D(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetPoint3D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetPoint4D(String)](M_GH_IO_Serialization_GH_IReader_GetPoint4D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetPoint4D(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetPoint4D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetSingle(String)](M_GH_IO_Serialization_GH_IReader_GetSingle.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetSingle(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetSingle_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetString(String)](M_GH_IO_Serialization_GH_IReader_GetString.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetString(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetString_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetVersion(String)](M_GH_IO_Serialization_GH_IReader_GetVersion.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetVersion(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetVersion_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [ItemExists(String)](M_GH_IO_Serialization_GH_IReader_ItemExists.htm) | Checks whether an item with the specified name exists. Only items without index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [ItemExists(String, Int32)](M_GH_IO_Serialization_GH_IReader_ItemExists_1.htm) | Checks whether an item with the specified name and index exists. Only items with index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [Read(BinaryReader)](M_GH_IO_Serialization_GH_IBinarySupport_Read.htm) | Called when an object is required to deserialize itself. (Inherited from [GH\_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm).) |
| Public method | [Read(XmlNode)](M_GH_IO_Serialization_GH_IXmlSupport_Read.htm) | Called when an object is required to deserialize itself. (Inherited from [GH\_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm).) |
| Public method | [TryGetBoolean(String, BooleanAddLanguageSpecificTextSet("LST82BCA545\_0?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetBoolean.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetBoolean(String, Int32, BooleanAddLanguageSpecificTextSet("LST82BCA545\_1?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetBoolean_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetBoundingBox(String, GH\_BoundingBoxAddLanguageSpecificTextSet("LST82BCA545\_2?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetBoundingBox.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetBoundingBox(String, Int32, GH\_BoundingBoxAddLanguageSpecificTextSet("LST82BCA545\_3?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetBoundingBox_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetByte(String, ByteAddLanguageSpecificTextSet("LST82BCA545\_4?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetByte.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetByte(String, Int32, ByteAddLanguageSpecificTextSet("LST82BCA545\_5?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetByte_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDate(String, DateTimeAddLanguageSpecificTextSet("LST82BCA545\_6?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDate.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDate(String, Int32, DateTimeAddLanguageSpecificTextSet("LST82BCA545\_7?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDate_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDecimal(String, DecimalAddLanguageSpecificTextSet("LST82BCA545\_8?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDecimal.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDecimal(String, Int32, DecimalAddLanguageSpecificTextSet("LST82BCA545\_9?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDecimal_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDouble(String, DoubleAddLanguageSpecificTextSet("LST82BCA545\_10?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDouble.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDouble(String, Int32, DoubleAddLanguageSpecificTextSet("LST82BCA545\_11?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDouble_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingColor(String, ColorAddLanguageSpecificTextSet("LST82BCA545\_12?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingColor.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingColor(String, Int32, ColorAddLanguageSpecificTextSet("LST82BCA545\_13?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingColor_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingPoint(String, PointAddLanguageSpecificTextSet("LST82BCA545\_14?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPoint.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingPoint(String, Int32, PointAddLanguageSpecificTextSet("LST82BCA545\_15?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPoint_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingPointF(String, PointFAddLanguageSpecificTextSet("LST82BCA545\_16?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPointF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingPointF(String, Int32, PointFAddLanguageSpecificTextSet("LST82BCA545\_17?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPointF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingRectangle(String, RectangleAddLanguageSpecificTextSet("LST82BCA545\_18?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingRectangle.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingRectangle(String, Int32, RectangleAddLanguageSpecificTextSet("LST82BCA545\_19?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingRectangle_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingRectangleF(String, RectangleFAddLanguageSpecificTextSet("LST82BCA545\_20?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingRectangleF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingRectangleF(String, Int32, RectangleFAddLanguageSpecificTextSet("LST82BCA545\_21?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingRectangleF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingSize(String, SizeAddLanguageSpecificTextSet("LST82BCA545\_22?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingSize.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingSize(String, Int32, SizeAddLanguageSpecificTextSet("LST82BCA545\_23?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingSize_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingSizeF(String, SizeFAddLanguageSpecificTextSet("LST82BCA545\_24?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingSizeF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingSizeF(String, Int32, SizeFAddLanguageSpecificTextSet("LST82BCA545\_25?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingSizeF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetGuid(String, GuidAddLanguageSpecificTextSet("LST82BCA545\_26?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetGuid.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetGuid(String, Int32, GuidAddLanguageSpecificTextSet("LST82BCA545\_27?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetGuid_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetInt32(String, Int32AddLanguageSpecificTextSet("LST82BCA545\_28?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetInt32_1.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetInt32(String, Int32, Int32AddLanguageSpecificTextSet("LST82BCA545\_29?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetInt32.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetInt64(String, Int64AddLanguageSpecificTextSet("LST82BCA545\_30?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetInt64_1.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetInt64(String, Int32, Int64AddLanguageSpecificTextSet("LST82BCA545\_31?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetInt64.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetInterval1D(String, GH\_Interval1DAddLanguageSpecificTextSet("LST82BCA545\_32?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetInterval1D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetInterval1D(String, Int32, GH\_Interval1DAddLanguageSpecificTextSet("LST82BCA545\_33?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetInterval1D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetInterval2D(String, GH\_Interval2DAddLanguageSpecificTextSet("LST82BCA545\_34?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetInterval2D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetInterval2D(String, Int32, GH\_Interval2DAddLanguageSpecificTextSet("LST82BCA545\_35?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetInterval2D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetLine(String, GH\_LineAddLanguageSpecificTextSet("LST82BCA545\_36?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetLine.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetLine(String, Int32, GH\_LineAddLanguageSpecificTextSet("LST82BCA545\_37?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetLine_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetPlane(String, GH\_PlaneAddLanguageSpecificTextSet("LST82BCA545\_38?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetPlane.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetPlane(String, Int32, GH\_PlaneAddLanguageSpecificTextSet("LST82BCA545\_39?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetPlane_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint2D(String, GH\_Point2DAddLanguageSpecificTextSet("LST82BCA545\_40?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetPoint2D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint2D(String, Int32, GH\_Point2DAddLanguageSpecificTextSet("LST82BCA545\_41?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetPoint2D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint3D(String, GH\_Point3DAddLanguageSpecificTextSet("LST82BCA545\_42?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetPoint3D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint3D(String, Int32, GH\_Point3DAddLanguageSpecificTextSet("LST82BCA545\_43?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetPoint3D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint4D(String, GH\_Point4DAddLanguageSpecificTextSet("LST82BCA545\_44?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetPoint4D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint4D(String, Int32, GH\_Point4DAddLanguageSpecificTextSet("LST82BCA545\_45?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetPoint4D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetSingle(String, SingleAddLanguageSpecificTextSet("LST82BCA545\_46?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetSingle_1.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetSingle(String, Int32, SingleAddLanguageSpecificTextSet("LST82BCA545\_47?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetSingle.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetString(String, StringAddLanguageSpecificTextSet("LST82BCA545\_48?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetString_1.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetString(String, Int32, StringAddLanguageSpecificTextSet("LST82BCA545\_49?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetString.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetVersion(String, GH\_VersionAddLanguageSpecificTextSet("LST82BCA545\_50?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetVersion.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetVersion(String, Int32, GH\_VersionAddLanguageSpecificTextSet("LST82BCA545\_51?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetVersion_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [Write(BinaryWriter)](M_GH_IO_Serialization_GH_IBinarySupport_Write.htm) | Called when an object is required to serialize itself. (Inherited from [GH\_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm).) |
| Public method | [Write(XmlWriter)](M_GH_IO_Serialization_GH_IXmlSupport_Write.htm) | Called when an object is required to serialize itself. (Inherited from [GH\_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)