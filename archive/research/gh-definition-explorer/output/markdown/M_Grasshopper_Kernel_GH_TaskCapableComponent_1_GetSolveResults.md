# M_Grasshopper_Kernel_GH_TaskCapableComponent_1_GetSolveResults

﻿ GH\_TaskCapableComponent(T).GetSolveResults Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_TaskCapableComponent(T) Class](../html/T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm "GH_TaskCapableComponent(T) Class")

[GH\_TaskCapableComponent(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm "GH_TaskCapableComponent(T) Methods")

[AfterSolveInstance Method](../html/M_Grasshopper_Kernel_GH_TaskCapableComponent_1_AfterSolveInstance.htm "AfterSolveInstance Method ")

[AppendAdditionalMenuItems Method](../html/M_Grasshopper_Kernel_GH_TaskCapableComponent_1_AppendAdditionalMenuItems.htm "AppendAdditionalMenuItems Method ")

[GetSolveResults Method](../html/M_Grasshopper_Kernel_GH_TaskCapableComponent_1_GetSolveResults.htm "GetSolveResults Method ")

[OnUseTasksClicked Method](../html/M_Grasshopper_Kernel_GH_TaskCapableComponent_1_OnUseTasksClicked.htm "OnUseTasksClicked Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_TaskCapableComponent_1_Read.htm "Read Method ")

[RequestTaskCancellation Method](../html/M_Grasshopper_Kernel_GH_TaskCapableComponent_1_RequestTaskCancellation.htm "RequestTaskCancellation Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_TaskCapableComponent_1_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TaskCapableComponentAddLanguageSpecificTextSet("LST46CB0AB6\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST46CB0AB6\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST46CB0AB6\_2?cpp=::|nu=.");GetSolveResults Method |

Call this method to await the associated task and retrieve its data.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected bool GetSolveResults(
	IGH_DataAccess access,
	out T data
)
```

```
Protected Function GetSolveResults ( 
	access As IGH_DataAccess,
	<OutAttribute> ByRef data As T
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

access
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST46CB0AB6\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_DataAccess](T_Grasshopper_Kernel_IGH_DataAccess.htm)  
    Access object identifying the task.

data
:   Type: [T](T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm)AddLanguageSpecificTextSet("LST46CB0AB6\_4?cpp=%");  
    Data (if any) will be returned here.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
If true, the data was successfully retrieved and can be assigned to outputs immediately.
If false, the data was not found and needs to be calculated by the caller.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TaskCapableComponentAddLanguageSpecificTextSet("LST46CB0AB6\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST46CB0AB6\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)