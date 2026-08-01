# Properties_T_GH_IO_Serialization_GH_IReader

﻿ GH\_IReader Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Properties](../html/Properties_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Properties")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReader Properties |

The [GH\_IReader](T_GH_IO_Serialization_GH_IReader.htm) type exposes the following members.

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

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)