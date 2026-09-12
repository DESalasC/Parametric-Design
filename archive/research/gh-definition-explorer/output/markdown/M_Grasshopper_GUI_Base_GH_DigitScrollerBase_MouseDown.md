# M_Grasshopper_GUI_Base_GH_DigitScrollerBase_MouseDown

﻿ GH\_DigitScrollerBase.MouseDown Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_DigitScrollerBase Class](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm "GH_DigitScrollerBase Class")

[GH\_DigitScrollerBase Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm "GH_DigitScrollerBase Methods")

[HandleTextInputAccepted Method](../html/M_Grasshopper_GUI_Base_GH_DigitScrollerBase_HandleTextInputAccepted.htm "HandleTextInputAccepted Method ")

[MouseDown Method](../html/M_Grasshopper_GUI_Base_GH_DigitScrollerBase_MouseDown.htm "MouseDown Method ")

[MouseMove Method](../html/M_Grasshopper_GUI_Base_GH_DigitScrollerBase_MouseMove.htm "MouseMove Method ")

[MouseUp Method](../html/M_Grasshopper_GUI_Base_GH_DigitScrollerBase_MouseUp.htm "MouseUp Method ")

[OnInvalidated Method](../html/M_Grasshopper_GUI_Base_GH_DigitScrollerBase_OnInvalidated.htm "OnInvalidated Method ")

[OnValueChanged Method](../html/M_Grasshopper_GUI_Base_GH_DigitScrollerBase_OnValueChanged.htm "OnValueChanged Method ")

[Render Method](../html/M_Grasshopper_GUI_Base_GH_DigitScrollerBase_Render.htm "Render Method ")

[SetupScroller Method](../html/M_Grasshopper_GUI_Base_GH_DigitScrollerBase_SetupScroller.htm "SetupScroller Method ")

[ShowTextInputBox Method](../html/Overload_Grasshopper_GUI_Base_GH_DigitScrollerBase_ShowTextInputBox.htm "ShowTextInputBox Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DigitScrollerBaseAddLanguageSpecificTextSet("LSTD03D0753\_0?cpp=::|nu=.");MouseDown Method |

Respond to mouse-down events.

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_DigitScrollerBaseAddLanguageSpecificTextSet("LSTD03D0753_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH_MouseAction MouseDown(
	MouseEventArgs args,
	PointF pt
)
```

```
Public Function MouseDown ( 
	args As MouseEventArgs,
	pt As PointF
) As GH_DigitScrollerBaseAddLanguageSpecificTextSet("LSTD03D0753_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH_MouseAction
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

args
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LSTD03D0753\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");MouseEventArgs](https://docs.microsoft.com/dotnet/api/system.windows.forms.mouseeventargs)  
    Mouse Event arguments.

pt
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTD03D0753\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Mouse cursor position in floating point accuracy.

#### Return Value

Type: [GH\_DigitScrollerBaseAddLanguageSpecificTextSet("LSTD03D0753\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MouseAction](T_Grasshopper_GUI_Base_GH_DigitScrollerBase_GH_MouseAction.htm)  
True if a Drag operation was started, false if the event went unnoticed.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DigitScrollerBase Class](T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm)

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)