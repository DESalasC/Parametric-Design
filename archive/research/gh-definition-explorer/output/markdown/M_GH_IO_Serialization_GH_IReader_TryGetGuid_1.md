# M_GH_IO_Serialization_GH_IReader_TryGetGuid_1

﻿ GH\_IReader.TryGetGuid Method (String, Int32, Guid)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

[TryGetGuid Method](../html/Overload_GH_IO_Serialization_GH_IReader_TryGetGuid.htm "TryGetGuid Method ")

[TryGetGuid Method (String, Guid)](../html/M_GH_IO_Serialization_GH_IReader_TryGetGuid.htm "TryGetGuid Method (String, Guid)")

[TryGetGuid Method (String, Int32, Guid)](../html/M_GH_IO_Serialization_GH_IReader_TryGetGuid_1.htm "TryGetGuid Method (String, Int32, Guid)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReaderAddLanguageSpecificTextSet("LST841A1785\_0?cpp=::|nu=.");TryGetGuid Method (String, Int32, GuidAddLanguageSpecificTextSet("LST841A1785\_1?cpp=%");) |

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
bool TryGetGuid(
	string item_name,
	int item_index,
	ref Guid value
)
```

```
Function TryGetGuid ( 
	item_name As String,
	item_index As Integer,
	ByRef value As Guid
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST841A1785\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST841A1785\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

value
:   Type: [SystemAddLanguageSpecificTextSet("LST841A1785\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LST841A1785\_5?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[TryGetGuid Overload](Overload_GH_IO_Serialization_GH_IReader_TryGetGuid.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)