# M_GH_IO_Serialization_GH_Chunk_ItemExists

﻿ GH\_Chunk.ItemExists Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[ItemExists Method](../html/Overload_GH_IO_Serialization_GH_Chunk_ItemExists.htm "ItemExists Method ")

[ItemExists Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_ItemExists.htm "ItemExists Method (String)")

[ItemExists Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_ItemExists_1.htm "ItemExists Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST7FA815D5\_0?cpp=::|nu=.");ItemExists Method (String) |

Gets the occupancy for a specific item name. Only items without index qualifiers are considered.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool ItemExists(
	string name
)
```

```
Public Function ItemExists ( 
	name As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST7FA815D5\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to check for.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if an item with a similar name already exists, false if not.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST7FA815D5\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ItemExists(String)](M_GH_IO_Serialization_GH_IReader_ItemExists.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[ItemExists Overload](Overload_GH_IO_Serialization_GH_Chunk_ItemExists.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)