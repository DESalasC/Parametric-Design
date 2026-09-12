# P_GH_IO_Serialization_GH_Chunk_Index

﻿ GH\_Chunk.Index Property 

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
| GH\_ChunkAddLanguageSpecificTextSet("LST28A04FED\_0?cpp=::|nu=.");Index Property |

Gets the index of this chunk. The index is set by the owner of this chunk.
Indices smaller than zero imply no index has been set.
The combination of name+index is always unique among a set of chunks in the same litter.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int Index { get; }
```

```
Public ReadOnly Property Index As Integer
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  

[Missing <value> documentation for "P:GH\_IO.Serialization.GH\_Chunk.Index"]

#### Implements

[GH\_IChunkAddLanguageSpecificTextSet("LST28A04FED\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Index](P_GH_IO_Serialization_GH_IChunk_Index.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)