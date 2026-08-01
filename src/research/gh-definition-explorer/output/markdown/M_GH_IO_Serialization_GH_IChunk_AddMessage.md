# M_GH_IO_Serialization_GH_IChunk_AddMessage

﻿ GH\_IChunk.AddMessage Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IChunk Interface](../html/T_GH_IO_Serialization_GH_IChunk.htm "GH_IChunk Interface")

[GH\_IChunk Methods](../html/Methods_T_GH_IO_Serialization_GH_IChunk.htm "GH_IChunk Methods")

[AddMessage Method](../html/M_GH_IO_Serialization_GH_IChunk_AddMessage.htm "AddMessage Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IChunkAddLanguageSpecificTextSet("LSTD2487C04\_0?cpp=::|nu=.");AddMessage Method |

Log a new message with the top-level archive.
Messages are collected during read/write operations,
and can be displayed to the user upon completion using GH\_Archive.ShowMessageLog().

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void AddMessage(
	string m,
	GH_Message_Type t
)
```

```
Sub AddMessage ( 
	m As String,
	t As GH_Message_Type
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

m
:   Type: [SystemAddLanguageSpecificTextSet("LSTD2487C04\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Message text.

t
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LSTD2487C04\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Message\_Type](T_GH_IO_Serialization_GH_Message_Type.htm)  
    Message type.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IChunk Interface](T_GH_IO_Serialization_GH_IChunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)