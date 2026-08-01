# T_Grasshopper_Kernel_GH_PreviewMeshArgs

﻿ GH\_PreviewMeshArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_PreviewMeshArgs Class](../html/T_Grasshopper_Kernel_GH_PreviewMeshArgs.htm "GH_PreviewMeshArgs Class")

[GH\_PreviewMeshArgs Constructor](../html/M_Grasshopper_Kernel_GH_PreviewMeshArgs__ctor.htm "GH_PreviewMeshArgs Constructor ")

[GH\_PreviewMeshArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_PreviewMeshArgs.htm "GH_PreviewMeshArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PreviewMeshArgs Class |

This class is passed to objects that implement IGH\_PreviewData during mesh drawing operations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST1B0E2D50\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST1B0E2D50\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PreviewMeshArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_PreviewMeshArgs
```

```
Public Class GH_PreviewMeshArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_PreviewMeshArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PreviewMeshArgs](M_Grasshopper_Kernel_GH_PreviewMeshArgs__ctor.htm) | Initializes a new instance of the GH\_PreviewMeshArgs class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Material](P_Grasshopper_Kernel_GH_PreviewMeshArgs_Material.htm) | Gets the material in which meshes ought to be drawn. |
| Public property | [MeshingParameters](P_Grasshopper_Kernel_GH_PreviewMeshArgs_MeshingParameters.htm) | Gets the meshing parameters which ought to be used for meshing breps and surfaces. If this property returns a null reference, meshes are supposed to be omitted. |
| Public property | [Pipeline](P_Grasshopper_Kernel_GH_PreviewMeshArgs_Pipeline.htm) | Gets the Display Pipeline we're currently drawing with. |
| Public property | [Viewport](P_Grasshopper_Kernel_GH_PreviewMeshArgs_Viewport.htm) | Gets the Viewport in which we're currently drawing. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)