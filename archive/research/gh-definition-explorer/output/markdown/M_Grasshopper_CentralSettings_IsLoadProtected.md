# M_Grasshopper_CentralSettings_IsLoadProtected

﻿ CentralSettings.IsLoadProtected Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[CentralSettings Class](../html/T_Grasshopper_CentralSettings.htm "CentralSettings Class")

[CentralSettings Methods](../html/Methods_T_Grasshopper_CentralSettings.htm "CentralSettings Methods")

[GetLoadMechanism Method](../html/M_Grasshopper_CentralSettings_GetLoadMechanism.htm "GetLoadMechanism Method ")

[IsLoadProtected Method](../html/M_Grasshopper_CentralSettings_IsLoadProtected.htm "IsLoadProtected Method ")

[SetLoadMechanism Method](../html/M_Grasshopper_CentralSettings_SetLoadMechanism.htm "SetLoadMechanism Method ")

[SetLoadProtected Method](../html/M_Grasshopper_CentralSettings_SetLoadProtected.htm "SetLoadProtected Method ")

[UserOkayWithBakingInvalidObject Method](../html/M_Grasshopper_CentralSettings_UserOkayWithBakingInvalidObject.htm "UserOkayWithBakingInvalidObject Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| CentralSettingsAddLanguageSpecificTextSet("LSTC6E2F0E2\_0?cpp=::|nu=.");IsLoadProtected Method |

Gets whether a certain plugin is load protected.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool IsLoadProtected(
	string pluginName
)
```

```
Public Shared Function IsLoadProtected ( 
	pluginName As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pluginName
:   Type: [SystemAddLanguageSpecificTextSet("LSTC6E2F0E2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the plugin file (without the extension).

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the plugin is load protected, false if not.

![](../icons/SectionExpanded.png)See Also

#### Reference

[CentralSettings Class](T_Grasshopper_CentralSettings.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)