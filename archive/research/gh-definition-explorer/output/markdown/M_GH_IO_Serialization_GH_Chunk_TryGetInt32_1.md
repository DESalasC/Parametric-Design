# M_GH_IO_Serialization_GH_Chunk_TryGetInt32_1

﻿ GH\_Chunk.TryGetInt32 Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetInt32 Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetInt32.htm "TryGetInt32 Method ")

[TryGetInt32 Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetInt32_1.htm "TryGetInt32 Method (String, Int32)")

[TryGetInt32 Method (String, Int32, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetInt32.htm "TryGetInt32 Method (String, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST5A47C06F\_0?cpp=::|nu=.");TryGetInt32 Method (String, Int32AddLanguageSpecificTextSet("LST5A47C06F\_1?cpp=%");) |

Gets the value of the item with the specified name.
Name comparison is not case-sensitive.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool TryGetInt32(
	string item_name,
	ref int value
)
```

```
Public Function TryGetInt32 ( 
	item_name As String,
	ByRef value As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST5A47C06F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [SystemAddLanguageSpecificTextSet("LST5A47C06F\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST5A47C06F\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST5A47C06F\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetInt32(String, Int32AddLanguageSpecificTextSet("LST5A47C06F\_6?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetInt32_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetInt32 Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetInt32.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)