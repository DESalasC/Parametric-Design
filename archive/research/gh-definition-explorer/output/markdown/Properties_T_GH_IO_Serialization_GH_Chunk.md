# Properties_T_GH_IO_Serialization_GH_Chunk

﻿ GH\_Chunk Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Properties](../html/Properties_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Properties")

[Archive Property](../html/P_GH_IO_Serialization_GH_Chunk_Archive.htm "Archive Property ")

[ArchiveLocation Property](../html/P_GH_IO_Serialization_GH_Chunk_ArchiveLocation.htm "ArchiveLocation Property ")

[ChunkCount Property](../html/P_GH_IO_Serialization_GH_Chunk_ChunkCount.htm "ChunkCount Property ")

[Chunks Property](../html/P_GH_IO_Serialization_GH_Chunk_Chunks.htm "Chunks Property ")

[HasComments Property](../html/P_GH_IO_Serialization_GH_Chunk_HasComments.htm "HasComments Property ")

[HasIndex Property](../html/P_GH_IO_Serialization_GH_Chunk_HasIndex.htm "HasIndex Property ")

[HasName Property](../html/P_GH_IO_Serialization_GH_Chunk_HasName.htm "HasName Property ")

[Index Property](../html/P_GH_IO_Serialization_GH_Chunk_Index.htm "Index Property ")

[ItemCount Property](../html/P_GH_IO_Serialization_GH_Chunk_ItemCount.htm "ItemCount Property ")

[Items Property](../html/P_GH_IO_Serialization_GH_Chunk_Items.htm "Items Property ")

[Name Property](../html/P_GH_IO_Serialization_GH_Chunk_Name.htm "Name Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Chunk Properties |

The [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm) type exposes the following members.

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

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)