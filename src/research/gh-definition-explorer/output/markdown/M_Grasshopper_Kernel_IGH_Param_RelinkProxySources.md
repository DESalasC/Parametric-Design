# M_Grasshopper_Kernel_IGH_Param_RelinkProxySources

﻿ IGH\_Param.RelinkProxySources Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Param Interface](../html/T_Grasshopper_Kernel_IGH_Param.htm "IGH_Param Interface")

[IGH\_Param Methods](../html/Methods_T_Grasshopper_Kernel_IGH_Param.htm "IGH_Param Methods")

[AddSource Method](../html/Overload_Grasshopper_Kernel_IGH_Param_AddSource.htm "AddSource Method ")

[AddVolatileData Method](../html/M_Grasshopper_Kernel_IGH_Param_AddVolatileData.htm "AddVolatileData Method ")

[AddVolatileDataList Method](../html/M_Grasshopper_Kernel_IGH_Param_AddVolatileDataList.htm "AddVolatileDataList Method ")

[AddVolatileDataTree Method](../html/M_Grasshopper_Kernel_IGH_Param_AddVolatileDataTree.htm "AddVolatileDataTree Method ")

[ClearProxySources Method](../html/M_Grasshopper_Kernel_IGH_Param_ClearProxySources.htm "ClearProxySources Method ")

[CreateProxySources Method](../html/M_Grasshopper_Kernel_IGH_Param_CreateProxySources.htm "CreateProxySources Method ")

[RelinkProxySources Method](../html/M_Grasshopper_Kernel_IGH_Param_RelinkProxySources.htm "RelinkProxySources Method ")

[RemoveAllSources Method](../html/M_Grasshopper_Kernel_IGH_Param_RemoveAllSources.htm "RemoveAllSources Method ")

[RemoveEffects Method](../html/M_Grasshopper_Kernel_IGH_Param_RemoveEffects.htm "RemoveEffects Method ")

[RemoveSource Method](../html/Overload_Grasshopper_Kernel_IGH_Param_RemoveSource.htm "RemoveSource Method ")

[ReplaceSource Method](../html/Overload_Grasshopper_Kernel_IGH_Param_ReplaceSource.htm "ReplaceSource Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ParamAddLanguageSpecificTextSet("LST9ACDACCC\_0?cpp=::|nu=.");RelinkProxySources Method |

Attempt to replace all proxy sources with real sources.
Proxy sources are used during file IO, when actual sources might not be available yet.
Once an IO operation has been completed there should be no more proxy sources.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool RelinkProxySources(
	GH_Document document
)
```

```
Function RelinkProxySources ( 
	document As GH_Document
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

document
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST9ACDACCC\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Document](T_Grasshopper_Kernel_GH_Document.htm)

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Param Interface](T_Grasshopper_Kernel_IGH_Param.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)