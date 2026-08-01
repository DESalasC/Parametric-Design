# Properties_T_GH_IO_Serialization_GH_IChunk

﻿ GH\_IChunk Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IChunk Interface](../html/T_GH_IO_Serialization_GH_IChunk.htm "GH_IChunk Interface")

[GH\_IChunk Properties](../html/Properties_T_GH_IO_Serialization_GH_IChunk.htm "GH_IChunk Properties")

[Archive Property](../html/P_GH_IO_Serialization_GH_IChunk_Archive.htm "Archive Property ")

[ArchiveLocation Property](../html/P_GH_IO_Serialization_GH_IChunk_ArchiveLocation.htm "ArchiveLocation Property ")

[ChunkCount Property](../html/P_GH_IO_Serialization_GH_IChunk_ChunkCount.htm "ChunkCount Property ")

[Chunks Property](../html/P_GH_IO_Serialization_GH_IChunk_Chunks.htm "Chunks Property ")

[Index Property](../html/P_GH_IO_Serialization_GH_IChunk_Index.htm "Index Property ")

[ItemCount Property](../html/P_GH_IO_Serialization_GH_IChunk_ItemCount.htm "ItemCount Property ")

[Items Property](../html/P_GH_IO_Serialization_GH_IChunk_Items.htm "Items Property ")

[Name Property](../html/P_GH_IO_Serialization_GH_IChunk_Name.htm "Name Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IChunk Properties |

The [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm) type exposes the following members.

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

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IChunk Interface](T_GH_IO_Serialization_GH_IChunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)