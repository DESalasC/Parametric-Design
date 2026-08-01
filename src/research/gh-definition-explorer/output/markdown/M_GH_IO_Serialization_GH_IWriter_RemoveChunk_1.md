# M_GH_IO_Serialization_GH_IWriter_RemoveChunk_1

﻿ GH\_IWriter.RemoveChunk Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[RemoveChunk Method](../html/Overload_GH_IO_Serialization_GH_IWriter_RemoveChunk.htm "RemoveChunk Method ")

[RemoveChunk Method (GH\_IChunk)](../html/M_GH_IO_Serialization_GH_IWriter_RemoveChunk.htm "RemoveChunk Method (GH_IChunk)")

[RemoveChunk Method (String)](../html/M_GH_IO_Serialization_GH_IWriter_RemoveChunk_1.htm "RemoveChunk Method (String)")

[RemoveChunk Method (String, Int32)](../html/M_GH_IO_Serialization_GH_IWriter_RemoveChunk_2.htm "RemoveChunk Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LST7507E884\_0?cpp=::|nu=.");RemoveChunk Method (String) |

Remove the first chunk with a matching name.
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
bool RemoveChunk(
	string chunk_name
)
```

```
Function RemoveChunk ( 
	chunk_name As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

chunk\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST7507E884\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of chunk to remove.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True is chunk was removed, false if no matching chunk could be found.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[RemoveChunk Overload](Overload_GH_IO_Serialization_GH_IWriter_RemoveChunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)