# M_GH_IO_Serialization_GH_Chunk_CreateChunk_1

﻿ GH\_Chunk.CreateChunk Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[CreateChunk Method](../html/Overload_GH_IO_Serialization_GH_Chunk_CreateChunk.htm "CreateChunk Method ")

[CreateChunk Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_CreateChunk.htm "CreateChunk Method (String)")

[CreateChunk Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_CreateChunk_1.htm "CreateChunk Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST60B67249\_0?cpp=::|nu=.");CreateChunk Method (String, Int32) |

Create a new child chunk with the specified name and index qualifier.
If another chunk already exists with similar properties, an exception will be thrown.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_IWriter CreateChunk(
	string chunk_name,
	int chunk_index
)
```

```
Public Function CreateChunk ( 
	chunk_name As String,
	chunk_index As Integer
) As GH_IWriter
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

chunk\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST60B67249\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of new child.

chunk\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST60B67249\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of new child.

#### Return Value

Type: [GH\_IWriter](T_GH_IO_Serialization_GH_IWriter.htm)  
The newly created child chunk.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST60B67249\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");CreateChunk(String, Int32)](M_GH_IO_Serialization_GH_IWriter_CreateChunk_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [ArgumentException](https://docs.microsoft.com/dotnet/api/system.argumentexception) | Thrown if the name+index coordinte is already occupied by another chunk. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[CreateChunk Overload](Overload_GH_IO_Serialization_GH_Chunk_CreateChunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)