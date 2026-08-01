# M_GH_IO_Serialization_GH_IWriter_SetInterval2D_1

﻿ GH\_IWriter.SetInterval2D Method (String, Int32, GH\_Interval2D)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetInterval2D Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetInterval2D.htm "SetInterval2D Method ")

[SetInterval2D Method (String, GH\_Interval2D)](../html/M_GH_IO_Serialization_GH_IWriter_SetInterval2D.htm "SetInterval2D Method (String, GH_Interval2D)")

[SetInterval2D Method (String, Int32, GH\_Interval2D)](../html/M_GH_IO_Serialization_GH_IWriter_SetInterval2D_1.htm "SetInterval2D Method (String, Int32, GH_Interval2D)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LST5FD6DA9D\_0?cpp=::|nu=.");SetInterval2D Method (String, Int32, GH\_Interval2D) |

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
void SetInterval2D(
	string item_name,
	int item_index,
	GH_Interval2D item_value
)
```

```
Sub SetInterval2D ( 
	item_name As String,
	item_index As Integer,
	item_value As GH_Interval2D
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST5FD6DA9D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST5FD6DA9D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

item\_value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST5FD6DA9D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Interval2D](T_GH_IO_Types_GH_Interval2D.htm)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetInterval2D Overload](Overload_GH_IO_Serialization_GH_IWriter_SetInterval2D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)