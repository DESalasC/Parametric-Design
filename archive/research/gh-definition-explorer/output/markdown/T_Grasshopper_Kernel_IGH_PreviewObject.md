# T_Grasshopper_Kernel_IGH_PreviewObject

﻿ IGH\_PreviewObject Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_PreviewObject Interface](../html/T_Grasshopper_Kernel_IGH_PreviewObject.htm "IGH_PreviewObject Interface")

[IGH\_PreviewObject Properties](../html/Properties_T_Grasshopper_Kernel_IGH_PreviewObject.htm "IGH_PreviewObject Properties")

[IGH\_PreviewObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_PreviewObject.htm "IGH_PreviewObject Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_PreviewObject Interface |

All IGH\_DocumentObjects that wish to participate in Viewport redraws must implement this interface.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_PreviewObject
```

```
Public Interface IGH_PreviewObject
```

AddLanguageTabSet("ID0EBCA");

The IGH\_PreviewObject type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ClippingBox](P_Grasshopper_Kernel_IGH_PreviewObject_ClippingBox.htm) | Gets the clipping box for this object. The clipping box is typically the union of the boundingboxes of all the geometry that is drawn by this object. |
| Public property | [Hidden](P_Grasshopper_Kernel_IGH_PreviewObject_Hidden.htm) | Gets or sets a value indicating whether or not this object is currently drawing preview flags. |
| Public property | [IsPreviewCapable](P_Grasshopper_Kernel_IGH_PreviewObject_IsPreviewCapable.htm) | Gets a value indicating whether or not this object (in its current state) can draw geometric previews at all. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_IGH_PreviewObject_DrawViewportMeshes.htm) | Implement this function to draw all shaded meshes. If the viewport does not support shading, this function will not be called. |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_IGH_PreviewObject_DrawViewportWires.htm) | Implement this function to draw all wire and point geometry previews. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)