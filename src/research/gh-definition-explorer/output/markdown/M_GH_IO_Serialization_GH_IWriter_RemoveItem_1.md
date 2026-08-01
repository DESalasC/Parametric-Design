# M_GH_IO_Serialization_GH_IWriter_RemoveItem_1

﻿ GH\_IWriter.RemoveItem Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[RemoveItem Method](../html/Overload_GH_IO_Serialization_GH_IWriter_RemoveItem.htm "RemoveItem Method ")

[RemoveItem Method (String)](../html/M_GH_IO_Serialization_GH_IWriter_RemoveItem.htm "RemoveItem Method (String)")

[RemoveItem Method (String, Int32)](../html/M_GH_IO_Serialization_GH_IWriter_RemoveItem_1.htm "RemoveItem Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LSTA56FAFC7\_0?cpp=::|nu=.");RemoveItem Method (String, Int32) |

Remove an indexed item from this chunk.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool RemoveItem(
	string itemName,
	int itemIndex
)
```

```
Function RemoveItem ( 
	itemName As String,
	itemIndex As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

itemName
:   Type: [SystemAddLanguageSpecificTextSet("LSTA56FAFC7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item.

itemIndex
:   Type: [SystemAddLanguageSpecificTextSet("LSTA56FAFC7\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[RemoveItem Overload](Overload_GH_IO_Serialization_GH_IWriter_RemoveItem.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)