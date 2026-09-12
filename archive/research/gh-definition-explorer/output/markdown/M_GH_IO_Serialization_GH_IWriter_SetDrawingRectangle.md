# M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangle

﻿ GH\_IWriter.SetDrawingRectangle Method (String, Rectangle)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetDrawingRectangle Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDrawingRectangle.htm "SetDrawingRectangle Method ")

[SetDrawingRectangle Method (String, Rectangle)](../html/M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangle.htm "SetDrawingRectangle Method (String, Rectangle)")

[SetDrawingRectangle Method (String, Int32, Rectangle)](../html/M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangle_1.htm "SetDrawingRectangle Method (String, Int32, Rectangle)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LSTD9EA704\_0?cpp=::|nu=.");SetDrawingRectangle Method (String, Rectangle) |

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
void SetDrawingRectangle(
	string item_name,
	Rectangle item_value
)
```

```
Sub SetDrawingRectangle ( 
	item_name As String,
	item_value As Rectangle
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTD9EA704\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTD9EA704\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetDrawingRectangle Overload](Overload_GH_IO_Serialization_GH_IWriter_SetDrawingRectangle.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)