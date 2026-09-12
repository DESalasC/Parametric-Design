# M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangle

﻿ GH\_Chunk.TryGetDrawingRectangle Method (String, Rectangle)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetDrawingRectangle Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangle.htm "TryGetDrawingRectangle Method ")

[TryGetDrawingRectangle Method (String, Rectangle)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangle.htm "TryGetDrawingRectangle Method (String, Rectangle)")

[TryGetDrawingRectangle Method (String, Int32, Rectangle)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangle_1.htm "TryGetDrawingRectangle Method (String, Int32, Rectangle)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTC4574F1E\_0?cpp=::|nu=.");TryGetDrawingRectangle Method (String, RectangleAddLanguageSpecificTextSet("LSTC4574F1E\_1?cpp=%");) |

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
public bool TryGetDrawingRectangle(
	string item_name,
	ref Rectangle value
)
```

```
Public Function TryGetDrawingRectangle ( 
	item_name As String,
	ByRef value As Rectangle
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTC4574F1E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTC4574F1E\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)AddLanguageSpecificTextSet("LSTC4574F1E\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LSTC4574F1E\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetDrawingRectangle(String, RectangleAddLanguageSpecificTextSet("LSTC4574F1E\_6?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingRectangle.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetDrawingRectangle Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetDrawingRectangle.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)