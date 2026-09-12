# T_Grasshopper_GUI_GH_VerticalScrollBar

﻿ GH\_VerticalScrollBar Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_VerticalScrollBar Class](../html/T_Grasshopper_GUI_GH_VerticalScrollBar.htm "GH_VerticalScrollBar Class")

[GH\_VerticalScrollBar Constructor](../html/M_Grasshopper_GUI_GH_VerticalScrollBar__ctor.htm "GH_VerticalScrollBar Constructor ")

[GH\_VerticalScrollBar Properties](../html/Properties_T_Grasshopper_GUI_GH_VerticalScrollBar.htm "GH_VerticalScrollBar Properties")

[GH\_VerticalScrollBar Methods](../html/Methods_T_Grasshopper_GUI_GH_VerticalScrollBar.htm "GH_VerticalScrollBar Methods")

[GH\_VerticalScrollBar Events](../html/Events_T_Grasshopper_GUI_GH_VerticalScrollBar.htm "GH_VerticalScrollBar Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_VerticalScrollBar Class |

Scroll bar control with floating point accuracy.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST99A36699\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST99A36699\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
    [System.ComponentModelAddLanguageSpecificTextSet("LST99A36699\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Component](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
      [System.Windows.FormsAddLanguageSpecificTextSet("LST99A36699\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
        [System.Windows.FormsAddLanguageSpecificTextSet("LST99A36699\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
          [System.Windows.FormsAddLanguageSpecificTextSet("LST99A36699\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Panel](https://docs.microsoft.com/dotnet/api/system.windows.forms.panel)  
            [Grasshopper.GUIAddLanguageSpecificTextSet("LST99A36699\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DoubleBufferedPanel](T_Grasshopper_GUI_GH_DoubleBufferedPanel.htm)  
              Grasshopper.GUIAddLanguageSpecificTextSet("LST99A36699\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_VerticalScrollBar

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_VerticalScrollBar : GH_DoubleBufferedPanel
```

```
Public Class GH_VerticalScrollBar
	Inherits GH_DoubleBufferedPanel
```

AddLanguageTabSet("ID1EBCA");

The GH\_VerticalScrollBar type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_VerticalScrollBar](M_Grasshopper_GUI_GH_VerticalScrollBar__ctor.htm) | Initializes a new instance of the GH\_VerticalScrollBar class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Grip](P_Grasshopper_GUI_GH_VerticalScrollBar_Grip.htm) | Gets the actual dimensions of the scroll bar grip. |
| Public property | [GripRegion](P_Grasshopper_GUI_GH_VerticalScrollBar_GripRegion.htm) | Gets the grip region for this scroll bar. The Grip Region is the area in which the grip can be found. It is essentially the Client area minus the padding. |
| Public property | [ImpliedVerticalOffset](P_Grasshopper_GUI_GH_VerticalScrollBar_ImpliedVerticalOffset.htm) | Gets or sets the offset of the target region as implied by the scroll ratio. If you set this value, the ratio is reverse engineered. |
| Public property | [ScreenHeight](P_Grasshopper_GUI_GH_VerticalScrollBar_ScreenHeight.htm) | Gets or sets the height of the screen area (the visible area) |
| Public property | [TargetHeight](P_Grasshopper_GUI_GH_VerticalScrollBar_TargetHeight.htm) | Gets or sets the height of the target area (the area being scrolled) |
| Public property | [TargetRatio](P_Grasshopper_GUI_GH_VerticalScrollBar_TargetRatio.htm) | Gets or sets the scroll ration. If the scroll ratio is changed, the OnScrollRatioChanged event will be raised. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [OnPaint](M_Grasshopper_GUI_GH_VerticalScrollBar_OnPaint.htm) | (Overrides [ControlAddLanguageSpecificTextSet("LST99A36699\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-windows-forms-control-onpaint(system-windows-forms-painteventargs)).) |
| Protected method | [OnPaintBackground](M_Grasshopper_GUI_GH_VerticalScrollBar_OnPaintBackground.htm) | (Overrides [ScrollableControlAddLanguageSpecificTextSet("LST99A36699\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-windows-forms-scrollablecontrol-onpaintbackground(system-windows-forms-painteventargs)).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [ScrollRatioChanged](E_Grasshopper_GUI_GH_VerticalScrollBar_ScrollRatioChanged.htm) |  |

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