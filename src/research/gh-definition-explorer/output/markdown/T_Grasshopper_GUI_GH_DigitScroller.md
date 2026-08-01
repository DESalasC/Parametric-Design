# T_Grasshopper_GUI_GH_DigitScroller

﻿ GH\_DigitScroller Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_DigitScroller Class](../html/T_Grasshopper_GUI_GH_DigitScroller.htm "GH_DigitScroller Class")

[GH\_DigitScroller Constructor](../html/M_Grasshopper_GUI_GH_DigitScroller__ctor.htm "GH_DigitScroller Constructor ")

[GH\_DigitScroller Properties](../html/Properties_T_Grasshopper_GUI_GH_DigitScroller.htm "GH_DigitScroller Properties")

[GH\_DigitScroller Methods](../html/Methods_T_Grasshopper_GUI_GH_DigitScroller.htm "GH_DigitScroller Methods")

[GH\_DigitScroller Events](../html/Events_T_Grasshopper_GUI_GH_DigitScroller.htm "GH_DigitScroller Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DigitScroller Class |

Provides the standard Grasshopper Digit scroller as a winforms Control.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST33431333\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST33431333\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
    [System.ComponentModelAddLanguageSpecificTextSet("LST33431333\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Component](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
      [System.Windows.FormsAddLanguageSpecificTextSet("LST33431333\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
        [System.Windows.FormsAddLanguageSpecificTextSet("LST33431333\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
          [System.Windows.FormsAddLanguageSpecificTextSet("LST33431333\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
            [System.Windows.FormsAddLanguageSpecificTextSet("LST33431333\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");UserControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.usercontrol)  
              GH\_TextInputBaseControl  
                Grasshopper.GUIAddLanguageSpecificTextSet("LST33431333\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DigitScroller

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DigitScroller : GH_TextInputBaseControl
```

```
Public Class GH_DigitScroller
	Inherits GH_TextInputBaseControl
```

AddLanguageTabSet("ID1EBCA");

The GH\_DigitScroller type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DigitScroller](M_Grasshopper_GUI_GH_DigitScroller__ctor.htm) | Initializes a new instance of the GH\_DigitScroller class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AllowRadixDrag](P_Grasshopper_GUI_GH_DigitScroller_AllowRadixDrag.htm) | Gets or sets whether the radix symbol can be dragged. |
| Public property | [AllowTextInput](P_Grasshopper_GUI_GH_DigitScroller_AllowTextInput.htm) | Gets or sets whether the control accepts text input override. |
| Public property | [Amplify](P_Grasshopper_GUI_GH_DigitScroller_Amplify.htm) | Gets or sets whether vertical mouse movement ought to be amplified. |
| Public property | [DecimalPlaces](P_Grasshopper_GUI_GH_DigitScroller_DecimalPlaces.htm) | Gets or sets the number of decimal places. |
| Public property | [DigitAlign](P_Grasshopper_GUI_GH_DigitScroller_DigitAlign.htm) | Gets or sets the digit align mode |
| Public property | [Digits](P_Grasshopper_GUI_GH_DigitScroller_Digits.htm) | Gets or sets the number of digits displayed in the scroller. |
| Public property | [DigitScroller](P_Grasshopper_GUI_GH_DigitScroller_DigitScroller.htm) | Gets the internal scroller object. |
| Public property | [Epsilon](P_Grasshopper_GUI_GH_DigitScroller_Epsilon.htm) | Gets the smallest possible change with the current settings. |
| Public property | [MaximumValue](P_Grasshopper_GUI_GH_DigitScroller_MaximumValue.htm) | Gets or sets the upper bound of the scroll value. |
| Public property | [MinimumValue](P_Grasshopper_GUI_GH_DigitScroller_MinimumValue.htm) | Gets or sets the lower bound of the scroll value. |
| Public property | [Prefix](P_Grasshopper_GUI_GH_DigitScroller_Prefix.htm) | Gets or sets the prefix text |
| Public property | [Radix](P_Grasshopper_GUI_GH_DigitScroller_Radix.htm) | Gets or sets the radix point index. |
| Public property | [Suffix](P_Grasshopper_GUI_GH_DigitScroller_Suffix.htm) | Gets or sets the prefix text |
| Public property | [Value](P_Grasshopper_GUI_GH_DigitScroller_Value.htm) | Gets or sets the value of this scroller. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Input\_Assign](M_Grasshopper_GUI_GH_DigitScroller_Input_Assign.htm) | (Overrides GH\_TextInputBaseControl.Input\_Assign(String).) |
| Protected method | [Input\_Parse](M_Grasshopper_GUI_GH_DigitScroller_Input_Parse.htm) | (Overrides GH\_TextInputBaseControl.Input\_Parse(String).) |
| Protected method | [Input\_Supply](M_Grasshopper_GUI_GH_DigitScroller_Input_Supply.htm) | (Overrides GH\_TextInputBaseControl.Input\_SupplyAddLanguageSpecificTextSet("LST33431333\_8?cs=()|vb=|cpp=()|nu=()|fs=()");.) |
| Protected method | [OnPaint](M_Grasshopper_GUI_GH_DigitScroller_OnPaint.htm) | (Overrides [ControlAddLanguageSpecificTextSet("LST33431333\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-windows-forms-control-onpaint(system-windows-forms-painteventargs)).) |
| Protected method | [OnPaintBackground](M_Grasshopper_GUI_GH_DigitScroller_OnPaintBackground.htm) | (Overrides [ScrollableControlAddLanguageSpecificTextSet("LST33431333\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol.onpaintbackground#system-windows-forms-scrollablecontrol-onpaintbackground(system-windows-forms-painteventargs)).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [ValueChanged](E_Grasshopper_GUI_GH_DigitScroller_ValueChanged.htm) |  |

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