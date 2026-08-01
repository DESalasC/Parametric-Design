# M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangleF

﻿ GH\_Chunk.SetDrawingRectangleF Method (String, RectangleF)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetDrawingRectangleF Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetDrawingRectangleF.htm "SetDrawingRectangleF Method ")

[SetDrawingRectangleF Method (String, RectangleF)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangleF.htm "SetDrawingRectangleF Method (String, RectangleF)")

[SetDrawingRectangleF Method (String, Int32, RectangleF)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingRectangleF_1.htm "SetDrawingRectangleF Method (String, Int32, RectangleF)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTC20524D4\_0?cpp=::|nu=.");SetDrawingRectangleF Method (String, RectangleF) |

Add a new data item to this chunk.
The name must be unique or an exception will be thrown.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void SetDrawingRectangleF(
	string item_name,
	RectangleF item_value
)
```

```
Public Sub SetDrawingRectangleF ( 
	item_name As String,
	item_value As RectangleF
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTC20524D4\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTC20524D4\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LSTC20524D4\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetDrawingRectangleF(String, RectangleF)](M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangleF.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetDrawingRectangleF Overload](Overload_GH_IO_Serialization_GH_Chunk_SetDrawingRectangleF.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)