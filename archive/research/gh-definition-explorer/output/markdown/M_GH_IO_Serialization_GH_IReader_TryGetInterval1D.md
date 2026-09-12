# M_GH_IO_Serialization_GH_IReader_TryGetInterval1D

﻿ GH\_IReader.TryGetInterval1D Method (String, GH\_Interval1D)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

[TryGetInterval1D Method](../html/Overload_GH_IO_Serialization_GH_IReader_TryGetInterval1D.htm "TryGetInterval1D Method ")

[TryGetInterval1D Method (String, GH\_Interval1D)](../html/M_GH_IO_Serialization_GH_IReader_TryGetInterval1D.htm "TryGetInterval1D Method (String, GH_Interval1D)")

[TryGetInterval1D Method (String, Int32, GH\_Interval1D)](../html/M_GH_IO_Serialization_GH_IReader_TryGetInterval1D_1.htm "TryGetInterval1D Method (String, Int32, GH_Interval1D)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReaderAddLanguageSpecificTextSet("LST20796E4C\_0?cpp=::|nu=.");TryGetInterval1D Method (String, GH\_Interval1DAddLanguageSpecificTextSet("LST20796E4C\_1?cpp=%");) |

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
bool TryGetInterval1D(
	string item_name,
	ref GH_Interval1D value
)
```

```
Function TryGetInterval1D ( 
	item_name As String,
	ByRef value As GH_Interval1D
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST20796E4C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST20796E4C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Interval1D](T_GH_IO_Types_GH_Interval1D.htm)AddLanguageSpecificTextSet("LST20796E4C\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[TryGetInterval1D Overload](Overload_GH_IO_Serialization_GH_IReader_TryGetInterval1D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)