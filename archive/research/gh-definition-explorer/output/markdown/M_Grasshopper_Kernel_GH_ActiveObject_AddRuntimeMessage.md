# M_Grasshopper_Kernel_GH_ActiveObject_AddRuntimeMessage

﻿ GH\_ActiveObject.AddRuntimeMessage Method 

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
| GH\_ActiveObjectAddLanguageSpecificTextSet("LST22F5765B\_0?cpp=::|nu=.");AddRuntimeMessage Method |

Add a new message to this object. Valid message type flags are Warning and Error.
If the Message string is empty or zero-length no message is added.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual void AddRuntimeMessage(
	GH_RuntimeMessageLevel level,
	string text
)
```

```
Public Overridable Sub AddRuntimeMessage ( 
	level As GH_RuntimeMessageLevel,
	text As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

level
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST22F5765B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RuntimeMessageLevel](T_Grasshopper_Kernel_GH_RuntimeMessageLevel.htm)  
    Type of message. Only Warnings and Errors are recorded.

text
:   Type: [SystemAddLanguageSpecificTextSet("LST22F5765B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Content of message.

#### Implements

[IGH\_ActiveObjectAddLanguageSpecificTextSet("LST22F5765B\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");AddRuntimeMessage(GH\_RuntimeMessageLevel, String)](M_Grasshopper_Kernel_IGH_ActiveObject_AddRuntimeMessage.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ActiveObject Class](T_Grasshopper_Kernel_GH_ActiveObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)