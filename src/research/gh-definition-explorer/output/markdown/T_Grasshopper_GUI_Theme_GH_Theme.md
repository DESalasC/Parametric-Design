# T_Grasshopper_GUI_Theme_GH_Theme

﻿ GH\_Theme Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Theme](../html/N_Grasshopper_GUI_Theme.htm "Grasshopper.GUI.Theme")

[GH\_Theme Class](../html/T_Grasshopper_GUI_Theme_GH_Theme.htm "GH_Theme Class")

[GH\_Theme Constructor](../html/Overload_Grasshopper_GUI_Theme_GH_Theme__ctor.htm "GH_Theme Constructor ")

[GH\_Theme Properties](../html/Properties_T_Grasshopper_GUI_Theme_GH_Theme.htm "GH_Theme Properties")

[GH\_Theme Methods](../html/Methods_T_Grasshopper_GUI_Theme_GH_Theme.htm "GH_Theme Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Theme Class |

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST7EA11E06\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.ThemeAddLanguageSpecificTextSet("LST7EA11E06\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Theme

**Namespace:**
 [Grasshopper.GUI.Theme](N_Grasshopper_GUI_Theme.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Theme : GH_ISerializable
```

```
Public Class GH_Theme
	Implements GH_ISerializable
```

AddLanguageTabSet("ID1EBCA");

The GH\_Theme type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ThemeAddLanguageSpecificTextSet("LST7EA11E06\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_Theme_GH_Theme__ctor.htm) | Create a new default theme. |
| Public method | [GH\_Theme(GH\_Theme)](M_Grasshopper_GUI_Theme_GH_Theme__ctor_1.htm) | Make a duplicate of another theme. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BackGround](P_Grasshopper_GUI_Theme_GH_Theme_BackGround.htm) | Gets the theme background settings. |
| Public propertyStatic member | [DefaultTheme](P_Grasshopper_GUI_Theme_GH_Theme_DefaultTheme.htm) |  |
| Public property | [Objects](P_Grasshopper_GUI_Theme_GH_Theme_Objects.htm) | Gets the theme objects and ZUI settings. |
| Public property | [Page](P_Grasshopper_GUI_Theme_GH_Theme_Page.htm) | Gets the theme page and grid settings. |
| Public property | [Palettes](P_Grasshopper_GUI_Theme_GH_Theme_Palettes.htm) | Gets the theme palette settings. |
| Public property | [Wires](P_Grasshopper_GUI_Theme_GH_Theme_Wires.htm) | Gets the theme wire settings. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [LoadTheme](M_Grasshopper_GUI_Theme_GH_Theme_LoadTheme.htm) | Instantiate all palette and gui defaults. This function reads the colour values out of grasshopper\_gui.xml settings database if it exists. |
| Public method | [Read](M_Grasshopper_GUI_Theme_GH_Theme_Read.htm) |  |
| Public method | [SaveTheme](M_Grasshopper_GUI_Theme_GH_Theme_SaveTheme.htm) | Store all palette and gui defaults. This function writes the colour values out to grasshopper\_gui.xml settings database. |
| Public method | [Write](M_Grasshopper_GUI_Theme_GH_Theme_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Theme Namespace](N_Grasshopper_GUI_Theme.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)