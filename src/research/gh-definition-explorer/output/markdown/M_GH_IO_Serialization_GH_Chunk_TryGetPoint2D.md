# M_GH_IO_Serialization_GH_Chunk_TryGetPoint2D

﻿ GH\_Chunk.TryGetPoint2D Method (String, GH\_Point2D)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetPoint2D Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetPoint2D.htm "TryGetPoint2D Method ")

[TryGetPoint2D Method (String, GH\_Point2D)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetPoint2D.htm "TryGetPoint2D Method (String, GH_Point2D)")

[TryGetPoint2D Method (String, Int32, GH\_Point2D)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetPoint2D_1.htm "TryGetPoint2D Method (String, Int32, GH_Point2D)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTBAFA547D\_0?cpp=::|nu=.");TryGetPoint2D Method (String, GH\_Point2DAddLanguageSpecificTextSet("LSTBAFA547D\_1?cpp=%");) |

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
public bool TryGetPoint2D(
	string item_name,
	ref GH_Point2D value
)
```

```
Public Function TryGetPoint2D ( 
	item_name As String,
	ByRef value As GH_Point2D
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTBAFA547D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LSTBAFA547D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Point2D](T_GH_IO_Types_GH_Point2D.htm)AddLanguageSpecificTextSet("LSTBAFA547D\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LSTBAFA547D\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetPoint2D(String, GH\_Point2DAddLanguageSpecificTextSet("LSTBAFA547D\_6?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetPoint2D.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetPoint2D Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetPoint2D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)