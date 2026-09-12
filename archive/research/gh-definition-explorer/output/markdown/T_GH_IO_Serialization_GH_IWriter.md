# T_GH_IO_Serialization_GH_IWriter

﻿ GH\_IWriter Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Properties](../html/Properties_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Properties")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriter Interface |

Provides access to a subset of GH\_Chunk methods used for writing archives.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface GH_IWriter : GH_IChunk, 
	GH_IBinarySupport, GH_IXmlSupport
```

```
Public Interface GH_IWriter
	Inherits GH_IChunk, GH_IBinarySupport, GH_IXmlSupport
```

AddLanguageTabSet("ID0EBCA");

The GH\_IWriter type exposes the following members.

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
| Public method | [AddComment](M_GH_IO_Serialization_GH_IWriter_AddComment.htm) | Adds a text comment to this chunk. Comments are serialized only if the output flavour is a human readable format. Comments are never deserialized, they are purely for the benefit of the humans reading the file data. |
| Public method | [AddMessage](M_GH_IO_Serialization_GH_IChunk_AddMessage.htm) | Log a new message with the top-level archive. Messages are collected during read/write operations, and can be displayed to the user upon completion using GH\_Archive.ShowMessageLog(). (Inherited from [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm).) |
| Public method | [CreateChunk(String)](M_GH_IO_Serialization_GH_IWriter_CreateChunk.htm) | Create a new child chunk with the specified name but without an index qualifier. If another chunk already exists with similar properties, an exception will be thrown. |
| Public method | [CreateChunk(String, Int32)](M_GH_IO_Serialization_GH_IWriter_CreateChunk_1.htm) | Create a new child chunk with the specified name and index qualifier. If another chunk already exists with similar properties, an exception will be thrown. |
| Public method | [Read(BinaryReader)](M_GH_IO_Serialization_GH_IBinarySupport_Read.htm) | Called when an object is required to deserialize itself. (Inherited from [GH\_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm).) |
| Public method | [Read(XmlNode)](M_GH_IO_Serialization_GH_IXmlSupport_Read.htm) | Called when an object is required to deserialize itself. (Inherited from [GH\_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm).) |
| Public method | [RemoveChunk(GH\_IChunk)](M_GH_IO_Serialization_GH_IWriter_RemoveChunk.htm) | Remove the specified chunk from the litter. |
| Public method | [RemoveChunk(String)](M_GH_IO_Serialization_GH_IWriter_RemoveChunk_1.htm) | Remove the first chunk with a matching name. Only chunks without index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [RemoveChunk(String, Int32)](M_GH_IO_Serialization_GH_IWriter_RemoveChunk_2.htm) | Remove the first chunk with a matching name and index. Only chunks with index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [RemoveItem(String)](M_GH_IO_Serialization_GH_IWriter_RemoveItem.htm) | Remove an unindexed item from this chunk. |
| Public method | [RemoveItem(String, Int32)](M_GH_IO_Serialization_GH_IWriter_RemoveItem_1.htm) | Remove an indexed item from this chunk. |
| Public method | [SetBoolean(String, Boolean)](M_GH_IO_Serialization_GH_IWriter_SetBoolean.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetBoolean(String, Int32, Boolean)](M_GH_IO_Serialization_GH_IWriter_SetBoolean_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetBoundingBox(String, GH\_BoundingBox)](M_GH_IO_Serialization_GH_IWriter_SetBoundingBox.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetBoundingBox(String, Int32, GH\_BoundingBox)](M_GH_IO_Serialization_GH_IWriter_SetBoundingBox_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetByte(String, Byte)](M_GH_IO_Serialization_GH_IWriter_SetByte.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetByte(String, Int32, Byte)](M_GH_IO_Serialization_GH_IWriter_SetByte_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetByteArray(String, AddLanguageSpecificTextSet("LST5198F49A\_0?cpp=array&lt;");ByteAddLanguageSpecificTextSet("LST5198F49A\_1?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_GH_IO_Serialization_GH_IWriter_SetByteArray.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetByteArray(String, Int32, AddLanguageSpecificTextSet("LST5198F49A\_2?cpp=array&lt;");ByteAddLanguageSpecificTextSet("LST5198F49A\_3?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_GH_IO_Serialization_GH_IWriter_SetByteArray_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDate(String, DateTime)](M_GH_IO_Serialization_GH_IWriter_SetDate.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDate(String, Int32, DateTime)](M_GH_IO_Serialization_GH_IWriter_SetDate_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDecimal(String, Decimal)](M_GH_IO_Serialization_GH_IWriter_SetDecimal.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDecimal(String, Int32, Decimal)](M_GH_IO_Serialization_GH_IWriter_SetDecimal_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDouble(String, Double)](M_GH_IO_Serialization_GH_IWriter_SetDouble.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDouble(String, Int32, Double)](M_GH_IO_Serialization_GH_IWriter_SetDouble_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDoubleArray(String, AddLanguageSpecificTextSet("LST5198F49A\_4?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LST5198F49A\_5?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_GH_IO_Serialization_GH_IWriter_SetDoubleArray.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDoubleArray(String, Int32, AddLanguageSpecificTextSet("LST5198F49A\_6?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LST5198F49A\_7?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_GH_IO_Serialization_GH_IWriter_SetDoubleArray_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingBitmap(String, Bitmap)](M_GH_IO_Serialization_GH_IWriter_SetDrawingBitmap.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingBitmap(String, Int32, Bitmap)](M_GH_IO_Serialization_GH_IWriter_SetDrawingBitmap_1.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingColor(String, Color)](M_GH_IO_Serialization_GH_IWriter_SetDrawingColor.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingColor(String, Int32, Color)](M_GH_IO_Serialization_GH_IWriter_SetDrawingColor_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingPoint(String, Point)](M_GH_IO_Serialization_GH_IWriter_SetDrawingPoint.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingPoint(String, Int32, Point)](M_GH_IO_Serialization_GH_IWriter_SetDrawingPoint_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingPointF(String, PointF)](M_GH_IO_Serialization_GH_IWriter_SetDrawingPointF.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingPointF(String, Int32, PointF)](M_GH_IO_Serialization_GH_IWriter_SetDrawingPointF_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingRectangle(String, Rectangle)](M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangle.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingRectangle(String, Int32, Rectangle)](M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangle_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingRectangleF(String, RectangleF)](M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangleF.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingRectangleF(String, Int32, RectangleF)](M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangleF_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingSize(String, Size)](M_GH_IO_Serialization_GH_IWriter_SetDrawingSize.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingSize(String, Int32, Size)](M_GH_IO_Serialization_GH_IWriter_SetDrawingSize_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingSizeF(String, SizeF)](M_GH_IO_Serialization_GH_IWriter_SetDrawingSizeF.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingSizeF(String, Int32, SizeF)](M_GH_IO_Serialization_GH_IWriter_SetDrawingSizeF_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetGuid(String, Guid)](M_GH_IO_Serialization_GH_IWriter_SetGuid.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetGuid(String, Int32, Guid)](M_GH_IO_Serialization_GH_IWriter_SetGuid_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetInt32(String, Int32)](M_GH_IO_Serialization_GH_IWriter_SetInt32.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetInt32(String, Int32, Int32)](M_GH_IO_Serialization_GH_IWriter_SetInt32_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetInt64(String, Int64)](M_GH_IO_Serialization_GH_IWriter_SetInt64_1.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetInt64(String, Int32, Int64)](M_GH_IO_Serialization_GH_IWriter_SetInt64.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetInterval1D(String, GH\_Interval1D)](M_GH_IO_Serialization_GH_IWriter_SetInterval1D.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetInterval1D(String, Int32, GH\_Interval1D)](M_GH_IO_Serialization_GH_IWriter_SetInterval1D_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetInterval2D(String, GH\_Interval2D)](M_GH_IO_Serialization_GH_IWriter_SetInterval2D.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetInterval2D(String, Int32, GH\_Interval2D)](M_GH_IO_Serialization_GH_IWriter_SetInterval2D_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetLine(String, GH\_Line)](M_GH_IO_Serialization_GH_IWriter_SetLine.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetLine(String, Int32, GH\_Line)](M_GH_IO_Serialization_GH_IWriter_SetLine_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPath(String, String, String)](M_GH_IO_Serialization_GH_IWriter_SetPath_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPath(String, Int32, String, String)](M_GH_IO_Serialization_GH_IWriter_SetPath.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPlane(String, GH\_Plane)](M_GH_IO_Serialization_GH_IWriter_SetPlane.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetPlane(String, Int32, GH\_Plane)](M_GH_IO_Serialization_GH_IWriter_SetPlane_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPoint2D(String, GH\_Point2D)](M_GH_IO_Serialization_GH_IWriter_SetPoint2D.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetPoint2D(String, Int32, GH\_Point2D)](M_GH_IO_Serialization_GH_IWriter_SetPoint2D_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPoint3D(String, GH\_Point3D)](M_GH_IO_Serialization_GH_IWriter_SetPoint3D.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetPoint3D(String, Int32, GH\_Point3D)](M_GH_IO_Serialization_GH_IWriter_SetPoint3D_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPoint4D(String, GH\_Point4D)](M_GH_IO_Serialization_GH_IWriter_SetPoint4D.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetPoint4D(String, Int32, GH\_Point4D)](M_GH_IO_Serialization_GH_IWriter_SetPoint4D_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetSingle(String, Single)](M_GH_IO_Serialization_GH_IWriter_SetSingle_1.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetSingle(String, Int32, Single)](M_GH_IO_Serialization_GH_IWriter_SetSingle.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetString(String, String)](M_GH_IO_Serialization_GH_IWriter_SetString_1.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetString(String, Int32, String)](M_GH_IO_Serialization_GH_IWriter_SetString.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetVersion(String, GH\_Version)](M_GH_IO_Serialization_GH_IWriter_SetVersion.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetVersion(String, Int32, GH\_Version)](M_GH_IO_Serialization_GH_IWriter_SetVersion_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetVersion(String, Int32, Int32, Int32)](M_GH_IO_Serialization_GH_IWriter_SetVersion_2.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetVersion(String, Int32, Int32, Int32, Int32)](M_GH_IO_Serialization_GH_IWriter_SetVersion_3.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [Write(BinaryWriter)](M_GH_IO_Serialization_GH_IBinarySupport_Write.htm) | Called when an object is required to serialize itself. (Inherited from [GH\_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm).) |
| Public method | [Write(XmlWriter)](M_GH_IO_Serialization_GH_IXmlSupport_Write.htm) | Called when an object is required to serialize itself. (Inherited from [GH\_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)