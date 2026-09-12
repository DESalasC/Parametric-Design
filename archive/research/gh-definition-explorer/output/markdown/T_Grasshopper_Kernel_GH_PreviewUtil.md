# T_Grasshopper_Kernel_GH_PreviewUtil

﻿ GH\_PreviewUtil Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_PreviewUtil Class](../html/T_Grasshopper_Kernel_GH_PreviewUtil.htm "GH_PreviewUtil Class")

[GH\_PreviewUtil Constructor](../html/Overload_Grasshopper_Kernel_GH_PreviewUtil__ctor.htm "GH_PreviewUtil Constructor ")

[GH\_PreviewUtil Properties](../html/Properties_T_Grasshopper_Kernel_GH_PreviewUtil.htm "GH_PreviewUtil Properties")

[GH\_PreviewUtil Methods](../html/Methods_T_Grasshopper_Kernel_GH_PreviewUtil.htm "GH_PreviewUtil Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PreviewUtil Class |

This class exposes functionality that makes it easy to draw temporary geometry in Rhino viewports.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTCAFDCA1E\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTCAFDCA1E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PreviewUtil

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_PreviewUtil : IDisposable
```

```
Public NotInheritable Class GH_PreviewUtil
	Implements IDisposable
```

AddLanguageTabSet("ID1EBCA");

The GH\_PreviewUtil type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PreviewUtilAddLanguageSpecificTextSet("LSTCAFDCA1E\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_PreviewUtil__ctor.htm) | Initializes a new instance of the GH\_PreviewUtil class |
| Public method | [GH\_PreviewUtil(Boolean)](M_Grasshopper_Kernel_GH_PreviewUtil__ctor_1.htm) | Initializes a new instance of the GH\_PreviewUtil class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Enabled](P_Grasshopper_Kernel_GH_PreviewUtil_Enabled.htm) | Gets or sets the enabled state of this Preview util. |
| Public property | [WireColour](P_Grasshopper_Kernel_GH_PreviewUtil_WireColour.htm) | Gets or sets the colour to use for Preview geometry. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddBox](M_Grasshopper_Kernel_GH_PreviewUtil_AddBox.htm) | Add a box to the temporary Preview lists. |
| Public method | [AddBrep](M_Grasshopper_Kernel_GH_PreviewUtil_AddBrep.htm) | Add a brep to the temporary Preview lists. |
| Public method | [AddCurve](M_Grasshopper_Kernel_GH_PreviewUtil_AddCurve.htm) | Add a curve to the temporary Preview lists. |
| Public method | [AddLine](M_Grasshopper_Kernel_GH_PreviewUtil_AddLine.htm) | Add a line to the temporary Preview lists. |
| Public method | [AddMesh](M_Grasshopper_Kernel_GH_PreviewUtil_AddMesh.htm) | Add a mesh to the temporary Preview lists. |
| Public method | [AddPlane](M_Grasshopper_Kernel_GH_PreviewUtil_AddPlane.htm) | Add a plane to the temporary Preview lists. |
| Public method | [AddPoint](M_Grasshopper_Kernel_GH_PreviewUtil_AddPoint.htm) | Add a point to the temporary Preview lists. |
| Public method | [AddVector](M_Grasshopper_Kernel_GH_PreviewUtil_AddVector.htm) | Add a vector to the temporary Preview lists. |
| Public method | [Clear](M_Grasshopper_Kernel_GH_PreviewUtil_Clear.htm) | Clear all temporary geometry. |
| Public method | [Dispose](M_Grasshopper_Kernel_GH_PreviewUtil_Dispose.htm) | Releases all resources used by the GH\_PreviewUtil |
| Public method | [Redraw](M_Grasshopper_Kernel_GH_PreviewUtil_Redraw.htm) | Forces a redraw the the viewports. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)