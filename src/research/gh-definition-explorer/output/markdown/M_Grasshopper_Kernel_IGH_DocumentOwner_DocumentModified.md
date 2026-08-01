# M_Grasshopper_Kernel_IGH_DocumentOwner_DocumentModified

﻿ IGH\_DocumentOwner.DocumentModified Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DocumentOwner Interface](../html/T_Grasshopper_Kernel_IGH_DocumentOwner.htm "IGH_DocumentOwner Interface")

[IGH\_DocumentOwner Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DocumentOwner.htm "IGH_DocumentOwner Methods")

[DocumentClosed Method](../html/M_Grasshopper_Kernel_IGH_DocumentOwner_DocumentClosed.htm "DocumentClosed Method ")

[DocumentModified Method](../html/M_Grasshopper_Kernel_IGH_DocumentOwner_DocumentModified.htm "DocumentModified Method ")

[OwnerDocument Method](../html/M_Grasshopper_Kernel_IGH_DocumentOwner_OwnerDocument.htm "OwnerDocument Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DocumentOwnerAddLanguageSpecificTextSet("LSTA2DB1A25\_0?cpp=::|nu=.");DocumentModified Method |

This method will be called whenever the owned document is modified.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void DocumentModified(
	GH_Document document
)
```

```
Sub DocumentModified ( 
	document As GH_Document
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

document
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTA2DB1A25\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Document](T_Grasshopper_Kernel_GH_Document.htm)  
    The modified document.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DocumentOwner Interface](T_Grasshopper_Kernel_IGH_DocumentOwner.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)