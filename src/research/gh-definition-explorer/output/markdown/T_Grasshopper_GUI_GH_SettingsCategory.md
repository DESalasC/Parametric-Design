# T_Grasshopper_GUI_GH_SettingsCategory

﻿ GH\_SettingsCategory Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_SettingsCategory Class](../html/T_Grasshopper_GUI_GH_SettingsCategory.htm "GH_SettingsCategory Class")

[GH\_SettingsCategory Constructor](../html/Overload_Grasshopper_GUI_GH_SettingsCategory__ctor.htm "GH_SettingsCategory Constructor ")

[GH\_SettingsCategory Properties](../html/Properties_T_Grasshopper_GUI_GH_SettingsCategory.htm "GH_SettingsCategory Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SettingsCategory Class |

Base implementation of IGH\_SettingsCategory.
Derive from this class and provide an empty constructor to play ball.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST9BE5ECF7\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST9BE5ECF7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SettingsCategory

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_SettingsCategory : IGH_SettingCategory
```

```
Public MustInherit Class GH_SettingsCategory
	Implements IGH_SettingCategory
```

AddLanguageTabSet("ID1EBCA");

The GH\_SettingsCategory type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_SettingsCategory(String, Bitmap)](M_Grasshopper_GUI_GH_SettingsCategory__ctor.htm) | Create a new top-level category. |
| Protected method | [GH\_SettingsCategory(String, String, Bitmap)](M_Grasshopper_GUI_GH_SettingsCategory__ctor_1.htm) | Create a new nested category. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Description](P_Grasshopper_GUI_GH_SettingsCategory_Description.htm) |  |
| Public property | [Icon](P_Grasshopper_GUI_GH_SettingsCategory_Icon.htm) |  |
| Public property | [Name](P_Grasshopper_GUI_GH_SettingsCategory_Name.htm) |  |
| Public property | [Parent](P_Grasshopper_GUI_GH_SettingsCategory_Parent.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)