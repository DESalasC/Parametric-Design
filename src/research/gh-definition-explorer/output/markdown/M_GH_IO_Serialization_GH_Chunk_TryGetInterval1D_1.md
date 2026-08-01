# M_GH_IO_Serialization_GH_Chunk_TryGetInterval1D_1

﻿ GH\_Chunk.TryGetInterval1D Method (String, Int32, GH\_Interval1D)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetInterval1D Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetInterval1D.htm "TryGetInterval1D Method ")

[TryGetInterval1D Method (String, GH\_Interval1D)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetInterval1D.htm "TryGetInterval1D Method (String, GH_Interval1D)")

[TryGetInterval1D Method (String, Int32, GH\_Interval1D)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetInterval1D_1.htm "TryGetInterval1D Method (String, Int32, GH_Interval1D)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST63F78D81\_0?cpp=::|nu=.");TryGetInterval1D Method (String, Int32, GH\_Interval1DAddLanguageSpecificTextSet("LST63F78D81\_1?cpp=%");) |

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
public bool TryGetInterval1D(
	string item_name,
	int item_index,
	ref GH_Interval1D value
)
```

```
Public Function TryGetInterval1D ( 
	item_name As String,
	item_index As Integer,
	ByRef value As GH_Interval1D
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST63F78D81\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST63F78D81\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST63F78D81\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Interval1D](T_GH_IO_Types_GH_Interval1D.htm)AddLanguageSpecificTextSet("LST63F78D81\_5?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST63F78D81\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetInterval1D(String, Int32, GH\_Interval1DAddLanguageSpecificTextSet("LST63F78D81\_7?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetInterval1D_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetInterval1D Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetInterval1D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)