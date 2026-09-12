# M_GH_IO_Serialization_GH_Chunk_RemoveItem_1

﻿ GH\_Chunk.RemoveItem Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[RemoveItem Method](../html/Overload_GH_IO_Serialization_GH_Chunk_RemoveItem.htm "RemoveItem Method ")

[RemoveItem Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_RemoveItem.htm "RemoveItem Method (String)")

[RemoveItem Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_RemoveItem_1.htm "RemoveItem Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST7B9E5019\_0?cpp=::|nu=.");RemoveItem Method (String, Int32) |

Remove an indexed item from this chunk.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool RemoveItem(
	string itemName,
	int itemIndex
)
```

```
Public Function RemoveItem ( 
	itemName As String,
	itemIndex As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

itemName
:   Type: [SystemAddLanguageSpecificTextSet("LST7B9E5019\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item.

itemIndex
:   Type: [SystemAddLanguageSpecificTextSet("LST7B9E5019\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST7B9E5019\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");RemoveItem(String, Int32)](M_GH_IO_Serialization_GH_IWriter_RemoveItem_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[RemoveItem Overload](Overload_GH_IO_Serialization_GH_Chunk_RemoveItem.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)