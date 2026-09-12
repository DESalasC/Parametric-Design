# M_GH_IO_Serialization_GH_Chunk_SetDrawingBitmap

﻿ GH\_Chunk.SetDrawingBitmap Method (String, Bitmap)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetDrawingBitmap Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetDrawingBitmap.htm "SetDrawingBitmap Method ")

[SetDrawingBitmap Method (String, Bitmap)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingBitmap.htm "SetDrawingBitmap Method (String, Bitmap)")

[SetDrawingBitmap Method (String, Int32, Bitmap)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingBitmap_1.htm "SetDrawingBitmap Method (String, Int32, Bitmap)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTD9A1A073\_0?cpp=::|nu=.");SetDrawingBitmap Method (String, Bitmap) |

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
public void SetDrawingBitmap(
	string item_name,
	Bitmap item_value
)
```

```
Public Sub SetDrawingBitmap ( 
	item_name As String,
	item_value As Bitmap
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTD9A1A073\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTD9A1A073\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Bitmap](https://docs.microsoft.com/dotnet/api/system.drawing.bitmap)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LSTD9A1A073\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetDrawingBitmap(String, Bitmap)](M_GH_IO_Serialization_GH_IWriter_SetDrawingBitmap.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetDrawingBitmap Overload](Overload_GH_IO_Serialization_GH_Chunk_SetDrawingBitmap.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)