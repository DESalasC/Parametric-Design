# M_GH_IO_Serialization_GH_IReader_TryGetDouble

﻿ GH\_IReader.TryGetDouble Method (String, Double)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IReader Methods](../html/Methods_T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Methods")

[TryGetDouble Method](../html/Overload_GH_IO_Serialization_GH_IReader_TryGetDouble.htm "TryGetDouble Method ")

[TryGetDouble Method (String, Double)](../html/M_GH_IO_Serialization_GH_IReader_TryGetDouble.htm "TryGetDouble Method (String, Double)")

[TryGetDouble Method (String, Int32, Double)](../html/M_GH_IO_Serialization_GH_IReader_TryGetDouble_1.htm "TryGetDouble Method (String, Int32, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IReaderAddLanguageSpecificTextSet("LST8D69E012\_0?cpp=::|nu=.");TryGetDouble Method (String, DoubleAddLanguageSpecificTextSet("LST8D69E012\_1?cpp=%");) |

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
bool TryGetDouble(
	string item_name,
	ref double value
)
```

```
Function TryGetDouble ( 
	item_name As String,
	ByRef value As Double
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST8D69E012\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [SystemAddLanguageSpecificTextSet("LST8D69E012\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)AddLanguageSpecificTextSet("LST8D69E012\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IReader Interface](T_GH_IO_Serialization_GH_IReader.htm)

[TryGetDouble Overload](Overload_GH_IO_Serialization_GH_IReader_TryGetDouble.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)