# Methods_T_Grasshopper_GUI_Base_GH_SliderBase

﻿ GH\_SliderBase Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_SliderBase Class](../html/T_Grasshopper_GUI_Base_GH_SliderBase.htm "GH_SliderBase Class")

[GH\_SliderBase Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_SliderBase.htm "GH_SliderBase Methods")

[FixDomain Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_FixDomain.htm "FixDomain Method ")

[FixValue Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_FixValue.htm "FixValue Method ")

[HandleTextInputAccepted Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_HandleTextInputAccepted.htm "HandleTextInputAccepted Method ")

[KeyDown Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_KeyDown.htm "KeyDown Method ")

[MouseDown Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_MouseDown.htm "MouseDown Method ")

[MouseMove Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_MouseMove.htm "MouseMove Method ")

[MouseUp Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_MouseUp.htm "MouseUp Method ")

[OnValueChanged Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_OnValueChanged.htm "OnValueChanged Method ")

[ProcessNumber Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_ProcessNumber.htm "ProcessNumber Method ")

[Render Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_Render.htm "Render Method ")

[SetSnapRanges Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_SetSnapRanges.htm "SetSnapRanges Method ")

[ShowTextInputBox Method](../html/Overload_Grasshopper_GUI_Base_GH_SliderBase_ShowTextInputBox.htm "ShowTextInputBox Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SliderBase Methods |

The [GH\_SliderBase](T_Grasshopper_GUI_Base_GH_SliderBase.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [FixDomain](M_Grasshopper_GUI_Base_GH_SliderBase_FixDomain.htm) | Fix the limits of the slider. Limits will be rounded according to slider type and accuracy. Also, a minimum range for all types is ensured. |
| Public method | [FixValue](M_Grasshopper_GUI_Base_GH_SliderBase_FixValue.htm) | Fix the value of the slider. The value will be rounded according to slider type and accuracy. Also, the value will be clipped to the limits. Before you call this function, ensure the limits are set up correctly. |
| Protected method | [HandleTextInputAccepted](M_Grasshopper_GUI_Base_GH_SliderBase_HandleTextInputAccepted.htm) | (Overrides [GH\_TextBoxInputBaseAddLanguageSpecificTextSet("LSTB80C9955\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");HandleTextInputAccepted(String)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_HandleTextInputAccepted.htm).) |
| Public method | [HideTextInputBox](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_HideTextInputBox.htm) | Hides the text-input override form (if it is displayed). (Inherited from [GH\_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).) |
| Public method | [KeyDown](M_Grasshopper_GUI_Base_GH_SliderBase_KeyDown.htm) | Respond to a KeyDown event. |
| Public method | [MouseDown](M_Grasshopper_GUI_Base_GH_SliderBase_MouseDown.htm) | Respond to mouse-down events. |
| Public method | [MouseMove](M_Grasshopper_GUI_Base_GH_SliderBase_MouseMove.htm) | Respond to mouse-move events. |
| Public method | [MouseUp](M_Grasshopper_GUI_Base_GH_SliderBase_MouseUp.htm) | Respond to mouse-up events. |
| Public method | [OnValueChanged](M_Grasshopper_GUI_Base_GH_SliderBase_OnValueChanged.htm) | Raise the ValueChanged event. |
| Public methodStatic member | [ProcessNumber](M_Grasshopper_GUI_Base_GH_SliderBase_ProcessNumber.htm) | Process a number using the given slider characteristics. |
| Public method | [Render](M_Grasshopper_GUI_Base_GH_SliderBase_Render.htm) | Render this slider into a Graphics context. |
| Public method | [RespondToEnter](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_RespondToEnter.htm) | (Inherited from [GH\_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).) |
| Public method | [RespondToEscape](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_RespondToEscape.htm) | (Inherited from [GH\_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).) |
| Public method | [SetSnapRanges](M_Grasshopper_GUI_Base_GH_SliderBase_SetSnapRanges.htm) | Assign a collection of snap ranges to this slider. |
| Public method | [ShowTextInputBox(Control)](M_Grasshopper_GUI_Base_GH_SliderBase_ShowTextInputBox.htm) |  |
| Public method | [ShowTextInputBox(Control, Boolean)](M_Grasshopper_GUI_Base_GH_SliderBase_ShowTextInputBox_1.htm) |  |
| Public method | [ShowTextInputBox(Control, Boolean, Matrix)](M_Grasshopper_GUI_Base_GH_SliderBase_ShowTextInputBox_2.htm) |  |
| Public method | [ShowTextInputBox(Control, String, Boolean)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_ShowTextInputBox.htm) | Display a floating text-box on top of the owner control. (Inherited from [GH\_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).) |
| Public method | [ShowTextInputBox(Control, Boolean, Matrix, String)](M_Grasshopper_GUI_Base_GH_SliderBase_ShowTextInputBox_3.htm) |  |
| Public method | [ShowTextInputBox(Control, String, Boolean, Boolean)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_ShowTextInputBox_1.htm) | Display a floating text-box on top of the owner control. (Inherited from [GH\_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).) |
| Public method | [ShowTextInputBox(Control, String, Boolean, Boolean, Matrix)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_ShowTextInputBox_2.htm) | Display a floating text-box on top of the owner control. (Inherited from [GH\_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_SliderBase Class](T_Grasshopper_GUI_Base_GH_SliderBase.htm)

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)