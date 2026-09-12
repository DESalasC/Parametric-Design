# T_GH_IO_Serialization_GH_IChunk

﻿ GH\_IChunk Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IChunk Interface](../html/T_GH_IO_Serialization_GH_IChunk.htm "GH_IChunk Interface")

[GH\_IChunk Properties](../html/Properties_T_GH_IO_Serialization_GH_IChunk.htm "GH_IChunk Properties")

[GH\_IChunk Methods](../html/Methods_T_GH_IO_Serialization_GH_IChunk.htm "GH_IChunk Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IChunk Interface |

Base interface for all Archive Chunks.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface GH_IChunk : GH_IBinarySupport, 
	GH_IXmlSupport
```

```
Public Interface GH_IChunk
	Inherits GH_IBinarySupport, GH_IXmlSupport
```

AddLanguageTabSet("ID0EBCA");

The GH\_IChunk type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Archive](P_GH_IO_Serialization_GH_IChunk_Archive.htm) | Gets a pointer to the archive that owns the Root of the tree this chunk belongs to. |
| Public property | [ArchiveLocation](P_GH_IO_Serialization_GH_IChunk_ArchiveLocation.htm) | Gets a string representing the URI with which the archive is associated. The location may be a null string. |
| Public property | [ChunkCount](P_GH_IO_Serialization_GH_IChunk_ChunkCount.htm) | Gets the number of child chunks contained in this chunk. The set of all child chunks is referred to as a 'litter'. |
| Public property | [Chunks](P_GH_IO_Serialization_GH_IChunk_Chunks.htm) | Gets a pointer to the internal list of child chunks. Do not access this list unless you know what you are doing. |
| Public property | [Index](P_GH_IO_Serialization_GH_IChunk_Index.htm) | Gets the index of this chunk. The index is set by the owner of this chunk. Indices smaller than zero imply no index has been set. The combination of name+index is always unique among a set of chunks in the same litter. |
| Public property | [ItemCount](P_GH_IO_Serialization_GH_IChunk_ItemCount.htm) | Gets the number of items contained in this chunk. |
| Public property | [Items](P_GH_IO_Serialization_GH_IChunk_Items.htm) | Gets a pointer to the internal list of items. Do not access this list unless you know what you are doing. |
| Public property | [Name](P_GH_IO_Serialization_GH_IChunk_Name.htm) | Gets the name of this chunk. The name is set by the owner of this chunk. Names must be at least 1 character long. The combination of name+index is always unique among a set of chunks in a single litter. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddMessage](M_GH_IO_Serialization_GH_IChunk_AddMessage.htm) | Log a new message with the top-level archive. Messages are collected during read/write operations, and can be displayed to the user upon completion using GH\_Archive.ShowMessageLog(). |
| Public method | [Read(BinaryReader)](M_GH_IO_Serialization_GH_IBinarySupport_Read.htm) | Called when an object is required to deserialize itself. (Inherited from [GH\_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm).) |
| Public method | [Read(XmlNode)](M_GH_IO_Serialization_GH_IXmlSupport_Read.htm) | Called when an object is required to deserialize itself. (Inherited from [GH\_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm).) |
| Public method | [Write(BinaryWriter)](M_GH_IO_Serialization_GH_IBinarySupport_Write.htm) | Called when an object is required to serialize itself. (Inherited from [GH\_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm).) |
| Public method | [Write(XmlWriter)](M_GH_IO_Serialization_GH_IXmlSupport_Write.htm) | Called when an object is required to serialize itself. (Inherited from [GH\_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)