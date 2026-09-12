# M_Grasshopper_Kernel_GH_UserObject_CreateDefaultPath

﻿ GH\_UserObject.CreateDefaultPath Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_UserObject Class](../html/T_Grasshopper_Kernel_GH_UserObject.htm "GH_UserObject Class")

[GH\_UserObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_UserObject.htm "GH_UserObject Methods")

[Clear Method](../html/M_Grasshopper_Kernel_GH_UserObject_Clear.htm "Clear Method ")

[CreateDefaultPath Method](../html/M_Grasshopper_Kernel_GH_UserObject_CreateDefaultPath.htm "CreateDefaultPath Method ")

[InstantiateObject Method](../html/M_Grasshopper_Kernel_GH_UserObject_InstantiateObject.htm "InstantiateObject Method ")

[ReadFromFile Method](../html/M_Grasshopper_Kernel_GH_UserObject_ReadFromFile.htm "ReadFromFile Method ")

[SaveToFile Method](../html/M_Grasshopper_Kernel_GH_UserObject_SaveToFile.htm "SaveToFile Method ")

[SetDataFromObject Method](../html/M_Grasshopper_Kernel_GH_UserObject_SetDataFromObject.htm "SetDataFromObject Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UserObjectAddLanguageSpecificTextSet("LST6F7172E\_0?cpp=::|nu=.");CreateDefaultPath Method |

Set the Path field for this user object to the default.
The default file name is derived from the Description.Name field.
This method also ensures the UserObject directory exists.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void CreateDefaultPath(
	bool avoid_conflict
)
```

```
Public Sub CreateDefaultPath ( 
	avoid_conflict As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

avoid\_conflict
:   Type: [SystemAddLanguageSpecificTextSet("LST6F7172E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, a unique file path is assigned.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_UserObject Class](T_Grasshopper_Kernel_GH_UserObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)