# M_GH_IO_Serialization_GH_IReader_TryGetPoint2D

﻿ GH\_IReader.TryGetPoint2D Method (String, GH\_Point2D)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

[TryGetPoint2D Method](../html/Overload_GH_IO_Serialization_GH_IReader_TryGetPoint2D.htm "TryGetPoint2D Method ")

[TryGetPoint2D Method (String, GH\_Point2D)](../html/M_GH_IO_Serialization_GH_IReader_TryGetPoint2D.htm "TryGetPoint2D Method (String, GH_Point2D)")

[TryGetPoint2D Method (String, Int32, GH\_Point2D)](../html/M_GH_IO_Serialization_GH_IReader_TryGetPoint2D_1.htm "TryGetPoint2D Method (String, Int32, GH_Point2D)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReaderAddLanguageSpecificTextSet("LSTC08CF884\_0?cpp=::|nu=.");TryGetPoint2D Method (String, GH\_Point2DAddLanguageSpecificTextSet("LSTC08CF884\_1?cpp=%");) |

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
bool TryGetPoint2D(
	string item_name,
	ref GH_Point2D value
)
```

```
Function TryGetPoint2D ( 
	item_name As String,
	ByRef value As GH_Point2D
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTC08CF884\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LSTC08CF884\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Point2D](T_GH_IO_Types_GH_Point2D.htm)AddLanguageSpecificTextSet("LSTC08CF884\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[TryGetPoint2D Overload](Overload_GH_IO_Serialization_GH_IReader_TryGetPoint2D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)