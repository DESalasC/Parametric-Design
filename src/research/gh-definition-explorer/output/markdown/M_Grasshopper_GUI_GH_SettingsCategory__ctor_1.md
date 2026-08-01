# M_Grasshopper_GUI_GH_SettingsCategory__ctor_1

﻿ GH\_SettingsCategory Constructor (String, String, Bitmap)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_SettingsCategory Class](../html/T_Grasshopper_GUI_GH_SettingsCategory.htm "GH_SettingsCategory Class")

[GH\_SettingsCategory Constructor](../html/Overload_Grasshopper_GUI_GH_SettingsCategory__ctor.htm "GH_SettingsCategory Constructor ")

[GH\_SettingsCategory Constructor (String, Bitmap)](../html/M_Grasshopper_GUI_GH_SettingsCategory__ctor.htm "GH_SettingsCategory Constructor (String, Bitmap)")

[GH\_SettingsCategory Constructor (String, String, Bitmap)](../html/M_Grasshopper_GUI_GH_SettingsCategory__ctor_1.htm "GH_SettingsCategory Constructor (String, String, Bitmap)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SettingsCategory Constructor (String, String, Bitmap) |

Create a new nested category.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected GH_SettingsCategory(
	string name,
	string parent,
	Bitmap icon
)
```

```
Protected Sub New ( 
	name As String,
	parent As String,
	icon As Bitmap
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST1C70B136\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Category name, keep it short.

parent
:   Type: [SystemAddLanguageSpecificTextSet("LST1C70B136\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of parent category. If the parent category hasn't been defined,
    the category will be placed under a "Misc" category.

icon
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST1C70B136\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Bitmap](https://docs.microsoft.com/dotnet/api/system.drawing.bitmap)  
    Category icon. If you supply an icon, it must be 48x48 pixels.
    If you supply a null instance, a generic Settings icon will be assigned.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_SettingsCategory Class](T_Grasshopper_GUI_GH_SettingsCategory.htm)

[GH\_SettingsCategory Overload](Overload_Grasshopper_GUI_GH_SettingsCategory__ctor.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)