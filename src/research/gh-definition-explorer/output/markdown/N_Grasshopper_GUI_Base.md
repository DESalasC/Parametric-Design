# N_Grasshopper_GUI_Base

﻿ Grasshopper.GUI.Base Namespace

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_ColourCube Class](../html/T_Grasshopper_GUI_Base_GH_ColourCube.htm "GH_ColourCube Class")

[GH\_ColourPickerBase Class](../html/T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm "GH_ColourPickerBase Class")

[GH\_ColourPickerBase.ColorChangedEventHandler Delegate](../html/T_Grasshopper_GUI_Base_GH_ColourPickerBase_ColorChangedEventHandler.htm "GH_ColourPickerBase.ColorChangedEventHandler Delegate")

[GH\_ColourPickerBase.InvalidatedEventHandler Delegate](../html/T_Grasshopper_GUI_Base_GH_ColourPickerBase_InvalidatedEventHandler.htm "GH_ColourPickerBase.InvalidatedEventHandler Delegate")

[GH\_ColourPickerEventArgs Class](../html/T_Grasshopper_GUI_Base_GH_ColourPickerEventArgs.htm "GH_ColourPickerEventArgs Class")

[GH\_ColourSpace Enumeration](../html/T_Grasshopper_GUI_Base_GH_ColourSpace.htm "GH_ColourSpace Enumeration")

[GH\_DigitAlign Enumeration](../html/T_Grasshopper_GUI_Base_GH_DigitAlign.htm "GH_DigitAlign Enumeration")

[GH\_DigitNumber Class](../html/T_Grasshopper_GUI_Base_GH_DigitNumber.htm "GH_DigitNumber Class")

[GH\_DigitScrollerBase Class](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm "GH_DigitScrollerBase Class")

[GH\_DigitScrollerBase.GH\_MouseAction Enumeration](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase_GH_MouseAction.htm "GH_DigitScrollerBase.GH_MouseAction Enumeration")

[GH\_DigitScrollerBase.InvalidatedEventHandler Delegate](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase_InvalidatedEventHandler.htm "GH_DigitScrollerBase.InvalidatedEventHandler Delegate")

[GH\_DigitScrollerBase.ValueChangedEventHandler Delegate](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerBase_ValueChangedEventHandler.htm "GH_DigitScrollerBase.ValueChangedEventHandler Delegate")

[GH\_DigitScrollerEventArgs Class](../html/T_Grasshopper_GUI_Base_GH_DigitScrollerEventArgs.htm "GH_DigitScrollerEventArgs Class")

[GH\_ScrollBarVerticalBase Class](../html/T_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase.htm "GH_ScrollBarVerticalBase Class")

[GH\_SliderAccuracy Enumeration](../html/T_Grasshopper_GUI_Base_GH_SliderAccuracy.htm "GH_SliderAccuracy Enumeration")

[GH\_SliderBase Class](../html/T_Grasshopper_GUI_Base_GH_SliderBase.htm "GH_SliderBase Class")

[GH\_SliderBase.DrawSliderChannel Delegate](../html/T_Grasshopper_GUI_Base_GH_SliderBase_DrawSliderChannel.htm "GH_SliderBase.DrawSliderChannel Delegate")

[GH\_SliderBase.TextInputHandler Delegate](../html/T_Grasshopper_GUI_Base_GH_SliderBase_TextInputHandler.htm "GH_SliderBase.TextInputHandler Delegate")

[GH\_SliderBase.ValueChangedEventHandler Delegate](../html/T_Grasshopper_GUI_Base_GH_SliderBase_ValueChangedEventHandler.htm "GH_SliderBase.ValueChangedEventHandler Delegate")

[GH\_SliderEventArgs Class](../html/T_Grasshopper_GUI_Base_GH_SliderEventArgs.htm "GH_SliderEventArgs Class")

[GH\_SliderGripDisplay Enumeration](../html/T_Grasshopper_GUI_Base_GH_SliderGripDisplay.htm "GH_SliderGripDisplay Enumeration")

[GH\_SliderRailDisplay Enumeration](../html/T_Grasshopper_GUI_Base_GH_SliderRailDisplay.htm "GH_SliderRailDisplay Enumeration")

[GH\_SliderTickDisplay Enumeration](../html/T_Grasshopper_GUI_Base_GH_SliderTickDisplay.htm "GH_SliderTickDisplay Enumeration")

[GH\_TextBoxInputBase Class](../html/T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm "GH_TextBoxInputBase Class")

[SliderSnapRange Structure](../html/T_Grasshopper_GUI_Base_SliderSnapRange.htm "SliderSnapRange Structure")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Grasshopper.GUI.Base Namespace |

This namespace contains general purpose UI elements that have been divorced from winforms Control handles. This allows them to be rendered on screen as part of a larger constellation of UI elements. There are dedicated winforms control implementations of all the elements in this namespace in the Grasshopper.GUI namespace.

![](../icons/SectionExpanded.png)Classes

|  | Class | Description |
| --- | --- | --- |
| Public class | [GH\_ColourCube](T_Grasshopper_GUI_Base_GH_ColourCube.htm) | Maintains a collection of graphical shapes and coordinates that specify important features of the Colour Space Cube graphics. |
| Public class | [GH\_ColourPickerBase](T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm) | Provides Colour picker GUI not tied to a control-handle. |
| Public class | [GH\_ColourPickerEventArgs](T_Grasshopper_GUI_Base_GH_ColourPickerEventArgs.htm) | Arguments passed via GH\_SliderBase.ValueChanged events. |
| Public class | [GH\_DigitNumber](T_Grasshopper_GUI_Base_GH_DigitNumber.htm) | Maintains and provides functionality for evaluating and modifying numbers as used in the GH\_DigitScrollerBase control. |
| Public class | [GH\_DigitScrollerBase](T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm) | Provides Numeric digit scrolling GUI not tied to a control-handle. |
| Public class | [GH\_DigitScrollerEventArgs](T_Grasshopper_GUI_Base_GH_DigitScrollerEventArgs.htm) | Arguments passed via GH\_digitScrollerBase.ValueChanged events. |
| Public class | [GH\_ScrollBarVerticalBase](T_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase.htm) | Provides basic vertical scroll bar logic. |
| Public class | [GH\_SliderBase](T_Grasshopper_GUI_Base_GH_SliderBase.htm) | Provides Numeric slider GUI not tied to a control-handle. |
| Public class | [GH\_SliderEventArgs](T_Grasshopper_GUI_Base_GH_SliderEventArgs.htm) | Arguments passed via GH\_SliderBase.ValueChanged events. |
| Public class | [GH\_TextBoxInputBase](T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm) |  |

![](../icons/SectionExpanded.png)Structures

|  | Structure | Description |
| --- | --- | --- |
| Public structure | [SliderSnapRange](T_Grasshopper_GUI_Base_SliderSnapRange.htm) | Represents a snap range on a slider. |

![](../icons/SectionExpanded.png)Delegates

|  | Delegate | Description |
| --- | --- | --- |
| Public delegate | [GH\_ColourPickerBaseAddLanguageSpecificTextSet("LSTB8F4CDC7\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");ColorChangedEventHandler](T_Grasshopper_GUI_Base_GH_ColourPickerBase_ColorChangedEventHandler.htm) |  |
| Public delegate | [GH\_ColourPickerBaseAddLanguageSpecificTextSet("LSTB8F4CDC7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");InvalidatedEventHandler](T_Grasshopper_GUI_Base_GH_ColourPickerBase_InvalidatedEventHandler.htm) |  |
| Public delegate | [GH\_DigitScrollerBaseAddLanguageSpecificTextSet("LSTB8F4CDC7\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");InvalidatedEventHandler](T_Grasshopper_GUI_Base_GH_DigitScrollerBase_InvalidatedEventHandler.htm) |  |
| Public delegate | [GH\_DigitScrollerBaseAddLanguageSpecificTextSet("LSTB8F4CDC7\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ValueChangedEventHandler](T_Grasshopper_GUI_Base_GH_DigitScrollerBase_ValueChangedEventHandler.htm) |  |
| Public delegate | [GH\_SliderBaseAddLanguageSpecificTextSet("LSTB8F4CDC7\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");DrawSliderChannel](T_Grasshopper_GUI_Base_GH_SliderBase_DrawSliderChannel.htm) | This delegate is used to intervene in the slider drawing process. |
| Public delegate | [GH\_SliderBaseAddLanguageSpecificTextSet("LSTB8F4CDC7\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");TextInputHandler](T_Grasshopper_GUI_Base_GH_SliderBase_TextInputHandler.htm) | Delegate used during Text Input handling. |
| Public delegate | [GH\_SliderBaseAddLanguageSpecificTextSet("LSTB8F4CDC7\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");ValueChangedEventHandler](T_Grasshopper_GUI_Base_GH_SliderBase_ValueChangedEventHandler.htm) |  |

![](../icons/SectionExpanded.png)Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
| Public enumeration | [GH\_ColourSpace](T_Grasshopper_GUI_Base_GH_ColourSpace.htm) | Enumerates the different colour spaces supported by the GH\_ColourPickerBase class. |
| Public enumeration | [GH\_DigitAlign](T_Grasshopper_GUI_Base_GH_DigitAlign.htm) | Enumerates the possible alignments for digits inside the GH\_DigitScroller control. |
| Public enumeration | [GH\_DigitScrollerBaseAddLanguageSpecificTextSet("LSTB8F4CDC7\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MouseAction](T_Grasshopper_GUI_Base_GH_DigitScrollerBase_GH_MouseAction.htm) | Enumerates the possible actions due to mouse-down mouse-move events. |
| Public enumeration | [GH\_SliderAccuracy](T_Grasshopper_GUI_Base_GH_SliderAccuracy.htm) | Enumerates the possible numeric slider accuracies. |
| Public enumeration | [GH\_SliderGripDisplay](T_Grasshopper_GUI_Base_GH_SliderGripDisplay.htm) | Enumerates the possible slider grip displays. |
| Public enumeration | [GH\_SliderRailDisplay](T_Grasshopper_GUI_Base_GH_SliderRailDisplay.htm) | Enumerates the possible slider rail displays. |
| Public enumeration | [GH\_SliderTickDisplay](T_Grasshopper_GUI_Base_GH_SliderTickDisplay.htm) | Enumerates the possible slider tick displays. |

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)