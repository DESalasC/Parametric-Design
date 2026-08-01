# M_GH_IO_Serialization_GH_IWriter_SetDecimal_1

﻿ GH\_IWriter.SetDecimal Method (String, Int32, Decimal)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetDecimal Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDecimal.htm "SetDecimal Method ")

[SetDecimal Method (String, Decimal)](../html/M_GH_IO_Serialization_GH_IWriter_SetDecimal.htm "SetDecimal Method (String, Decimal)")

[SetDecimal Method (String, Int32, Decimal)](../html/M_GH_IO_Serialization_GH_IWriter_SetDecimal_1.htm "SetDecimal Method (String, Int32, Decimal)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LSTA332FDCF\_0?cpp=::|nu=.");SetDecimal Method (String, Int32, Decimal) |

Add a new data item to this chunk.
The combination of name and index must be unique or an exception will be thrown.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void SetDecimal(
	string item_name,
	int item_index,
	decimal item_value
)
```

```
Sub SetDecimal ( 
	item_name As String,
	item_index As Integer,
	item_value As Decimal
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTA332FDCF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTA332FDCF\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

item\_value
:   Type: [SystemAddLanguageSpecificTextSet("LSTA332FDCF\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Decimal](https://docs.microsoft.com/dotnet/api/system.decimal)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetDecimal Overload](Overload_GH_IO_Serialization_GH_IWriter_SetDecimal.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)