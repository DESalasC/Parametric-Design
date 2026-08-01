# M_GH_IO_Serialization_GH_IWriter_SetDate

﻿ GH\_IWriter.SetDate Method (String, DateTime)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetDate Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDate.htm "SetDate Method ")

[SetDate Method (String, DateTime)](../html/M_GH_IO_Serialization_GH_IWriter_SetDate.htm "SetDate Method (String, DateTime)")

[SetDate Method (String, Int32, DateTime)](../html/M_GH_IO_Serialization_GH_IWriter_SetDate_1.htm "SetDate Method (String, Int32, DateTime)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LSTA2430C1E\_0?cpp=::|nu=.");SetDate Method (String, DateTime) |

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
void SetDate(
	string item_name,
	DateTime item_value
)
```

```
Sub SetDate ( 
	item_name As String,
	item_value As DateTime
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTA2430C1E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [SystemAddLanguageSpecificTextSet("LSTA2430C1E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");DateTime](https://docs.microsoft.com/dotnet/api/system.datetime)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetDate Overload](Overload_GH_IO_Serialization_GH_IWriter_SetDate.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)