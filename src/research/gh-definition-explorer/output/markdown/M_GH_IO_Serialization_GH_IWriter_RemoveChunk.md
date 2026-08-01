# M_GH_IO_Serialization_GH_IWriter_RemoveChunk

﻿ GH\_IWriter.RemoveChunk Method (GH\_IChunk)

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
| GH\_IWriterAddLanguageSpecificTextSet("LST28284853\_0?cpp=::|nu=.");RemoveChunk Method (GH\_IChunk) |

Remove the specified chunk from the litter.

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
	GH_IChunk chunk
)
```

```
Function RemoveChunk ( 
	chunk As GH_IChunk
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

chunk
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LST28284853\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm)  
    Chunk to remove.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True is chunk was removed, false if chunk is not part of this litter.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](https://docs.microsoft.com/dotnet/api/system.argumentnullexception) | Thrown if chunk is a null reference. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[RemoveChunk Overload](Overload_GH_IO_Serialization_GH_IWriter_RemoveChunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)