# T_Grasshopper_GUI_GH_Slider_Obsolete

﻿ GH\_Slider\_Obsolete Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_Slider\_Obsolete Class](../html/T_Grasshopper_GUI_GH_Slider_Obsolete.htm "GH_Slider_Obsolete Class")

[GH\_Slider\_Obsolete Constructor](../html/M_Grasshopper_GUI_GH_Slider_Obsolete__ctor.htm "GH_Slider_Obsolete Constructor ")

[GH\_Slider\_Obsolete Properties](../html/Properties_T_Grasshopper_GUI_GH_Slider_Obsolete.htm "GH_Slider_Obsolete Properties")

[GH\_Slider\_Obsolete Methods](../html/Methods_T_Grasshopper_GUI_GH_Slider_Obsolete.htm "GH_Slider_Obsolete Methods")

[GH\_Slider\_Obsolete Events](../html/Events_T_Grasshopper_GUI_GH_Slider_Obsolete.htm "GH_Slider_Obsolete Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Slider\_Obsolete Class |

General purpose numeric slider.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTE9D4B02B\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTE9D4B02B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
    [System.ComponentModelAddLanguageSpecificTextSet("LSTE9D4B02B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Component](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
      [System.Windows.FormsAddLanguageSpecificTextSet("LSTE9D4B02B\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
        [System.Windows.FormsAddLanguageSpecificTextSet("LSTE9D4B02B\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
          [System.Windows.FormsAddLanguageSpecificTextSet("LSTE9D4B02B\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
            [System.Windows.FormsAddLanguageSpecificTextSet("LSTE9D4B02B\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");UserControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.usercontrol)  
              Grasshopper.GUIAddLanguageSpecificTextSet("LSTE9D4B02B\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Slider\_Obsolete

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Slider_Obsolete : UserControl
```

```
Public Class GH_Slider_Obsolete
	Inherits UserControl
```

AddLanguageTabSet("ID1EBCA");

The GH\_Slider\_Obsolete type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_Slider\_Obsolete](M_Grasshopper_GUI_GH_Slider_Obsolete__ctor.htm) | Initializes a new instance of the GH\_Slider\_Obsolete class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [DisplayFormat](P_Grasshopper_GUI_GH_Slider_Obsolete_DisplayFormat.htm) | Gets or sets the display format fo the slider. This is the formatting that is applied prior to drawing. The default is {0} which results in a 1:1 display. Use this to append units or symbols. |
| Public property | [DrawRail](P_Grasshopper_GUI_GH_Slider_Obsolete_DrawRail.htm) | Gets or sets a flag that control whether or not grip rails are drawn. |
| Public property | [GripBackColor](P_Grasshopper_GUI_GH_Slider_Obsolete_GripBackColor.htm) | Background colour of slider grip. |
| Public property | [GripForeColor](P_Grasshopper_GUI_GH_Slider_Obsolete_GripForeColor.htm) | Foreground colour of slider grip. |
| Public property | [IsIntermediate](P_Grasshopper_GUI_GH_Slider_Obsolete_IsIntermediate.htm) | Gets the intermediate flag. If True, the user is currently dragging the slider. |
| Public property | [Max](P_Grasshopper_GUI_GH_Slider_Obsolete_Max.htm) | Gets or sets the maximum allowed value. |
| Public property | [Min](P_Grasshopper_GUI_GH_Slider_Obsolete_Min.htm) | Gets or sets the minimum allowed value. |
| Public property | [NumericFormat](P_Grasshopper_GUI_GH_Slider_Obsolete_NumericFormat.htm) | Gets or sets the numeric format for the slider. This is the formatting that is applied to the number. The default is #0.00 which results in a two digit rounding scheme. |
| Public property | [TextInputMode](P_Grasshopper_GUI_GH_Slider_Obsolete_TextInputMode.htm) | Gets or sets the Text input mode for this slider. |
| Public property | [TickFrequency](P_Grasshopper_GUI_GH_Slider_Obsolete_TickFrequency.htm) | Gets or sets the tick frequency of the slider. |
| Public property | [Value](P_Grasshopper_GUI_GH_Slider_Obsolete_Value.htm) | Gets or sets the current value. |
| Public property | [ValueF](P_Grasshopper_GUI_GH_Slider_Obsolete_ValueF.htm) | Gets or sets the current value in single-floating-point precision. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Dispose](M_Grasshopper_GUI_GH_Slider_Obsolete_Dispose.htm) | Releases the unmanaged resources used by the GH\_Slider\_Obsolete and optionally releases the managed resources (Overrides [ContainerControlAddLanguageSpecificTextSet("LSTE9D4B02B\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Dispose(Boolean)](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol.dispose#system-windows-forms-containercontrol-dispose(system-boolean)).) |
| Protected method | [OnPaint](M_Grasshopper_GUI_GH_Slider_Obsolete_OnPaint.htm) | (Overrides [ControlAddLanguageSpecificTextSet("LSTE9D4B02B\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-windows-forms-control-onpaint(system-windows-forms-painteventargs)).) |
| Protected method | [OnPaintBackground](M_Grasshopper_GUI_GH_Slider_Obsolete_OnPaintBackground.htm) | (Overrides [ScrollableControlAddLanguageSpecificTextSet("LSTE9D4B02B\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-windows-forms-scrollablecontrol-onpaintbackground(system-windows-forms-painteventargs)).) |
| Public method | [OnValueChanged](M_Grasshopper_GUI_GH_Slider_Obsolete_OnValueChanged.htm) | Raise the ValueChanged event |
| Public methodStatic member | [SendMessage](M_Grasshopper_GUI_GH_Slider_Obsolete_SendMessage.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [ValueChanged](E_Grasshopper_GUI_GH_Slider_Obsolete_ValueChanged.htm) | Raised whenever the value of the slider is changed via GUI interaction. |

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