# M_GH_IO_Serialization_GH_IWriter_SetBoundingBox

﻿ GH\_IWriter.SetBoundingBox Method (String, GH\_BoundingBox)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetBoundingBox Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetBoundingBox.htm "SetBoundingBox Method ")

[SetBoundingBox Method (String, GH\_BoundingBox)](../html/M_GH_IO_Serialization_GH_IWriter_SetBoundingBox.htm "SetBoundingBox Method (String, GH_BoundingBox)")

[SetBoundingBox Method (String, Int32, GH\_BoundingBox)](../html/M_GH_IO_Serialization_GH_IWriter_SetBoundingBox_1.htm "SetBoundingBox Method (String, Int32, GH_BoundingBox)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LST9FAFB92E\_0?cpp=::|nu=.");SetBoundingBox Method (String, GH\_BoundingBox) |

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
void SetBoundingBox(
	string item_name,
	GH_BoundingBox item_value
)
```

```
Sub SetBoundingBox ( 
	item_name As String,
	item_value As GH_BoundingBox
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST9FAFB92E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST9FAFB92E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_BoundingBox](T_GH_IO_Types_GH_BoundingBox.htm)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetBoundingBox Overload](Overload_GH_IO_Serialization_GH_IWriter_SetBoundingBox.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)