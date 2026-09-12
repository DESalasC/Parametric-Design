# M_GH_IO_Serialization_GH_Chunk_FindItem_1

﻿ GH\_Chunk.FindItem Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[FindItem Method](../html/Overload_GH_IO_Serialization_GH_Chunk_FindItem.htm "FindItem Method ")

[FindItem Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_FindItem.htm "FindItem Method (String)")

[FindItem Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_FindItem_1.htm "FindItem Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST98A742C7\_0?cpp=::|nu=.");FindItem Method (String, Int32) |

Finds the first item that matches the given name and index.
Only items with index qualifiers are considered.
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
public GH_Item FindItem(
	string name,
	int index
)
```

```
Public Function FindItem ( 
	name As String,
	index As Integer
) As GH_Item
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST98A742C7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to search for.

index
:   Type: [SystemAddLanguageSpecificTextSet("LST98A742C7\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to search for.
    If less than zero, then FindItem(string name) is called instead.

#### Return Value

Type: [GH\_Item](T_GH_IO_Types_GH_Item.htm)  
The item that matches the given name and index,
or null of no matching item could be found.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST98A742C7\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");FindItem(String, Int32)](M_GH_IO_Serialization_GH_IReader_FindItem_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[FindItem Overload](Overload_GH_IO_Serialization_GH_Chunk_FindItem.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)