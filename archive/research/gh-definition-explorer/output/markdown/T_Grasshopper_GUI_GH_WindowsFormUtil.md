# T_Grasshopper_GUI_GH_WindowsFormUtil

﻿ GH\_WindowsFormUtil Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_WindowsFormUtil Class](../html/T_Grasshopper_GUI_GH_WindowsFormUtil.htm "GH_WindowsFormUtil Class")

[GH\_WindowsFormUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_WindowsFormUtil.htm "GH_WindowsFormUtil Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_WindowsFormUtil Class |

Exposes some static (Shared) utility functions for positioning custom windows.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST490C674D\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST490C674D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_WindowsFormUtil

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_WindowsFormUtil
```

```
Public NotInheritable Class GH_WindowsFormUtil
```

AddLanguageTabSet("ID1EBCA");

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [CenterFormOnCursor(Form, Boolean)](M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnCursor_1.htm) | Positions a Form so that it is centered around the cursor |
| Public methodStatic member | [CenterFormOnCursor(Window, Boolean)](M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnCursor.htm) | Positions a Form so that it is centered around the cursor |
| Public methodStatic member | [CenterFormOnEditor(Form, Boolean)](M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnEditor_1.htm) | Positions a Form so that it is centered on the active editor. If the editor doesn't exist or is hidden, the form will be centered on the screen instead. |
| Public methodStatic member | [CenterFormOnEditor(Window, Boolean)](M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnEditor.htm) | Positions a Form so that it is centered on the active editor. If the editor doesn't exist or is hidden, the form will be centered on the screen instead. |
| Public methodStatic member | [CenterFormOnScreen(Form, Boolean)](M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnScreen_1.htm) | Positions a Form so that it is centered on the current screen. The current screen being defined as the screen containing the cursor. |
| Public methodStatic member | [CenterFormOnScreen(Window, Boolean)](M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnScreen.htm) | Positions a Form so that it is centered on the current screen. The current screen being defined as the screen containing the cursor. |
| Public methodStatic member | [CenterFormOnWindow(Form, Form, Boolean)](M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnWindow_1.htm) | Positions a Form so that it is centered on the supplied window. If the window doesn't exist or is hidden, the form will be centered on the screen instead. |
| Public methodStatic member | [CenterFormOnWindow(Window, Window, Boolean)](M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnWindow.htm) | Positions a Form so that it is centered on the supplied window. If the window doesn't exist or is hidden, the form will be centered on the screen instead. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)