# M_GH_IO_Serialization_GH_IWriter_SetPath

﻿ GH\_IWriter.SetPath Method (String, Int32, String, String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetPath Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetPath.htm "SetPath Method ")

[SetPath Method (String, String, String)](../html/M_GH_IO_Serialization_GH_IWriter_SetPath_1.htm "SetPath Method (String, String, String)")

[SetPath Method (String, Int32, String, String)](../html/M_GH_IO_Serialization_GH_IWriter_SetPath.htm "SetPath Method (String, Int32, String, String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LSTADD29CA8\_0?cpp=::|nu=.");SetPath Method (String, Int32, String, String) |

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
void SetPath(
	string item_name,
	int item_index,
	string absolutePath,
	string basePath
)
```

```
Sub SetPath ( 
	item_name As String,
	item_index As Integer,
	absolutePath As String,
	basePath As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTADD29CA8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTADD29CA8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

absolutePath
:   Type: [SystemAddLanguageSpecificTextSet("LSTADD29CA8\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Absolute path to store.

basePath
:   Type: [SystemAddLanguageSpecificTextSet("LSTADD29CA8\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Base path. This will be used to also store a relative path.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetPath Overload](Overload_GH_IO_Serialization_GH_IWriter_SetPath.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)