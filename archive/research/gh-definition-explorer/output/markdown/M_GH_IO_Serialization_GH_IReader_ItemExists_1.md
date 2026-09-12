# M_GH_IO_Serialization_GH_IReader_ItemExists_1

﻿ GH\_IReader.ItemExists Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

[ItemExists Method](../html/Overload_GH_IO_Serialization_GH_IReader_ItemExists.htm "ItemExists Method ")

[ItemExists Method (String)](../html/M_GH_IO_Serialization_GH_IReader_ItemExists.htm "ItemExists Method (String)")

[ItemExists Method (String, Int32)](../html/M_GH_IO_Serialization_GH_IReader_ItemExists_1.htm "ItemExists Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReaderAddLanguageSpecificTextSet("LST4BB48A9C\_0?cpp=::|nu=.");ItemExists Method (String, Int32) |

Checks whether an item with the specified name and index exists.
Only items with index qualifiers are considered.
Name comparisons are not case-sensitive.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool ItemExists(
	string name,
	int index
)
```

```
Function ItemExists ( 
	name As String,
	index As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST4BB48A9C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to test for.

index
:   Type: [SystemAddLanguageSpecificTextSet("LST4BB48A9C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to test for.
    If index is less than zero, then ItemExists(string name) is called instead.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if an item with the specified name and index exists, otherwise false.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[ItemExists Overload](Overload_GH_IO_Serialization_GH_IReader_ItemExists.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)