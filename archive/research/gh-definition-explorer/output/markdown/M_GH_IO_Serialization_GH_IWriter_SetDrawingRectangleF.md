# M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangleF

﻿ GH\_IWriter.SetDrawingRectangleF Method (String, RectangleF)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetDrawingRectangleF Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDrawingRectangleF.htm "SetDrawingRectangleF Method ")

[SetDrawingRectangleF Method (String, RectangleF)](../html/M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangleF.htm "SetDrawingRectangleF Method (String, RectangleF)")

[SetDrawingRectangleF Method (String, Int32, RectangleF)](../html/M_GH_IO_Serialization_GH_IWriter_SetDrawingRectangleF_1.htm "SetDrawingRectangleF Method (String, Int32, RectangleF)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LST184E9B7\_0?cpp=::|nu=.");SetDrawingRectangleF Method (String, RectangleF) |

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
void SetDrawingRectangleF(
	string item_name,
	RectangleF item_value
)
```

```
Sub SetDrawingRectangleF ( 
	item_name As String,
	item_value As RectangleF
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST184E9B7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST184E9B7\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetDrawingRectangleF Overload](Overload_GH_IO_Serialization_GH_IWriter_SetDrawingRectangleF.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)