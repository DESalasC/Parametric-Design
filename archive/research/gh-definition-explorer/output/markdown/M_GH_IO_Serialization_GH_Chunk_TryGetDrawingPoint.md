# M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint

﻿ GH\_Chunk.TryGetDrawingPoint Method (String, Point)

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
| GH\_ChunkAddLanguageSpecificTextSet("LST27513747\_0?cpp=::|nu=.");TryGetDrawingPoint Method (String, PointAddLanguageSpecificTextSet("LST27513747\_1?cpp=%");) |

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
public bool TryGetDrawingPoint(
	string item_name,
	ref Point value
)
```

```
Public Function TryGetDrawingPoint ( 
	item_name As String,
	ByRef value As Point
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST27513747\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST27513747\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Point](https://docs.microsoft.com/dotnet/api/system.drawing.point)AddLanguageSpecificTextSet("LST27513747\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST27513747\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetDrawingPoint(String, PointAddLanguageSpecificTextSet("LST27513747\_6?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPoint.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetDrawingPoint Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetDrawingPoint.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)