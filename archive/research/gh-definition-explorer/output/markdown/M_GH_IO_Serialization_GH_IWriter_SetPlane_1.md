# M_GH_IO_Serialization_GH_IWriter_SetPlane_1

﻿ GH\_IWriter.SetPlane Method (String, Int32, GH\_Plane)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetPlane Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetPlane.htm "SetPlane Method ")

[SetPlane Method (String, GH\_Plane)](../html/M_GH_IO_Serialization_GH_IWriter_SetPlane.htm "SetPlane Method (String, GH_Plane)")

[SetPlane Method (String, Int32, GH\_Plane)](../html/M_GH_IO_Serialization_GH_IWriter_SetPlane_1.htm "SetPlane Method (String, Int32, GH_Plane)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LSTC2009BC8\_0?cpp=::|nu=.");SetPlane Method (String, Int32, GH\_Plane) |

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
void SetPlane(
	string item_name,
	int item_index,
	GH_Plane item_value
)
```

```
Sub SetPlane ( 
	item_name As String,
	item_index As Integer,
	item_value As GH_Plane
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTC2009BC8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTC2009BC8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

item\_value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LSTC2009BC8\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Plane](T_GH_IO_Types_GH_Plane.htm)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetPlane Overload](Overload_GH_IO_Serialization_GH_IWriter_SetPlane.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)