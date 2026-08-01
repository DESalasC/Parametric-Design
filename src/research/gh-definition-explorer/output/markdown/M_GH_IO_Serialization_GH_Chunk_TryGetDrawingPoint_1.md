# M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint_1

﻿ GH\_Chunk.TryGetDrawingPoint Method (String, Int32, Point)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetDrawingPoint Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint.htm "TryGetDrawingPoint Method ")

[TryGetDrawingPoint Method (String, Point)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint.htm "TryGetDrawingPoint Method (String, Point)")

[TryGetDrawingPoint Method (String, Int32, Point)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint_1.htm "TryGetDrawingPoint Method (String, Int32, Point)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST3504C1E\_0?cpp=::|nu=.");TryGetDrawingPoint Method (String, Int32, PointAddLanguageSpecificTextSet("LST3504C1E\_1?cpp=%");) |

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
public bool TryGetDrawingPoint(
	string item_name,
	int item_index,
	ref Point value
)
```

```
Public Function TryGetDrawingPoint ( 
	item_name As String,
	item_index As Integer,
	ByRef value As Point
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST3504C1E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST3504C1E\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3504C1E\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Point](https://docs.microsoft.com/dotnet/api/system.drawing.point)AddLanguageSpecificTextSet("LST3504C1E\_5?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST3504C1E\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetDrawingPoint(String, Int32, PointAddLanguageSpecificTextSet("LST3504C1E\_7?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPoint_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetDrawingPoint Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)