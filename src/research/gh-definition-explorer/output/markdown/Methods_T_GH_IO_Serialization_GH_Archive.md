# Methods_T_GH_IO_Serialization_GH_Archive

﻿ GH\_Archive Methods 

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
| GH\_Archive Methods |

The [GH\_Archive](T_GH_IO_Serialization_GH_Archive.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddMessage(GH\_Message)](M_GH_IO_Serialization_GH_Archive_AddMessage.htm) | Add a new message to the record. |
| Public method | [AddMessage(String, GH\_Message\_Type)](M_GH_IO_Serialization_GH_Archive_AddMessage_1.htm) | Add a new message to the record. |
| Public methodCode example | [AppendObject](M_GH_IO_Serialization_GH_Archive_AppendObject.htm) | Appends a target object into the root node of this archive tree. If the root doesn't exist yet, it will be created. Existing objects at the root scope will not be affected. |
| Public method | [ClearMessages](M_GH_IO_Serialization_GH_Archive_ClearMessages.htm) | Remove all messages from the log. |
| Public method | [CreateNewRoot](M_GH_IO_Serialization_GH_Archive_CreateNewRoot.htm) | Discards the current data tree and instantiates a new root node. This root node contains some comments, a version value containing the current version of GH\_IO.dll and a DateTime value containing the current date and time. |
| Public method | [CreateTopLevelNode](M_GH_IO_Serialization_GH_Archive_CreateTopLevelNode.htm) | Creates and returns a new root node for this archive in the form of a GH\_IWriter instance. Typically you do not call this method. If you want to add an object to the archive, use AppendObject() instead. |
| Public method | [Deserialize\_Binary](M_GH_IO_Serialization_GH_Archive_Deserialize_Binary.htm) | Deserializes an array of bytes. |
| Public method | [Deserialize\_Xml](M_GH_IO_Serialization_GH_Archive_Deserialize_Xml.htm) | Deserializes an Xml string. |
| Public method | [ExtractObject](M_GH_IO_Serialization_GH_Archive_ExtractObject.htm) | Extract a target object from the data tree. |
| Public method | [MessageCountAddLanguageSpecificTextSet("LST1E3663F\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_GH_IO_Serialization_GH_Archive_MessageCount.htm) | Gets the number of messages recorded since the most recent IO operation began. |
| Public method | [MessageCount(Boolean, Boolean, Boolean)](M_GH_IO_Serialization_GH_Archive_MessageCount_1.htm) | Gets the number of messages recorded since the most recent IO operation began. Message count can be filtered by message type. |
| Public methodStatic member | [OpenFileDialog](M_GH_IO_Serialization_GH_Archive_OpenFileDialog.htm) | Displays a standard OpenFileDialog with all the fields set to cater for Grasshopper files. |
| Public method | [ReadFromFile](M_GH_IO_Serialization_GH_Archive_ReadFromFile.htm) | Reads a new archive tree from a file. |
| Public methodStatic member | [SaveFileDialog](M_GH_IO_Serialization_GH_Archive_SaveFileDialog.htm) | Displays a standard SaveFileDialog with all the fields set to cater for Grasshopper files. |
| Public method | [Serialize\_Binary](M_GH_IO_Serialization_GH_Archive_Serialize_Binary.htm) | Serializes the data tree into a Binary byte array. |
| Public method | [Serialize\_Xml](M_GH_IO_Serialization_GH_Archive_Serialize_Xml.htm) | Serializes the data tree into an Xml string. |
| Public method | [ShowMessageLog](M_GH_IO_Serialization_GH_Archive_ShowMessageLog.htm) | Displays the message log viewer. You should typically only display the viewer if the WorstCaseMessageType equals GH\_Message\_Type.warning or GH\_Message\_Type.error |
| Public method | [WriteToFile](M_GH_IO_Serialization_GH_Archive_WriteToFile.htm) | Writes the current tree to a file. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Archive Class](T_GH_IO_Serialization_GH_Archive.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)