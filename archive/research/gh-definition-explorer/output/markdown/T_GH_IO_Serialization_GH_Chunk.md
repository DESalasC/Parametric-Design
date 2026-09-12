# T_GH_IO_Serialization_GH_Chunk

﻿ GH\_Chunk Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Constructor](../html/Overload_GH_IO_Serialization_GH_Chunk__ctor.htm "GH_Chunk Constructor ")

[GH\_Chunk Properties](../html/Properties_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Properties")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[GH\_Chunk Fields](../html/Fields_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Chunk Class |

Full implementation of GH\_IChunk, GH\_IReader, GH\_IWriter, GH\_IBinarySupport and GH\_IXmlSupport.
Instances of this class are usually disguised as one of the interfaces it implements.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST3ECB6502\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  GH\_IO.SerializationAddLanguageSpecificTextSet("LST3ECB6502\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Chunk  
    [GH\_IO.SerializationAddLanguageSpecificTextSet("LST3ECB6502\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LooseChunk](T_GH_IO_Serialization_GH_LooseChunk.htm)

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Chunk : GH_IWriter, GH_IChunk, 
	GH_IBinarySupport, GH_IXmlSupport, GH_IReader
```

```
Public Class GH_Chunk
	Implements GH_IWriter, GH_IChunk, GH_IBinarySupport, GH_IXmlSupport, 
	GH_IReader
```

AddLanguageTabSet("ID1EBCA");

The GH\_Chunk type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_ChunkAddLanguageSpecificTextSet("LST3ECB6502\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](M_GH_IO_Serialization_GH_Chunk__ctor.htm) | Blank constructor. You typically do not need to create your own Chunks. The GH\_Archive class will create top-level chunks and existing chunks can create child chunks. |
| Protected method | [GH\_Chunk(GH\_Archive)](M_GH_IO_Serialization_GH_Chunk__ctor_1.htm) | Constructor. You typically do not need to create your own Chunks. The GH\_Archive class will create top-level chunks and existing chunks can create child chunks. |
| Protected method | [GH\_Chunk(GH\_Archive, String)](M_GH_IO_Serialization_GH_Chunk__ctor_2.htm) | Constructor. You typically do not need to create your own Chunks. The GH\_Archive class will create top-level chunks and existing chunks can create child chunks. |
| Protected method | [GH\_Chunk(GH\_Archive, String, Int32)](M_GH_IO_Serialization_GH_Chunk__ctor_3.htm) | Constructor. You typically do not need to create your own Chunks. The GH\_Archive class will create top-level chunks and existing chunks can create child chunks. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Archive](P_GH_IO_Serialization_GH_Chunk_Archive.htm) | Gets a pointer to the archive that owns the Root of the tree this chunk belongs to. |
| Public property | [ArchiveLocation](P_GH_IO_Serialization_GH_Chunk_ArchiveLocation.htm) | Gets a string representing the URI with which the archive is associated. The location may be a null string. |
| Public property | [ChunkCount](P_GH_IO_Serialization_GH_Chunk_ChunkCount.htm) | Gets the number of child chunks contained in this chunk. The set of all child chunks is referred to as a 'litter'. |
| Public property | [Chunks](P_GH_IO_Serialization_GH_Chunk_Chunks.htm) | Gets a pointer to the internal list of child chunks. Do not access this list unless you know what you are doing. |
| Public property | [HasComments](P_GH_IO_Serialization_GH_Chunk_HasComments.htm) | Gets a value that indicates whether or not comments have been stored in this chunk. |
| Public property | [HasIndex](P_GH_IO_Serialization_GH_Chunk_HasIndex.htm) | Gets the index existence implication. The item is considered to have an index qualifier if the index value is larger than or equal to zero. |
| Public property | [HasName](P_GH_IO_Serialization_GH_Chunk_HasName.htm) | Gets the name validity of this item. The item is considered to have an invalid name if string.IsNullOrEmpty(name) |
| Public property | [Index](P_GH_IO_Serialization_GH_Chunk_Index.htm) | Gets the index of this chunk. The index is set by the owner of this chunk. Indices smaller than zero imply no index has been set. The combination of name+index is always unique among a set of chunks in the same litter. |
| Public property | [ItemCount](P_GH_IO_Serialization_GH_Chunk_ItemCount.htm) | Gets the number of items contained in this chunk. |
| Public property | [Items](P_GH_IO_Serialization_GH_Chunk_Items.htm) | Gets a pointer to the internal list of items. Do not access this list unless you know what you are doing. |
| Public property | [Name](P_GH_IO_Serialization_GH_Chunk_Name.htm) | Gets the name of this chunk. The name is set by the owner of this chunk. Names must be at least 1 character long. The combination of name+index is always unique among a set of chunks in a single litter. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddComment](M_GH_IO_Serialization_GH_Chunk_AddComment.htm) | Adds a text comment to this chunk. Comments are serialized only if the output flavour is a human readable format. Comments are never deserialized, they are purely for the benefit of the humans reading the file data. |
| Public method | [AddMessage](M_GH_IO_Serialization_GH_Chunk_AddMessage.htm) | Log a new message with the top-level archive. Messages are collected during read/write operations, and can be displayed to the user upon completion using GH\_Archive.ShowMessageLog(). |
| Public method | [ChunkExists(String)](M_GH_IO_Serialization_GH_Chunk_ChunkExists.htm) | Checks whether a chunk with the specified name exists in the litter. Only chunks without index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [ChunkExists(String, Int32)](M_GH_IO_Serialization_GH_Chunk_ChunkExists_1.htm) | Checks whether a chunk with the specified name and index exists in the litter. Only chunks with index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [CopyValuesFromChunk](M_GH_IO_Serialization_GH_Chunk_CopyValuesFromChunk.htm) | Copy all values and sub-chunks from another chunk. |
| Public method | [CopyValuesToChunk](M_GH_IO_Serialization_GH_Chunk_CopyValuesToChunk.htm) | Copy all values and sub-chunks in this chunk to another chunk which does not point to the same archive. |
| Public method | [CreateChunk(String)](M_GH_IO_Serialization_GH_Chunk_CreateChunk.htm) | Create a new child chunk with the specified name and without an index qualifier. If another chunk already exists with similar properties, an exception will be thrown. |
| Public method | [CreateChunk(String, Int32)](M_GH_IO_Serialization_GH_Chunk_CreateChunk_1.htm) | Create a new child chunk with the specified name and index qualifier. If another chunk already exists with similar properties, an exception will be thrown. |
| Public method | [FindChunk(String)](M_GH_IO_Serialization_GH_Chunk_FindChunk.htm) | Finds the first chunk in the litter that matches the given name. Only chunks without index qualifiers are considered. |
| Public method | [FindChunk(String, Int32)](M_GH_IO_Serialization_GH_Chunk_FindChunk_1.htm) | Finds the first chunk in the list that matches the given name and index. Only chunks with index qualifiers are considered. |
| Public method | [FindItem(String)](M_GH_IO_Serialization_GH_Chunk_FindItem.htm) | Finds the first item that matches the given name. Only items without index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [FindItem(String, Int32)](M_GH_IO_Serialization_GH_Chunk_FindItem_1.htm) | Finds the first item that matches the given name and index. Only items with index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [GetBoolean(String)](M_GH_IO_Serialization_GH_Chunk_GetBoolean.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetBoolean(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetBoolean_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetBoundingBox(String)](M_GH_IO_Serialization_GH_Chunk_GetBoundingBox.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetBoundingBox(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetBoundingBox_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetByte(String)](M_GH_IO_Serialization_GH_Chunk_GetByte.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetByte(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetByte_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetByteArray(String)](M_GH_IO_Serialization_GH_Chunk_GetByteArray.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetByteArray(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetByteArray_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDate(String)](M_GH_IO_Serialization_GH_Chunk_GetDate.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDate(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDate_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDecimal(String)](M_GH_IO_Serialization_GH_Chunk_GetDecimal.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDecimal(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDecimal_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDouble(String)](M_GH_IO_Serialization_GH_Chunk_GetDouble.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDouble(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDouble_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDoubleArray(String)](M_GH_IO_Serialization_GH_Chunk_GetDoubleArray.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDoubleArray(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDoubleArray_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingBitmap(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingBitmap.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingBitmap(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingBitmap_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingColor(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingColor.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingColor(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingColor_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingPoint(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingPoint.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingPoint(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingPoint_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingPointF(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingPointF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingPointF(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingPointF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingRectangle(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingRectangle.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingRectangle(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingRectangle_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingRectangleF(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingRectangleF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingRectangleF(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingRectangleF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingSize(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingSize.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingSize(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingSize_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetDrawingSizeF(String)](M_GH_IO_Serialization_GH_Chunk_GetDrawingSizeF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetDrawingSizeF(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetDrawingSizeF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetGuid(String)](M_GH_IO_Serialization_GH_Chunk_GetGuid.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetGuid(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetGuid_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetInt32(String)](M_GH_IO_Serialization_GH_Chunk_GetInt32.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetInt32(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetInt32_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetInt64(String)](M_GH_IO_Serialization_GH_Chunk_GetInt64.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetInt64(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetInt64_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetInterval1D(String)](M_GH_IO_Serialization_GH_Chunk_GetInterval1D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetInterval1D(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetInterval1D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetInterval2D(String)](M_GH_IO_Serialization_GH_Chunk_GetInterval2D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetInterval2D(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetInterval2D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetLine(String)](M_GH_IO_Serialization_GH_Chunk_GetLine.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetLine(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetLine_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetPath(String, String)](M_GH_IO_Serialization_GH_Chunk_GetPath_1.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetPath(String, Int32, String)](M_GH_IO_Serialization_GH_Chunk_GetPath.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetPlane(String)](M_GH_IO_Serialization_GH_Chunk_GetPlane.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetPlane(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetPlane_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetPoint2D(String)](M_GH_IO_Serialization_GH_Chunk_GetPoint2D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetPoint2D(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetPoint2D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetPoint3D(String)](M_GH_IO_Serialization_GH_Chunk_GetPoint3D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetPoint3D(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetPoint3D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetPoint4D(String)](M_GH_IO_Serialization_GH_Chunk_GetPoint4D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetPoint4D(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetPoint4D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetSingle(String)](M_GH_IO_Serialization_GH_Chunk_GetSingle.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetSingle(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetSingle_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetString(String)](M_GH_IO_Serialization_GH_Chunk_GetString.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetString(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetString_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [GetVersion(String)](M_GH_IO_Serialization_GH_Chunk_GetVersion.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [GetVersion(String, Int32)](M_GH_IO_Serialization_GH_Chunk_GetVersion_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public methodStatic member | [InstantiateRoot](M_GH_IO_Serialization_GH_Chunk_InstantiateRoot.htm) | Construct a new instance of GH\_Chunk which acts as a Root node. If you **must** create a chunk from scratch, use this static method to create one. |
| Public method | [ItemExists(String)](M_GH_IO_Serialization_GH_Chunk_ItemExists.htm) | Gets the occupancy for a specific item name. Only items without index qualifiers are considered. |
| Public method | [ItemExists(String, Int32)](M_GH_IO_Serialization_GH_Chunk_ItemExists_1.htm) | Checks whether an item with the specified name and index exists. Only items with index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [Read(BinaryReader)](M_GH_IO_Serialization_GH_Chunk_Read.htm) | Read this chunk and all child chunks from a binary stream. |
| Public method | [Read(XmlNode)](M_GH_IO_Serialization_GH_Chunk_Read_1.htm) | Read this chunk and all child chunks from an Xml node. |
| Public method | [RemoveChunk(GH\_IChunk)](M_GH_IO_Serialization_GH_Chunk_RemoveChunk.htm) | Remove the specified chunk from the litter. |
| Public method | [RemoveChunk(String)](M_GH_IO_Serialization_GH_Chunk_RemoveChunk_1.htm) | Remove the first chunk with a matching name. Only chunks without index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [RemoveChunk(String, Int32)](M_GH_IO_Serialization_GH_Chunk_RemoveChunk_2.htm) | Remove the first chunk with a matching name and index. Only chunks with index qualifiers are considered. Name comparisons are not case-sensitive. |
| Public method | [RemoveItem(String)](M_GH_IO_Serialization_GH_Chunk_RemoveItem.htm) | Remove an unindexed item from this chunk. |
| Public method | [RemoveItem(String, Int32)](M_GH_IO_Serialization_GH_Chunk_RemoveItem_1.htm) | Remove an indexed item from this chunk. |
| Public method | [SetBoolean(String, Boolean)](M_GH_IO_Serialization_GH_Chunk_SetBoolean.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetBoolean(String, Int32, Boolean)](M_GH_IO_Serialization_GH_Chunk_SetBoolean_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetBoundingBox(String, GH\_BoundingBox)](M_GH_IO_Serialization_GH_Chunk_SetBoundingBox.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetBoundingBox(String, Int32, GH\_BoundingBox)](M_GH_IO_Serialization_GH_Chunk_SetBoundingBox_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetByte(String, Byte)](M_GH_IO_Serialization_GH_Chunk_SetByte.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetByte(String, Int32, Byte)](M_GH_IO_Serialization_GH_Chunk_SetByte_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetByteArray(String, AddLanguageSpecificTextSet("LST3ECB6502\_4?cpp=array&lt;");ByteAddLanguageSpecificTextSet("LST3ECB6502\_5?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_GH_IO_Serialization_GH_Chunk_SetByteArray.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetByteArray(String, Int32, AddLanguageSpecificTextSet("LST3ECB6502\_6?cpp=array&lt;");ByteAddLanguageSpecificTextSet("LST3ECB6502\_7?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_GH_IO_Serialization_GH_Chunk_SetByteArray_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDate(String, DateTime)](M_GH_IO_Serialization_GH_Chunk_SetDate.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDate(String, Int32, DateTime)](M_GH_IO_Serialization_GH_Chunk_SetDate_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDecimal(String, Decimal)](M_GH_IO_Serialization_GH_Chunk_SetDecimal.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDecimal(String, Int32, Decimal)](M_GH_IO_Serialization_GH_Chunk_SetDecimal_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDouble(String, Double)](M_GH_IO_Serialization_GH_Chunk_SetDouble.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDouble(String, Int32, Double)](M_GH_IO_Serialization_GH_Chunk_SetDouble_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDoubleArray(String, AddLanguageSpecificTextSet("LST3ECB6502\_8?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LST3ECB6502\_9?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_GH_IO_Serialization_GH_Chunk_SetDoubleArray.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDoubleArray(String, Int32, AddLanguageSpecificTextSet("LST3ECB6502\_10?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LST3ECB6502\_11?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_GH_IO_Serialization_GH_Chunk_SetDoubleArray_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingBitmap(String, Bitmap)](M_GH_IO_Serialization_GH_Chunk_SetDrawingBitmap.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingBitmap(String, Int32, Bitmap)](M_GH_IO_Serialization_GH_Chunk_SetDrawingBitmap_1.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingColor(String, Color)](M_GH_IO_Serialization_GH_Chunk_SetDrawingColor.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingColor(String, Int32, Color)](M_GH_IO_Serialization_GH_Chunk_SetDrawingColor_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingPoint(String, Point)](M_GH_IO_Serialization_GH_Chunk_SetDrawingPoint.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingPoint(String, Int32, Point)](M_GH_IO_Serialization_GH_Chunk_SetDrawingPoint_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingPointF(String, PointF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingPointF.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingPointF(String, Int32, PointF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingPointF_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingRectangle(String, Rectangle)](M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangle.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingRectangle(String, Int32, Rectangle)](M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangle_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingRectangleF(String, RectangleF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangleF.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingRectangleF(String, Int32, RectangleF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangleF_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingSize(String, Size)](M_GH_IO_Serialization_GH_Chunk_SetDrawingSize.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingSize(String, Int32, Size)](M_GH_IO_Serialization_GH_Chunk_SetDrawingSize_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetDrawingSizeF(String, SizeF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingSizeF.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetDrawingSizeF(String, Int32, SizeF)](M_GH_IO_Serialization_GH_Chunk_SetDrawingSizeF_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetGuid(String, Guid)](M_GH_IO_Serialization_GH_Chunk_SetGuid.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetGuid(String, Int32, Guid)](M_GH_IO_Serialization_GH_Chunk_SetGuid_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetInt32(String, Int32)](M_GH_IO_Serialization_GH_Chunk_SetInt32.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetInt32(String, Int32, Int32)](M_GH_IO_Serialization_GH_Chunk_SetInt32_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetInt64(String, Int64)](M_GH_IO_Serialization_GH_Chunk_SetInt64_1.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetInt64(String, Int32, Int64)](M_GH_IO_Serialization_GH_Chunk_SetInt64.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetInterval1D(String, GH\_Interval1D)](M_GH_IO_Serialization_GH_Chunk_SetInterval1D.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetInterval1D(String, Int32, GH\_Interval1D)](M_GH_IO_Serialization_GH_Chunk_SetInterval1D_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetInterval2D(String, GH\_Interval2D)](M_GH_IO_Serialization_GH_Chunk_SetInterval2D.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetInterval2D(String, Int32, GH\_Interval2D)](M_GH_IO_Serialization_GH_Chunk_SetInterval2D_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetLine(String, GH\_Line)](M_GH_IO_Serialization_GH_Chunk_SetLine.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetLine(String, Int32, GH\_Line)](M_GH_IO_Serialization_GH_Chunk_SetLine_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPath(String, String, String)](M_GH_IO_Serialization_GH_Chunk_SetPath_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPath(String, Int32, String, String)](M_GH_IO_Serialization_GH_Chunk_SetPath.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPlane(String, GH\_Plane)](M_GH_IO_Serialization_GH_Chunk_SetPlane.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetPlane(String, Int32, GH\_Plane)](M_GH_IO_Serialization_GH_Chunk_SetPlane_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPoint2D(String, GH\_Point2D)](M_GH_IO_Serialization_GH_Chunk_SetPoint2D.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetPoint2D(String, Int32, GH\_Point2D)](M_GH_IO_Serialization_GH_Chunk_SetPoint2D_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPoint3D(String, GH\_Point3D)](M_GH_IO_Serialization_GH_Chunk_SetPoint3D.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetPoint3D(String, Int32, GH\_Point3D)](M_GH_IO_Serialization_GH_Chunk_SetPoint3D_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetPoint4D(String, GH\_Point4D)](M_GH_IO_Serialization_GH_Chunk_SetPoint4D.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetPoint4D(String, Int32, GH\_Point4D)](M_GH_IO_Serialization_GH_Chunk_SetPoint4D_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetSingle(String, Single)](M_GH_IO_Serialization_GH_Chunk_SetSingle_1.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetSingle(String, Int32, Single)](M_GH_IO_Serialization_GH_Chunk_SetSingle.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetString(String, String)](M_GH_IO_Serialization_GH_Chunk_SetString_1.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetString(String, Int32, String)](M_GH_IO_Serialization_GH_Chunk_SetString.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetVersion(String, GH\_Version)](M_GH_IO_Serialization_GH_Chunk_SetVersion.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetVersion(String, Int32, GH\_Version)](M_GH_IO_Serialization_GH_Chunk_SetVersion_1.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [SetVersion(String, Int32, Int32, Int32)](M_GH_IO_Serialization_GH_Chunk_SetVersion_2.htm) | Add a new data item to this chunk. The name must be unique or an exception will be thrown. |
| Public method | [SetVersion(String, Int32, Int32, Int32, Int32)](M_GH_IO_Serialization_GH_Chunk_SetVersion_3.htm) | Add a new data item to this chunk. The combination of name and index must be unique or an exception will be thrown. |
| Public method | [TryGetBoolean(String, BooleanAddLanguageSpecificTextSet("LST3ECB6502\_12?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetBoolean.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetBoolean(String, Int32, BooleanAddLanguageSpecificTextSet("LST3ECB6502\_13?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetBoolean_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetBoundingBox(String, GH\_BoundingBoxAddLanguageSpecificTextSet("LST3ECB6502\_14?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetBoundingBox.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetBoundingBox(String, Int32, GH\_BoundingBoxAddLanguageSpecificTextSet("LST3ECB6502\_15?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetBoundingBox_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetByte(String, ByteAddLanguageSpecificTextSet("LST3ECB6502\_16?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetByte.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetByte(String, Int32, ByteAddLanguageSpecificTextSet("LST3ECB6502\_17?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetByte_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDate(String, DateTimeAddLanguageSpecificTextSet("LST3ECB6502\_18?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDate.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDate(String, Int32, DateTimeAddLanguageSpecificTextSet("LST3ECB6502\_19?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDate_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDecimal(String, DecimalAddLanguageSpecificTextSet("LST3ECB6502\_20?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDecimal.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDecimal(String, Int32, DecimalAddLanguageSpecificTextSet("LST3ECB6502\_21?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDecimal_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDouble(String, DoubleAddLanguageSpecificTextSet("LST3ECB6502\_22?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDouble.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDouble(String, Int32, DoubleAddLanguageSpecificTextSet("LST3ECB6502\_23?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDouble_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingColor(String, ColorAddLanguageSpecificTextSet("LST3ECB6502\_24?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingColor.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingColor(String, Int32, ColorAddLanguageSpecificTextSet("LST3ECB6502\_25?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingColor_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingPoint(String, PointAddLanguageSpecificTextSet("LST3ECB6502\_26?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingPoint(String, Int32, PointAddLanguageSpecificTextSet("LST3ECB6502\_27?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingPointF(String, PointFAddLanguageSpecificTextSet("LST3ECB6502\_28?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPointF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingPointF(String, Int32, PointFAddLanguageSpecificTextSet("LST3ECB6502\_29?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPointF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingRectangle(String, RectangleAddLanguageSpecificTextSet("LST3ECB6502\_30?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangle.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingRectangle(String, Int32, RectangleAddLanguageSpecificTextSet("LST3ECB6502\_31?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangle_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingRectangleF(String, RectangleFAddLanguageSpecificTextSet("LST3ECB6502\_32?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangleF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingRectangleF(String, Int32, RectangleFAddLanguageSpecificTextSet("LST3ECB6502\_33?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangleF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingSize(String, SizeAddLanguageSpecificTextSet("LST3ECB6502\_34?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSize.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingSize(String, Int32, SizeAddLanguageSpecificTextSet("LST3ECB6502\_35?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSize_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingSizeF(String, SizeFAddLanguageSpecificTextSet("LST3ECB6502\_36?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSizeF.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetDrawingSizeF(String, Int32, SizeFAddLanguageSpecificTextSet("LST3ECB6502\_37?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSizeF_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetGuid(String, GuidAddLanguageSpecificTextSet("LST3ECB6502\_38?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetGuid.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetGuid(String, Int32, GuidAddLanguageSpecificTextSet("LST3ECB6502\_39?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetGuid_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetInt32(String, Int32AddLanguageSpecificTextSet("LST3ECB6502\_40?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetInt32_1.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetInt32(String, Int32, Int32AddLanguageSpecificTextSet("LST3ECB6502\_41?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetInt32.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetInt64(String, Int64AddLanguageSpecificTextSet("LST3ECB6502\_42?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetInt64_1.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetInt64(String, Int32, Int64AddLanguageSpecificTextSet("LST3ECB6502\_43?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetInt64.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetInterval1D(String, GH\_Interval1DAddLanguageSpecificTextSet("LST3ECB6502\_44?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetInterval1D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetInterval1D(String, Int32, GH\_Interval1DAddLanguageSpecificTextSet("LST3ECB6502\_45?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetInterval1D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetInterval2D(String, GH\_Interval2DAddLanguageSpecificTextSet("LST3ECB6502\_46?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetInterval2D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetInterval2D(String, Int32, GH\_Interval2DAddLanguageSpecificTextSet("LST3ECB6502\_47?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetInterval2D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetLine(String, GH\_LineAddLanguageSpecificTextSet("LST3ECB6502\_48?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetLine.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetLine(String, Int32, GH\_LineAddLanguageSpecificTextSet("LST3ECB6502\_49?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetLine_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetPlane(String, GH\_PlaneAddLanguageSpecificTextSet("LST3ECB6502\_50?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetPlane.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetPlane(String, Int32, GH\_PlaneAddLanguageSpecificTextSet("LST3ECB6502\_51?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetPlane_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint2D(String, GH\_Point2DAddLanguageSpecificTextSet("LST3ECB6502\_52?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint2D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint2D(String, Int32, GH\_Point2DAddLanguageSpecificTextSet("LST3ECB6502\_53?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint2D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint3D(String, GH\_Point3DAddLanguageSpecificTextSet("LST3ECB6502\_54?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint3D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint3D(String, Int32, GH\_Point3DAddLanguageSpecificTextSet("LST3ECB6502\_55?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint3D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint4D(String, GH\_Point4DAddLanguageSpecificTextSet("LST3ECB6502\_56?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint4D.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetPoint4D(String, Int32, GH\_Point4DAddLanguageSpecificTextSet("LST3ECB6502\_57?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetPoint4D_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetSingle(String, SingleAddLanguageSpecificTextSet("LST3ECB6502\_58?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetSingle_1.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetSingle(String, Int32, SingleAddLanguageSpecificTextSet("LST3ECB6502\_59?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetSingle.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetString(String, StringAddLanguageSpecificTextSet("LST3ECB6502\_60?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetString_1.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetString(String, Int32, StringAddLanguageSpecificTextSet("LST3ECB6502\_61?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetString.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [TryGetVersion(String, GH\_VersionAddLanguageSpecificTextSet("LST3ECB6502\_62?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetVersion.htm) | Gets the value of the item with the specified name. Name comparison is not case-sensitive. |
| Public method | [TryGetVersion(String, Int32, GH\_VersionAddLanguageSpecificTextSet("LST3ECB6502\_63?cpp=%");)](M_GH_IO_Serialization_GH_Chunk_TryGetVersion_1.htm) | Gets the value of the item with the specified name and index. Name comparison is not case-sensitive. |
| Public method | [Write(BinaryWriter)](M_GH_IO_Serialization_GH_Chunk_Write.htm) | Write this chunk and all child chunks to a binary stream. |
| Public method | [Write(XmlWriter)](M_GH_IO_Serialization_GH_Chunk_Write_1.htm) | Serialize this chunk into an Xml stream. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_archive](F_GH_IO_Serialization_GH_Chunk_m_archive.htm) | Pointer to the archive that owns the Root of the tree this chunk belongs to. |
| Protected field | [m\_chunks](F_GH_IO_Serialization_GH_Chunk_m_chunks.htm) | Dictionary of sub-chunks contained within this chunk. |
| Protected field | [m\_comments](F_GH_IO_Serialization_GH_Chunk_m_comments.htm) | List of text comments. This list is automatically instantiated once the first comment is added. |
| Protected field | [m\_index](F_GH_IO_Serialization_GH_Chunk_m_index.htm) | Index of this chunk. This field is set only once, during construction. A negative index indicates no index qualifier has been set. |
| Protected field | [m\_items](F_GH_IO_Serialization_GH_Chunk_m_items.htm) | The list of nodes contained within this chunk. |
| Protected field | [m\_name](F_GH_IO_Serialization_GH_Chunk_m_name.htm) | Name of this chunk. This field is set only once, during construction. |
| Protected fieldStatic member | [name\_comp](F_GH_IO_Serialization_GH_Chunk_name_comp.htm) | Comparison flag to use when comparing names. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)