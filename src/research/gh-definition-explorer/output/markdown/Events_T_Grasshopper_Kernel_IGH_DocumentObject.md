# Events_T_Grasshopper_Kernel_IGH_DocumentObject

﻿ IGH\_DocumentObject Events

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DocumentObject Interface](../html/T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Interface")

[IGH\_DocumentObject Events](../html/Events_T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Events")

[AttributesChanged Event](../html/E_Grasshopper_Kernel_IGH_DocumentObject_AttributesChanged.htm "AttributesChanged Event")

[DisplayExpired Event](../html/E_Grasshopper_Kernel_IGH_DocumentObject_DisplayExpired.htm "DisplayExpired Event")

[ObjectChanged Event](../html/E_Grasshopper_Kernel_IGH_DocumentObject_ObjectChanged.htm "ObjectChanged Event")

[PingDocument Event](../html/E_Grasshopper_Kernel_IGH_DocumentObject_PingDocument.htm "PingDocument Event")

[PreviewExpired Event](../html/E_Grasshopper_Kernel_IGH_DocumentObject_PreviewExpired.htm "PreviewExpired Event")

[SolutionExpired Event](../html/E_Grasshopper_Kernel_IGH_DocumentObject_SolutionExpired.htm "SolutionExpired Event")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DocumentObject Events |

The [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [AttributesChanged](E_Grasshopper_Kernel_IGH_DocumentObject_AttributesChanged.htm) | Raised whenever the number or kind of attributes changes. This event is handled by GH\_Documents who subsequently wipe their attribute caches. |
| Public event | [DisplayExpired](E_Grasshopper_Kernel_IGH_DocumentObject_DisplayExpired.htm) | Raised whenever the display (on the Canvas) of a certain object becomes invalid. |
| Public event | [ObjectChanged](E_Grasshopper_Kernel_IGH_DocumentObject_ObjectChanged.htm) | Raised whenever some property of the object changes that would affect remote instances. |
| Public event | [PingDocument](E_Grasshopper_Kernel_IGH_DocumentObject_PingDocument.htm) | Raised whenever an object needs to know which GH\_Document it belongs to. |
| Public event | [PreviewExpired](E_Grasshopper_Kernel_IGH_DocumentObject_PreviewExpired.htm) | Raised whenever the display (in the Rhino viewports) of a certain object becomes invalid. |
| Public event | [SolutionExpired](E_Grasshopper_Kernel_IGH_DocumentObject_SolutionExpired.htm) | Raised whenever the solution of a certain object becomes invalid. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DocumentObject Interface](T_Grasshopper_Kernel_IGH_DocumentObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)