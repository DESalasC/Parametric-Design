# T_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs

﻿ GH\_GradientChangedEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Gradient](../html/N_Grasshopper_GUI_Gradient.htm "Grasshopper.GUI.Gradient")

[GH\_GradientChangedEventArgs Class](../html/T_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs.htm "GH_GradientChangedEventArgs Class")

[GH\_GradientChangedEventArgs Constructor](../html/M_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs__ctor.htm "GH_GradientChangedEventArgs Constructor ")

[GH\_GradientChangedEventArgs Properties](../html/Properties_T_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs.htm "GH_GradientChangedEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GradientChangedEventArgs Class |

Arguments for te GradientChanged event.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST958370D\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST958370D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.GUI.GradientAddLanguageSpecificTextSet("LST958370D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GradientChangedEventArgs

**Namespace:**
 [Grasshopper.GUI.Gradient](N_Grasshopper_GUI_Gradient.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_GradientChangedEventArgs : EventArgs
```

```
Public Class GH_GradientChangedEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_GradientChangedEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_GradientChangedEventArgs](M_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs__ctor.htm) | Initializes a new instance of the GH\_GradientChangedEventArgs class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Gradient](P_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs_Gradient.htm) | Gets the gradient that raised this event. |
| Public property | [Intermediate](P_Grasshopper_GUI_Gradient_GH_GradientChangedEventArgs_Intermediate.htm) | Gets whether this event is intermediate. I.e. whether it will be followed by another, similar event. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Gradient Namespace](N_Grasshopper_GUI_Gradient.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)