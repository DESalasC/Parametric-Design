# M_Grasshopper_Kernel_IGH_RenderAwareData_AppendRenderGeometry

﻿ IGH\_RenderAwareData.AppendRenderGeometry Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_RenderAwareData Interface](../html/T_Grasshopper_Kernel_IGH_RenderAwareData.htm "IGH_RenderAwareData Interface")

[IGH\_RenderAwareData Methods](../html/Methods_T_Grasshopper_Kernel_IGH_RenderAwareData.htm "IGH_RenderAwareData Methods")

[AppendRenderGeometry Method](../html/M_Grasshopper_Kernel_IGH_RenderAwareData_AppendRenderGeometry.htm "AppendRenderGeometry Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_RenderAwareDataAddLanguageSpecificTextSet("LST9EE56E29\_0?cpp=::|nu=.");AppendRenderGeometry Method |

Push this geometry down a render pipeline.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void AppendRenderGeometry(
	GH_RenderArgs args,
	RenderMaterial material
)
```

```
Sub AppendRenderGeometry ( 
	args As GH_RenderArgs,
	material As RenderMaterial
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

args
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST9EE56E29\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RenderArgs](T_Grasshopper_Kernel_GH_RenderArgs.htm)  
    Render pipeline details.

material
:   Type: RenderMaterial  
    Material to use if you can't think of one yourself.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_RenderAwareData Interface](T_Grasshopper_Kernel_IGH_RenderAwareData.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)