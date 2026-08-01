# M_GH_IO_Serialization_GH_Chunk_FindItem

﻿ GH\_Chunk.FindItem Method (String)

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
| GH\_ChunkAddLanguageSpecificTextSet("LST68A234C9\_0?cpp=::|nu=.");FindItem Method (String) |

Finds the first item that matches the given name.
Only items without index qualifiers are considered.
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
	string name
)
```

```
Public Function FindItem ( 
	name As String
) As GH_Item
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST68A234C9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to search for.

#### Return Value

Type: [GH\_Item](T_GH_IO_Types_GH_Item.htm)  
The item that matches the given name,
or null of no matching item could be found.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST68A234C9\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");FindItem(String)](M_GH_IO_Serialization_GH_IReader_FindItem.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[FindItem Overload](Overload_GH_IO_Serialization_GH_Chunk_FindItem.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)