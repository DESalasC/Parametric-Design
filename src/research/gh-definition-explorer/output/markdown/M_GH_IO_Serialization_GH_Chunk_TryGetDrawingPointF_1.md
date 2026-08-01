# M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPointF_1

﻿ GH\_Chunk.TryGetDrawingPointF Method (String, Int32, PointF)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetDrawingPointF Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetDrawingPointF.htm "TryGetDrawingPointF Method ")

[TryGetDrawingPointF Method (String, PointF)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPointF.htm "TryGetDrawingPointF Method (String, PointF)")

[TryGetDrawingPointF Method (String, Int32, PointF)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetDrawingPointF_1.htm "TryGetDrawingPointF Method (String, Int32, PointF)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST6E35E958\_0?cpp=::|nu=.");TryGetDrawingPointF Method (String, Int32, PointFAddLanguageSpecificTextSet("LST6E35E958\_1?cpp=%");) |

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
public bool TryGetDrawingPointF(
	string item_name,
	int item_index,
	ref PointF value
)
```

```
Public Function TryGetDrawingPointF ( 
	item_name As String,
	item_index As Integer,
	ByRef value As PointF
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST6E35E958\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST6E35E958\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST6E35E958\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)AddLanguageSpecificTextSet("LST6E35E958\_5?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST6E35E958\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetDrawingPointF(String, Int32, PointFAddLanguageSpecificTextSet("LST6E35E958\_7?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingPointF_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetDrawingPointF Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetDrawingPointF.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)