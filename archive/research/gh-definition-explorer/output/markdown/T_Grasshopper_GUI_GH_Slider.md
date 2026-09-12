# T_Grasshopper_GUI_GH_Slider

﻿ GH\_Slider Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_Slider Class](../html/T_Grasshopper_GUI_GH_Slider.htm "GH_Slider Class")

[GH\_Slider Constructor](../html/M_Grasshopper_GUI_GH_Slider__ctor.htm "GH_Slider Constructor ")

[GH\_Slider Properties](../html/Properties_T_Grasshopper_GUI_GH_Slider.htm "GH_Slider Properties")

[GH\_Slider Methods](../html/Methods_T_Grasshopper_GUI_GH_Slider.htm "GH_Slider Methods")

[GH\_Slider Events](../html/Events_T_Grasshopper_GUI_GH_Slider.htm "GH_Slider Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Slider Class |

Provides a standard Grasshopper slider as a winforms control.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST1A4EA9E8\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST1A4EA9E8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
    [System.ComponentModelAddLanguageSpecificTextSet("LST1A4EA9E8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Component](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
      [System.Windows.FormsAddLanguageSpecificTextSet("LST1A4EA9E8\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
        [System.Windows.FormsAddLanguageSpecificTextSet("LST1A4EA9E8\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
          [System.Windows.FormsAddLanguageSpecificTextSet("LST1A4EA9E8\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
            [System.Windows.FormsAddLanguageSpecificTextSet("LST1A4EA9E8\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");UserControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.usercontrol)  
              GH\_TextInputBaseControl  
                Grasshopper.GUIAddLanguageSpecificTextSet("LST1A4EA9E8\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Slider

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Slider : GH_TextInputBaseControl
```

```
Public Class GH_Slider
	Inherits GH_TextInputBaseControl
```

AddLanguageTabSet("ID1EBCA");

The GH\_Slider type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_Slider](M_Grasshopper_GUI_GH_Slider__ctor.htm) | Initializes a new instance of the GH\_Slider class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ControlEdgeColour](P_Grasshopper_GUI_GH_Slider_ControlEdgeColour.htm) | Gets or sets the EdgeColor for this slider control. |
| Public property | [ControlShadowColour](P_Grasshopper_GUI_GH_Slider_ControlShadowColour.htm) | Gets or sets the Shadow colour for this control. |
| Public property | [DecimalPlaces](P_Grasshopper_GUI_GH_Slider_DecimalPlaces.htm) | Gets or sets the number of decimal places allowed for Floating Point Sliders. |
| Public property | [DrawControlBorder](P_Grasshopper_GUI_GH_Slider_DrawControlBorder.htm) | Gets or sets whether the border of the slider should be drawn. |
| Public property | [DrawControlShadows](P_Grasshopper_GUI_GH_Slider_DrawControlShadows.htm) | Gets or sets whether the drop shadows of the slider should be drawn. |
| Public property | [FormatMask](P_Grasshopper_GUI_GH_Slider_FormatMask.htm) | Gets or sets the string format mask to use for the display. Should contain at least one "{0}" element. |
| Public property | [GripBottomColour](P_Grasshopper_GUI_GH_Slider_GripBottomColour.htm) | Gets or sets the fill colour for the bottom edge of the slider grip. |
| Public property | [GripDisplay](P_Grasshopper_GUI_GH_Slider_GripDisplay.htm) | Gets or sets how the slider grip (or thumb) is drawn. |
| Public property | [GripEdgeColour](P_Grasshopper_GUI_GH_Slider_GripEdgeColour.htm) | Gets or sets the edge colour for the slider grip. |
| Public property | [GripTopColour](P_Grasshopper_GUI_GH_Slider_GripTopColour.htm) | Gets or sets the fill colour for the top edge of the slider grip. |
| Public property | [Maximum](P_Grasshopper_GUI_GH_Slider_Maximum.htm) | Gets or sets the upper numeric limit for the slider range. |
| Public property | [Minimum](P_Grasshopper_GUI_GH_Slider_Minimum.htm) | Gets or sets the lower numeric limit for the slider range. |
| Public property | [RailBrightColour](P_Grasshopper_GUI_GH_Slider_RailBrightColour.htm) | Gets or sets the edge colour for the bright parts of the rail. |
| Public property | [RailDarkColour](P_Grasshopper_GUI_GH_Slider_RailDarkColour.htm) | Gets or sets the edge colour for the dark parts of the rail. |
| Public property | [RailDisplay](P_Grasshopper_GUI_GH_Slider_RailDisplay.htm) | Gets or sets how the slider rail (or track) is drawn. |
| Public property | [RailEmptyColour](P_Grasshopper_GUI_GH_Slider_RailEmptyColour.htm) | Gets or sets the fill colour for the empty portion of the rail. |
| Public property | [RailFullColour](P_Grasshopper_GUI_GH_Slider_RailFullColour.htm) | Gets or sets the fill colour for the full portion of the rail. |
| Public property | [ShadowSize](P_Grasshopper_GUI_GH_Slider_ShadowSize.htm) | Gets or sets the size of the border shadow along all edges of the box. |
| Public property | [TextColour](P_Grasshopper_GUI_GH_Slider_TextColour.htm) | Gets or sets the fill colour for the slider text. |
| Public property | [TickCount](P_Grasshopper_GUI_GH_Slider_TickCount.htm) | Gets or sets the number of ticks. |
| Public property | [TickDisplay](P_Grasshopper_GUI_GH_Slider_TickDisplay.htm) | Gets or sets how the slider ticks are drawn. |
| Public property | [TickFrequency](P_Grasshopper_GUI_GH_Slider_TickFrequency.htm) | Gets or sets the frequency of large ticks vs small ticks. |
| Public property | [Type](P_Grasshopper_GUI_GH_Slider_Type.htm) | Gets or sets the numeric type of this slider. |
| Public property | [Value](P_Grasshopper_GUI_GH_Slider_Value.htm) | Gets or sets the numeric value for the slider range. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Input\_Assign](M_Grasshopper_GUI_GH_Slider_Input_Assign.htm) | (Overrides GH\_TextInputBaseControl.Input\_Assign(String).) |
| Protected method | [Input\_Parse](M_Grasshopper_GUI_GH_Slider_Input_Parse.htm) | (Overrides GH\_TextInputBaseControl.Input\_Parse(String).) |
| Protected method | [Input\_Supply](M_Grasshopper_GUI_GH_Slider_Input_Supply.htm) | (Overrides GH\_TextInputBaseControl.Input\_SupplyAddLanguageSpecificTextSet("LST1A4EA9E8\_8?cs=()|vb=|cpp=()|nu=()|fs=()");.) |
| Protected method | [OnPaint](M_Grasshopper_GUI_GH_Slider_OnPaint.htm) | (Overrides [ControlAddLanguageSpecificTextSet("LST1A4EA9E8\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-windows-forms-control-onpaint(system-windows-forms-painteventargs)).) |
| Protected method | [OnPaintBackground](M_Grasshopper_GUI_GH_Slider_OnPaintBackground.htm) | (Overrides [ScrollableControlAddLanguageSpecificTextSet("LST1A4EA9E8\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-windows-forms-scrollablecontrol-onpaintbackground(system-windows-forms-painteventargs)).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [ValueChanged](E_Grasshopper_GUI_GH_Slider_ValueChanged.htm) | Raised whenever the value of the slider is changed via GUI interaction. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Extension Methods

|  | Name | Description |
| --- | --- | --- |
| Public Extension Method | [ToEto](M_Grasshopper_EtoExtensions_ToEto_7.htm) | (Defined by [EtoExtensions](T_Grasshopper_EtoExtensions.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)