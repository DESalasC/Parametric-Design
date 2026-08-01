# M_GH_IO_Serialization_GH_Chunk_TryGetPoint3D_1

﻿ GH\_Chunk.TryGetPoint3D Method (String, Int32, GH\_Point3D)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetPoint3D Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetPoint3D.htm "TryGetPoint3D Method ")

[TryGetPoint3D Method (String, GH\_Point3D)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetPoint3D.htm "TryGetPoint3D Method (String, GH_Point3D)")

[TryGetPoint3D Method (String, Int32, GH\_Point3D)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetPoint3D_1.htm "TryGetPoint3D Method (String, Int32, GH_Point3D)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTBC9943C8\_0?cpp=::|nu=.");TryGetPoint3D Method (String, Int32, GH\_Point3DAddLanguageSpecificTextSet("LSTBC9943C8\_1?cpp=%");) |

Gets the value of the item with the specified name and index.
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
public bool TryGetPoint3D(
	string item_name,
	int item_index,
	ref GH_Point3D value
)
```

```
Public Function TryGetPoint3D ( 
	item_name As String,
	item_index As Integer,
	ByRef value As GH_Point3D
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTBC9943C8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTBC9943C8\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LSTBC9943C8\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Point3D](T_GH_IO_Types_GH_Point3D.htm)AddLanguageSpecificTextSet("LSTBC9943C8\_5?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LSTBC9943C8\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetPoint3D(String, Int32, GH\_Point3DAddLanguageSpecificTextSet("LSTBC9943C8\_7?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetPoint3D_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetPoint3D Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetPoint3D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)