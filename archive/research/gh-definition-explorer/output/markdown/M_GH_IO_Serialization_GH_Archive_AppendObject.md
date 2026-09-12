# M_GH_IO_Serialization_GH_Archive_AppendObject

﻿ GH\_Archive.AppendObject Method  

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
| GH\_ArchiveAddLanguageSpecificTextSet("LSTE793EE90\_0?cpp=::|nu=.");AppendObject Method |

Appends a target object into the root node of this archive tree.
If the root doesn't exist yet, it will be created. Existing objects at the root scope
will not be affected.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool AppendObject(
	GH_ISerializable target,
	string targetName
)
```

```
Public Function AppendObject ( 
	target As GH_ISerializable,
	targetName As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

target
:   Type: [GH\_IOAddLanguageSpecificTextSet("LSTE793EE90\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ISerializable](T_GH_IO_GH_ISerializable.htm)  
    Object to append. Cannot be null.

targetName
:   Type: [SystemAddLanguageSpecificTextSet("LSTE793EE90\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of object to append, name must be unique.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on succes, false on failure.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](https://docs.microsoft.com/dotnet/api/system.argumentnullexception) | Thrown if target is a null reference. |
| [ArgumentNullException](https://docs.microsoft.com/dotnet/api/system.argumentnullexception) | Thrown if the target\_name is null or empty. |

![](../icons/SectionExpanded.png)Examples

This sample shows how to create a new archive and serialize a single top level object.

C#

[Copy](# "Copy")

```
bool CreateFile(string file_name, GH_ISerializable target, string target_name) 
{
  GH_Archive archive = new GH_Archive();
  archive.AppendObject(target, target_name);
  return archive.WriteToFile(file_name, true);
}
```

AddLanguageTabSet("ID0EAAABA");

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Archive Class](T_GH_IO_Serialization_GH_Archive.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)