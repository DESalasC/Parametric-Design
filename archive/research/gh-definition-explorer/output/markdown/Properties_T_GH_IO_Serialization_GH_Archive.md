# Properties_T_GH_IO_Serialization_GH_Archive

﻿ GH\_Archive Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Archive Class](../html/T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Class")

[GH\_Archive Properties](../html/Properties_T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Properties")

[FileName Property](../html/P_GH_IO_Serialization_GH_Archive_FileName.htm "FileName Property ")

[GetRootNode Property](../html/P_GH_IO_Serialization_GH_Archive_GetRootNode.htm "GetRootNode Property ")

[GH\_IO\_Version Property](../html/P_GH_IO_Serialization_GH_Archive_GH_IO_Version.htm "GH_IO_Version Property ")

[GrasshopperBinaryExtension Property](../html/P_GH_IO_Serialization_GH_Archive_GrasshopperBinaryExtension.htm "GrasshopperBinaryExtension Property ")

[GrasshopperUserExtension Property](../html/P_GH_IO_Serialization_GH_Archive_GrasshopperUserExtension.htm "GrasshopperUserExtension Property ")

[GrasshopperXmlExtension Property](../html/P_GH_IO_Serialization_GH_Archive_GrasshopperXmlExtension.htm "GrasshopperXmlExtension Property ")

[IsBinaryPath Property](../html/P_GH_IO_Serialization_GH_Archive_IsBinaryPath.htm "IsBinaryPath Property ")

[IsPath Property](../html/P_GH_IO_Serialization_GH_Archive_IsPath.htm "IsPath Property ")

[IsXmlPath Property](../html/P_GH_IO_Serialization_GH_Archive_IsXmlPath.htm "IsXmlPath Property ")

[Messages Property](../html/P_GH_IO_Serialization_GH_Archive_Messages.htm "Messages Property ")

[Path Property](../html/P_GH_IO_Serialization_GH_Archive_Path.htm "Path Property ")

[WorstCaseMessageType Property](../html/P_GH_IO_Serialization_GH_Archive_WorstCaseMessageType.htm "WorstCaseMessageType Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Archive Properties |

The [GH\_Archive](T_GH_IO_Serialization_GH_Archive.htm) type exposes the following members.

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

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Archive Class](T_GH_IO_Serialization_GH_Archive.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)