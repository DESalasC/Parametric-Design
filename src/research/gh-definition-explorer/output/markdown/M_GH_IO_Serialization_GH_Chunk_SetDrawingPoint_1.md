# M_GH_IO_Serialization_GH_Chunk_SetDrawingPoint_1

﻿ GH\_Chunk.SetDrawingPoint Method (String, Int32, Point)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetDrawingPoint Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetDrawingPoint.htm "SetDrawingPoint Method ")

[SetDrawingPoint Method (String, Point)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingPoint.htm "SetDrawingPoint Method (String, Point)")

[SetDrawingPoint Method (String, Int32, Point)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingPoint_1.htm "SetDrawingPoint Method (String, Int32, Point)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTF6BBA934\_0?cpp=::|nu=.");SetDrawingPoint Method (String, Int32, Point) |

Add a new data item to this chunk.
The combination of name and index must be unique or an exception will be thrown.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void SetDrawingPoint(
	string item_name,
	int item_index,
	Point item_value
)
```

```
Public Sub SetDrawingPoint ( 
	item_name As String,
	item_index As Integer,
	item_value As Point
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTF6BBA934\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTF6BBA934\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

item\_value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF6BBA934\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Point](https://docs.microsoft.com/dotnet/api/system.drawing.point)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LSTF6BBA934\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");SetDrawingPoint(String, Int32, Point)](M_GH_IO_Serialization_GH_IWriter_SetDrawingPoint_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetDrawingPoint Overload](Overload_GH_IO_Serialization_GH_Chunk_SetDrawingPoint.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)