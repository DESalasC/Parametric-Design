# T_Grasshopper_GUI_GH_SamplingSphere

﻿ GH\_SamplingSphere Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_SamplingSphere Class](../html/T_Grasshopper_GUI_GH_SamplingSphere.htm "GH_SamplingSphere Class")

[GH\_SamplingSphere Constructor](../html/M_Grasshopper_GUI_GH_SamplingSphere__ctor.htm "GH_SamplingSphere Constructor ")

[GH\_SamplingSphere Properties](../html/Properties_T_Grasshopper_GUI_GH_SamplingSphere.htm "GH_SamplingSphere Properties")

[GH\_SamplingSphere Methods](../html/Methods_T_Grasshopper_GUI_GH_SamplingSphere.htm "GH_SamplingSphere Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SamplingSphere Class |

Represents a coloured sphere that can be sampled at various rotations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST249EBC42\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST249EBC42\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SamplingSphere

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_SamplingSphere
```

```
Public Class GH_SamplingSphere
```

AddLanguageTabSet("ID1EBCA");

The GH\_SamplingSphere type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_SamplingSphere](M_Grasshopper_GUI_GH_SamplingSphere__ctor.htm) | Initializes a new instance of the GH\_SamplingSphere class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [SampleCount](P_Grasshopper_GUI_GH_SamplingSphere_SampleCount.htm) | Gets the total number of samples contained in this sampling grid. |
| Public property | [Size](P_Grasshopper_GUI_GH_SamplingSphere_Size.htm) | Gets the size of this sample grid. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [SampleSphere(Sphere)](M_Grasshopper_GUI_GH_SamplingSphere_SampleSphere.htm) | Sample the UV locations of a sphere. The sphere should be centered on the world origin. |
| Public method | [SampleSphere(Sphere, GH\_MemoryBitmap)](M_Grasshopper_GUI_GH_SamplingSphere_SampleSphere_1.htm) | Sample a sphere with a UV texture and return a bitmap of sampled values. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)