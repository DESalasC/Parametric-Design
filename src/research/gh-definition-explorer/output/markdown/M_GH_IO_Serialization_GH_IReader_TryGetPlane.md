# M_GH_IO_Serialization_GH_IReader_TryGetPlane

﻿ GH\_IReader.TryGetPlane Method (String, GH\_Plane)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

[TryGetPlane Method](../html/Overload_GH_IO_Serialization_GH_IReader_TryGetPlane.htm "TryGetPlane Method ")

[TryGetPlane Method (String, GH\_Plane)](../html/M_GH_IO_Serialization_GH_IReader_TryGetPlane.htm "TryGetPlane Method (String, GH_Plane)")

[TryGetPlane Method (String, Int32, GH\_Plane)](../html/M_GH_IO_Serialization_GH_IReader_TryGetPlane_1.htm "TryGetPlane Method (String, Int32, GH_Plane)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReaderAddLanguageSpecificTextSet("LST11D162BE\_0?cpp=::|nu=.");TryGetPlane Method (String, GH\_PlaneAddLanguageSpecificTextSet("LST11D162BE\_1?cpp=%");) |

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
bool TryGetPlane(
	string item_name,
	ref GH_Plane value
)
```

```
Function TryGetPlane ( 
	item_name As String,
	ByRef value As GH_Plane
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST11D162BE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST11D162BE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Plane](T_GH_IO_Types_GH_Plane.htm)AddLanguageSpecificTextSet("LST11D162BE\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[TryGetPlane Overload](Overload_GH_IO_Serialization_GH_IReader_TryGetPlane.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)