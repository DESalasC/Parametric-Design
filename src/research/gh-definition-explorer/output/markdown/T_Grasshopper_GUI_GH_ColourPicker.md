# T_Grasshopper_GUI_GH_ColourPicker

﻿ GH\_ColourPicker Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_ColourPicker Class](../html/T_Grasshopper_GUI_GH_ColourPicker.htm "GH_ColourPicker Class")

[GH\_ColourPicker Constructor](../html/M_Grasshopper_GUI_GH_ColourPicker__ctor.htm "GH_ColourPicker Constructor ")

[GH\_ColourPicker Properties](../html/Properties_T_Grasshopper_GUI_GH_ColourPicker.htm "GH_ColourPicker Properties")

[GH\_ColourPicker Methods](../html/Methods_T_Grasshopper_GUI_GH_ColourPicker.htm "GH_ColourPicker Methods")

[GH\_ColourPicker Events](../html/Events_T_Grasshopper_GUI_GH_ColourPicker.htm "GH_ColourPicker Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ColourPicker Class |

Provides the standard Grasshopper Colour picker as a winforms Control.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTD719B047\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTD719B047\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
    [System.ComponentModelAddLanguageSpecificTextSet("LSTD719B047\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Component](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
      [System.Windows.FormsAddLanguageSpecificTextSet("LSTD719B047\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
        [System.Windows.FormsAddLanguageSpecificTextSet("LSTD719B047\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
          [System.Windows.FormsAddLanguageSpecificTextSet("LSTD719B047\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
            [System.Windows.FormsAddLanguageSpecificTextSet("LSTD719B047\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");UserControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.usercontrol)  
              Grasshopper.GUIAddLanguageSpecificTextSet("LSTD719B047\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ColourPicker

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ColourPicker : UserControl
```

```
Public Class GH_ColourPicker
	Inherits UserControl
```

AddLanguageTabSet("ID1EBCA");

The GH\_ColourPicker type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ColourPicker](M_Grasshopper_GUI_GH_ColourPicker__ctor.htm) | Initializes a new instance of the GH\_ColourPicker class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AllowNumericInput](P_Grasshopper_GUI_GH_ColourPicker_AllowNumericInput.htm) | Gets or sets whether this colour picker pops up a textbox on channel slider double clicks. |
| Public property | [Colour](P_Grasshopper_GUI_GH_ColourPicker_Colour.htm) | Gets or sets the colour currently specified in the picker. |
| Public property | [DesiredHeight](P_Grasshopper_GUI_GH_ColourPicker_DesiredHeight.htm) | Gets the ideal height for this control given the current width and UI settings. |
| Public property | [ShowAlphaSlider](P_Grasshopper_GUI_GH_ColourPicker_ShowAlphaSlider.htm) | Gets or sets whether the alpha channel slider is included. |
| Public property | [ShowChannelSliders](P_Grasshopper_GUI_GH_ColourPicker_ShowChannelSliders.htm) | Gets or sets whether the channel sliders are included. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Dispose](M_Grasshopper_GUI_GH_ColourPicker_Dispose.htm) | Releases the unmanaged resources used by the GH\_ColourPicker and optionally releases the managed resources (Overrides [ContainerControlAddLanguageSpecificTextSet("LSTD719B047\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Dispose(Boolean)](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol.dispose#system-windows-forms-containercontrol-dispose(system-boolean)).) |
| Protected method | [OnPaint](M_Grasshopper_GUI_GH_ColourPicker_OnPaint.htm) | (Overrides [ControlAddLanguageSpecificTextSet("LSTD719B047\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-windows-forms-control-onpaint(system-windows-forms-painteventargs)).) |
| Protected method | [OnPaintBackground](M_Grasshopper_GUI_GH_ColourPicker_OnPaintBackground.htm) | (Overrides [ScrollableControlAddLanguageSpecificTextSet("LSTD719B047\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-windows-forms-scrollablecontrol-onpaintbackground(system-windows-forms-painteventargs)).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [ColourChanged](E_Grasshopper_GUI_GH_ColourPicker_ColourChanged.htm) | Raised whenever the value of the slider is changed via GUI interaction. |

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