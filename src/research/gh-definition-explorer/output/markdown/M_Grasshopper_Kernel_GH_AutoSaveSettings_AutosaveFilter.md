# M_Grasshopper_Kernel_GH_AutoSaveSettings_AutosaveFilter

﻿ GH\_AutoSaveSettings.AutosaveFilter Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_AutoSaveSettings Class](../html/T_Grasshopper_Kernel_GH_AutoSaveSettings.htm "GH_AutoSaveSettings Class")

[GH\_AutoSaveSettings Methods](../html/Methods_T_Grasshopper_Kernel_GH_AutoSaveSettings.htm "GH_AutoSaveSettings Methods")

[AutosaveFilter Method](../html/M_Grasshopper_Kernel_GH_AutoSaveSettings_AutosaveFilter.htm "AutosaveFilter Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AutoSaveSettingsAddLanguageSpecificTextSet("LST3FBABE87\_0?cpp=::|nu=.");AutosaveFilter Method |

Tests a given trigger to see if it allows an autosave operation.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool AutosaveFilter(
	GH_AutoSaveTrigger trigger
)
```

```
Public Shared Function AutosaveFilter ( 
	trigger As GH_AutoSaveTrigger
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

trigger
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST3FBABE87\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AutoSaveTrigger](T_Grasshopper_Kernel_GH_AutoSaveTrigger.htm)  
    Trigger to filter.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the trigger ought to start an AutoSave op.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AutoSaveSettings Class](T_Grasshopper_Kernel_GH_AutoSaveSettings.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)