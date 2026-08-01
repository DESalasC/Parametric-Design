# M_Grasshopper_GUI_GH_EtoUtil_CenterFormOnCursor

﻿ GH\_EtoUtil.CenterFormOnCursor Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_EtoUtil Class](../html/T_Grasshopper_GUI_GH_EtoUtil.htm "GH_EtoUtil Class")

[GH\_EtoUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_EtoUtil.htm "GH_EtoUtil Methods")

[CenterFormOnCursor Method](../html/M_Grasshopper_GUI_GH_EtoUtil_CenterFormOnCursor.htm "CenterFormOnCursor Method ")

[CenterFormOnEditor Method](../html/M_Grasshopper_GUI_GH_EtoUtil_CenterFormOnEditor.htm "CenterFormOnEditor Method ")

[CenterFormOnScreen Method](../html/M_Grasshopper_GUI_GH_EtoUtil_CenterFormOnScreen.htm "CenterFormOnScreen Method ")

[CenterFormOnWindow Method](../html/M_Grasshopper_GUI_GH_EtoUtil_CenterFormOnWindow.htm "CenterFormOnWindow Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_EtoUtilAddLanguageSpecificTextSet("LST1F372D3B\_0?cpp=::|nu=.");CenterFormOnCursor Method |

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
	this Window F,
	bool limitToScreen
)
```

```
<ExtensionAttribute>
Public Shared Sub CenterFormOnCursor ( 
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
:   Type: [SystemAddLanguageSpecificTextSet("LST1F372D3B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, the Form won't be allowed to extend beyond the limits of the screen containing the cursor.

#### Usage Note

In Visual Basic and C#, you can call this method as an instance method on any object of type Window. When you use instance method syntax to call this method, omit the first parameter. For more information, see [Extension Methods (Visual Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-guide/language-features/procedures/extension-methods) or [Extension Methods (C# Programming Guide)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-structs/extension-methods).

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_EtoUtil Class](T_Grasshopper_GUI_GH_EtoUtil.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)