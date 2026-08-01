# T_Grasshopper_Kernel_IGH_PreviewArgs

﻿ IGH\_PreviewArgs Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_PreviewArgs Interface](../html/T_Grasshopper_Kernel_IGH_PreviewArgs.htm "IGH_PreviewArgs Interface")

[IGH\_PreviewArgs Properties](../html/Properties_T_Grasshopper_Kernel_IGH_PreviewArgs.htm "IGH_PreviewArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_PreviewArgs Interface |

Preview display arguments for IGH\_PreviewObjects.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_PreviewArgs
```

```
Public Interface IGH_PreviewArgs
```

AddLanguageTabSet("ID0EBCA");

The IGH\_PreviewArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [DefaultCurveThickness](P_Grasshopper_Kernel_IGH_PreviewArgs_DefaultCurveThickness.htm) | Gets the curve thickness as defined by the viewport display scheme. |
| Public property | [Display](P_Grasshopper_Kernel_IGH_PreviewArgs_Display.htm) | Gets the Pipeline that is being used to draw the current preview. |
| Public property | [Document](P_Grasshopper_Kernel_IGH_PreviewArgs_Document.htm) | Gets the Grasshopper document that is currently drawing the preview. |
| Public property | [MeshingParameters](P_Grasshopper_Kernel_IGH_PreviewArgs_MeshingParameters.htm) | Gets the meshing parameters to be used during meshing breps. |
| Public property | [ShadeMaterial](P_Grasshopper_Kernel_IGH_PreviewArgs_ShadeMaterial.htm) | Gets the document default material for unselected Faces. |
| Public property | [ShadeMaterial\_Selected](P_Grasshopper_Kernel_IGH_PreviewArgs_ShadeMaterial_Selected.htm) | Gets the document default material for selected Faces. |
| Public property | [Viewport](P_Grasshopper_Kernel_IGH_PreviewArgs_Viewport.htm) | Gets the Viewport in which the current preview is drawn. |
| Public property | [WireColour](P_Grasshopper_Kernel_IGH_PreviewArgs_WireColour.htm) | Gets the document default colour for unselected Wires. |
| Public property | [WireColour\_Selected](P_Grasshopper_Kernel_IGH_PreviewArgs_WireColour_Selected.htm) | Gets the document default colour for selected Wires. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)