# T_Grasshopper_GUI_Base_GH_ColourPickerBase

﻿ GH\_ColourPickerBase Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_ColourPickerBase Class](../html/T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm "GH_ColourPickerBase Class")

[GH\_ColourPickerBase Constructor](../html/M_Grasshopper_GUI_Base_GH_ColourPickerBase__ctor.htm "GH_ColourPickerBase Constructor ")

[GH\_ColourPickerBase Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm "GH_ColourPickerBase Properties")

[GH\_ColourPickerBase Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm "GH_ColourPickerBase Methods")

[GH\_ColourPickerBase Events](../html/Events_T_Grasshopper_GUI_Base_GH_ColourPickerBase.htm "GH_ColourPickerBase Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ColourPickerBase Class |

Provides Colour picker GUI not tied to a control-handle.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST3732CD81\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.BaseAddLanguageSpecificTextSet("LST3732CD81\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ColourPickerBase

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ColourPickerBase
```

```
Public Class GH_ColourPickerBase
```

AddLanguageTabSet("ID1EBCA");

The GH\_ColourPickerBase type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ColourPickerBase](M_Grasshopper_GUI_Base_GH_ColourPickerBase__ctor.htm) | Create a new instance of the Colour Picker base control. This constructor assigns the default Colour space model and involves a call to the Grasshopper core settings server. You must call SetupColourPicker() prior to rendering this control on screen. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AutoSize](P_Grasshopper_GUI_Base_GH_ColourPickerBase_AutoSize.htm) | Gets or sets a value indicating whether the width and height of the Bounds are adjusted to fit the UI. |
| Public property | [BackColour](P_Grasshopper_GUI_Base_GH_ColourPickerBase_BackColour.htm) | Gets or sets the background colour of the picker. |
| Public property | [BaseColour](P_Grasshopper_GUI_Base_GH_ColourPickerBase_BaseColour.htm) | Gets the original base colour for this picker. Use SetupColourPicker to assign this colour. |
| Public property | [Bounds](P_Grasshopper_GUI_Base_GH_ColourPickerBase_Bounds.htm) | Gets or sets the Bounds for this control. |
| Public property | [ColourSpace](P_Grasshopper_GUI_Base_GH_ColourPickerBase_ColourSpace.htm) | Gets the Colour space mode used in this picker. |
| Public property | [DesiredHeight](P_Grasshopper_GUI_Base_GH_ColourPickerBase_DesiredHeight.htm) | Gets the ideal height for this colour picker given it's width and UI settings. |
| Public property | [DrawAlphaSlider](P_Grasshopper_GUI_Base_GH_ColourPickerBase_DrawAlphaSlider.htm) | Gets or sets whether or not the alpha slider is included in the UI. |
| Public property | [DrawBackground](P_Grasshopper_GUI_Base_GH_ColourPickerBase_DrawBackground.htm) | Gets or sets whether the background of the picker is drawn. |
| Public property | [DrawChannelSliders](P_Grasshopper_GUI_Base_GH_ColourPickerBase_DrawChannelSliders.htm) | Gets or sets whether or not the three basic channel sliders are included in the UI. |
| Public property | [DropperPreviewBox](P_Grasshopper_GUI_Base_GH_ColourPickerBase_DropperPreviewBox.htm) | Gets the rectangle in which the eye-dropped preview will be drawn. |
| Public property | [Font](P_Grasshopper_GUI_Base_GH_ColourPickerBase_Font.htm) | Gets or sets the Font used in this Colour Picker. Do not Dispose the Font returned by this property. |
| Public property | [IsTextInput](P_Grasshopper_GUI_Base_GH_ColourPickerBase_IsTextInput.htm) | Gets whether any of the slider is currently displaying a text input box. |
| Public property | [Padding](P_Grasshopper_GUI_Base_GH_ColourPickerBase_Padding.htm) | Gets or sets the Padding for this control. |
| Public property | [PickColour](P_Grasshopper_GUI_Base_GH_ColourPickerBase_PickColour.htm) | Gets the picked colour. |
| Public property | [SRCSpaceBox](P_Grasshopper_GUI_Base_GH_ColourPickerBase_SRCSpaceBox.htm) | Gets the rectangle containing the eye-dropper function. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Invalidate](M_Grasshopper_GUI_Base_GH_ColourPickerBase_Invalidate.htm) | Raise the Invalidated event. |
| Public method | [MouseClick](M_Grasshopper_GUI_Base_GH_ColourPickerBase_MouseClick.htm) | Respond to mouse-click events. |
| Public method | [MouseDoubleClick](M_Grasshopper_GUI_Base_GH_ColourPickerBase_MouseDoubleClick.htm) | Respond to mouse-doubleclick events. |
| Public method | [MouseDown](M_Grasshopper_GUI_Base_GH_ColourPickerBase_MouseDown.htm) | Respond to mouse-down events. |
| Public method | [MouseMove](M_Grasshopper_GUI_Base_GH_ColourPickerBase_MouseMove.htm) | Respond to mouse-move events. |
| Public method | [MouseUp](M_Grasshopper_GUI_Base_GH_ColourPickerBase_MouseUp.htm) | Respond to mouse-up events. |
| Public method | [OnColorChanged](M_Grasshopper_GUI_Base_GH_ColourPickerBase_OnColorChanged.htm) | Raise the ColorChanged event. |
| Public method | [Render](M_Grasshopper_GUI_Base_GH_ColourPickerBase_Render.htm) | Render this slider into a Graphics context. |
| Public method | [RespondToEnter](M_Grasshopper_GUI_Base_GH_ColourPickerBase_RespondToEnter.htm) |  |
| Public method | [RespondToEscape](M_Grasshopper_GUI_Base_GH_ColourPickerBase_RespondToEscape.htm) |  |
| Public method | [SetUiScaling](M_Grasshopper_GUI_Base_GH_ColourPickerBase_SetUiScaling.htm) |  |
| Public method | [SetupColourPicker(Color, Point4d, GH\_ColourSpace)](M_Grasshopper_GUI_Base_GH_ColourPickerBase_SetupColourPicker.htm) | Setup all UI elements. |
| Public method | [SetupColourPicker(Color, Color, GH\_ColourSpace)](M_Grasshopper_GUI_Base_GH_ColourPickerBase_SetupColourPicker_1.htm) | Setup all UI elements. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [ColorChanged](E_Grasshopper_GUI_Base_GH_ColourPickerBase_ColorChanged.htm) | Raised whenever the color of this picker is changed due to User-Interface methods. |
| Public event | [Invalidated](E_Grasshopper_GUI_Base_GH_ColourPickerBase_Invalidated.htm) | Raised whenever a redraw is required. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)