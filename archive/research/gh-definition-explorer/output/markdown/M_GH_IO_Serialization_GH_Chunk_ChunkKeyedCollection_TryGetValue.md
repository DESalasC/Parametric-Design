# M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_TryGetValue

﻿ GH\_Chunk.ChunkKeyedCollection.TryGetValue Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk.ChunkKeyedCollection Class](../html/T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm "GH_Chunk.ChunkKeyedCollection Class")

[ChunkKeyedCollection Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm "ChunkKeyedCollection Methods")

[Add Method](../html/M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_Add.htm "Add Method ")

[Clear Method](../html/M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_Clear.htm "Clear Method ")

[GetEnumerator Method](../html/M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_GetEnumerator.htm "GetEnumerator Method ")

[Remove Method](../html/Overload_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_Remove.htm "Remove Method ")

[TryGetValue Method](../html/M_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection_TryGetValue.htm "TryGetValue Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST91A9D529\_0?cpp=::|nu=.");ChunkKeyedCollectionAddLanguageSpecificTextSet("LST91A9D529\_1?cpp=::|nu=.");TryGetValue Method |

Try and find the chunk that belongs to a given ID.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool TryGetValue(
	ID id,
	out GH_Chunk chunk
)
```

```
Public Function TryGetValue ( 
	id As ID,
	<OutAttribute> ByRef chunk As GH_Chunk
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

id
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LST91A9D529\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ID](T_GH_IO_Serialization_ID.htm)  
    ID to look for.

chunk
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LST91A9D529\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm)AddLanguageSpecificTextSet("LST91A9D529\_4?cpp=%");  
    Chunk result.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True is a chunk was found, false if otherwise.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ChunkAddLanguageSpecificTextSet("LST91A9D529\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ChunkKeyedCollection Class](T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)