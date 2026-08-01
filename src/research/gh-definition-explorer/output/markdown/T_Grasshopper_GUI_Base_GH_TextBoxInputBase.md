# T_Grasshopper_GUI_Base_GH_TextBoxInputBase

﻿ GH\_TextBoxInputBase Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_TextBoxInputBase Class](../html/T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm "GH_TextBoxInputBase Class")

[GH\_TextBoxInputBase Constructor](../html/M_Grasshopper_GUI_Base_GH_TextBoxInputBase__ctor.htm "GH_TextBoxInputBase Constructor ")

[GH\_TextBoxInputBase Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm "GH_TextBoxInputBase Properties")

[GH\_TextBoxInputBase Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_TextBoxInputBase.htm "GH_TextBoxInputBase Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TextBoxInputBase Class |

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTB8B380AE\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.BaseAddLanguageSpecificTextSet("LSTB8B380AE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_TextBoxInputBase  
    [Grasshopper.GUI.BaseAddLanguageSpecificTextSet("LSTB8B380AE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DigitScrollerBase](T_Grasshopper_GUI_Base_GH_DigitScrollerBase.htm)  
    [Grasshopper.GUI.BaseAddLanguageSpecificTextSet("LSTB8B380AE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SliderBase](T_Grasshopper_GUI_Base_GH_SliderBase.htm)

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_TextBoxInputBase
```

```
Public MustInherit Class GH_TextBoxInputBase
```

AddLanguageTabSet("ID1EBCA");

The GH\_TextBoxInputBase type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_TextBoxInputBase](M_Grasshopper_GUI_Base_GH_TextBoxInputBase__ctor.htm) | Initializes a new instance of the GH\_TextBoxInputBase class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Font](P_Grasshopper_GUI_Base_GH_TextBoxInputBase_Font.htm) | Gets or sets the Font to use in this control. |
| Public property | [IsTextInput](P_Grasshopper_GUI_Base_GH_TextBoxInputBase_IsTextInput.htm) | Gets whether the text input box is currently on screen. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [HandleTextInputAccepted](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_HandleTextInputAccepted.htm) |  |
| Public method | [HideTextInputBox](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_HideTextInputBox.htm) | Hides the text-input override form (if it is displayed). |
| Public method | [RespondToEnter](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_RespondToEnter.htm) |  |
| Public method | [RespondToEscape](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_RespondToEscape.htm) |  |
| Public method | [ShowTextInputBox(Control, String, Boolean)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_ShowTextInputBox.htm) | Display a floating text-box on top of the owner control. |
| Public method | [ShowTextInputBox(Control, String, Boolean, Boolean)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_ShowTextInputBox_1.htm) | Display a floating text-box on top of the owner control. |
| Public method | [ShowTextInputBox(Control, String, Boolean, Boolean, Matrix)](M_Grasshopper_GUI_Base_GH_TextBoxInputBase_ShowTextInputBox_2.htm) | Display a floating text-box on top of the owner control. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)