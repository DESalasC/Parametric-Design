# M_GH_IO_Serialization_GH_Archive_Deserialize_Binary

﻿ GH\_Archive.Deserialize\_Binary Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Archive Class](../html/T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Class")

[GH\_Archive Methods](../html/Methods_T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Methods")

[AddMessage Method](../html/Overload_GH_IO_Serialization_GH_Archive_AddMessage.htm "AddMessage Method ")

[AppendObject Method](../html/M_GH_IO_Serialization_GH_Archive_AppendObject.htm "AppendObject Method ")

[ClearMessages Method](../html/M_GH_IO_Serialization_GH_Archive_ClearMessages.htm "ClearMessages Method ")

[CreateNewRoot Method](../html/M_GH_IO_Serialization_GH_Archive_CreateNewRoot.htm "CreateNewRoot Method ")

[CreateTopLevelNode Method](../html/M_GH_IO_Serialization_GH_Archive_CreateTopLevelNode.htm "CreateTopLevelNode Method ")

[Deserialize\_Binary Method](../html/M_GH_IO_Serialization_GH_Archive_Deserialize_Binary.htm "Deserialize_Binary Method ")

[Deserialize\_Xml Method](../html/M_GH_IO_Serialization_GH_Archive_Deserialize_Xml.htm "Deserialize_Xml Method ")

[ExtractObject Method](../html/M_GH_IO_Serialization_GH_Archive_ExtractObject.htm "ExtractObject Method ")

[MessageCount Method](../html/Overload_GH_IO_Serialization_GH_Archive_MessageCount.htm "MessageCount Method ")

[OpenFileDialog Method](../html/M_GH_IO_Serialization_GH_Archive_OpenFileDialog.htm "OpenFileDialog Method ")

[ReadFromFile Method](../html/M_GH_IO_Serialization_GH_Archive_ReadFromFile.htm "ReadFromFile Method ")

[SaveFileDialog Method](../html/M_GH_IO_Serialization_GH_Archive_SaveFileDialog.htm "SaveFileDialog Method ")

[Serialize\_Binary Method](../html/M_GH_IO_Serialization_GH_Archive_Serialize_Binary.htm "Serialize_Binary Method ")

[Serialize\_Xml Method](../html/M_GH_IO_Serialization_GH_Archive_Serialize_Xml.htm "Serialize_Xml Method ")

[ShowMessageLog Method](../html/M_GH_IO_Serialization_GH_Archive_ShowMessageLog.htm "ShowMessageLog Method ")

[WriteToFile Method](../html/M_GH_IO_Serialization_GH_Archive_WriteToFile.htm "WriteToFile Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ArchiveAddLanguageSpecificTextSet("LST6EA835C6\_0?cpp=::|nu=.");Deserialize\_Binary Method |

Deserializes an array of bytes.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool Deserialize_Binary(
	byte[] data
)
```

```
Public Function Deserialize_Binary ( 
	data As Byte()
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

data
:   Type: AddLanguageSpecificTextSet("LST6EA835C6\_1?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LST6EA835C6\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Byte](https://docs.microsoft.com/dotnet/api/system.byte)AddLanguageSpecificTextSet("LST6EA835C6\_3?cpp=&gt;|vb=()|nu=[]");  
    Byte array to deserialize.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](https://docs.microsoft.com/dotnet/api/system.argumentnullexception) | Thrown if data is a null reference. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Archive Class](T_GH_IO_Serialization_GH_Archive.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)