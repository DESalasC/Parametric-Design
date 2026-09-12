# M_Grasshopper_Kernel_GH_SettingsServer_EntryType

﻿ GH\_SettingsServer.EntryType Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_SettingsServer Class](../html/T_Grasshopper_Kernel_GH_SettingsServer.htm "GH_SettingsServer Class")

[GH\_SettingsServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_SettingsServer.htm "GH_SettingsServer Methods")

[Clear Method](../html/M_Grasshopper_Kernel_GH_SettingsServer_Clear.htm "Clear Method ")

[ConstainsEntry Method](../html/M_Grasshopper_Kernel_GH_SettingsServer_ConstainsEntry.htm "ConstainsEntry Method ")

[DeleteValue Method](../html/M_Grasshopper_Kernel_GH_SettingsServer_DeleteValue.htm "DeleteValue Method ")

[EntryNames Method](../html/M_Grasshopper_Kernel_GH_SettingsServer_EntryNames.htm "EntryNames Method ")

[EntryType Method](../html/M_Grasshopper_Kernel_GH_SettingsServer_EntryType.htm "EntryType Method ")

[GetValue Method](../html/Overload_Grasshopper_Kernel_GH_SettingsServer_GetValue.htm "GetValue Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_SettingsServer_Read.htm "Read Method ")

[SetValue Method](../html/Overload_Grasshopper_Kernel_GH_SettingsServer_SetValue.htm "SetValue Method ")

[ShowSettingsBrowser Method](../html/M_Grasshopper_Kernel_GH_SettingsServer_ShowSettingsBrowser.htm "ShowSettingsBrowser Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_SettingsServer_Write.htm "Write Method ")

[WritePersistentSettings Method](../html/M_Grasshopper_Kernel_GH_SettingsServer_WritePersistentSettings.htm "WritePersistentSettings Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SettingsServerAddLanguageSpecificTextSet("LST1A03DF05\_0?cpp=::|nu=.");EntryType Method |

Gets the type of a specific entry.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_SettingsType EntryType(
	string name
)
```

```
Public Function EntryType ( 
	name As String
) As GH_SettingsType
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST1A03DF05\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of entry.

#### Return Value

Type: [GH\_SettingsType](T_Grasshopper_Kernel_GH_SettingsType.htm)  
Type of entry. If entry doesn't exist, GH\_SettingsType.\_unknown is returned.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_SettingsServer Class](T_Grasshopper_Kernel_GH_SettingsServer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)