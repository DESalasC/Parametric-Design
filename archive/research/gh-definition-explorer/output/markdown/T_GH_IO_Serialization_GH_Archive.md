# T_GH_IO_Serialization_GH_Archive

﻿ GH\_Archive Class 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Archive Class](../html/T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Class")

[GH\_Archive Constructor](../html/M_GH_IO_Serialization_GH_Archive__ctor.htm "GH_Archive Constructor ")

[GH\_Archive Properties](../html/Properties_T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Properties")

[GH\_Archive Methods](../html/Methods_T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Archive Class |

This is the base archive class which takes care of all (de)serialization and messaging.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST99EB91FF\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  GH\_IO.SerializationAddLanguageSpecificTextSet("LST99EB91FF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Archive

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Archive
```

```
Public Class GH_Archive
```

AddLanguageTabSet("ID1EBCA");

The GH\_Archive type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_Archive](M_GH_IO_Serialization_GH_Archive__ctor.htm) | Initializes a new instance of the GH\_Archive class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [FileName](P_GH_IO_Serialization_GH_Archive_FileName.htm) | Gets the filename (without extension) of the currently loaded data tree. If the path field has not been set, "unnamed" is returned. |
| Public property | [GetRootNode](P_GH_IO_Serialization_GH_Archive_GetRootNode.htm) | Gets the root node of this archive. Typically you do not need to modify the Root. Use functions like CreateTopLevelNode(), AppendObject() and ExtractObject() instead. If you modify the Root node, you may corrupt the archive. |
| Public propertyStatic member | [GH\_IO\_Version](P_GH_IO_Serialization_GH_Archive_GH_IO_Version.htm) | Gets the version number of the current GH\_IO build. |
| Public propertyStatic member | [GrasshopperBinaryExtension](P_GH_IO_Serialization_GH_Archive_GrasshopperBinaryExtension.htm) | Gets the file extension (including the dot) associated with Grasshopper® Binary data. |
| Public propertyStatic member | [GrasshopperUserExtension](P_GH_IO_Serialization_GH_Archive_GrasshopperUserExtension.htm) | Gets the file extension (including the dot) associated with Grasshopper® User Object file. |
| Public propertyStatic member | [GrasshopperXmlExtension](P_GH_IO_Serialization_GH_Archive_GrasshopperXmlExtension.htm) | Gets the file extension (including the dot) associated with Grasshopper® XML data. |
| Public property | [IsBinaryPath](P_GH_IO_Serialization_GH_Archive_IsBinaryPath.htm) | Gets a value that indicates whether the Path field points to a Binary Grasshopper file. |
| Public property | [IsPath](P_GH_IO_Serialization_GH_Archive_IsPath.htm) | Gets a value that indicates whether or not the path field has been set. |
| Public property | [IsXmlPath](P_GH_IO_Serialization_GH_Archive_IsXmlPath.htm) | Gets a value that indicates whether the Path field points to an Xml Grasshopper file. |
| Public property | [Messages](P_GH_IO_Serialization_GH_Archive_Messages.htm) | Gets the internal list of messages. |
| Public property | [Path](P_GH_IO_Serialization_GH_Archive_Path.htm) | Gets the path to the file from which this archive was read and/or written to. If the archive hasn't been read or written yet, this field will be null. |
| Public property | [WorstCaseMessageType](P_GH_IO_Serialization_GH_Archive_WorstCaseMessageType.htm) | Gets the worst case message type. If the record contains at least 1 error, the worst case is GH\_Message\_Type.error. If the record contains no errors, but at least 1 warning, the worst case is GH\_Message\_Type.warning. If the record contains no messages or only infos, the worst case type is GH\_Message\_Type.info. |

[Top](#PageHeader)

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
| Public method | [MessageCountAddLanguageSpecificTextSet("LST99EB91FF\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_GH_IO_Serialization_GH_Archive_MessageCount.htm) | Gets the number of messages recorded since the most recent IO operation began. |
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

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)