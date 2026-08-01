# M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnEditor

﻿ GH\_WindowsFormUtil.CenterFormOnEditor Method (Window, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_WindowsFormUtil Class](../html/T_Grasshopper_GUI_GH_WindowsFormUtil.htm "GH_WindowsFormUtil Class")

[GH\_WindowsFormUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_WindowsFormUtil.htm "GH_WindowsFormUtil Methods")

[CenterFormOnEditor Method](../html/Overload_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnEditor.htm "CenterFormOnEditor Method ")

[CenterFormOnEditor Method (Form, Boolean)](../html/M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnEditor_1.htm "CenterFormOnEditor Method (Form, Boolean)")

[CenterFormOnEditor Method (Window, Boolean)](../html/M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnEditor.htm "CenterFormOnEditor Method (Window, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_WindowsFormUtilAddLanguageSpecificTextSet("LST60B0E88\_0?cpp=::|nu=.");CenterFormOnEditor Method (Window, Boolean) |

Positions a Form so that it is centered on the active editor. If the editor doesn't exist or is hidden,
the form will be centered on the screen instead.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void CenterFormOnEditor(
	Window F,
	bool limitToScreen
)
```

```
Public Shared Sub CenterFormOnEditor ( 
	F As Window,
	limitToScreen As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

F
:   Type: Window  
    The Form to adjust

limitToScreen
:   Type: [SystemAddLanguageSpecificTextSet("LST60B0E88\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, the Form won't be allowed to extend beyond the limits of the screen containing the cursor.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_WindowsFormUtil Class](T_Grasshopper_GUI_GH_WindowsFormUtil.htm)

[CenterFormOnEditor Overload](Overload_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnEditor.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)