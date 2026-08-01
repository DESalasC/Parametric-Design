# M_GH_IO_Serialization_GH_IReader_TryGetInterval2D_1

﻿ GH\_IReader.TryGetInterval2D Method (String, Int32, GH\_Interval2D)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

[TryGetInterval2D Method](../html/Overload_GH_IO_Serialization_GH_IReader_TryGetInterval2D.htm "TryGetInterval2D Method ")

[TryGetInterval2D Method (String, GH\_Interval2D)](../html/M_GH_IO_Serialization_GH_IReader_TryGetInterval2D.htm "TryGetInterval2D Method (String, GH_Interval2D)")

[TryGetInterval2D Method (String, Int32, GH\_Interval2D)](../html/M_GH_IO_Serialization_GH_IReader_TryGetInterval2D_1.htm "TryGetInterval2D Method (String, Int32, GH_Interval2D)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReaderAddLanguageSpecificTextSet("LSTCF05AC14\_0?cpp=::|nu=.");TryGetInterval2D Method (String, Int32, GH\_Interval2DAddLanguageSpecificTextSet("LSTCF05AC14\_1?cpp=%");) |

Gets the value of the item with the specified name and index.
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
bool TryGetInterval2D(
	string item_name,
	int item_index,
	ref GH_Interval2D value
)
```

```
Function TryGetInterval2D ( 
	item_name As String,
	item_index As Integer,
	ByRef value As GH_Interval2D
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTCF05AC14\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTCF05AC14\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LSTCF05AC14\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Interval2D](T_GH_IO_Types_GH_Interval2D.htm)AddLanguageSpecificTextSet("LSTCF05AC14\_5?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[TryGetInterval2D Overload](Overload_GH_IO_Serialization_GH_IReader_TryGetInterval2D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)