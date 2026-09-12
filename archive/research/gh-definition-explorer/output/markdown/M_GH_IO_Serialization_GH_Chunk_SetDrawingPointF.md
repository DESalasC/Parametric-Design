# M_GH_IO_Serialization_GH_Chunk_SetDrawingPointF

﻿ GH\_Chunk.SetDrawingPointF Method (String, PointF)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetDrawingPointF Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetDrawingPointF.htm "SetDrawingPointF Method ")

[SetDrawingPointF Method (String, PointF)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingPointF.htm "SetDrawingPointF Method (String, PointF)")

[SetDrawingPointF Method (String, Int32, PointF)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingPointF_1.htm "SetDrawingPointF Method (String, Int32, PointF)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST8B81E7A3\_0?cpp=::|nu=.");SetDrawingPointF Method (String, PointF) |

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
public void SetDrawingPointF(
	string item_name,
	PointF item_value
)
```

```
Public Sub SetDrawingPointF ( 
	item_name As String,
	item_value As PointF
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST8B81E7A3\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST8B81E7A3\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST8B81E7A3\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetDrawingPointF(String, PointF)](M_GH_IO_Serialization_GH_IWriter_SetDrawingPointF.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetDrawingPointF Overload](Overload_GH_IO_Serialization_GH_Chunk_SetDrawingPointF.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)