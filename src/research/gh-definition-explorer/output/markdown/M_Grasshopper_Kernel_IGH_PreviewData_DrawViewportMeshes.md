# M_Grasshopper_Kernel_IGH_PreviewData_DrawViewportMeshes

﻿ IGH\_PreviewData.DrawViewportMeshes Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_PreviewData Interface](../html/T_Grasshopper_Kernel_IGH_PreviewData.htm "IGH_PreviewData Interface")

[IGH\_PreviewData Methods](../html/Methods_T_Grasshopper_Kernel_IGH_PreviewData.htm "IGH_PreviewData Methods")

[DrawViewportMeshes Method](../html/M_Grasshopper_Kernel_IGH_PreviewData_DrawViewportMeshes.htm "DrawViewportMeshes Method ")

[DrawViewportWires Method](../html/M_Grasshopper_Kernel_IGH_PreviewData_DrawViewportWires.htm "DrawViewportWires Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_PreviewDataAddLanguageSpecificTextSet("LSTEC95EC4A\_0?cpp=::|nu=.");DrawViewportMeshes Method |

Implement this function to draw all shaded meshes.
If the viewport does not support shading, this function will not be called.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void DrawViewportMeshes(
	GH_PreviewMeshArgs args
)
```

```
Sub DrawViewportMeshes ( 
	args As GH_PreviewMeshArgs
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

args
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTEC95EC4A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PreviewMeshArgs](T_Grasshopper_Kernel_GH_PreviewMeshArgs.htm)  
    Drawing arguments.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_PreviewData Interface](T_Grasshopper_Kernel_IGH_PreviewData.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)