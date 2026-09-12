# M_GH_IO_Serialization_GH_Chunk_ChunkExists

﻿ GH\_Chunk.ChunkExists Method (String)

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
| GH\_ChunkAddLanguageSpecificTextSet("LST1B06D16C\_0?cpp=::|nu=.");ChunkExists Method (String) |

Checks whether a chunk with the specified name exists in the litter.
Only chunks without index qualifiers are considered.
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
	string name
)
```

```
Public Function ChunkExists ( 
	name As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST1B06D16C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of chunk to test for.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if a chunk with the specified name exists, otherwise false.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST1B06D16C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ChunkExists(String)](M_GH_IO_Serialization_GH_IReader_ChunkExists.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[ChunkExists Overload](Overload_GH_IO_Serialization_GH_Chunk_ChunkExists.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)