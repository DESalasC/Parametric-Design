# M_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessages

﻿ GH\_ActiveObject.RuntimeMessages Method 

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
| GH\_ActiveObjectAddLanguageSpecificTextSet("LSTBCB1599\_0?cpp=::|nu=.");RuntimeMessages Method |

Gets the list of cached runtime messages that were recorded during solver-time processes.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual IList<string> RuntimeMessages(
	GH_RuntimeMessageLevel level
)
```

```
Public Overridable Function RuntimeMessages ( 
	level As GH_RuntimeMessageLevel
) As IList(Of String)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

level
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTBCB1599\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RuntimeMessageLevel](T_Grasshopper_Kernel_GH_RuntimeMessageLevel.htm)  
    Runtime message type to retrieve.

#### Return Value

Type: [IList](https://docs.microsoft.com/dotnet/api/system.collections.generic.ilist-1)AddLanguageSpecificTextSet("LSTBCB1599\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LSTBCB1599\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of runtime message strings.

#### Implements

[IGH\_ActiveObjectAddLanguageSpecificTextSet("LSTBCB1599\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");RuntimeMessages(GH\_RuntimeMessageLevel)](M_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessages.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ActiveObject Class](T_Grasshopper_Kernel_GH_ActiveObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)