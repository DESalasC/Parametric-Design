# P_GH_IO_Serialization_GH_IChunk_Index

﻿ GH\_IChunk.Index Property 

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
| GH\_IChunkAddLanguageSpecificTextSet("LSTD54874B3\_0?cpp=::|nu=.");Index Property |

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
int Index { get; }
```

```
ReadOnly Property Index As Integer
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  

[Missing <value> documentation for "P:GH\_IO.Serialization.GH\_IChunk.Index"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IChunk Interface](T_GH_IO_Serialization_GH_IChunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)