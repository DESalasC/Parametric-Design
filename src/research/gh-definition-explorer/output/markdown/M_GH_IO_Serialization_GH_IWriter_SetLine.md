# M_GH_IO_Serialization_GH_IWriter_SetLine

﻿ GH\_IWriter.SetLine Method (String, GH\_Line)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetLine Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetLine.htm "SetLine Method ")

[SetLine Method (String, GH\_Line)](../html/M_GH_IO_Serialization_GH_IWriter_SetLine.htm "SetLine Method (String, GH_Line)")

[SetLine Method (String, Int32, GH\_Line)](../html/M_GH_IO_Serialization_GH_IWriter_SetLine_1.htm "SetLine Method (String, Int32, GH_Line)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LSTE221F0E7\_0?cpp=::|nu=.");SetLine Method (String, GH\_Line) |

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
void SetLine(
	string item_name,
	GH_Line item_value
)
```

```
Sub SetLine ( 
	item_name As String,
	item_value As GH_Line
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTE221F0E7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LSTE221F0E7\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Line](T_GH_IO_Types_GH_Line.htm)  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetLine Overload](Overload_GH_IO_Serialization_GH_IWriter_SetLine.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)