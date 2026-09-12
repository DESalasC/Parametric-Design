# T_Grasshopper_GUI_IGH_SettingCategory

﻿ IGH\_SettingCategory Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[IGH\_SettingCategory Interface](../html/T_Grasshopper_GUI_IGH_SettingCategory.htm "IGH_SettingCategory Interface")

[IGH\_SettingCategory Properties](../html/Properties_T_Grasshopper_GUI_IGH_SettingCategory.htm "IGH_SettingCategory Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_SettingCategory Interface |

Represents a single category in the Settings UI.
Implement this interface or derive from GH\_SettingsCategory
to add a new Category to the Grasshopper Settings interface.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_SettingCategory
```

```
Public Interface IGH_SettingCategory
```

AddLanguageTabSet("ID0EBCA");

The IGH\_SettingCategory type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Description](P_Grasshopper_GUI_IGH_SettingCategory_Description.htm) | Category description. |
| Public property | [Icon](P_Grasshopper_GUI_IGH_SettingCategory_Icon.htm) | Category icon. Image should be 48x48 pixels. |
| Public property | [Name](P_Grasshopper_GUI_IGH_SettingCategory_Name.htm) | Category name (not case sensitive). Use dots to separate subcategories. |
| Public property | [Parent](P_Grasshopper_GUI_IGH_SettingCategory_Parent.htm) | Gets the name of the parent category. If the category is supposed to be top-level, this property will return null or a String.Empty. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)