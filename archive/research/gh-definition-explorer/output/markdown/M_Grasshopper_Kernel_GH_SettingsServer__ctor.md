# M_Grasshopper_Kernel_GH_SettingsServer__ctor

﻿ GH\_SettingsServer Constructor (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_SettingsServer Class](../html/T_Grasshopper_Kernel_GH_SettingsServer.htm "GH_SettingsServer Class")

[GH\_SettingsServer Constructor](../html/Overload_Grasshopper_Kernel_GH_SettingsServer__ctor.htm "GH_SettingsServer Constructor ")

[GH\_SettingsServer Constructor (String)](../html/M_Grasshopper_Kernel_GH_SettingsServer__ctor.htm "GH_SettingsServer Constructor (String)")

[GH\_SettingsServer Constructor (String, Boolean)](../html/M_Grasshopper_Kernel_GH_SettingsServer__ctor_1.htm "GH_SettingsServer Constructor (String, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SettingsServer Constructor (String) |

Create a new instance of the GH\_SettingsServer class. The server
will be associated with a settings xml file in the %ApplicationData%\Grasshopper\ directory.
If a file with the same name already exists, its settings will be automatically loaded.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_SettingsServer(
	string databaseName
)
```

```
Public Sub New ( 
	databaseName As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

databaseName
:   Type: [SystemAddLanguageSpecificTextSet("LST6CB8A6AC\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the settings server
    (equals the name of the xml file so it must adhere to FAT, FAT32 and NTFS naming conventions).

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_SettingsServer Class](T_Grasshopper_Kernel_GH_SettingsServer.htm)

[GH\_SettingsServer Overload](Overload_Grasshopper_Kernel_GH_SettingsServer__ctor.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)