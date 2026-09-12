# T_Grasshopper_Kernel_IGH_PreviewData

﻿ IGH\_PreviewData Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_PreviewData Interface](../html/T_Grasshopper_Kernel_IGH_PreviewData.htm "IGH_PreviewData Interface")

[IGH\_PreviewData Properties](../html/Properties_T_Grasshopper_Kernel_IGH_PreviewData.htm "IGH_PreviewData Properties")

[IGH\_PreviewData Methods](../html/Methods_T_Grasshopper_Kernel_IGH_PreviewData.htm "IGH_PreviewData Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_PreviewData Interface |

All IGH\_Goo types that wish to participate in Viewport redraws must implement this interface.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_PreviewData
```

```
Public Interface IGH_PreviewData
```

AddLanguageTabSet("ID0EBCA");

The IGH\_PreviewData type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ClippingBox](P_Grasshopper_Kernel_IGH_PreviewData_ClippingBox.htm) | Gets the clipping box for this data. The clipping box is typically the same as the boundingbox. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_IGH_PreviewData_DrawViewportMeshes.htm) | Implement this function to draw all shaded meshes. If the viewport does not support shading, this function will not be called. |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_IGH_PreviewData_DrawViewportWires.htm) | Implement this function to draw all wire and point previews. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)