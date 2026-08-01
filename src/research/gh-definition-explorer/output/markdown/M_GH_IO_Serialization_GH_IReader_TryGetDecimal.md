# M_GH_IO_Serialization_GH_IReader_TryGetDecimal

﻿ GH\_IReader.TryGetDecimal Method (String, Decimal)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

[TryGetDecimal Method](../html/Overload_GH_IO_Serialization_GH_IReader_TryGetDecimal.htm "TryGetDecimal Method ")

[TryGetDecimal Method (String, Decimal)](../html/M_GH_IO_Serialization_GH_IReader_TryGetDecimal.htm "TryGetDecimal Method (String, Decimal)")

[TryGetDecimal Method (String, Int32, Decimal)](../html/M_GH_IO_Serialization_GH_IReader_TryGetDecimal_1.htm "TryGetDecimal Method (String, Int32, Decimal)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReaderAddLanguageSpecificTextSet("LSTC4F2FEF3\_0?cpp=::|nu=.");TryGetDecimal Method (String, DecimalAddLanguageSpecificTextSet("LSTC4F2FEF3\_1?cpp=%");) |

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
bool TryGetDecimal(
	string item_name,
	ref decimal value
)
```

```
Function TryGetDecimal ( 
	item_name As String,
	ByRef value As Decimal
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTC4F2FEF3\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [SystemAddLanguageSpecificTextSet("LSTC4F2FEF3\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Decimal](https://docs.microsoft.com/dotnet/api/system.decimal)AddLanguageSpecificTextSet("LSTC4F2FEF3\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[TryGetDecimal Overload](Overload_GH_IO_Serialization_GH_IReader_TryGetDecimal.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)