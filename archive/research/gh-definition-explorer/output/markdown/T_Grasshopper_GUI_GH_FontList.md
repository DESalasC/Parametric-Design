# T_Grasshopper_GUI_GH_FontList

﻿ GH\_FontList Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_FontList Class](../html/T_Grasshopper_GUI_GH_FontList.htm "GH_FontList Class")

[GH\_FontList Constructor](../html/M_Grasshopper_GUI_GH_FontList__ctor.htm "GH_FontList Constructor ")

[GH\_FontList Properties](../html/Properties_T_Grasshopper_GUI_GH_FontList.htm "GH_FontList Properties")

[GH\_FontList Methods](../html/Methods_T_Grasshopper_GUI_GH_FontList.htm "GH_FontList Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FontList Class |

Represents the installed Font collection. This control allows
both navigation and selection of Font Families.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTF80CBF51\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTF80CBF51\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
    [System.ComponentModelAddLanguageSpecificTextSet("LSTF80CBF51\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Component](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
      [System.Windows.FormsAddLanguageSpecificTextSet("LSTF80CBF51\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
        [System.Windows.FormsAddLanguageSpecificTextSet("LSTF80CBF51\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
          [System.Windows.FormsAddLanguageSpecificTextSet("LSTF80CBF51\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Panel](https://docs.microsoft.com/dotnet/api/system.windows.forms.panel)  
            [Grasshopper.GUIAddLanguageSpecificTextSet("LSTF80CBF51\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DoubleBufferedPanel](T_Grasshopper_GUI_GH_DoubleBufferedPanel.htm)  
              Grasshopper.GUIAddLanguageSpecificTextSet("LSTF80CBF51\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FontList

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_FontList : GH_DoubleBufferedPanel
```

```
Public Class GH_FontList
	Inherits GH_DoubleBufferedPanel
```

AddLanguageTabSet("ID1EBCA");

The GH\_FontList type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_FontList](M_Grasshopper_GUI_GH_FontList__ctor.htm) | Initializes a new instance of the GH\_FontList class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [DisplayText](P_Grasshopper_GUI_GH_FontList_DisplayText.htm) | Gets or sets the placeholder string. |
| Public property | [Filter](P_Grasshopper_GUI_GH_FontList_Filter.htm) | Gets or sets the filter string. You must call RecreateFontList() before the new font list is created. |
| Public property | [FontFamily](P_Grasshopper_GUI_GH_FontList_FontFamily.htm) | Gets or sets the selected font family. |
| Public property | [FontSize](P_Grasshopper_GUI_GH_FontList_FontSize.htm) | Gets or sets the font size. |
| Public property | [FontStyle](P_Grasshopper_GUI_GH_FontList_FontStyle.htm) | Gets or sets the font style for all families. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CreateFont](M_Grasshopper_GUI_GH_FontList_CreateFont.htm) | Create a font that best approximates the current settings. |
| Protected method | [OnPaint](M_Grasshopper_GUI_GH_FontList_OnPaint.htm) | (Overrides [ControlAddLanguageSpecificTextSet("LSTF80CBF51\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-windows-forms-control-onpaint(system-windows-forms-painteventargs)).) |
| Protected method | [OnPaintBackground](M_Grasshopper_GUI_GH_FontList_OnPaintBackground.htm) | (Overrides [ScrollableControlAddLanguageSpecificTextSet("LSTF80CBF51\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-windows-forms-scrollablecontrol-onpaintbackground(system-windows-forms-painteventargs)).) |
| Public method | [RecreateFontList](M_Grasshopper_GUI_GH_FontList_RecreateFontList.htm) |  |

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