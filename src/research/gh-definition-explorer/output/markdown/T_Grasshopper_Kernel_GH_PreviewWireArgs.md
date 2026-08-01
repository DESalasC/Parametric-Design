# T_Grasshopper_Kernel_GH_PreviewWireArgs

﻿ GH\_PreviewWireArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_PreviewWireArgs Class](../html/T_Grasshopper_Kernel_GH_PreviewWireArgs.htm "GH_PreviewWireArgs Class")

[GH\_PreviewWireArgs Constructor](../html/M_Grasshopper_Kernel_GH_PreviewWireArgs__ctor.htm "GH_PreviewWireArgs Constructor ")

[GH\_PreviewWireArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_PreviewWireArgs.htm "GH_PreviewWireArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PreviewWireArgs Class |

This class is passed to objects that implement IGH\_PreviewData during wire drawing operations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST6B61C57B\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST6B61C57B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PreviewWireArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_PreviewWireArgs
```

```
Public Class GH_PreviewWireArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_PreviewWireArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PreviewWireArgs](M_Grasshopper_Kernel_GH_PreviewWireArgs__ctor.htm) | Initializes a new instance of the GH\_PreviewWireArgs class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Color](P_Grasshopper_Kernel_GH_PreviewWireArgs_Color.htm) | Gets the color in which wires ought to be drawn. |
| Public property | [Pipeline](P_Grasshopper_Kernel_GH_PreviewWireArgs_Pipeline.htm) | Gets the Display Pipeline we're currently drawing with. |
| Public property | [Thickness](P_Grasshopper_Kernel_GH_PreviewWireArgs_Thickness.htm) | Gets the thickness in which wires ought to be drawn. |
| Public property | [Viewport](P_Grasshopper_Kernel_GH_PreviewWireArgs_Viewport.htm) | Gets the Viewport in which we're currently drawing. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)