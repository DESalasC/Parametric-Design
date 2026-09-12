# M_GH_IO_Serialization_GH_Chunk_RemoveChunk_2

﻿ GH\_Chunk.RemoveChunk Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[RemoveChunk Method](../html/Overload_GH_IO_Serialization_GH_Chunk_RemoveChunk.htm "RemoveChunk Method ")

[RemoveChunk Method (GH\_IChunk)](../html/M_GH_IO_Serialization_GH_Chunk_RemoveChunk.htm "RemoveChunk Method (GH_IChunk)")

[RemoveChunk Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_RemoveChunk_1.htm "RemoveChunk Method (String)")

[RemoveChunk Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_RemoveChunk_2.htm "RemoveChunk Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTC0184D5D\_0?cpp=::|nu=.");RemoveChunk Method (String, Int32) |

Remove the first chunk with a matching name and index.
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
public bool RemoveChunk(
	string chunk_name,
	int chunk_index
)
```

```
Public Function RemoveChunk ( 
	chunk_name As String,
	chunk_index As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

chunk\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTC0184D5D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of chunk to remove.

chunk\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTC0184D5D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of chunk to remove.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True is chunk was removed, false if no matching chunk could be found.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LSTC0184D5D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");RemoveChunk(String, Int32)](M_GH_IO_Serialization_GH_IWriter_RemoveChunk_2.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[RemoveChunk Overload](Overload_GH_IO_Serialization_GH_Chunk_RemoveChunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)