# M_GH_IO_Serialization_GH_Chunk_ChunkExists_1

﻿ GH\_Chunk.ChunkExists Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[ChunkExists Method](../html/Overload_GH_IO_Serialization_GH_Chunk_ChunkExists.htm "ChunkExists Method ")

[ChunkExists Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_ChunkExists.htm "ChunkExists Method (String)")

[ChunkExists Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_ChunkExists_1.htm "ChunkExists Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTCC4B4266\_0?cpp=::|nu=.");ChunkExists Method (String, Int32) |

Checks whether a chunk with the specified name and index exists in the litter.
Only chunks with index qualifiers are considered.
Name comparisons are not case-sensitive.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool ChunkExists(
	string name,
	int index
)
```

```
Public Function ChunkExists ( 
	name As String,
	index As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LSTCC4B4266\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of chunk to test for.

index
:   Type: [SystemAddLanguageSpecificTextSet("LSTCC4B4266\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of chunk to test for.
    If less than zero, ChunkExists(string name) is called instead.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if a chunk with the specified name and index exists, otherwise false.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LSTCC4B4266\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ChunkExists(String, Int32)](M_GH_IO_Serialization_GH_IReader_ChunkExists_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[ChunkExists Overload](Overload_GH_IO_Serialization_GH_Chunk_ChunkExists.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)