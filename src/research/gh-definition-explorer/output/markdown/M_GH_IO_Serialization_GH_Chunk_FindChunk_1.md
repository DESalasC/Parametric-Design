# M_GH_IO_Serialization_GH_Chunk_FindChunk_1

﻿ GH\_Chunk.FindChunk Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[FindChunk Method](../html/Overload_GH_IO_Serialization_GH_Chunk_FindChunk.htm "FindChunk Method ")

[FindChunk Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_FindChunk.htm "FindChunk Method (String)")

[FindChunk Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_FindChunk_1.htm "FindChunk Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST34660E0\_0?cpp=::|nu=.");FindChunk Method (String, Int32) |

Finds the first chunk in the list that matches the given name and index.
Only chunks with index qualifiers are considered.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_IReader FindChunk(
	string name,
	int index
)
```

```
Public Function FindChunk ( 
	name As String,
	index As Integer
) As GH_IReader
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST34660E0\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of chunk to search for.

index
:   Type: [SystemAddLanguageSpecificTextSet("LST34660E0\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of chunk to search for.
    If less than zero, FindChunk(string chunk\_name) is called instead.

#### Return Value

Type: [GH\_IReader](T_GH_IO_Serialization_GH_IReader.htm)  
The child chunk that matches the given name and index,
or null of no matching chunk could be found.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST34660E0\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");FindChunk(String, Int32)](M_GH_IO_Serialization_GH_IReader_FindChunk_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[FindChunk Overload](Overload_GH_IO_Serialization_GH_Chunk_FindChunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)