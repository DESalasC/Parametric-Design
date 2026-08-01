# T_Grasshopper_Kernel_GH_BakeUtility

﻿ GH\_BakeUtility Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_BakeUtility Class](../html/T_Grasshopper_Kernel_GH_BakeUtility.htm "GH_BakeUtility Class")

[GH\_BakeUtility Constructor](../html/M_Grasshopper_Kernel_GH_BakeUtility__ctor.htm "GH_BakeUtility Constructor ")

[GH\_BakeUtility Properties](../html/Properties_T_Grasshopper_Kernel_GH_BakeUtility.htm "GH_BakeUtility Properties")

[GH\_BakeUtility Methods](../html/Methods_T_Grasshopper_Kernel_GH_BakeUtility.htm "GH_BakeUtility Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_BakeUtility Class |

A utility class for baking. We heavily recommend you use this for any baking,
as it handles invalid objects correctly.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST6D5ECD7E\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST6D5ECD7E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_BakeUtility

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_BakeUtility
```

```
Public Class GH_BakeUtility
```

AddLanguageTabSet("ID1EBCA");

The GH\_BakeUtility type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_BakeUtility](M_Grasshopper_Kernel_GH_BakeUtility__ctor.htm) | Create a new baker. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BakedCount](P_Grasshopper_Kernel_GH_BakeUtility_BakedCount.htm) | Gets the number of successful baking operations. |
| Public property | [BakedIds](P_Grasshopper_Kernel_GH_BakeUtility_BakedIds.htm) | Gets all collected object ids. |
| Public property | [InvalidCount](P_Grasshopper_Kernel_GH_BakeUtility_InvalidCount.htm) | Gets the number of invalid objects encountered. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeObject](M_Grasshopper_Kernel_GH_BakeUtility_BakeObject.htm) | Try and bake a single object. |
| Public method | [BakeObjects](M_Grasshopper_Kernel_GH_BakeUtility_BakeObjects.htm) | Bake a bunch of objects. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)