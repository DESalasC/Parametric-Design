# T_Grasshopper_GUI_Base_GH_SliderEventArgs

﻿ GH\_SliderEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_SliderEventArgs Class](../html/T_Grasshopper_GUI_Base_GH_SliderEventArgs.htm "GH_SliderEventArgs Class")

[GH\_SliderEventArgs Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_SliderEventArgs.htm "GH_SliderEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SliderEventArgs Class |

Arguments passed via GH\_SliderBase.ValueChanged events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTEA76896D\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTEA76896D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.GUI.BaseAddLanguageSpecificTextSet("LSTEA76896D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SliderEventArgs

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_SliderEventArgs : EventArgs
```

```
Public Class GH_SliderEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_SliderEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Intermediate](P_Grasshopper_GUI_Base_GH_SliderEventArgs_Intermediate.htm) | Gets a value indicating whether the change was an intermediate one. |
| Public property | [Slider](P_Grasshopper_GUI_Base_GH_SliderEventArgs_Slider.htm) | Gets the instance of the slider that raised the event. |
| Public property | [Value](P_Grasshopper_GUI_Base_GH_SliderEventArgs_Value.htm) | Gets the new value of the slider. This value is cached, so even if the slider subsequently updates, this property remains constant. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)