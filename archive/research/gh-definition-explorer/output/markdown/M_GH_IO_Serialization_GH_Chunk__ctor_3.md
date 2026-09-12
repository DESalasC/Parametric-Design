# M_GH_IO_Serialization_GH_Chunk__ctor_3

﻿ GH\_Chunk Constructor (GH\_Archive, String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Constructor](../html/Overload_GH_IO_Serialization_GH_Chunk__ctor.htm "GH_Chunk Constructor ")

[GH\_Chunk Constructor](../html/M_GH_IO_Serialization_GH_Chunk__ctor.htm "GH_Chunk Constructor ")

[GH\_Chunk Constructor (GH\_Archive)](../html/M_GH_IO_Serialization_GH_Chunk__ctor_1.htm "GH_Chunk Constructor (GH_Archive)")

[GH\_Chunk Constructor (GH\_Archive, String)](../html/M_GH_IO_Serialization_GH_Chunk__ctor_2.htm "GH_Chunk Constructor (GH_Archive, String)")

[GH\_Chunk Constructor (GH\_Archive, String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk__ctor_3.htm "GH_Chunk Constructor (GH_Archive, String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Chunk Constructor (GH\_Archive, String, Int32) |

Constructor. You typically do not need to create your own Chunks. The GH\_Archive class
will create top-level chunks and existing chunks can create child chunks.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected GH_Chunk(
	GH_Archive chunk_archive,
	string chunk_name,
	int chunk_index
)
```

```
Protected Sub New ( 
	chunk_archive As GH_Archive,
	chunk_name As String,
	chunk_index As Integer
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

chunk\_archive
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LST923FC932\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Archive](T_GH_IO_Serialization_GH_Archive.htm)  
    Owner archive.

chunk\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST923FC932\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of this chunk.

chunk\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST923FC932\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of this chunk.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[GH\_Chunk Overload](Overload_GH_IO_Serialization_GH_Chunk__ctor.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)