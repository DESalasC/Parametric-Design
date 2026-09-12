# M_Grasshopper_Kernel_IGH_DocumentObject_OnDisplayExpired

﻿ IGH\_DocumentObject.OnDisplayExpired Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DocumentObject Interface](../html/T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Interface")

[IGH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Methods")

[AddedToDocument Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_AddedToDocument.htm "AddedToDocument Method ")

[AppendMenuItems Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_AppendMenuItems.htm "AppendMenuItems Method ")

[CreateAttributes Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_CreateAttributes.htm "CreateAttributes Method ")

[DocumentContextChanged Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_DocumentContextChanged.htm "DocumentContextChanged Method ")

[ExpirePreview Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_ExpirePreview.htm "ExpirePreview Method ")

[ExpireSolution Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_ExpireSolution.htm "ExpireSolution Method ")

[IsolateObject Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_IsolateObject.htm "IsolateObject Method ")

[MovedBetweenDocuments Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_MovedBetweenDocuments.htm "MovedBetweenDocuments Method ")

[OnAttributesChanged Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnAttributesChanged.htm "OnAttributesChanged Method ")

[OnDisplayExpired Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnDisplayExpired.htm "OnDisplayExpired Method ")

[OnObjectChanged Method](../html/Overload_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged.htm "OnObjectChanged Method ")

[OnPingDocument Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnPingDocument.htm "OnPingDocument Method ")

[OnPreviewExpired Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnPreviewExpired.htm "OnPreviewExpired Method ")

[OnSolutionExpired Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnSolutionExpired.htm "OnSolutionExpired Method ")

[RecordUndoEvent Method](../html/Overload_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent.htm "RecordUndoEvent Method ")

[RemovedFromDocument Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_RemovedFromDocument.htm "RemovedFromDocument Method ")

[TriggerAutoSave Method](../html/Overload_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave.htm "TriggerAutoSave Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DocumentObjectAddLanguageSpecificTextSet("LSTDE97AE2B\_0?cpp=::|nu=.");OnDisplayExpired Method |

Raises the DisplayExpired event on the toplevel object.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void OnDisplayExpired(
	bool redraw
)
```

```
Sub OnDisplayExpired ( 
	redraw As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

redraw
:   Type: [SystemAddLanguageSpecificTextSet("LSTDE97AE2B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, the canvas will be immediately redrawn.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DocumentObject Interface](T_Grasshopper_Kernel_IGH_DocumentObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)