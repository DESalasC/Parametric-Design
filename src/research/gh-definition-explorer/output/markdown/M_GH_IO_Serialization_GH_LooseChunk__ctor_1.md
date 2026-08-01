# M_GH_IO_Serialization_GH_LooseChunk__ctor_1

﻿ GH\_LooseChunk Constructor (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_LooseChunk Class](../html/T_GH_IO_Serialization_GH_LooseChunk.htm "GH_LooseChunk Class")

[GH\_LooseChunk Constructor](../html/Overload_GH_IO_Serialization_GH_LooseChunk__ctor.htm "GH_LooseChunk Constructor ")

[GH\_LooseChunk Constructor (String)](../html/M_GH_IO_Serialization_GH_LooseChunk__ctor.htm "GH_LooseChunk Constructor (String)")

[GH\_LooseChunk Constructor (String, Int32)](../html/M_GH_IO_Serialization_GH_LooseChunk__ctor_1.htm "GH_LooseChunk Constructor (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LooseChunk Constructor (String, Int32) |

Create a new loose chunk. A loose chunk does not have an owner archive
and thus cannot store runtime messages.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_LooseChunk(
	string chunk_name,
	int chunk_index
)
```

```
Public Sub New ( 
	chunk_name As String,
	chunk_index As Integer
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

chunk\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST5E16E584\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of this chunk.

chunk\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST5E16E584\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of this chunk, negative one for no index.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_LooseChunk Class](T_GH_IO_Serialization_GH_LooseChunk.htm)

[GH\_LooseChunk Overload](Overload_GH_IO_Serialization_GH_LooseChunk__ctor.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)