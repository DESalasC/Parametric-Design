# M_Grasshopper_Kernel_GH_ActiveObject_ExpireSolution

﻿ GH\_ActiveObject.ExpireSolution Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ActiveObject Class](../html/T_Grasshopper_Kernel_GH_ActiveObject.htm "GH_ActiveObject Class")

[GH\_ActiveObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_ActiveObject.htm "GH_ActiveObject Methods")

[AddRuntimeMessage Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_AddRuntimeMessage.htm "AddRuntimeMessage Method ")

[AppendAdditionalMenuItems Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_AppendAdditionalMenuItems.htm "AppendAdditionalMenuItems Method ")

[AppendMenuItems Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_AppendMenuItems.htm "AppendMenuItems Method ")

[ClearData Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_ClearData.htm "ClearData Method ")

[ClearRuntimeMessages Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_ClearRuntimeMessages.htm "ClearRuntimeMessages Method ")

[CollectData Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_CollectData.htm "CollectData Method ")

[ComputeData Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_ComputeData.htm "ComputeData Method ")

[DependsOn Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_DependsOn.htm "DependsOn Method ")

[ExpireDownStreamObjects Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_ExpireDownStreamObjects.htm "ExpireDownStreamObjects Method ")

[ExpireSolution Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_ExpireSolution.htm "ExpireSolution Method ")

[Menu\_AppendBakeItem Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendBakeItem.htm "Menu_AppendBakeItem Method ")

[Menu\_AppendEnableItem Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendEnableItem.htm "Menu_AppendEnableItem Method ")

[Menu\_AppendPreviewItem Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendPreviewItem.htm "Menu_AppendPreviewItem Method ")

[Menu\_AppendRuntimeMessages Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendRuntimeMessages.htm "Menu_AppendRuntimeMessages Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Read.htm "Read Method ")

[RegisterRemoteIDs Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_RegisterRemoteIDs.htm "RegisterRemoteIDs Method ")

[RuntimeMessages Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessages.htm "RuntimeMessages Method ")

[SDKCompliancy Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_SDKCompliancy.htm "SDKCompliancy Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ActiveObjectAddLanguageSpecificTextSet("LSTCFA77943\_0?cpp=::|nu=.");ExpireSolution Method |

Informs the document that owns this object that the solution has expired.
The current object will be set to BLANK as a result. This method is recursive,
it will also expire any and all objects which depend on this object.
If you want a less destructive expiration, consider using ClearData().
If this object is already Blank, you should consider not expiring it.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public override void ExpireSolution(
	bool recompute
)
```

```
Public Overrides Sub ExpireSolution ( 
	recompute As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

recompute
:   Type: [SystemAddLanguageSpecificTextSet("LSTCFA77943\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, the document will be instructed to solve the new state.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ActiveObject Class](T_Grasshopper_Kernel_GH_ActiveObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)