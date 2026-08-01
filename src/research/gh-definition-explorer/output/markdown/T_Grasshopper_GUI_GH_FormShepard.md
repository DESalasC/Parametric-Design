# T_Grasshopper_GUI_GH_FormShepard

﻿ GH\_FormShepard Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_FormShepard Class](../html/T_Grasshopper_GUI_GH_FormShepard.htm "GH_FormShepard Class")

[GH\_FormShepard Constructor](../html/M_Grasshopper_GUI_GH_FormShepard__ctor.htm "GH_FormShepard Constructor ")

[GH\_FormShepard Properties](../html/Properties_T_Grasshopper_GUI_GH_FormShepard.htm "GH_FormShepard Properties")

[GH\_FormShepard Methods](../html/Methods_T_Grasshopper_GUI_GH_FormShepard.htm "GH_FormShepard Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FormShepard Class |

A Form shepard is used to herde a bunch of floating forms.
Important forms that potentially spout child forms might choose to
implement one.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST6B0D9FAB\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST6B0D9FAB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FormShepard

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_FormShepard
```

```
Public Class GH_FormShepard
```

AddLanguageTabSet("ID1EBCA");

The GH\_FormShepard type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_FormShepard](M_Grasshopper_GUI_GH_FormShepard__ctor.htm) | Create a new form shepard. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Sheep](P_Grasshopper_GUI_GH_FormShepard_Sheep.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [RegisterForm](M_Grasshopper_GUI_GH_FormShepard_RegisterForm.htm) | Add a sheep form to the flock. This form will be affected by the location and size of the main form. |
| Public method | [UnregisterForm](M_Grasshopper_GUI_GH_FormShepard_UnregisterForm.htm) | Remove a sheep from the flock. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)