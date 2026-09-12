# M_GH_IO_Serialization_GH_Chunk_SetDrawingSizeF_1

﻿ GH\_Chunk.SetDrawingSizeF Method (String, Int32, SizeF)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetDrawingSizeF Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetDrawingSizeF.htm "SetDrawingSizeF Method ")

[SetDrawingSizeF Method (String, SizeF)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingSizeF.htm "SetDrawingSizeF Method (String, SizeF)")

[SetDrawingSizeF Method (String, Int32, SizeF)](../html/M_GH_IO_Serialization_GH_Chunk_SetDrawingSizeF_1.htm "SetDrawingSizeF Method (String, Int32, SizeF)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTA7B584C0\_0?cpp=::|nu=.");SetDrawingSizeF Method (String, Int32, SizeF) |

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
public void SetDrawingSizeF(
	string item_name,
	int item_index,
	SizeF item_value
)
```

```
Public Sub SetDrawingSizeF ( 
	item_name As String,
	item_index As Integer,
	item_value As SizeF
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTA7B584C0\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTA7B584C0\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

item\_value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTA7B584C0\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SizeF](https://docs.microsoft.com/dotnet/api/system.drawing.sizef)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LSTA7B584C0\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");SetDrawingSizeF(String, Int32, SizeF)](M_GH_IO_Serialization_GH_IWriter_SetDrawingSizeF_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetDrawingSizeF Overload](Overload_GH_IO_Serialization_GH_Chunk_SetDrawingSizeF.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)