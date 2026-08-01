# T_Grasshopper_GUI_Base_GH_ColourPickerEventArgs

﻿ GH\_ColourPickerEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_ColourPickerEventArgs Class](../html/T_Grasshopper_GUI_Base_GH_ColourPickerEventArgs.htm "GH_ColourPickerEventArgs Class")

[GH\_ColourPickerEventArgs Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_ColourPickerEventArgs.htm "GH_ColourPickerEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ColourPickerEventArgs Class |

Arguments passed via GH\_SliderBase.ValueChanged events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTCB0423D2\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTCB0423D2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.GUI.BaseAddLanguageSpecificTextSet("LSTCB0423D2\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ColourPickerEventArgs

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ColourPickerEventArgs : EventArgs
```

```
Public Class GH_ColourPickerEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_ColourPickerEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Colour](P_Grasshopper_GUI_Base_GH_ColourPickerEventArgs_Colour.htm) | Gets the new value of the colour picker. This value is cached, so even if the picker subsequently updates, this property remains constant. |
| Public property | [ColourPicker](P_Grasshopper_GUI_Base_GH_ColourPickerEventArgs_ColourPicker.htm) | Gets the instance of the picker that raised the event. |
| Public property | [Intermediate](P_Grasshopper_GUI_Base_GH_ColourPickerEventArgs_Intermediate.htm) | Gets a value indicating whether the change was an intermediate one. |
| Public property | [Original](P_Grasshopper_GUI_Base_GH_ColourPickerEventArgs_Original.htm) | Gets the original value of the colour picker. This value is cached, so even if the picker subsequently updates, this property remains constant. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)