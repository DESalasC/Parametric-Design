# M_GH_IO_Serialization_GH_IWriter_SetInt64_1

﻿ GH\_IWriter.SetInt64 Method (String, Int64)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetInt64 Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetInt64.htm "SetInt64 Method ")

[SetInt64 Method (String, Int64)](../html/M_GH_IO_Serialization_GH_IWriter_SetInt64_1.htm "SetInt64 Method (String, Int64)")

[SetInt64 Method (String, Int32, Int64)](../html/M_GH_IO_Serialization_GH_IWriter_SetInt64.htm "SetInt64 Method (String, Int32, Int64)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LSTC715DACC\_0?cpp=::|nu=.");SetInt64 Method (String, Int64) |

Add a new data item to this chunk.
The name must be unique or an exception will be thrown.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void SetInt64(
	string item_name,
	long item_value
)
```

```
Sub SetInt64 ( 
	item_name As String,
	item_value As Long
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTC715DACC\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [SystemAddLanguageSpecificTextSet("LSTC715DACC\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int64](https://docs.microsoft.com/dotnet/api/system.int64)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetInt64 Overload](Overload_GH_IO_Serialization_GH_IWriter_SetInt64.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)