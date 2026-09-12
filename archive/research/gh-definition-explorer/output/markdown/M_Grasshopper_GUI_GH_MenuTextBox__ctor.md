# M_Grasshopper_GUI_GH_MenuTextBox__ctor

﻿ GH\_MenuTextBox Constructor 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_MenuTextBox Class](../html/T_Grasshopper_GUI_GH_MenuTextBox.htm "GH_MenuTextBox Class")

[GH\_MenuTextBox Constructor](../html/M_Grasshopper_GUI_GH_MenuTextBox__ctor.htm "GH_MenuTextBox Constructor ")

[GH\_MenuTextBox Properties](../html/Properties_T_Grasshopper_GUI_GH_MenuTextBox.htm "GH_MenuTextBox Properties")

[GH\_MenuTextBox Methods](../html/Methods_T_Grasshopper_GUI_GH_MenuTextBox.htm "GH_MenuTextBox Methods")

[GH\_MenuTextBox Events](../html/Events_T_Grasshopper_GUI_GH_MenuTextBox.htm "GH_MenuTextBox Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MenuTextBox Constructor |

Constructor for TextBox collection.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_MenuTextBox(
	ToolStripDropDown dropDown,
	string text,
	bool lockFocus
)
```

```
Public Sub New ( 
	dropDown As ToolStripDropDown,
	text As String,
	lockFocus As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

dropDown
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LSTE5DD20C9\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");ToolStripDropDown](https://docs.microsoft.com/dotnet/api/system.windows.forms.toolstripdropdown)  
    The menu dropdown into which to embed this textbox control.

text
:   Type: [SystemAddLanguageSpecificTextSet("LSTE5DD20C9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The original text to be displayed in the textbox.

lockFocus
:   Type: [SystemAddLanguageSpecificTextSet("LSTE5DD20C9\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, the control will disable the other menu items when it gets focus.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MenuTextBox Class](T_Grasshopper_GUI_GH_MenuTextBox.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)