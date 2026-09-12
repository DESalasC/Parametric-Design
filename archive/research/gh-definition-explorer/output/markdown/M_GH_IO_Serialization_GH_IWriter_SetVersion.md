# M_GH_IO_Serialization_GH_IWriter_SetVersion

﻿ GH\_IWriter.SetVersion Method (String, GH\_Version)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetVersion Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetVersion.htm "SetVersion Method ")

[SetVersion Method (String, GH\_Version)](../html/M_GH_IO_Serialization_GH_IWriter_SetVersion.htm "SetVersion Method (String, GH_Version)")

[SetVersion Method (String, Int32, GH\_Version)](../html/M_GH_IO_Serialization_GH_IWriter_SetVersion_1.htm "SetVersion Method (String, Int32, GH_Version)")

[SetVersion Method (String, Int32, Int32, Int32)](../html/M_GH_IO_Serialization_GH_IWriter_SetVersion_2.htm "SetVersion Method (String, Int32, Int32, Int32)")

[SetVersion Method (String, Int32, Int32, Int32, Int32)](../html/M_GH_IO_Serialization_GH_IWriter_SetVersion_3.htm "SetVersion Method (String, Int32, Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LST89237D90\_0?cpp=::|nu=.");SetVersion Method (String, GH\_Version) |

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
void SetVersion(
	string item_name,
	GH_Version item_value
)
```

```
Sub SetVersion ( 
	item_name As String,
	item_value As GH_Version
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST89237D90\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST89237D90\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Version](T_GH_IO_Types_GH_Version.htm)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetVersion Overload](Overload_GH_IO_Serialization_GH_IWriter_SetVersion.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)