# M_GH_IO_Serialization_GH_IReader_GetDouble_1

﻿ GH\_IReader.GetDouble Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

[GetDouble Method](../html/Overload_GH_IO_Serialization_GH_IReader_GetDouble.htm "GetDouble Method ")

[GetDouble Method (String)](../html/M_GH_IO_Serialization_GH_IReader_GetDouble.htm "GetDouble Method (String)")

[GetDouble Method (String, Int32)](../html/M_GH_IO_Serialization_GH_IReader_GetDouble_1.htm "GetDouble Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReaderAddLanguageSpecificTextSet("LSTDD3BB55C\_0?cpp=::|nu=.");GetDouble Method (String, Int32) |

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
double GetDouble(
	string item_name,
	int item_index
)
```

```
Function GetDouble ( 
	item_name As String,
	item_index As Integer
) As Double
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTDD3BB55C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTDD3BB55C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

#### Return Value

Type: [Double](https://docs.microsoft.com/dotnet/api/system.double)  
The inner value of the item.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [OverflowException](https://docs.microsoft.com/dotnet/api/system.overflowexception) | Thrown if the type conversion fails. |
| [InvalidCastException](https://docs.microsoft.com/dotnet/api/system.invalidcastexception) | Thrown if the type conversion is invalid. |
| [NullReferenceException](https://docs.microsoft.com/dotnet/api/system.nullreferenceexception) | Thrown if the item with the specified name and index does not exist. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[GetDouble Overload](Overload_GH_IO_Serialization_GH_IReader_GetDouble.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)