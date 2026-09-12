# M_GH_IO_Serialization_GH_IReader_TryGetPoint2D_1

﻿ GH\_IReader.TryGetPoint2D Method (String, Int32, GH\_Point2D)

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
| GH\_IReaderAddLanguageSpecificTextSet("LST20EBE72D\_0?cpp=::|nu=.");TryGetPoint2D Method (String, Int32, GH\_Point2DAddLanguageSpecificTextSet("LST20EBE72D\_1?cpp=%");) |

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
bool TryGetPoint2D(
	string item_name,
	int item_index,
	ref GH_Point2D value
)
```

```
Function TryGetPoint2D ( 
	item_name As String,
	item_index As Integer,
	ByRef value As GH_Point2D
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST20EBE72D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST20EBE72D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST20EBE72D\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Point2D](T_GH_IO_Types_GH_Point2D.htm)AddLanguageSpecificTextSet("LST20EBE72D\_5?cpp=%");  
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