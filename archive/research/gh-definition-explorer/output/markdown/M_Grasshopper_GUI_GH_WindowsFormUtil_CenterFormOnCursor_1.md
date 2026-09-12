# M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnCursor_1

﻿ GH\_WindowsFormUtil.CenterFormOnCursor Method (Form, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_WindowsFormUtil Class](../html/T_Grasshopper_GUI_GH_WindowsFormUtil.htm "GH_WindowsFormUtil Class")

[GH\_WindowsFormUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_WindowsFormUtil.htm "GH_WindowsFormUtil Methods")

[CenterFormOnCursor Method](../html/Overload_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnCursor.htm "CenterFormOnCursor Method ")

[CenterFormOnCursor Method (Form, Boolean)](../html/M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnCursor_1.htm "CenterFormOnCursor Method (Form, Boolean)")

[CenterFormOnCursor Method (Window, Boolean)](../html/M_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnCursor.htm "CenterFormOnCursor Method (Window, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_WindowsFormUtilAddLanguageSpecificTextSet("LSTCF3652AC\_0?cpp=::|nu=.");CenterFormOnCursor Method (Form, Boolean) |

Positions a Form so that it is centered around the cursor

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void CenterFormOnCursor(
	Form F,
	bool limitToScreen
)
```

```
Public Shared Sub CenterFormOnCursor ( 
	F As Form,
	limitToScreen As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

F
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LSTCF3652AC\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Form](https://docs.microsoft.com/dotnet/api/system.windows.forms.form)  
    The Form to adjust

limitToScreen
:   Type: [SystemAddLanguageSpecificTextSet("LSTCF3652AC\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, the Form won't be allowed to extend beyond the limits of the screen containing the cursor.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_WindowsFormUtil Class](T_Grasshopper_GUI_GH_WindowsFormUtil.htm)

[CenterFormOnCursor Overload](Overload_Grasshopper_GUI_GH_WindowsFormUtil_CenterFormOnCursor.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)