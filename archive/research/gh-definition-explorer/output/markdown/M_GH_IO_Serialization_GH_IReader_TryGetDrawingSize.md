# M_GH_IO_Serialization_GH_IReader_TryGetDrawingSize

﻿ GH\_IReader.TryGetDrawingSize Method (String, Size)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

[TryGetDrawingSize Method](../html/Overload_GH_IO_Serialization_GH_IReader_TryGetDrawingSize.htm "TryGetDrawingSize Method ")

[TryGetDrawingSize Method (String, Size)](../html/M_GH_IO_Serialization_GH_IReader_TryGetDrawingSize.htm "TryGetDrawingSize Method (String, Size)")

[TryGetDrawingSize Method (String, Int32, Size)](../html/M_GH_IO_Serialization_GH_IReader_TryGetDrawingSize_1.htm "TryGetDrawingSize Method (String, Int32, Size)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReaderAddLanguageSpecificTextSet("LST576BDC2D\_0?cpp=::|nu=.");TryGetDrawingSize Method (String, SizeAddLanguageSpecificTextSet("LST576BDC2D\_1?cpp=%");) |

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
bool TryGetDrawingSize(
	string item_name,
	ref Size value
)
```

```
Function TryGetDrawingSize ( 
	item_name As String,
	ByRef value As Size
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST576BDC2D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST576BDC2D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Size](https://docs.microsoft.com/dotnet/api/system.drawing.size)AddLanguageSpecificTextSet("LST576BDC2D\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[TryGetDrawingSize Overload](Overload_GH_IO_Serialization_GH_IReader_TryGetDrawingSize.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)