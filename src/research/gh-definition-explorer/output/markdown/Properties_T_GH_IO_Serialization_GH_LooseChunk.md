# Properties_T_GH_IO_Serialization_GH_LooseChunk

﻿ GH\_LooseChunk Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_LooseChunk Class](../html/T_GH_IO_Serialization_GH_LooseChunk.htm "GH_LooseChunk Class")

[GH\_LooseChunk Constructor](../html/Overload_GH_IO_Serialization_GH_LooseChunk__ctor.htm "GH_LooseChunk Constructor ")

[GH\_LooseChunk Properties](../html/Properties_T_GH_IO_Serialization_GH_LooseChunk.htm "GH_LooseChunk Properties")

[GH\_LooseChunk Methods](../html/Methods_T_GH_IO_Serialization_GH_LooseChunk.htm "GH_LooseChunk Methods")

[GH\_LooseChunk Fields](../html/Fields_T_GH_IO_Serialization_GH_LooseChunk.htm "GH_LooseChunk Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LooseChunk Properties |

The [GH\_LooseChunk](T_GH_IO_Serialization_GH_LooseChunk.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Archive](P_GH_IO_Serialization_GH_Chunk_Archive.htm) | Gets a pointer to the archive that owns the Root of the tree this chunk belongs to. (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |
| Public property | [ArchiveLocation](P_GH_IO_Serialization_GH_Chunk_ArchiveLocation.htm) | Gets a string representing the URI with which the archive is associated. The location may be a null string. (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |
| Public property | [ChunkCount](P_GH_IO_Serialization_GH_Chunk_ChunkCount.htm) | Gets the number of child chunks contained in this chunk. The set of all child chunks is referred to as a 'litter'. (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |
| Public property | [Chunks](P_GH_IO_Serialization_GH_Chunk_Chunks.htm) | Gets a pointer to the internal list of child chunks. Do not access this list unless you know what you are doing. (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |
| Public property | [HasComments](P_GH_IO_Serialization_GH_Chunk_HasComments.htm) | Gets a value that indicates whether or not comments have been stored in this chunk. (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |
| Public property | [HasIndex](P_GH_IO_Serialization_GH_Chunk_HasIndex.htm) | Gets the index existence implication. The item is considered to have an index qualifier if the index value is larger than or equal to zero. (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |
| Public property | [HasName](P_GH_IO_Serialization_GH_Chunk_HasName.htm) | Gets the name validity of this item. The item is considered to have an invalid name if string.IsNullOrEmpty(name) (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |
| Public property | [Index](P_GH_IO_Serialization_GH_Chunk_Index.htm) | Gets the index of this chunk. The index is set by the owner of this chunk. Indices smaller than zero imply no index has been set. The combination of name+index is always unique among a set of chunks in the same litter. (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |
| Public property | [ItemCount](P_GH_IO_Serialization_GH_Chunk_ItemCount.htm) | Gets the number of items contained in this chunk. (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |
| Public property | [Items](P_GH_IO_Serialization_GH_Chunk_Items.htm) | Gets a pointer to the internal list of items. Do not access this list unless you know what you are doing. (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |
| Public property | [Name](P_GH_IO_Serialization_GH_Chunk_Name.htm) | Gets the name of this chunk. The name is set by the owner of this chunk. Names must be at least 1 character long. The combination of name+index is always unique among a set of chunks in a single litter. (Inherited from [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_LooseChunk Class](T_GH_IO_Serialization_GH_LooseChunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)