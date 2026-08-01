# T_Grasshopper_Kernel_GH_SettingsServer

﻿ GH\_SettingsServer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_SettingsServer Class](../html/T_Grasshopper_Kernel_GH_SettingsServer.htm "GH_SettingsServer Class")

[GH\_SettingsServer Constructor](../html/Overload_Grasshopper_Kernel_GH_SettingsServer__ctor.htm "GH_SettingsServer Constructor ")

[GH\_SettingsServer Properties](../html/Properties_T_Grasshopper_Kernel_GH_SettingsServer.htm "GH_SettingsServer Properties")

[GH\_SettingsServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_SettingsServer.htm "GH_SettingsServer Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SettingsServer Class |

A single instance of this class is maintained at module level under the
accessor "Settings".

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST5D19821E\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST5D19821E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SettingsServer

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_SettingsServer : GH_ISerializable
```

```
Public NotInheritable Class GH_SettingsServer
	Implements GH_ISerializable
```

AddLanguageTabSet("ID1EBCA");

The GH\_SettingsServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_SettingsServer(String)](M_Grasshopper_Kernel_GH_SettingsServer__ctor.htm) | Create a new instance of the GH\_SettingsServer class. The server will be associated with a settings xml file in the %ApplicationData%\Grasshopper\ directory. If a file with the same name already exists, its settings will be automatically loaded. |
| Public method | [GH\_SettingsServer(String, Boolean)](M_Grasshopper_Kernel_GH_SettingsServer__ctor_1.htm) | Create a new instance of the GH\_SettingsServer class. The server will be associated with a settings xml file in the %ApplicationData%\Grasshopper\ directory. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Count](P_Grasshopper_Kernel_GH_SettingsServer_Count.htm) | Gets the total number of settings stored in this database. |
| Public property | [DatabaseName](P_Grasshopper_Kernel_GH_SettingsServer_DatabaseName.htm) | Gets the name of this settings database. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Clear](M_Grasshopper_Kernel_GH_SettingsServer_Clear.htm) | Destroy all settings. |
| Public method | [ConstainsEntry](M_Grasshopper_Kernel_GH_SettingsServer_ConstainsEntry.htm) | Tests to see if a given entry is stored in this settings database. |
| Public method | [DeleteValue](M_Grasshopper_Kernel_GH_SettingsServer_DeleteValue.htm) |  |
| Public method | [EntryNames](M_Grasshopper_Kernel_GH_SettingsServer_EntryNames.htm) | Gets a list of all the entry names in this settings. |
| Public method | [EntryType](M_Grasshopper_Kernel_GH_SettingsServer_EntryType.htm) | Gets the type of a specific entry. |
| Public method | [GetValue(String, Boolean)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue.htm) |  |
| Public method | [GetValue(String, Byte)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_1.htm) |  |
| Public method | [GetValue(String, DateTime)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_2.htm) |  |
| Public method | [GetValue(String, Double)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_3.htm) |  |
| Public method | [GetValue(String, Color)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_4.htm) |  |
| Public method | [GetValue(String, Point)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_5.htm) |  |
| Public method | [GetValue(String, Rectangle)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_6.htm) |  |
| Public method | [GetValue(String, Size)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_7.htm) |  |
| Public method | [GetValue(String, Int32)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_8.htm) |  |
| Public method | [GetValue(String, String)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_9.htm) |  |
| Public method | [Read](M_Grasshopper_Kernel_GH_SettingsServer_Read.htm) | Low-level deserializer. |
| Public method | [SetValue(String)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue.htm) |  |
| Public method | [SetValue(String, Boolean)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_1.htm) |  |
| Public method | [SetValue(String, Byte)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_2.htm) |  |
| Public method | [SetValue(String, DateTime)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_3.htm) |  |
| Public method | [SetValue(String, Double)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_4.htm) |  |
| Public method | [SetValue(String, Color)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_5.htm) |  |
| Public method | [SetValue(String, Point)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_6.htm) |  |
| Public method | [SetValue(String, Rectangle)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_7.htm) |  |
| Public method | [SetValue(String, Size)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_8.htm) |  |
| Public method | [SetValue(String, Int32)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_9.htm) |  |
| Public method | [SetValue(String, String)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_10.htm) |  |
| Public method | [ShowSettingsBrowser](M_Grasshopper_Kernel_GH_SettingsServer_ShowSettingsBrowser.htm) |  |
| Public method | [Write](M_Grasshopper_Kernel_GH_SettingsServer_Write.htm) | Low-level serializer. |
| Public method | [WritePersistentSettings](M_Grasshopper_Kernel_GH_SettingsServer_WritePersistentSettings.htm) | Store all settings in the xml file now. You *must* call this function if you want the current settings to persist between sessions. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)