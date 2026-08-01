# M_GH_IO_Serialization_GH_IWriter_SetPoint3D_1

﻿ GH\_IWriter.SetPoint3D Method (String, Int32, GH\_Point3D)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetPoint3D Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetPoint3D.htm "SetPoint3D Method ")

[SetPoint3D Method (String, GH\_Point3D)](../html/M_GH_IO_Serialization_GH_IWriter_SetPoint3D.htm "SetPoint3D Method (String, GH_Point3D)")

[SetPoint3D Method (String, Int32, GH\_Point3D)](../html/M_GH_IO_Serialization_GH_IWriter_SetPoint3D_1.htm "SetPoint3D Method (String, Int32, GH_Point3D)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LST25C32CAA\_0?cpp=::|nu=.");SetPoint3D Method (String, Int32, GH\_Point3D) |

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
void SetPoint3D(
	string item_name,
	int item_index,
	GH_Point3D item_value
)
```

```
Sub SetPoint3D ( 
	item_name As String,
	item_index As Integer,
	item_value As GH_Point3D
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST25C32CAA\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST25C32CAA\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

item\_value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST25C32CAA\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Point3D](T_GH_IO_Types_GH_Point3D.htm)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetPoint3D Overload](Overload_GH_IO_Serialization_GH_IWriter_SetPoint3D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)