# T_Grasshopper_GUI_IGH_SettingFrontend

﻿ IGH\_SettingFrontend Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[IGH\_SettingFrontend Interface](../html/T_Grasshopper_GUI_IGH_SettingFrontend.htm "IGH_SettingFrontend Interface")

[IGH\_SettingFrontend Properties](../html/Properties_T_Grasshopper_GUI_IGH_SettingFrontend.htm "IGH_SettingFrontend Properties")

[IGH\_SettingFrontend Methods](../html/Methods_T_Grasshopper_GUI_IGH_SettingFrontend.htm "IGH_SettingFrontend Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_SettingFrontend Interface |

Represents a single setting in the Settings UI.
Implement this interface to participate in the Grasshopper Settings interface.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_SettingFrontend
```

```
Public Interface IGH_SettingFrontend
```

AddLanguageTabSet("ID0EBCA");

The IGH\_SettingFrontend type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Category](P_Grasshopper_GUI_IGH_SettingFrontend_Category.htm) | Category of this setting. |
| Public property | [Keywords](P_Grasshopper_GUI_IGH_SettingFrontend_Keywords.htm) | Optional keywords for this setting. |
| Public property | [Name](P_Grasshopper_GUI_IGH_SettingFrontend_Name.htm) | Name of this setting. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [SettingsUI](M_Grasshopper_GUI_IGH_SettingFrontend_SettingsUI.htm) | Create the winforms UI portion for this setting. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)