# M_GH_IO_Serialization_GH_Chunk_SetDrawingSize_1

﻿ GH\_Chunk.SetDrawingSize Method (String, Int32, Size)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetDrawingSize Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetDrawingSize.htm "SetDrawingSize Method ")

[SetDrawingSize Method (String, Size)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingSize.htm "SetDrawingSize Method (String, Size)")

[SetDrawingSize Method (String, Int32, Size)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingSize_1.htm "SetDrawingSize Method (String, Int32, Size)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTF48CC905\_0?cpp=::|nu=.");SetDrawingSize Method (String, Int32, Size) |

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
public void SetDrawingSize(
	string item_name,
	int item_index,
	Size item_value
)
```

```
Public Sub SetDrawingSize ( 
	item_name As String,
	item_index As Integer,
	item_value As Size
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTF48CC905\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTF48CC905\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

item\_value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF48CC905\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Size](https://docs.microsoft.com/dotnet/api/system.drawing.size)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LSTF48CC905\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");SetDrawingSize(String, Int32, Size)](M_GH_IO_Serialization_GH_IWriter_SetDrawingSize_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetDrawingSize Overload](Overload_GH_IO_Serialization_GH_Chunk_SetDrawingSize.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)