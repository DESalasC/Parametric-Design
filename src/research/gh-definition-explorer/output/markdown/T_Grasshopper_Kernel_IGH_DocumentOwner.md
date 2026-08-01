# T_Grasshopper_Kernel_IGH_DocumentOwner

﻿ IGH\_DocumentOwner Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DocumentOwner Interface](../html/T_Grasshopper_Kernel_IGH_DocumentOwner.htm "IGH_DocumentOwner Interface")

[IGH\_DocumentOwner Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DocumentOwner.htm "IGH_DocumentOwner Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DocumentOwner Interface |

Implement this interface if you want to be the owner assigned to a document in the Grasshopper documentserver.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_DocumentOwner
```

```
Public Interface IGH_DocumentOwner
```

AddLanguageTabSet("ID0EBCA");

The IGH\_DocumentOwner type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [DocumentClosed](M_Grasshopper_Kernel_IGH_DocumentOwner_DocumentClosed.htm) | This method will be called whenever the owner document was closed. |
| Public method | [DocumentModified](M_Grasshopper_Kernel_IGH_DocumentOwner_DocumentModified.htm) | This method will be called whenever the owned document is modified. |
| Public method | [OwnerDocument](M_Grasshopper_Kernel_IGH_DocumentOwner_OwnerDocument.htm) | If the IGH\_DocumentOwner is part of a GH\_Document of its own, this function will return that document. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)